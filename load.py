"""
Für zukünftige Sachen
Daten in MongoDB Laden und PySpark verwenden um darauf zuzugreifen
DBS-Architektur bei passenden Daten Strukturieren (Key-Analyse z.B.)
"""
import os
import mysql.connector
import extract
import transform
import pdb

'''
To-Do:
In SQL: Create Table mit Columns und dtypes IF EXISTS
        ALTER TABLE / INSERT neue Daten nach Scheduling (Eine Zeile dazu oder Join?)
Query für Exploration/Mining (und das Ergebnis automatisch visualisieren)
'''
def new_table(symbol):
    #if already exists?
    mycursor.execute(f"""CREATE TABLE IF NOT EXISTS {symbol} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp DATETIME,
        open FLOAT,
        high FLOAT,
        low FLOAT,
        close FLOAT,
        volume INTEGER,
        rate_of_change DECIMAL(6,3)
        )""")

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

def insert_schema(dataframe, schema):
    df = dataframe
    data = df.values.tolist()
    placeholders = ', '.join(['%s'] * len(df.columns))
    columns = ', '.join(df.columns)
    sql = f"INSERT INTO {extract.symbol} ({columns}) VALUES ({placeholders})"

    mycursor.executemany(sql, data)
    mydb.commit()


#Server nicht nur lokal laufen lassen -> my.ini
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password= os.getenv("MYSQL_PASSWORD"),
    database="finance"
    )


mycursor = mydb.cursor() #"Herzstück"
table = extract.symbol

#Create nur wenn noch nicht da
new_table(table)
show_tables()
#pdb.set_trace()
#INSERT SCHEMA NUR WENN EMPTY! Left Join?
insert_schema(transform.df, table) #wieso geht das jetzt nicht?
show_schema(table)
show_values(table) #head!
#Automatische Visualisierung des reingeladenen Stocks, wenn encode_single

mycursor.close()
mydb.close()

#Damit habe ich dann alles in SQL geladen, jetzt noch Flow Control & Queries (+ Visualisierung)
#Weitere Querys und Visualisierung vorerst Nicole überlassen
