from login_environments_variables import LOGIN, PASSWORD, SERVER, PATH
import MetaTrader5 as mt5

# visualizza i dati sul pacchetto MetaTrader 5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# stabilisce la connessione al terminale MetaTrader 5
if not mt5.initialize(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER):
    print("initialize() fallito, error code =", mt5.last_error())
    quit()

# ottiene tutti i simboli
symbols = mt5.symbols_get()
print('Simboli: ', len(symbols))
count = 0
# visualizza i primi cinque
for s in symbols:
    count += 1
    print("{}. {}".format(count, s.name))
    if count == 5: break
print()

# ottiene simboli contenenti RU nei loro nomi
ru_symbols = mt5.symbols_get("*RU*")
print('len(*RU*): ', len(ru_symbols))
for s in ru_symbols:
    print(s.name)
print()

# ottiene simboli i cui nomi non contengono USD, EUR, JPY e GBP
group_symbols = mt5.symbols_get(group="*,!*USD*,!*EUR*,!*JPY*,!*GBP*")
print('len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):', len(group_symbols))
for s in group_symbols:
    print(s.name, ":", s)

# interrompe la connessione al terminale MetaTrader 5
mt5.shutdown()