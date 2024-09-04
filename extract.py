import requests
import io
import pandas as pd

#Verschiedene Arten der Extraltion?
#API, Scraping, Download aus Datenbanken

API_key = "WD8OJ44ZLWCEXHRB" #Diesen noch als env Variable speichern
symbol = "AB" #Mehrere symbole gleichzeitig?
datatype = "csv"

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey={API_key}&datatype={datatype}'
r = requests.get(url)
data = r.content.decode("utf-8")
financial_data = pd.read_csv(io.StringIO(data))
#TODO: Scheduling Job, alle Symbole auf einmal.
#Tagesdaten aller Symbols jeweils Speichern und nur aktuellen neu dazu nehmen.
