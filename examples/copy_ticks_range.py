from enviroments_variables import LOGIN, PASSWORD, SERVER, PATH
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
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# imposta il fuso orario su UTC
timezone = pytz.timezone("Etc/UTC")
# crea oggetti 'datetime' nel fuso orario UTC per evitare l'implementazione di un fuso orario locale
utc_from = datetime(2020, 1, 10, tzinfo=timezone)
utc_to = datetime(2020, 1, 11, tzinfo=timezone)
# richiesta tick di AUDUSD entro 11.01.2020 - 11.01.2020
ticks = mt5.copy_ticks_range("AUDUSD", utc_from, utc_to, mt5.COPY_TICKS_ALL)
print("Tick ricevuti:", len(ticks))

# interrompe la connessione al terminale MetaTrader 5
mt5.shutdown()

# visualizza i dati su ogni tick su una nuova riga
print("Visualizza i ticks ottenuti 'così come sono' ")
count = 0
for tick in ticks:
    count += 1
    print(tick)
    if count >= 10:
        break

# crea DataFrame dai dati ottenuti
ticks_frame = pd.DataFrame(ticks)
# converti il tempo in secondi nel formato datetime
ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit='s')

# display data
print("\nDisplay dataframe with ticks")
print(ticks_frame.head(10))