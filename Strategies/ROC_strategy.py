from enviroments_variables import LOGIN, PASSWORD, SERVER, PATH, SYMBOL, LOT, MAGIC
import MetaTrader5 as mt5
from financial_tools.financial_tools import ROC_from_pos
import time

# visualizza i dati sul pacchetto MetaTrader 5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

mt5.shutdown()

########################################################################################################################
print("=" * 200 + '\n' + "=" * 200)
########################################################################################################################
# stabilisce la connessione al terminale MetaTrader 5
if not mt5.initialize(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER):
    print("initialize() fallito, error code =", mt5.last_error())
    quit()

# visualizza i dati sulla versione MetaTrader 5
print(mt5.version())

# ora si connette ad un account di trading specificando la password
authorized = mt5.login(login=LOGIN, password=PASSWORD, server=SERVER)
if authorized:
    # visualizza i dati dell'account di trading 'così come sono'
    print(mt5.account_info())
    # visualizza i dati del conto di trading sotto forma di un elenco
    print("Show account_info()._asdict():")
    account_info_dict = mt5.account_info()._asdict()
    for prop in account_info_dict:
        print("  {}={}".format(prop, account_info_dict[prop]))
else:
    print("fallimento nella connessione all'account #{}, error code: {}".format(26947266, mt5.last_error()))
########################################################################################################################
print("=" * 200 + '\n' + "=" * 200)
########################################################################################################################

cnt = 0
orders = []
long_condition_1 = False
long_condition_2 = False
long_condition_3 = False
close_condition = False

while(True):

    time.sleep(1)

    account_info_dict = mt5.account_info()._asdict()

    balance = account_info_dict["balance"]
    margin_free = account_info_dict["margin_free"]

    #####################################################
    ROC_100 = ROC_from_pos(0, 200, symbol=SYMBOL, time_frame=mt5.TIMEFRAME_H4, timeperiod=100)[-1]
    ROC_50 = ROC_from_pos(0, 200, symbol=SYMBOL, time_frame=mt5.TIMEFRAME_H4, timeperiod=50)[-1]
    ROC_20 = ROC_from_pos(0, 200, symbol=SYMBOL, time_frame=mt5.TIMEFRAME_H4, timeperiod=20)[-1]
    #####################################################

    #####################################################
    if cnt > 1:
        ROC_20_down_0_previous_state = ROC_20_down_0_current_state
        ROC_20_up_negative5_previous_state = ROC_20_up_negative5_current_state

    if ROC_20 >= 0:
        ROC_20_down_0_state = False
    else:
        ROC_20_down_0_state = True
    if ROC_20 >= -5:
        ROC_20_up_negative5_state = True
    else:
        ROC_20_up_negative5_state = False

    ROC_20_down_0_current_state = ROC_20_down_0_state
    ROC_20_up_negative5_current_state = ROC_20_up_negative5_state
    #####################################################

    #####################################################
    long_condition_1 = ROC_100 >= 0
    long_condition_2 = ROC_50 >= 0
    if cnt > 1:
        long_condition_3 = ROC_20_down_0_previous_state and not ROC_20_down_0_current_state
        close_condition = ROC_20_up_negative5_previous_state and not ROC_20_up_negative5_current_state
    #####################################################

    if cnt > 1 and int(time.time()) % 10 == 0:
        print("=" * 200)
        print(f"  | ROC(100) > 0: {long_condition_1} | ROC(50) > 0: {long_condition_2} | "
              f"ROC(20) up cross 0: {long_condition_3} | ROC(20) down cross -5: {close_condition} | \n")

        account_info_dict = mt5.account_info()._asdict()

        for prop in account_info_dict:
            print("  {}={}".format(prop, account_info_dict[prop]))

        print(f"\n\n  {time.strftime('%d/%m/%Y')}-{time.strftime('%H:%M:%S')}")
        print("=" * 200)

        if long_condition_1 and long_condition_2 and long_condition_3:
            print("=" * 200)
            print(f"  Buy signal: {long_condition_1 and long_condition_2 and long_condition_3}")
            print("=" * 200)
        elif close_condition:
            print("=" * 200)
            print(f"  Sell signal: {close_condition} \n")
            print("=" * 200)
    #####################################################
    if long_condition_1 and long_condition_2 and long_condition_3:

        point = mt5.symbol_info(SYMBOL).point
        price = mt5.symbol_info_tick(SYMBOL).ask
        deviation = 20
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": SYMBOL,
            "volume": LOT,
            "type": mt5.ORDER_TYPE_BUY,
            "price": price,
            "sl": 0.0, # no stop loss
            "tp": price * 100, # no take profit
            "deviation": deviation,
            "magic": MAGIC,
            "comment": "python script open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN,
        }

        # invia una richiesta di trading
        result = mt5.order_send(request)
        # controlla il risultato dell'esecuzione
        print("1. order_send(): by {} {} lots at {} with deviation={} points".format(SYMBOL, LOT, price, deviation));
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print("2. order_send fallito, retcode={}".format(result.retcode))
        else:
            orders.append(result.order)

    if close_condition and orders:# presente ordine in atto:

        for order in orders:
            position_id = order
            price = mt5.symbol_info_tick(SYMBOL).bid
            deviation = 20
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": SYMBOL,
                "volume": LOT,
                "type": mt5.ORDER_TYPE_SELL,
                "position": position_id,
                "price": price,
                "deviation": deviation,
                "magic": MAGIC,
                "comment": "python script close",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_IOC,
            }

            # invia una richiesta di trading
            result = mt5.order_send(request)
            # controlla il risultato dell'esecuzione
            print("3. chiudi pozione #{}: sell {} {} lotti a {} con deviazione={} punti".format(position_id, SYMBOL, LOT,
                                                                                                price,
                                                                                                deviation))
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                print("4. order_send fallito, retcode={}".format(result.retcode))
                print("   risultato", result)
            else:
                print("4. posizione #{} chiusa, {}".format(position_id, result))
                orders.remove(order)
    #####################################################
    cnt += 1
