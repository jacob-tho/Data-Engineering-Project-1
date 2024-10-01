import mysql.connector
import os
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates
#import main
#from main import symbol_list Wie genau funktionieren import-statements? Wieso wird main immer komplett ausgeführt?
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
symbol_list = ["DELL", "SMCI", "RGTI", "RCAT", "QUBT", "QMCO", "QBTS", "PSTG", "NNDM", "LOGI", "DM", "UDMY", "UTI", "TAL", "STRA", "SKIL", "LINC", "IH", "EEIQ", "FOX", "IMAX", "MANU", "NFLX", "PARA", "WBD"]

def plot(symbol):
    #Eventuell zu jedem Graph noch ein Subplot mit "rate_of_change"?
    """
    Funktion zum plotten der jeweiligen Zeitreihe.
    To-Do: Subplot mit rate_of_change (kleineres, aktuelles Zeitintervall mit Prediction!)
    """
    mycursor.execute(f"SELECT timestamp, close, rate_of_change FROM {symbol} ORDER BY timestamp desc")
    rows = mycursor.fetchall()
    x_axis = []
    y_axis = []
    y_axis_change = [] #Das muss noch in irgendeiner Form Standardisiert/Normalisiert werden!!!
    for row in rows:
        date_part = row[0]
        close = row[1]
        rate_of_change = row[2]
        cleaned = (datetime.datetime(date_part.year, date_part.month, date_part.day), close, rate_of_change)
        x_axis.append(cleaned[0])
        y_axis.append(cleaned[1])
        y_axis_change.append(cleaned[2])

    '''
    fig, ax = plt.subplots(2,1)

    ax[0].plot(x_axis, y_axis)
    ax[0].set_title(f"{symbol}-Graph")
    ax[1].plot(x_axis, y_axis_change)
    ax[1].set_title(f"{symbol}-Graph Veränderungen")
    plt.show()
    '''
    plt.plot(x_axis, y_axis)
    plt.title(f"{symbol}-Graph")
    plt.show()
#for symbol in main.symbols:
#    plot(symbol)
plot("ae")
