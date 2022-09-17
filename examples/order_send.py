from login_environments_variables import LOGIN, PASSWORD, SERVER, PATH
import time
import MetaTrader5 as mt5

# visualizza i dati sul pacchetto MetaTrader 5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# stabilisce la connessione al terminale MetaTrader 5
if not mt5.initialize(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER):
    print("initialize() fallito, error code =", mt5.last_error())
    quit()

print("=" * 200)
print("Show account_info()._asdict():")
account_info_dict = mt5.account_info()._asdict()
for prop in account_info_dict:
    print("  {}={}".format(prop, account_info_dict[prop]))
print("=" * 200)

# prepara la struttura della richiesta di buy
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

lot = 0.1
point = mt5.symbol_info(symbol).point
price = mt5.symbol_info_tick(symbol).ask
deviation = 20
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_BUY,
    "price": price,
    "sl": price - 100 * point,
    "tp": price + 100 * point,
    "deviation": deviation,
    "magic": 234000,
    "comment": "python script open",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_IOC,
}

# invia una richiesta di trading
result = mt5.order_send(request)
# controlla il risultato dell'esecuzione
print("1. order_send(): by {} {} lots at {} with deviation={} points".format(symbol, lot, price, deviation));
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("2. order_send fallito, retcode={}".format(result.retcode))
    # richiede il risultato come dizionario e lo visualizza elemento per elemento
    result_dict = result._asdict()
    for field in result_dict.keys():
        print("   {}={}".format(field, result_dict[field]))
        # se questa è una struttura di richiesta di trading, visualizzala anche elemento per elemento
        if field == "request":
            traderequest_dict = result_dict[field]._asdict()
            for tradereq_filed in traderequest_dict:
                print("       traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))
    print("shutdown() and quit")
    mt5.shutdown()
    quit()

print("=" * 200)
print("Show account_info()._asdict():")
account_info_dict = mt5.account_info()._asdict()
for prop in account_info_dict:
    print("  {}={}".format(prop, account_info_dict[prop]))
print("=" * 200)

print("2. order_send fatto, ", result)
print("   aperta posizione con POSITION_TICKET={}".format(result.order))
print("   sleep per 2 secondi prima di chiudere la posizione #{}".format(result.order))
time.sleep(2)
# crea una richiesta di chiusura
position_id = result.order
price = mt5.symbol_info_tick(symbol).bid
deviation = 20
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": mt5.ORDER_TYPE_SELL,
    "position": position_id,
    "price": price,
    "deviation": deviation,
    "magic": 234000,
    "comment": "python script close",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_IOC,
}
# invia una richiesta di trading
result = mt5.order_send(request)
# controlla il risultato dell'esecuzione
print("3. chiudi pozione #{}: sell {} {} lotti a {} con deviazione={} punti".format(position_id, symbol, lot, price,
                                                                                    deviation))
if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("4. order_send fallito, retcode={}".format(result.retcode))
    print("   risultato", result)
else:
    print("4. posizione #{} chiusa, {}".format(position_id, result))
    # richiede il risultato come dizionario e lo visualizza elemento per elemento
    result_dict = result._asdict()
    for field in result_dict.keys():
        print("   {}={}".format(field, result_dict[field]))
        # se questa è una struttura di richiesta di trading, visualizzala anche elemento per elemento
        if field == "request":
            traderequest_dict = result_dict[field]._asdict()
            for tradereq_filed in traderequest_dict:
                print("       traderequest: {}={}".format(tradereq_filed, traderequest_dict[tradereq_filed]))

print("=" * 200)
print("Show account_info()._asdict():")
account_info_dict = mt5.account_info()._asdict()
for prop in account_info_dict:
    print("  {}={}".format(prop, account_info_dict[prop]))
print("=" * 200)

# interrompe la connessione al terminale MetaTrader 5
mt5.shutdown()