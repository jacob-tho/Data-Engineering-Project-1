import requests
import io

#Verschiedene Arten der Extraltion?
#API, Scraping, Download aus Datenbanken

API_key = "WD8OJ44ZLWCEXHRB" #Diesen noch als env Variable speichern
symbol = "AAPL" #Mehrere symbole gleichzeitig?
datatype = "csv"

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey={API_key}&datatype={datatype}'
r = requests.get(url)
data = r.content.decode("utf-8")

#TODO: Scheduling Job
