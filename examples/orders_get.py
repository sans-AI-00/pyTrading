from login_enviroments_variables import LOGIN, PASSWORD, SERVER, PATH
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

# visualizza i dati sugli ordini attivi su GBPUSD
orders = mt5.orders_get(symbol="GBPUSD")
if orders == None:
    print("Niente ordini su GBPUSD, error code={}".format(mt5.last_error()))
elif len(orders) > 0:
    print("Totale ordini su GBPUSD:", len(orders))
    # mostra tutti gli ordini attivi
    for order in orders:
        print(order)
print()

# ottiene l'elenco degli ordini sui simboli i cui nomi contengono "*GBP*"
gbp_orders = mt5.orders_get(group="*GBP*")
if gbp_orders == None:
    print("Niente ordini col gruppo=\"*GBP*\", error code={}".format(mt5.last_error()))
elif len(gbp_orders) > 0:
    print("orders_get(group=\"*GBP*\")={}".format(len(gbp_orders)))
    # visualizza questi ordini come una tabella usando pandas.DataFrame
    df = pd.DataFrame(list(gbp_orders), columns=gbp_orders[0]._asdict().keys())
    df.drop(
        ['time_done', 'time_done_msc', 'position_id', 'position_by_id', 'reason', 'volume_initial', 'price_stoplimit'],
        axis=1, inplace=True)
    df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')
    print(df)

# interrompe la connessione al terminale MetaTrader 5
mt5.shutdown()