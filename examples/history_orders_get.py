from login_environments_variables import LOGIN, PASSWORD, SERVER, PATH
from datetime import datetime
import MetaTrader5 as mt5
import pandas as pd

pd.set_option('display.max_columns', 500)  # numero di colonne da visualizzare
pd.set_option('display.width', 1500)  # larghezza massima della tabella da visualizzare
# visualizza i dati sul pacchetto MetaTrader 5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)
print()
# stabilisce la connessione al terminale MetaTrader 5
if not mt5.initialize(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER):
    print("initialize() fallito, error code =", mt5.last_error())
    quit()

# ottiene il numero di ordini nella cronistoria
from_date = datetime(2020, 1, 1)
to_date = datetime.now()
history_orders = mt5.history_orders_get(from_date, to_date, group="*GBP*")
if history_orders == None:
    print("Nessun ordine della cronistoria con gruppo=\"*GBP*\", error code={}".format(mt5.last_error()))
elif len(history_orders) > 0:
    print("history_orders_get({}, {}, group=\"*GBP*\")={}".format(from_date, to_date, len(history_orders)))
print()

# mostra tutti gli ordini storici per un ticket di posizione
position_id = 530218319
position_history_orders = mt5.history_orders_get(position=position_id)
if position_history_orders == None:
    print("Nessun ordine con posizione #{}".format(position_id))
    print("error code =", mt5.last_error())
elif len(position_history_orders) > 0:
    print("Totale ordini della cronistoria sulla posizione #{}: {}".format(position_id, len(position_history_orders)))
    # visualizza tutti gli ordini storici con il ticket della posizione specificata
    for position_order in position_history_orders:
        print(position_order)
    print()
    # visualizza questi ordini come una tabella usando pandas.DataFrame
    df = pd.DataFrame(list(position_history_orders), columns=position_history_orders[0]._asdict().keys())
    df.drop(
        ['time_expiration', 'type_time', 'state', 'position_by_id', 'reason', 'volume_current', 'price_stoplimit', 'sl',
         'tp'], axis=1, inplace=True)
    df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')
    df['time_done'] = pd.to_datetime(df['time_done'], unit='s')
    print(df)

# interrompe la connessione al terminale MetaTrader 5
mt5.shutdown()