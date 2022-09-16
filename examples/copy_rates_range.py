from login_enviroments_variables import LOGIN, PASSWORD, SERVER, PATH
from datetime import datetime
import MetaTrader5 as mt5

# visualizza i dati sul pacchetto MetaTrader 5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# importa il modulo 'pandas' per visualzzare i dati ottenuti in forma tabellare
import pandas as pd

pd.set_option('display.max_columns', 500)  # numero di colonne da visualizzare
pd.set_option('display.width', 1500)  # max table width to display
# import pytz module for working with time zone
import pytz

# stabilisce la connessione al terminale MetaTrader 5
if not mt5.initialize(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER):
    print("initialize() fallito, error code =", mt5.last_error())
    quit()

# imposta fuso orario UTC
timezone = pytz.timezone("Etc/UTC")
# crea oggetti 'datetime' nel fuso orario UTC per evitare l'implementazione di un offset fuso orario locale
utc_from = datetime(2020, 1, 10, tzinfo=timezone)
utc_to = datetime(2020, 1, 11, hour=13, tzinfo=timezone)
# ottiene barre da USDJPY M5 nell'intervallo 2020.01.10 00:00 - 2020.01.11 13:00 in UTC time zone
rates = mt5.copy_rates_range("USDJPY", mt5.TIMEFRAME_M5, utc_from, utc_to)

# chiude la connessione a MetaTrader 5 terminal
mt5.shutdown()

# visualizza ogni elemento dei dati ottenuti in una nuova riga
print("Visualizza i dati ottenuti 'così come sono' ")
counter = 0
for rate in rates:
    counter += 1
    if counter <= 10:
        print(rate)

# crea DataFrame dai dati ottenuti
rates_frame = pd.DataFrame(rates)
# converte il tempo in secondi nel formato 'datetime'
rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')

# display data
print("\nMostra dataframe con i dati")
print(rates_frame.head(10))