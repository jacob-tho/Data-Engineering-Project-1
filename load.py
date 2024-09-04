"""
Für zukünftige Sachen
Daten in MongoDB Laden und PySpark verwenden um darauf zuzugreifen
DBS-Architektur bei passenden Daten Strukturieren (Key-Analyse z.B.)
"""
import os
import mysql.connector
import extract
import transform

'''
To-Do:
In SQL: Create Table mit Columns und dtypes IF EXISTS
Query für Exploration/Mining
Nicole: GitHub einrichten und einladen, oh-my-git
'''
def new_table(symbol):
    #if already exists?
    mycursor.execute(f"""CREATE TABLE {symbol} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp DATETIME,
        open FLOAT,
        high FLOAT,
        low FLOAT,
        close FLOAT,
        volume INTEGER)""")

def show_tables():
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)

def show_schema(schema):
    mycursor.execute(f"DESCRIBE {name}")
    schema = mycursor.fetchall()
    for column in schema:
        print(column)

def show_values(schema):
    mycursor.execute(f"SELECT * FROM {schema}")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)

def insert_schema(dataframe, schema):
    df = dataframe
    data = df.values.tolist()
    placeholders = ', '.join(['%s'] * len(df.columns))
    columns = ', '.join(df.columns)
    sql = f"INSERT INTO {name} ({columns}) VALUES ({placeholders})"

    mycursor.executemany(sql, data)
    mydb.commit()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password= os.getenv("MYSQL_PASSWORD"),
    database="finance"
    )
mycursor = mydb.cursor() #"Herzstück"
schema = extract.symbol
new_table(schema)
show_tables()
#INSERT SCHEMA NUR WENN EMPTY!
insert_schema(extract.financial_data, schema)
show_schema(schema)
#show_values(schema)

mycursor.close()
mydb.close()

#Damit habe ich dann alles in SQL geladen, jetzt noch Flow Control & Queries (+ Visualisierung)
