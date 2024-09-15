import extract
import transform
import load
import mysql.connector
from apscheduler.schedulers.blocking import BlockingScheduler
import pdb

import os

#url_symbols = "https://api.stockanalysis.com/api/screener/s/f?m=s&s=asc&c=s,n,industry,marketCap&cn=6000&p=1&i=stocks"
#symbols = extract.scrape_all(url_symbols)
API_key = "9QY34XA07MHS3WBM"#os.getenv("API_KEY")
symbol_list = ["DELL", "SMCI", "RGTI", "RCAT", "QUBT", "QMCO", "QBTS", "PSTG", "NNDM", "LOGI", "DM", "UDMY", "UTI", "TAL", "STRA", "SKIL", "LINC", "IH", "EEIQ", "FOX", "IMAX", "MANU", "NFLX", "PARA", "WBD"]
datatype = "csv"
mydb = load.mydb
mycursor = mydb.cursor()


def etl_pipeline(symbol_list):
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

etl_pipeline(symbol_list)
#scheduler = BlockingScheduler
#scheduler.add_job(etl_pipeline, "cron", hour=6, minute=0)

#scheduler.start()
