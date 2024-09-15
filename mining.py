import mysql.connector
import os
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates

"""
Normale Prozedur: EDA; PDA
Time Series visulalisieren. Lineare Regression?. Allgemein schauen, was man mit Time-Series so machen kann.
Time Series als ODE auffassen? Typische TS verwenden, Stückweise zu Neural ODE übergehen.
Vergleiche ziehen zu "klassischen" ML Algorithmen, wie schneiden diese jeweils ab?
Umformung in nicht - time series -> Feature Engineering
"""
mydb = mysql.connector.connect(
host="localhost",
user="root",
password= os.getenv("MYSQL_PASSWORD"),
database="finance"
)
mycursor = mydb.cursor()

mycursor.execute(f"SELECT timestamp, close FROM dell")
rows = mycursor.fetchall()
x_axis = []
y_axis = []
for row in rows:
    date_part = row[0]
    close = row[1]
    cleaned = (datetime.datetime(date_part.year, date_part.month, date_part.day), close)
    x_axis.append(cleaned[0])
    y_axis.append(cleaned[1])

plt.plot(x_axis, y_axis)
plt.show()
#plt.show()
