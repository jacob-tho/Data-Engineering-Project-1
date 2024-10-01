"""
Für zukünftige Sachen
Daten in MongoDB Laden und PySpark verwenden um darauf zuzugreifen
DBS-Architektur bei passenden Daten Strukturieren (Key-Analyse z.B.)
"""
import os
import mysql.connector
import transform
import pandas as pd
import datetime
import requests

DECIMAL_ACCURACY = 6

'''
To-Do:
Query für Exploration/Mining (und das Ergebnis automatisch visualisieren)
'''
def new_table(symbol):
    """
    Neues Schema, wenn es nicht existiert. Datentypen werden von dataframe übernommen. ID kommt noch hinzu.
    """
    requests.get(f"https://www.lohse-und-lohse.de/DEP/create_table_if_not_exists.php?pw=lo34bf&symbol={symbol}")

def show_tables():
    """
    Zeigt an, welche Tables existieren. Schneller Überblick, ob reinladen eines neuen Tables funktioniert
    """
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)

def show_schema(schema):
    """
    Kurzbeschreibung des Schemas (dtypes, column names)
    """
    mycursor.execute(f"DESCRIBE {extract.symbol}")
    schema = mycursor.fetchall()
    for column in schema:
        print(column)

def show_values(schema):
    """
    Wenn nötig: Zeige alle Werte des Schemas
    """
    response = requests.get(f"https://www.lohse-und-lohse.de/DEP/get_newest_stock_data.php?pw=lo34bf&symbol={schema}")
    return response

def insert_many(dataframe, schema):
    """
    Wird verwendet für insert_schema(). Wird aufgerufen, falls neues Schema kreiert wurde und leer ist.
    Lädt alle Werte des Dataframes in das Schema (1:1 Mapping)
    """
    df = dataframe
    for data in df.iloc:
        insert_one(data, schema)

def insert_one(dataframe, schema):
    """
    Wird verwendet für insert_schema(). Wird aufgerufen, falls Schema schon Werte enthält und
    der neuste Wert noch nicht in der Datenbank ist.
    """
    df = dataframe.values.tolist()[0]
    data_obj = {
            "timestamp": df[0],
            "open": df[1],
            "high": df[2],
            "low": df[3],
            "close": df[4],
            "volume": df[5],
            "rate_of_change": df[6],
            }
    json_obj = json.dumps(data_obj)
    requests.get(f"https://www.lohse-und-lohse.de/DEP/insert_single_stock.php?pw=lo34bf&symbol={schema}&stock_data={json_obj}")

def standardize(sql, df):
    """
    Standardisierung von SQL Row und Pandas Dataframe Row. Checke auf Duplikate
    """
    sql_standardized = [sql[1].strftime("%Y-%m-%d"),
    round(float(sql[2]), DECIMAL_ACCURACY),
    round(float(sql[3]), DECIMAL_ACCURACY),
    round(float(sql[4]), DECIMAL_ACCURACY),
    round(float(sql[5]), DECIMAL_ACCURACY),
    sql[6],
    round(float(sql[7]), DECIMAL_ACCURACY)]

    df_standardized = [pd.to_datetime(df[0]).strftime("%Y-%m-%d"),
    round(float(df[1]), DECIMAL_ACCURACY),
    round(float(df[2]), DECIMAL_ACCURACY),
    round(float(df[3]), DECIMAL_ACCURACY),
    round(float(df[4]), DECIMAL_ACCURACY),
    round(float(df[5]), DECIMAL_ACCURACY),
    df[6],
    round(float(df[1]), DECIMAL_ACCURACY),]

    duplicate = sql_standardized[:3] == df_standardized[:3]
    return duplicate

def insert_schema(dataframe, schema):
    """
    Werte von pd.df in mySQL Datenbank laden. Wenn leer: Alle reinladen.
    Wenn nicht leer: Schaue, ob neuester Wert bereits in Schema.
    Wenn nicht in Schema: Füge neusten Wert hinzu.
    Wenn in Schema: Nichts reinladen
    """
    mycursor.execute(f"SELECT COUNT(*) FROM {schema}")
    count = mycursor.fetchone()[0]
    if count == 0:
        insert_many(dataframe, schema)
    else:
        mycursor.execute(f"SELECT * FROM {schema} ORDER BY timestamp desc LIMIT 1")
        first_row_db = mycursor.fetchone()
        df = dataframe.head(1)
        first_row_df = df.values.tolist()[0]
        if standardize(first_row_db, first_row_df) is not True:
            #pdb.set_trace()
            insert_one(df, schema)
        else:
            print("Erster Wert überschneidet sich. Kein neuer Wert reingeladen.")
    mydb.commit()

#Server nicht nur lokal laufen lassen -> my.ini

mydb = mysql.connector.connect(
host="localhost",
user="root",
password=os.getenv("MYSQL_PASSWORD"),
database="finance"
)

mycursor = mydb.cursor() #"Herzstück"

def load(symbol, data):
    new_table(symbol)
    #show_tables()
    insert_schema(data, symbol)

#show_schema(table)
#show_values(table) #head!

#Damit habe ich dann alles in SQL geladen, jetzt noch Flow Control & Queries (+ Visualisierung)
