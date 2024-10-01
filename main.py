import extract
import transform
import load
import mysql.connector
from apscheduler.schedulers.blocking import BlockingScheduler
import pdb
import os

#TO-DO: IP-Addressen in Liste speichern und nur neue zulassen! Scheduling über DB?
url_symbols = "https://api.stockanalysis.com/api/screener/s/f?m=s&s=asc&c=s,n,industry,marketCap&cn=6000&p=1&i=stocks"
symbols = extract.scrape_all(url_symbols)
API_key = os.getenv("API_KEY")
datatype = "csv"
mydb = load.mydb
mycursor = mydb.cursor()
used_ips = set()

def biggest_change(symbol, stock, current_high, current_high_name, current_low, current_low_name):
    #Berechne größten Gewinn/Verlust über alle Stocks

    new_rate = stock["rate_of_change"][0]
    if new_rate > current_high:
        current_high = new_rate
        current_high_name = symbol
    elif new_rate < current_low:
        current_low = new_rate
        current_low_name = symbol

    return current_high, current_high_name, current_low, current_low_name

def etl_pipeline(symbol_list, highest_change, highest_change_name, lowest_change, lowest_change_name):
    """
    Für jedes Symbol aus der Liste einmal die Pipeline durchlaufen lassen
    Extrahiere Daten aus URL, Transformiere (neue Spalte, bereinigen) und lade in MySQL Datenbank
    Nach Anzahl an Versuchen IP-Addresse ändern
    Größte Änderungsrate bestimmen
    """
    print("Start der Pipeline")
    runs=0
    for symbol in symbol_list:
        runs+=1
        if runs%10==0 and runs <= 6000:
            while extract.get_current_ip() in used_ips:
                extract.renew_tor_ip()
        current_ip = extract.get_current_ip()
        used_ips.add(current_ip)
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={API_key}&datatype={datatype}'
        df = transform.transform(url)
        highest_change, highest_change_name, lowest_change, lowest_change_name = biggest_change(symbol, df, highest_change, highest_change_name, lowest_change, lowest_change_name)
        db = load.load(symbol, df)

    #Gebe Signifikanten Wert aus
    highest_change = round(highest_change, 3)
    lowest_change = round(lowest_change, 3)
    print("\n")
    print(f"Den größten Gewinn hat {highest_change_name} gemacht mit {highest_change}")
    print(f"Den größten Verlust hat {lowest_change_name} gemacht mit {lowest_change}")

    #mining (z.B: größter Gewinn und Verlust über Dashboard. Insgesamte Änderung.)
    #Auswahl über Eingabe bestimmter Stocks, auf denen dann Prediction zum nächsten Tag gegeben wird
    mycursor.close()
    mydb.close()
    print("Job erledigt")

"""
Scheduler, der das Programm täglich um 10 Uhr Vormittag ausführt. Noch in Bearbeitung.
"""
highest_change = float(0)
lowest_change = float(0)
highest_change_name = None
lowest_change_name = None
etl_pipeline(symbols[:10], highest_change, highest_change_name, lowest_change, lowest_change_name)
'''
scheduler = BlockingScheduler()
scheduler.add_job(etl_pipeline, "cron", hour=10, minute=0, args=[symbol_list]) #Das funktioniert noch nicht so ganz -> Docs durchlesen!

scheduler.start()
'''
