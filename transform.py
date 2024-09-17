import extract
import pandas as pd

#TO-DO: Alles abgehakt :)
#In diesem Fall sind die Daten schon sehr "sauber". Bei anderem Projekt auf unsaubere Daten achten zur Übung

def df_info(df):
    """
    Gibt Überblick über den jeweiligen Dataframe
    """
    print(df.head())
    print(f"Anzahl der Zeilen und Spalten: {df.shape}")
    print(df.dtypes)

def df_cleaning(df, column, value):
    #Diese Funktion ist eigentlich unnötig, da sehr saubere Daten
    print(df[df.isnull().any(axis=1)])
    df[column].fillna(value)
    df.drop_duplicates()


def new_column(df, column_name="rate_of_change"):
    """
    Kreiert neue Spalte "Rate of change". Wird berechnet durch close-Wert geteilt durch close-Wert vom Vortag,
    um prozentuale Änderungsrate zum Vortag zu erkennen.
    """
    df[column_name] = -100 * (1 - df["close"]/df["close"].shift(-1))
    df.fillna(0)
    return df

def transform(data):
    """
    Alle vorherigen Funktionen in logischer Reienfolge. Dabei wird der Wert des letzten Eintrages durch 0 ersetzt,
    da dieser keinen Vortag hat und NaN ist.
    """
    df = extract.encode_single(data)#(extract.url)
    df_info(df)
    df = new_column(df)
    df = df.where((pd.notnull(df)), 0) #NaN mit "0" ersetzen
    return df

#Gibt es eine Möglichkeit ein Recommendation-System zu machen, bei dem unpassende Spalten dtype ändern?
#-> Eigenes Projekt


#Welche Fragen könnten einen interessieren? All-time high, wie viel ist es seitdem runtergegangen?
#Wirtschaftler mögen Prozentwerte viel lieber
#Average daily return, correlation between stocks, periods of significant change
