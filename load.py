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

'''
To-Do:
Query für Exploration/Mining (und das Ergebnis automatisch visualisieren)
'''
def new_table(symbol):
    mycursor.execute(f"""CREATE TABLE IF NOT EXISTS {symbol} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp DATETIME,
        open FLOAT,
        high FLOAT,
        low FLOAT,
        close FLOAT,
        volume INTEGER,
        rate_of_change DECIMAL(15,3)
        )""") #rate_of_change dtype ändern?

def show_tables():
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)

def show_schema(schema):
    mycursor.execute(f"DESCRIBE {extract.symbol}")
    schema = mycursor.fetchall()
    for column in schema:
        print(column)

def show_values(schema):
    mycursor.execute(f"SELECT * FROM {schema}")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)

def insert_many(dataframe, schema):
    df = dataframe
    data = df.values.tolist()
    placeholders = ', '.join(['%s'] * len(df.columns))
    columns = ', '.join(df.columns)
    sql = f"INSERT INTO {schema} ({columns}) VALUES ({placeholders})"
    mycursor.executemany(sql, data)

def insert_schema(dataframe, schema):
    mycursor.execute(f"SELECT COUNT(*) FROM {schema}")
    count = mycursor.fetchone()[0]
    if count == 0:
        insert_many(dataframe, schema)
    else:
        mycursor.execute(f"SELECT * FROM {schema} ORDER BY timestamp desc LIMIT 1")
        first_row_db = mycursor.fetchone()
        df = dataframe.head(1)
        first_row_df = df.values.tolist()[0]
        if first_row_db != first_row_df:
            #Das funktioniert noch nicht ganz! Es gibt noch Duplikate
            placeholders = ', '.join(['%s'] * len(df.columns))
            columns = ', '.join(df.columns)
            sql = f"INSERT INTO {schema} ({columns}) VALUES ({placeholders})"
            mycursor.execute(sql, first_row_df)
        else:
            print("Erster Wert überschneidet sich. Kein neuer Wert reingeladen.")
    mydb.commit()


#Server nicht nur lokal laufen lassen -> my.ini


mydb = mysql.connector.connect(
host="localhost",
user="root",
password= os.getenv("MYSQL_PASSWORD"),
database="finance"
)
mycursor = mydb.cursor() #"Herzstück"

def load(symbol, data):
    new_table(symbol)
    show_tables()
    insert_schema(data, symbol)

#show_schema(table)
#show_values(table) #head!

#Damit habe ich dann alles in SQL geladen, jetzt noch Flow Control & Queries (+ Visualisierung)
