import requests
from bs4 import BeautifulSoup
import io #das kommt dann raus
import pandas as pd
import os #das kommt dann raus
import re

#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.chrome.options import Options


#Verschiedene Arten der Extraltion?
#API, Scraping, Download aus Datenbanken

API_key = os.getenv("API_KEY")
symbol = "AAPL"
datatype = "csv"

#URL muss dann geändert werden
url_symbols = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey={API_key}&datatype={datatype}'
"""
class Stock_Scraper: #Selenium
    def __init__(self, driver_path, headless = True):
        self.driver_path = driver_path
        self.headless = headless
        self.driver = self.initialize_driver()

    def initialize_driver(self):
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = Service(self.driver_path)
        return webdriver.Chrome(service=service, options=chrome_options)

    def load_page(self, url):
        self.driver.get(url)

    def scrape_symbols(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html, "lxml")
        symbols = soup.find("div", id="main-table-wrap").findAll("a", href=True)
        return [symbol.get_text(strip=True) for symbol in symbols]

    def click_next_button(self):
        try:
            next_button = self.driver.find_element(By.CSS_SELECTOR, "button.controls-btn")
            next_button.click()
            return True
        except Exception as e:
            print(f"Error or no more symbols to load: {e}")
            return False

    def scrape_symbols(self):
        symbols_set = set()

        while True:
            new_symbols = self.extract_symbols()
            symbols_set.update(new_symbols)

            if not self.click_next_button():
                break

            time.sleep(2)  # Give time for new symbols to load

        return list(symbols_set)

    def close(self):
        self.driver.quit()
"""

def scrape_symbols(url):
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
    html = requests.get(url, headers = headers)
    html = html.content.decode()
    bsObj = BeautifulSoup(html, features="lxml")
    list = bsObj.find("div", id= "main-table-wrap").findAll("a",href=re.compile("^(/stocks/)"))
    symbols = [symbol.get_text(strip=True) for symbol in list]
    #print(symbols)
    print(len(symbols))
    return symbols

def encode_single(url):
    r = requests.get(url)
    data = r.content.decode("utf-8")
    data = pd.read_csv(io.StringIO(data))#, sep="delimiter", header=None)
    return data

financial_data = encode_single(url)

'''
Selenium To-Do
#driver_path = r"C:\Chromedriver\chrome-win64\chrome.exe"
#url = "https://stockanalysis.com/stocks/"

#scraper = Stock_Scraper(driver_path)
#scraper.load_page(url)
#all_symbols = scraper.scrape_symbols()

#print(f"Total symbols scraped: {len(all_symbols)}")
#print(all_symbols)

#scraper.close()
#Wie schaffe ich es, ALLE auf einmal zu machen, nicht nur die, die angezeigt sind? -> Selenium scheinbar
#Danach: for symbol in symbol encode_single in main!

#Selenium: While sich die Listengröße ändert -> Scrape, Drücke auf den Button


#scrape_symbols("https://stockanalysis.com/stocks/")
'''

#TODO: Alle Symbole auf einmal. -> Selenium fast fertig!
