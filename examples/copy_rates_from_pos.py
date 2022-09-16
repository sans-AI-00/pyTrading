from login_enviroments_variables import LOGIN, PASSWORD, SERVER, PATH
import MetaTrader5 as mt5

# visualizza i dati sul pacchetto MetaTrader 5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# importa il modulo 'pandas' per visualizzare i dati ottenuti in forma tabellare
import pandas as pd

pd.set_option('display.max_columns', 500)  # numero di colonne da visualizzare
pd.set_option('display.width', 1500)  # max table width to display

# stabilisce la connessione al terminale MetaTrader 5
if not mt5.initialize(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER):
    print("initialize() fallito, error code =", mt5.last_error())
    quit()

# ottiene 10 barre D1 GBPUSD dal giorno corrente
rates = mt5.copy_rates_from_pos("GBPUSD", mt5.TIMEFRAME_D1, 0, 10)

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