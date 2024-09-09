import extract
import transform
import load
from apscheduler.schedulers.blocking import BlockingScheduler

import os

API_key = os.getenv("API_KEY")
url_symbols = "https://api.stockanalysis.com/api/screener/s/f?m=s&s=asc&c=s,n,industry,marketCap&cn=6000&p=1&i=stocks"
symbols = extract.scrape_all(url_symbols)
datatype = "csv"



def etl_pipeline:
    print("Start der Pipeline")
    #Code
    for symbol in symbols:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey={API_key}&datatype={datatype}'
        #Hier einmal das ganze Symbol loaden.
    
    #url anpassen und encode_single
    #transform
    #load
    #mining (z.B: größter Gewinn und Verlust über Dashboard. Insgesamte Änderung.)
    #Auswahl über Eingabe bestimmter Stocks, auf denen dann Prediction zum nächsten Tag gegeben wird
    print("Job erledigt")

#scheduler = BlockingScheduler
#scheduler.add_job(etl_pipeline, "cron", hour=6, minute=0)

#scheduler.start()
