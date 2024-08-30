"""
Für zukünftige Sachen
Daten in MongoDB Laden und PySpark verwenden um darauf zuzugreifen
DBS-Architektur
"""
import os
import mysql.connector
import scraping

'''
To-Do:
In SQL: Create Table mit Columns und dtypes
Query for Mining/Exploration
Nicole: GitHub einrichten und einladen, oh-my-git
'''
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password= os.getenv("MYSQL_PASSWORD"),
    database="finance"
)
mycursor = mydb.cursor() #"Herzstück"
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

def show_schema(name):
    mycursor.execute(f"DESCRIBE {name}")
    schema = mycursor.fetchall()
    for column in schema:
        print(column)

def show_values(schema):
    mycursor.execute(f"SELECT * FROM {schema}")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)

def insert_schema(dataframe, name):
    df = dataframe
    data = df.values.tolist()
    placeholders = ', '.join(['%s'] * len(df.columns))
    columns = ', '.join(df.columns)
    sql = f"INSERT INTO {name} ({columns}) VALUES ({placeholders})"

    mycursor.executemany(sql, data)
    mydb.commit()

new_table(scraping.symbol)
show_tables()
#INSERT SCHEMA NUR WENN EMPTY!
insert_schema(scraping.financial_data, scraping.symbol)
show_schema(scraping.symbol)
show_values(scraping.symbol)

mycursor.close()
mydb.close()
#mydb.close()
#Damit habe ich dann alles in SQL geladen, jetzt nur noch Queries
