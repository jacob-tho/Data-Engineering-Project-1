###Test Code über das Buch "Web Scraping with Python"
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

"""
Anschauen: Was für Tags und Attribute sind so die wichtigsten/häufigsten?
html = urlopen(url) um die Website "anzufragen" -> Exception Handling, falls es diese nicht gibt
bsObj = BeautifulSoup(html.read(), features="lxml") Standard-Command, um das in das gewünschte Objekt umzuwandeln
findAll(tagName: list/ set, tagAttribute: dict, recursion = True, text (ignorieren), limit = None (bei 1 == fin())) -> fetcht und speichert in einer Liste
für tagAttribute werden manchmal regEx gebaucht, macht Dinge leichter
Tag.attrs -> Returned ein dict mit allen Attributen.
get_text() returned die Strings ohne den tags (ist "schöner"). Sollte als letztes geschehen, da wir mit den Tags navigieren!!!
Hierarchie in den Tags (da nested Struktur): Eine Ebene drunter = children, Irgendeine Ebene drunter = descendants
next_siblings() ist innerhalb einer Ebene (horizontal)
"""
# Welche Funktionen werden oft re-used?
def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("Diese Website existiert nicht")
        return None
    try:
        bsObj = BeautifulSoup(html.read(), features="lxml")
        title = bsObj.h1
    except AttributeError as e:
        return None
    return title

title = get_title("http://pythonscraping.com/pages/page1.html")
if title is None:
    print("No title found")
else:
    print(title)


"""
html = urlopen("http://pythonscraping.com/pages/page1.html")
#Two potential Errors: Not finding the site; Not finding the server -> Exception Handling
#Im Allgemeinen sehr gute Praxis mit Exception Handling, da Fehler "None" Output haben

#print(html.read()) #Gibt den HTML Source Code aus -> Gibt aber noch CSS und JS!

bsObj = BeautifulSoup(html.read(), features="lxml")
print(bsObj.div) #Was nach dem Punkt steht ist der Tag, der ausgegeben wird!
"""
#find(), findAll(), get_text(), RegEx!!!, tag, name, attrs
#Bis ausschließlich Output in Documentation & Chapter 2 vom Buch (oder auch 3?)
