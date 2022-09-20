import MetaTrader5 as mt5
import pandas as pd
from login_environments_variables import LOGIN, SERVER, PATH, PASSWORD
# from datetime import datetime
# import time

def convert_from_array_to_dataframe(data):
    data_as_dict = {"Open": [], "High": [], "Low": [], "Close": [], "Volume": []}
    keys = ("Open", "High", "Low", "Close", "Volume")
    index = list()
    for row in data:
        time_stamp = row[0]
        #date_time = datetime.fromtimestamp(time_stamp)
        #index.append(date_time.strftime('%d/%m/%Y').replace("/", "-"))#+ " " + date_time.strftime('%H:%M:%S'))
        index.append(time_stamp)
        for key in keys:
            data_as_dict[key].append(row[keys.index(key) + 1])

    data_as_dataframe = pd.DataFrame(index=None, data=data_as_dict)

    return data_as_dataframe

#######################################################################
############################# EXAMPLE #################################


if __name__ == "__main__":

    if not mt5.initialize(server=SERVER, path=PATH, login=LOGIN, password=PASSWORD):
        print("initialize() fallito, error code =", mt5.last_error())
        quit()

    data_as_array = mt5.copy_rates_from_pos("Google", mt5.TIMEFRAME_H4, 0, 10000)

    print("=" * 25 + "Data as array" + "=" * 25)
    print(data_as_array)
    print("\n")
    data_as_dataframe = convert_from_array_to_dataframe(data_as_array)

    print("=" * 15 + "Data as dataframe" + "=" * 15)
    print(data_as_dataframe)
    print("\n")