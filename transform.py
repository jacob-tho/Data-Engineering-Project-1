import extract
import pandas as pd

#TO-DO: Neue Spalte "rate of change" von closed value. Immer nur das erste hinzufügen (soll dann oben stehen)
#       Erste Spalte date time sieht sehr komisch aus

"""
Pandas section:
Exploration: head, info, describe, shape, columns, dtypes
Cleaning: drop_na, fill_na, drop_duplicates, replace, rename, as_type
Fehlt noch Ausreißer-Bereinigung
Transformation: apply, map, groupby, pivot?, sort_values, merge, agg, concat
-> Integration
Selection/Filtering: loc, iloc, [condition]
"""
#Duplikate entfernen, Null-Werte bereinigen, Datentypen checken
#Was sind noch Standard / Must-do Aufgaben mit Pandas?
#In diesem Fall sind die Daten schon sehr "sauber". Bei anderem Projekt auf unsaubere Daten achten zur Übung

def df_info(df):
    print(df.head())
    print(f"Anzahl der Zeilen und Spalten: {df.shape}")
    print(df.dtypes)
df_info(extract.financial_data)
#extract.financial_data = extract.financial_data.astype({"timestamp": "datetime64[ns]"})
#Alternative: financial_data = pd.to_datetime(financial_data["timestamp"])

def df_cleaning(df, column, value):
    #Ausgeben, ob null-Werte (Bool), bei true bereinigen
    print(df[df.isnull().any(axis=1)])
    df[column].fillna(value)
    df.drop_duplicates()
#financial_data.drop_duplicates()

def new_column(column_name="rate_of_change"): #dtype float?
    pass

    
#Gibt es eine Möglichkeit ein Recommendation-System zu machen, bei dem unpassende Spalten dtype ändern?
#-> Eigenes Projekt

'''
To-Do: Unclean Dataset aufbereiten. Funktionen zur Bereinigung und Standardisierung schreiben
Spalten hinzufügen?
'''

#Welche Fragen könnten einen interessieren? All-time high, wie viel ist es seitdem runtergegangen?
#Wirtschaftler mögen Prozentwerte viel lieber
#Average daily return, correlation between stocks, periods of significant change
