"""
Für zukünftige Sachen
Daten in MongoDB Laden und PySpark verwenden um darauf zuzugreifen
DBS-Architektur
"""
import mysql.connector
import scraping

'''
To-Do:
In SQL: Create Table mit Columns und dtypes
Query for Mining/Exploration
'''
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Melli123.",
    database="finance"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
'''
Das funktioniert nicht
mycursor.execute(f"""CREATE TABLE {scraping.symbol} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME,
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    volume INTEGER)""")
'''
for x in mycursor:
    print(x)
financial_data.to_sql("name", mydb, if_exists="replace", index=False)
mydb.commit()
mydb.close()
#Damit habe ich dann alles in SQL geladen, jetzt nur noch Queries
