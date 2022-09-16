from login_enviroments_variables import LOGIN, PASSWORD, SERVER, PATH
import MetaTrader5 as mt5

# visualizza i dati sul pacchetto MetaTrader 5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# stabilisce la connessione al terminale MetaTrader 5
if not mt5.initialize(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER):
    print("initialize() fallito, error code =", mt5.last_error())
    quit()

# tentativo di abilitare la visualizzazione di GBPUSD in MarketWatch
selected = mt5.symbol_select("GBPUSD", True)
if not selected:
    print("Fallimento nel selezionare GBPUSD")
    mt5.shutdown()
    quit()

# mostra l'ultimo tick GBPUSD
lasttick = mt5.symbol_info_tick("GBPUSD")
print(lasttick)
# visualizza i valori dei tick sotto forma di un elenco
print("Mostra symbol_info_tick(\"GBPUSD\")._asdict():")
symbol_info_tick_dict = mt5.symbol_info_tick("GBPUSD")._asdict()
for prop in symbol_info_tick_dict:
    print("  {}={}".format(prop, symbol_info_tick_dict[prop]))

# interrompe la connessione al terminale MetaTrader 5
mt5.shutdown()