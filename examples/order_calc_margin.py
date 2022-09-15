from enviroments_variables import LOGIN, PASSWORD, SERVER, PATH
import MetaTrader5 as mt5

# visualizza i dati sul pacchetto MetaTrader 5
print("Autore del pacchetto MetaTrader5:", mt5.__author__)
print("Versione del pacchetto MetaTrader5:", mt5.__version__)

# stabilisce la connessione al terminale MetaTrader 5
if not mt5.initialize(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER):
    print("initialize() fallito, error code =", mt5.last_error())
    quit()

# ottiene valuta del conto
account_currency = mt5.account_info().currency
print("Valuta del conto:", account_currency)

# dispone la lista dei simboli
symbols = ("EURUSD", "GBPUSD", "USDJPY", "USDCHF", "EURJPY", "GBPJPY")
print("Simboli col margine da controllare:", symbols)
action = mt5.ORDER_TYPE_BUY
lot = 0.1
for symbol in symbols:
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(symbol, "non trovato, saltato")
        continue
    if not symbol_info.visible:
        print(symbol, "se non visibile, provare ad attivarlo")
        if not mt5.symbol_select(symbol, True):
            print("symbol_select({}}) fallito, saltato", symbol)
            continue
    ask = mt5.symbol_info_tick(symbol).ask
    margin = mt5.order_calc_margin(action, symbol, lot, ask)
    if margin != None:
        print("   {} buy {} margine lotto: {} {}".format(symbol, lot, margin, account_currency));
    else:
        print("order_calc_margin fallito: , error code =", mt5.last_error())

# interrompe la connessione al terminale MetaTrader 5
mt5.shutdown()