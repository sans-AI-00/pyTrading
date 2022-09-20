LOGIN = 26947266
PASSWORD = "G7!-#pL4?"
SERVER = "XM.COM-MT5"
PATH = "C:\\Program Files\\XM_MT5\\terminal64.exe"

import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime
import time
# covert list to dataframe

if not mt5.initialize(server=SERVER, path=PATH, login=LOGIN, password=PASSWORD):
    print("initialize() fallito, error code =", mt5.last_error())
    quit()

rates = mt5.copy_rates_from_pos("EURUSD", mt5.TIMEFRAME_H4, 0, 10000)

print(rates)

def convert_from_array_to_dataframe(data):
    data_as_dict = {"Open": [], "High": [], "Low": [], "Close": [], "Volume": []}
    keys = ("Open", "High", "Low", "Close", "Volume")
    index = list()
    for row in data:
        time_stamp = row[0]
        date_time = datetime.fromtimestamp(time_stamp)
        #index.append(date_time.strftime('%d/%m/%Y').replace("/", "-"))#+ " " + date_time.strftime('%H:%M:%S'))
        index.append(time.time())
        for key in keys:
            data_as_dict[key].append(row[keys.index(key) + 1])

    data_as_dataframe = pd.DataFrame(index=None, data=data_as_dict)

    return data_as_dataframe
