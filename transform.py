import extract
import pandas as pd

#TO-DO: Immer nur das erste hinzufügen (soll dann oben stehen)
#       Erste Spalte date time sieht komisch aus?

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

def df_cleaning(df, column, value):
    #Diese Funktion ist eigentlich unnötig, da sehr saubere Daten
    print(df[df.isnull().any(axis=1)])
    df[column].fillna(value)
    df.drop_duplicates()


def new_column(df, column_name="rate_of_change"): #dtype float? Oder gibt es bessere Alternativen?
    df[column_name] = -100 * (1 - df["close"]/df["close"].shift(-1))
    df.fillna(0)
    return df

df = extract.encode_single(extract.url)
df_info(df)
df = new_column(df)
df = df.where((pd.notnull(df)), 0) #NaN mit "0" ersetzen


#Gibt es eine Möglichkeit ein Recommendation-System zu machen, bei dem unpassende Spalten dtype ändern?
#-> Eigenes Projekt


#Welche Fragen könnten einen interessieren? All-time high, wie viel ist es seitdem runtergegangen?
#Wirtschaftler mögen Prozentwerte viel lieber
#Average daily return, correlation between stocks, periods of significant change
