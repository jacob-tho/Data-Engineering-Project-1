import requests
import pandas as pd
import io

#Verschiedene Arten der Extraltion?
#API, Scraping, Download. Datembanken

API_key = "demo"
symbol = "IBM"
datatype = "csv"
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey={API_key}&datatype={datatype}'
r = requests.get(url)
data = r.content.decode("utf-8") #wieso das?

"""
Pandas section:
Exploration: head, info, describe, shape, columns, dtypes
Cleaning: drop_na, fill_na, drop_duplicates, replace, rename, as_type
Transformation: apply, map, groupby, pivot?, sort_values, merge, agg, concat
Selection/Filtering: loc, iloc, [condition]
"""
#Duplikate entfernen, Null-Werte bereinigen, Datentypen checken
#Was sind noch Standard / Must-do Aufgaben mit Pandas?
financial_data = pd.read_csv(io.StringIO(data)) #wieso das?

def df_info(df):
    print(df.head())
    print(f"Anzahl der Zeilen und Spalten: {df.shape}")
    print(df.dtypes)
df_info(financial_data)
financial_data = financial_data.astype({"timestamp": "datetime64[ns]"})

def df_cleaning(df, column, value):
    print(df[df.isnull().any(axis=1)])
    df[column].fillna(value)
    df.drop_duplicates()
#Alternative: financial_data = pd.to_datetime(financial_data["timestamp"])
#Gibt es eine Möglichkeit ein Recommendation-System zu machen, bei dem unpassende Spalten dtype ändern?

'''
To-Do: Unclean Dataset aufbereiten.
Datansatz bereinigen -> in SQL -> darauf dann mit pandas wieder zurückgreifen
'''
#financial_data.drop_duplicates()
#print(financial_data[financial_data.isnull().any(axis=1)])# -> Leer, also keine NaN-Werte
#print(financial_data.sort_values("timestamp"))

#Welche Fragen könnten einen interessieren? All-time high, wie viel ist es seitdem runtergegangen?
#Wirtschaftler mögen Prozentwerte viel lieber
#Average daily return, correlation between stocks, periods of significant change

#print(financial_data[financial_data["volume"]==financial_data["volume"].max()])
#print(financial_data.nlargest(3, "volume"))
#print(financial_data["high"]-financial_data["low"].idxmax())
