from enviroments_variables import LOGIN, PASSWORD, SERVER, PATH
from datetime import datetime
import MetaTrader5 as mt5

# visualizza i dati sul pacchetto MetaTrader 5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# importa il modulo 'pandas' per visualizzare i dati ottenuti in forma tabellare
import pandas as pd

pd.set_option('display.max_columns', 500)  # numero di colonne da visualizzare
pd.set_option('display.width', 1500)  # max table width to display
# importa il modulo pytz per lavorare con il fuso orario
import pytz

# stabilisce la connessione al terminale MetaTrader 5
if not mt5.initialize(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER):
    print("initialize() fallito, error code =", mt5.last_error())
    quit()

# imposta il fuso orario su UTC
timezone = pytz.timezone("Etc/UTC")
# crea un oggetto 'datetime' nel fuso orario UTC per evitare l'implementazione di un fuso orario locale
utc_from = datetime(2020, 1, 10, tzinfo=timezone)
# ottiene 10 barre EUR4 USD H4 a partire dal 01.10.2020 nel fuso orario UTC
rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_H4, utc_from, 10)

# interrompe la connessione al terminale MetaTrader 5
mt5.shutdown()
# visualizza ogni elemento dei dati ottenuti in una nuova riga
print("Mostra i dati ottenuti 'così come sono' '")
for rate in rates:
    print(rate)

# create DataFrame dai dati ottenuti
rates_frame = pd.DataFrame(rates)
# converti il tempo in secondi nel formato datetime
rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')

# visualizza dati
print("\nMostra dataframe con dati")
print(rates_frame)