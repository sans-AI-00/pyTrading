from login_enviroments_variables import LOGIN, PASSWORD, SERVER, PATH
from datetime import datetime
import MetaTrader5 as mt5

# visualizza i dati sul pacchetto MetaTrader 5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# stabilisce la connessione al terminale MetaTrader 5
if not mt5.initialize(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER):
    print("initialize() fallito, error code =", mt5.last_error())
    quit()

# ottiene il numero di deals nella cronistoria
from_date = datetime(2020, 1, 1)
to_date = datetime.now()
deals = mt5.history_deals_total(from_date, to_date)
if deals > 0:
    print("Deals totali=", deals)
else:
    print("Deals non trovati nella cronistoria")

# interrompe la connessione al terminale MetaTrader 5
mt5.shutdown()