"""
Für zukünftige Sachen
Daten in MongoDB Laden und PySpark verwenden um darauf zuzugreifen
DBS-Architektur bei passenden Daten Strukturieren (Key-Analyse z.B.)
"""
import os
import mysql.connector
#import extract
import transform
#import pdb
import pandas as pd
import datetime

DECIMAL_ACCURACY = 6

'''
To-Do:
Query für Exploration/Mining (und das Ergebnis automatisch visualisieren)
'''
def new_table(symbol):
    """
    Neues Schema, wenn es nicht existiert. Datentypen werden von dataframe übernommen. ID kommt noch hinzu.
    """
    mycursor.execute(f"""CREATE TABLE IF NOT EXISTS {symbol} (id INT AUTO_INCREMENT PRIMARY KEY,
     timestamp DATETIME,
     open FLOAT,
     high FLOAT,
     low FLOAT,
     close FLOAT,
     volume INTEGER,
     rate_of_change DECIMAL(15,3)
     )""")

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
    mycursor.execute(f"SELECT * FROM {schema}")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)

def insert_many(dataframe, schema):
    """
    Wird verwendet für insert_schema(). Wird aufgerufen, falls neues Schema kreiert wurde und leer ist.
    Lädt alle Werte des Dataframes in das Schema (1:1 Mapping)
    """
    df = dataframe
    data = df.values.tolist()
    placeholders = ', '.join(['%s'] * len(df.columns))
    columns = ', '.join(df.columns)
    sql = f"INSERT INTO {schema} ({columns}) VALUES ({placeholders})"
    mycursor.executemany(sql, data)

def insert_one(dataframe, schema):
    """
    Wird verwendet für insert_schema(). Wird aufgerufen, falls Schema schon Werte enthält und
    der neuste Wert noch nicht in der Datenbank ist.
    """
    df = dataframe.values.tolist()[0]
    placeholders = ', '.join(['%s'] * len(dataframe.columns))
    columns = ', '.join(dataframe.columns)
    sql = f"INSERT INTO {schema} ({columns}) VALUES ({placeholders})"
    mycursor.execute(sql, df)

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
