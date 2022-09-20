import pandas as pd
import numpy as np
import MetaTrader5 as mt5
import talib

def ROC_from_pos(start, n, symbol="EURUSD", time_frame=mt5.TIMEFRAME_H4, timeperiod=10):

    rates = mt5.copy_rates_from_pos(symbol, time_frame, start, n)

    close = np.array([rate[4] for rate in rates])

    ROC_values = talib.ROC(close, timeperiod=timeperiod)

    return ROC_values