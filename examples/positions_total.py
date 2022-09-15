from enviroments_variables import LOGIN, PASSWORD, SERVER, PATH
import MetaTrader5 as mt5

# visualizza i dati sul pacchetto MetaTrader 5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# stabilisce la connessione al terminale MetaTrader 5
if not mt5.initialize(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER):
    print("initialize() fallito, error code =", mt5.last_error())
    quit()

# verifica la presenza di posizioni aperte
positions_total = mt5.positions_total()
if positions_total > 0:
    print("Totale posizioni=", positions_total)
else:
    print("Posizioni non trovate")

# interrompe la connessione al terminale MetaTrader 5
mt5.shutdown()