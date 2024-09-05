import extract
import transform
import load
from apscheduler.schedulers.blocking import BlockingScheduler

def etl_pipeline:
    print("Start der Pipeline")
    #Code
    #extract()
    #for symbol in extract.symbols
    #url anpassen und encode_single
    #transform
    #load
    #mining (z.B: größter Gewinn und Verlust über Dashboard. Insgesamte Änderung.)
    #Auswahl über Eingabe bestimmter Stocks, auf denen dann Prediction zum nächsten Tag gegeben wird
    print("Job erledigt")

scheduler = BlockingScheduler
scheduler.add_job(etl_pipeline, "cron", hour=6, minute=0)

scheduler.start()
