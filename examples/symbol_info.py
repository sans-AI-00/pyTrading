from login_environments_variables import LOGIN, PASSWORD, SERVER, PATH
import MetaTrader5 as mt5

# visualizza i dati sul pacchetto MetaTrader 5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# stabilisce la connessione al terminale MetaTrader 5
if not mt5.initialize(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER):
    print("initialize() fallito, error code =", mt5.last_error())
    quit()

# tenta di abilitare la visualizzazione del simbolo EURJPY in MarketWatch
selected = mt5.symbol_select("EURJPY", True)
if not selected:
    print("Fallimento nel selezionare EURJPY")
    mt5.shutdown()
    quit()

# visualizza le proprietà del simbolo EURJPY
symbol_info = mt5.symbol_info("EURJPY")
if symbol_info != None:
    # mostra i dati del terminale 'così come sono'
    print(symbol_info)
    print("EURJPY: spread =", symbol_info.spread, "  digits =", symbol_info.digits)
    # mostra le proprietà del simbolo come lista
    print("Show symbol_info(\"EURJPY\")._asdict():")
    symbol_info_dict = mt5.symbol_info("EURJPY")._asdict()
    for prop in symbol_info_dict:
        print("  {}={}".format(prop, symbol_info_dict[prop]))

# interrompe la connessione al terminale MetaTrader 5
mt5.shutdown()