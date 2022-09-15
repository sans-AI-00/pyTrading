from enviroments_variables import LOGIN, PASSWORD, SERVER, PATH
from datetime import datetime
import MetaTrader5 as mt5

# visualizza i dati sul pacchetto MetaTrader 5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# stabilisce la connessione al terminale MetaTrader 5
if not mt5.initialize(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER):
    print("initialize() fallito, error code =", mt5.last_error())
    quit()

# ottiene il numero di ordini nella cronistoria
from_date = datetime(2020, 1, 1)
to_date = datetime.now()
history_orders = mt5.history_orders_total(from_date, datetime.now())
if history_orders > 0:
    print("Totale ordini cronistorici =", history_orders)
else:
    print("Ordini non trovati nella cronistoria")

# interrompe la connessione al terminale MetaTrader 5
mt5.shutdown()