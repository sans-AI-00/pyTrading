import pandas as pd
import numpy as np
import MetaTrader5 as mt5
import talib

def ROC_from_pos(start, n, symbol="EURUSD", time_frame=mt5.TIMEFRAME_H4, timeperiod=10):
    # ottiene ultime 100 barre EUR4 USD H4
    rates = mt5.copy_rates_from_pos(symbol, time_frame, start, n)

    #print("Mostra i dati ottenuti 'così come sono' '")
    #for rate in rates:
    #    print(rate)

    # create DataFrame dai dati ottenuti
    rates_frame = pd.DataFrame(rates)
    # converti il tempo in secondi nel formato datetime
    rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')

    # visualizza dati
    #print("\nMostra dataframe con dati")
    #print(rates_frame)

    close = np.array([rate[4] for rate in rates])
    #print(close)

    ROC_values = talib.ROC(close, timeperiod=timeperiod)
    #print(ROC_values)

    return ROC_values