import requests
from bs4 import BeautifulSoup
import io #das kommt dann raus
import pandas as pd
import os #das kommt dann raus
import re
import json


'''
Mit BS4 gescraped, konnte jedoch nur die ersten 500 Elemente (da JS-Script)
def scrape_symbols(url):
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
    html = requests.get(url, headers = headers)
    html = html.content.decode()
    bsObj = BeautifulSoup(html, features="lxml")
    list = bsObj.find("div", id= "main-table-wrap").findAll("a",href=re.compile("^(/stocks/)"))
    symbols = [symbol.get_text(strip=True) for symbol in list]
    print(len(symbols))
    return symbols
    #url = "https://stockanalysis.com/stocks/"
'''

def scrape_all(url):
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)

    try:
        data = response.json()
        #print("JSON Datei:", json.dumps(data, indent=2))
        #print(data)

    except json.JSONDecodeError:
        print("Konnte nicht geparsed werden")
        return

    # Dict, zweites Element, dict{nur ein key: [List aller items {Dict für jedes item}]}
    '''
    dict.keys [nummer zwei], dict[erstes element], for loop für jedes element: jedes value vom ersten key
    '''
    results = []
    outer_keys = list(data.keys())
    second_key = outer_keys[1]

    inner_dict = data[second_key]
    inner_keys = list(inner_dict.keys())
    first_inner_key = inner_keys[0]

    list_of_elements= inner_dict[first_inner_key]

    for item in list_of_elements:
        item_keys = list(item.keys())
        first_item_key = item_keys[0]
        value = item[first_item_key]
        results.append(value)
    return results

def encode_single(url):
    r = requests.get(url)
    data = r.content.decode("utf-8")
    data = pd.read_csv(io.StringIO(data))
    return data

API_key = os.getenv("API_KEY") #IST LIMITIERT AUF 25 PRO TAG"
symbol = "ACI"
datatype = "csv"

#URL muss dann geändert werden
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey={API_key}&datatype={datatype}'
financial_data = encode_single(url)
#print(financial_data)
url_symbols = "https://api.stockanalysis.com/api/screener/s/f?m=s&s=asc&c=s,n,industry,marketCap&cn=6000&p=1&i=stocks"
