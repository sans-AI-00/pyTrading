from login_environments_variables import LOGIN, PASSWORD, SERVER, PATH
import MetaTrader5 as mt5

# visualizza i dati sul pacchetto MetaTrader 5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# stabilisce la connessione al terminale MetaTrader 5
if not mt5.initialize(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER):
    print("initialize() fallito, error code =", mt5.last_error())
    quit()

# verifica la presenza di ordini attivi
orders = mt5.orders_total()
if orders > 0:
    print("Totale ordini=", orders)
else:
    print("Ordini non trovati")

# interrompe la connessione al terminale MetaTrader 5
mt5.shutdown()