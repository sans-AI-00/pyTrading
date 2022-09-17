from login_environments_variables import LOGIN, PASSWORD, SERVER, PATH
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

# ottiene posizioni aperte su USDCHF
positions = mt5.positions_get(symbol="USDCHF")
if positions == None:
    print("Niente posizioni su USDCHF, error code={}".format(mt5.last_error()))
elif len(positions) > 0:
    print("Totale posizioni su USDCHF =", len(positions))
    # mostra tutte le posizioni aperte
    for position in positions:
        print(position)

# ottiene l'elenco delle posizioni sui simboli i cui nomi contengono "*USD*"
usd_positions = mt5.positions_get(group="*USD*")
if usd_positions == None:
    print("Niente posizioni col gruppo=\"*USD*\", error code={}".format(mt5.last_error()))
elif len(usd_positions) > 0:
    print("positions_get(group=\"*USD*\")={}".format(len(usd_positions)))
    # visualizza queste posizioni come una tabella usando pandas.DataFrame
    df = pd.DataFrame(list(usd_positions), columns=usd_positions[0]._asdict().keys())
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.drop(['time_update', 'time_msc', 'time_update_msc', 'external_id'], axis=1, inplace=True)
    print(df)

# interrompe la connessione al terminale MetaTrader 5
mt5.shutdown()