from login_environments_variables import LOGIN, PASSWORD, SERVER, PATH
import MetaTrader5 as mt5

# mostra i dati sul package MetaTrader 5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# stabilisce una connessione al terminale di trading MetaTrader 5
if not mt5.initialize(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER):
    print("initialize() fallito, error code =", mt5.last_error())
    quit()

# ottiene la valuta dell'account
account_currency = mt5.account_info().currency
print("Valuta dell'account:", account_currency)

# prepara la struttura richiesta
symbol = "USDJPY"
symbol_info = mt5.symbol_info(symbol)
if symbol_info is None:
    print(symbol, "non trovato, non posso chiamare order_check()")
    mt5.shutdown()
    quit()

# se il simbolo non è disponibile in MarketWatch, aggiungerlo
if not symbol_info.visible:
    print(symbol, "non è visibile, prova ad attivarlo")
    if not mt5.symbol_select(symbol, True):
        print("symbol_select({}}) failed, exit", symbol)
        mt5.shutdown()
        quit()

# prepara la richiesta
point = mt5.symbol_info(symbol).point
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": 1.0,
    "type": mt5.ORDER_TYPE_BUY,
    "price": mt5.symbol_info_tick(symbol).ask,
    "sl": mt5.symbol_info_tick(symbol).ask - 100 * point,
    "tp": mt5.symbol_info_tick(symbol).ask + 100 * point,
    "deviation": 10,
    "magic": 234000,
    "comment": "python script",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_RETURN,
}

# esegue il controllo e visualizza il risultato "così com'è"
result = mt5.order_check(request)
print(result);
# richiede il risultato come dizionario e lo visualizza elemento per elemento
result_dict = result._asdict()
for field in result_dict.keys():
    print("   {}={}".format(field, result_dict[field]))
    # se questa è una struttura di richiesta di trading, visualizzala anche elemento per elemento
    if field == "request":
        traderequest_dict = result_dict[field]._asdict()
        for tradereq_filed in traderequest_dict:
            print("       traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))

# interrompe la connessione al terminale MetaTrader
mt5.shutdown()
