from login_enviroments_variables import LOGIN, PASSWORD, SERVER, PATH
import MetaTrader5 as mt5

# visualizza i dati sul pacchetto MetaTrader 5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

mt5.shutdown()

# stabilisce la connessione al terminale MetaTrader 5
if not mt5.initialize(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER):
    print("initialize() fallito, error code =", mt5.last_error())
    quit()

# visualizza i dati sulla versione MetaTrader 5
print(mt5.version())

"""
# connessione all'account di trade senza specificare una password ed un server
account = 17221085
authorized = mt5.login(
    account)  # la password del database del terminale viene applicata se i dati di connessione sono impostati per essere ricordati
if authorized:
    print("connesso all'account #{}".format(account))
else:
    print("fallimento nella connessione all'account #{}, error code: {}".format(account, mt5.last_error()))
"""

# ora si connette ad un altro account di trading specificando la password

authorized = mt5.login(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER)
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

# interrompe la connessione al terminale MetaTrader 5
mt5.shutdown()