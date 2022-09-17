from login_environments_variables import LOGIN, PASSWORD, SERVER, PATH
import MetaTrader5 as mt5
from datetime import datetime
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

# ottiene il numero di deals nella cronistoria
from_date = datetime(2020, 1, 1)
to_date = datetime.now()
# ottiene deals per simboli i cui nomi contengono "GBP" entro un intervallo specificato
deals = mt5.history_deals_get(from_date, to_date, group="*GBP*")
if deals == None:
    print("Nessun deals per il gruppo=\"*USD*\", error code={}".format(mt5.last_error()))
elif len(deals) > 0:
    print("history_deals_get({}, {}, group=\"*GBP*\")={}".format(from_date, to_date, len(deals)))

# ottiene deals per simboli i cui nomi non contengono né "EUR" né "GBP"
deals = mt5.history_deals_get(from_date, to_date, group="*,!*EUR*,!*GBP*")
if deals == None:
    print("Nessun deal, error code={}".format(mt5.last_error()))
elif len(deals) > 0:
    print("history_deals_get(from_date, to_date, group=\"*,!*EUR*,!*GBP*\") =", len(deals))
    # mostra tutti i deals ottenuti 'così come sono'<
    for deal in deals:
        print("  ", deal)
    print()
    # mostra questi deals come una tabella usando pandas.DataFrame
    df = pd.DataFrame(list(deals), columns=deals[0]._asdict().keys())
    df['time'] = pd.to_datetime(df['time'], unit='s')
    print(df)
print("")

# ottiene tutti i deals relativi alla posizione #530218319
position_id = 530218319
position_deals = mt5.history_deals_get(position=position_id)
if position_deals == None:
    print("Nessun deal con la posizione #{}".format(position_id))
    print("error code =", mt5.last_error())
elif len(position_deals) > 0:
    print("Deals con id posizione #{}: {}".format(position_id, len(position_deals)))
    # mostra questi deals come una tabella usando pandas.DataFrame
    df = pd.DataFrame(list(position_deals), columns=position_deals[0]._asdict().keys())
    df['time'] = pd.to_datetime(df['time'], unit='s')
    print(df)

# interrompe la connessione al terminale MetaTrader 5
mt5.shutdown()