import requests
#from bs4 import BeautifulSoup
import io
import pandas as pd
#import re
import socks
from stem import Signal
from stem.control import Controller
import time
import os
#import pdb
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
    #Ruft die Website auf, die Alle Symbole enthält und speichert jedes Symbol in einer Liste
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
    response = requests.get(url, headers=headers)

    try:
        data = response.json()

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


def get_url_via_tor(url: str) ->str:
    #URL-Access mit Tor-Browser
    proxies = {
        'http': 'socks5h://127.0.0.1:9150',
        'https': 'socks5h://127.0.0.1:9150'
    }

    try:
        response = requests.get(url, proxies=proxies, timeout=10)
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def renew_tor_ip():
    #IP-Addresse wechseln
    with Controller.from_port(port=9151) as controller:
        controller.authenticate(password=os.getenv("MYSQL_PASSWORD"))
        controller.signal(Signal.NEWNYM)
        time.sleep(2)

def get_current_ip():
    proxies = {
        'http': 'socks5h://127.0.0.1:9150',
        'https': 'socks5h://127.0.0.1:9150'
    }
    url = "http://httpbin.org/ip"
    response = requests.get(url, proxies=proxies)
    return response.json()["origin"]

def encode_single(url: str) -> pd.DataFrame:
    """
    Greift auf API zu (mittels Tor) und lädt CSV Daten in pandas Dataframe
    """
    data = get_url_via_tor(url)
    data = pd.read_csv(io.StringIO(data))
    return data
renew_tor_ip()
