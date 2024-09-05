import requests
from bs4 import BeautifulSoup
import io
import pandas as pd
import os
import re
from urllib.request import urlopen


#Verschiedene Arten der Extraltion?
#API, Scraping, Download aus Datenbanken

API_key = os.getenv("API_KEY")
symbol = "AAT"
datatype = "csv"

#URL muss dann geändert werden
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey={API_key}&datatype={datatype}'

#Wie schaffe ich es, ALLE auf einmal zu machen, nicht nur die, die angezeigt sind? -> Selenium scheinbar
#Danach: for symbol in symbol encode_single in main!
def scrape_symbols(url):
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
    html = requests.get(url, headers = headers)
    html = html.content.decode()
    bsObj = BeautifulSoup(html, features="lxml")
    list = bsObj.find("div", id= "main-table-wrap").findAll("a",href=re.compile("^(/stocks/)"))
    symbols = [symbol.get_text(strip=True) for symbol in list]
    print(symbols)
    return symbols



scrape_symbols("https://stockanalysis.com/stocks/")

def encode_single(url):
    r = requests.get(url)
    data = r.content.decode("utf-8")
    data = pd.read_csv(io.StringIO(data))
    return data

#financial_data = encode_single(url)

#TODO: Alle Symbole auf einmal. -> Selenium
#Scheduling in Main (Passiert wohl als letztes)
#Tagesdaten aller Symbols jeweils Speichern und nur aktuellen neu dazu nehmen.
