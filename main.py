import extract
import transform
import load
import mysql.connector
from apscheduler.schedulers.blocking import BlockingScheduler
import pdb

import os

#url_symbols = "https://api.stockanalysis.com/api/screener/s/f?m=s&s=asc&c=s,n,industry,marketCap&cn=6000&p=1&i=stocks"
#symbols = extract.scrape_all(url_symbols)
"""
API_KEY, Liste aller 25 zu betrachtenden Symbole und Connection zur MySQL-Datenbank
"""
API_key = os.getenv("API_KEY")
symbol_list = ["DELL", "SMCI", "RGTI", "RCAT", "QUBT", "QMCO", "QBTS", "PSTG", "NNDM", "LOGI", "DM", "UDMY", "UTI", "TAL", "STRA", "SKIL", "LINC", "IH", "EEIQ", "FOX", "IMAX", "MANU", "NFLX", "PARA", "WBD"]
datatype = "csv"
mydb = load.mydb
mycursor = mydb.cursor()


def etl_pipeline(symbol_list):
    """
    Für jedes Symbol aus der Liste einmal die Pipeline durchlaufen
    Extrahiere Daten aus URL, Transformiere (neue Spalte, bereinigen) und lade in MySQL Datenbank
    """
    print("Start der Pipeline")
    for symbol in symbol_list:
        #if symbol == "rcat":
        #pdb.set_trace()
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={API_key}&datatype={datatype}'
        df = transform.transform(url)
        db = load.load(symbol, df)

    #mining (z.B: größter Gewinn und Verlust über Dashboard. Insgesamte Änderung.)
    #Auswahl über Eingabe bestimmter Stocks, auf denen dann Prediction zum nächsten Tag gegeben wird
    mycursor.close()
    mydb.close()
    print("Job erledigt")

"""
Scheduler, der das Programm täglich um 6 Uhr Vormittag ausführt. Noch in Bearbeitung.
"""
scheduler = BlockingScheduler
scheduler.add_job(etl_pipeline(symbol_list), "cron", hour=6, minute=0) #Das funktioniert noch nicht so ganz -> Docs durchlesen!

scheduler.start()
