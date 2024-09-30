import requests
import json

def show_values(schema):
    """
    Wenn nötig: Zeige alle Werte des Schemas
    """
    response = requests.get(f"https://www.lohse-und-lohse.de/DEP/get_complete_stock_data.php?pw=lo34bf&symbol={schema}")
    return json.loads(response.text)

def insert_one(df, schema):
    """
    Wird verwendet für insert_schema(). Wird aufgerufen, falls Schema schon Werte enthält und
    der neuste Wert noch nicht in der Datenbank ist.
    """
    #df = dataframe.values.tolist()[0]
    " Transformiere die Liste in ein Dictionary "
    data_obj = {
            "timestamp": df[0],
            "open": df[1],
            "high": df[2],
            "low": df[3],
            "close": df[4],
            "volume": df[5],
            "rate_of_change": df[6],
            }
    json_obj = json.dumps(data_obj)
    requests.get(f"https://www.lohse-und-lohse.de/DEP/insert_single_stock.php?pw=lo34bf&symbol={schema}&stock_data={json_obj}")

def new_table(symbol):
    """
    Neues Schema, wenn es nicht existiert. Datentypen werden von dataframe übernommen. ID kommt noch hinzu.
    """
    requests.get(f"https://www.lohse-und-lohse.de/DEP/create_table_if_not_exists.php?pw=lo34bf&symbol={symbol}")

new_table("QUACK")
