from login_enviroments_variables import LOGIN, PASSWORD, SERVER, PATH
import MetaTrader5 as mt5

# visualizza i dati sul pacchetto MetaTrader 5
print("Autore del pacchetto MetaTrader5:", mt5.__author__)
print("Versione del pacchetto MetaTrader5:", mt5.__version__)

# stabilisce la connessione al terminale MetaTrader 5
if not mt5.initialize(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER):
    print("initialize() fallito, error code =", mt5.last_error())
    quit()

# ottiene la valuta dell'account
account_currency = mt5.account_info().currency
print("Valuta dell'account:", account_currency)

# dispone la lista dei simboli
symbols = ("EURUSD", "GBPUSD", "USDJPY")
print("Simboli da controllarne il margine:", symbols)
# profitto stimato per acquisti e vendite
lot = 1.0
distance = 300
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
    point = mt5.symbol_info(symbol).point
    symbol_tick = mt5.symbol_info_tick(symbol)
    ask = symbol_tick.ask
    bid = symbol_tick.bid
    buy_profit = mt5.order_calc_profit(mt5.ORDER_TYPE_BUY, symbol, lot, ask, ask + distance * point)
    if buy_profit != None:
        print("   buy {} {} lot: profitto su {} punti => {} {}".format(symbol, lot, distance, buy_profit,
                                                                       account_currency));
    else:
        print("order_calc_profit(ORDER_TYPE_BUY) fallito, error code =", mt5.last_error())
    sell_profit = mt5.order_calc_profit(mt5.ORDER_TYPE_SELL, symbol, lot, bid, bid - distance * point)
    if sell_profit != None:
        print("   sell {} {} lots: profitto su {}punti => {} {}".format(symbol, lot, distance, sell_profit,
                                                                        account_currency));
    else:
        print("order_calc_profit(ORDER_TYPE_SELL) fallito, error code =", mt5.last_error())
    print()

# interrompe la connessione al terminale MetaTrader
mt5.shutdown()