# Informazioni utili

riga 1-5: si ffettua l'importazione di tutte le librerie necessarie per il corretto funzionamento del codice. 
Da *strategy_environments_variables* si importano le varibili globali *SYMBOL*, *LOT* e *MAGIC*, le quali definiscono 
l'asset sul quale operiamo, l'importo di ogni investimento e la targa identificativa dell'EA che si intende mettere a mercato.
Da *login_environments_variables* si importano le variabili globali *LOGIN*, *PASSWORD*, *SERVER* e *PATH*, le quali definiscono le credenziali 
di accesso al conto personale dell'utente. Da *MetaTrader5* (rinominato come *mt5*) si importano le funzioni dell'API di Meta Trader 5, grazie alle quali è possibile "comunicare" con il terminale
MT5 convertendo i comandi python in azioni effettive eseguite sulla piattaforma Meta Trader 5. Dal modulo *financial_tools.financial_tools* si importano gli indicatori da utilizzare all'interno della strategia,
nel caso in esame si fa utilizzo del solo indicatore "ROC" implementato dalla funzione *ROC_from_pos*.
Il modulo *time* è un modulo della libreira standard di python che ci permette di lavorare con date e orari.

riga 8-9: si stampano a video le variabili *mt5.__author__* e *mt5.__version__* che restituiscono rispettivamente l'autore della libreria MetaTrader5 e la versione corrente che si sta utilizzando.

riga 16-19: il comando *mt5.initialize(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER)* è utilizzato per stabilire una connessione con il terminale di Meta Trader 5. Esso restituisce *True* in caso di connessione avventuta, latrimenti *False*.
Se l'esito è *False* allora viene stampato a video il messaggio di errore descritto dal comando *print("initialize() fallito, error code =", mt5.last_error())*, dove *mt5.last_error()* è una funzione della libreria che restituisce l'ultimo errore rilevato dalla 
libreria MetaTrader5. Per maggiori info vedere https://www.mql5.com/it/docs/integration/python_metatrader5/mt5initialize_py .

riga 22-32: la funzione *mt5.login(login=LOGIN, password=PASSWORD, server=SERVER)* effettua un tentativo di login alla piattaforma di trading, restituisce in output *True*  se il login avviene corretamente, altrimenti *False*. L'esito del login viene associato alla variabile boleana *authorized*.
Dunque se *authorized* è *True* si effettuano i seguenti comandi:
1) la funzione *print(mt5.account_info())* stampa a video le informazioni principali dell'account personale del conto Meta Trader 5.
2) con il comando *account_info_dict = mt5.account_info()._asdict()* associamo alla variabile *account_info_dic* le informazioni dell'account convertite in formato di "dizionario"
3) dunque con il comando *print("  {}={}".format(prop, account_info_dict[prop]))* andiamo a stampare tali informazioni estraendole una dopo l'altra dalla variabile *account_info_dict* "ciclando" sul valore *prop* che ad ogni ciclo assume il valore della chiave successiva del dizionario delle informazioni.
4) se la variabile *authorized* è *False* viene stampato a video un messaggio di errore mediante il comando *print("fallimento nella connessione all'account #{}, error code: {}".format(26947266, mt5.last_error()))*.

Per maggiori info vedere https://www.mql5.com/it/docs/integration/python_metatrader5/mt5login_py , https://www.mql5.com/it/docs/integration/python_metatrader5/mt5accountinfo_py .

riga 37-42: Inizializiamo le seguenti variabili:
1) *cnt* è una variabile di tipo "intero" che tiene il conto di quante volte lo script è andato ad *interrogare* l'API di Meta Trader 5 al fie di prelevare le informazioni utili sui prezzi ed eventualmente inviare comandi da fa eseguire all'API stessa (ad esempio ordini di acquisto e vendita). 
2) *orders* è una variabile di tipo "lista" all'interno della quale si inseriscono i "ticket" degli ordini eseguiti, per tenere traccia delle operazioni effettuate, così da poterle richiamare per eventuali modifiche o chiusure in momenti successivi.
3) *long_condition_1*, *long_condition_2*, *long_condition_3* e *close_condition*, sono variaibli boleane che rappresentano le condizioni long e short della strategia. Inizialmente esse sono tutte inizializzate con valore *False*.

riga 44: con il comando *while(True):* definiamo un ciclo "while" senza regola di interruzione, dunque idealmente capace di "ciclare" all'infinito finchè non avviene la chiusura manuale dello script. Tutti i comandi scritti con indentatura all'interno del corpo del ciclo "while" duqnue saranno ripetuti a loop.

riga 46: *time.sleep(1)* è un comando della libreira *time* che fa si che il compilatore attenda un secondo prima di passare ai comandi successivi, esso dunque ci permette di regolare una frequenza con la quale il ciclo "while" andrà a ripetere a loop i comandi sottostanti (in questo caso un cilco al seocondo).

riga 48-51: con il comando *account_info_dict = mt5.account_info()._asdict()*, come già visto, associamo le informazioni correnti del conto alla variabile dizionario *account_info_dict*. Con il comando *balance = account_info_dict["balance"]* associamo l'informazione relativa alla chiave "balance" alla variabile *balace*
che rappresenta appunto il capitale totale presente sul conto al momento della "chiamata". Analogamente con il comando *margin_free = account_info_dict["margin_free"]*, andiamo a prelevare l'informazione relativa al capitale libero, ossia disponibile per la messa a mercato delle operazioni. Assoceremo tale valore alla variabile *margin_free*.

riga 54-56: associamo alle variabili *ROC_100*, *ROC_50* e *ROC_20*, i valori del "ROC" valutato su 100,50 e 20 periodi, rispettivamente.
Tali variabili rappresentato il valore del "ROC" misurato all'instante attuale (variabile decimale). 
La funzione *ROC_from_pos(start, stop, symbol, time_frame, timeperiod)* restituisce una lista contenente i valori del "ROC" misurati a partire dalla barra di indice "start" (più recente) fino alla barra di indice "stop" (precedente situata nel passato), duqnue se "start - stop = 200" otteniamo una lista contenente i 200 valori del "ROC" 
misurati su ognuna delle 200 barre, cronologicamente ordinati in modo tale che la freccia del tempo punti verso destra.
La variabile di input "symbol" richiede l'inserimento della stringa relativa all'asset sul quale intendiamo operare.
La variabile di input "time_frame" richiede l'inseriemnto del time frame sul quale opera la strategia, mentre la variabile "time_period" necessita del valore numerico relativo al periodo utilizzato dall'indicatore "ROC".
Ad esempio il seguente comando *ROC_100 = ROC_from_pos(0, 200, symbol=SYMBOL, time_frame=mt5.TIMEFRAME_H4, timeperiod=100)[-1]* associa alla variabile *ROC_100* l'ultimo valore misurato (valore presente, indice della lista [-1]) della lista delle misurazioni del "ROC" . Avendo considerato come input, "start" = 0 (barra iniziale corrispondente al presente),
"stop"=200 (200 barre nel passato), "SYMBOL" che identifica l'asset da utilizzare (variabile di tipo stringa definita nello script *strategy_environments_variables.py*) e modificabile dall'utente, un time frame di 4H definita dalla variabile *mt5.TIMEFRAME_H4* (oggetto time frame definito nella libreria MetaTrader5), ed infine un valore di 100 per il periodo relativo all'indicatore "ROC". 

riga 60-74: il blocco di codice rappresentato da queste righe verrà descritto con maggiore precisione al termine del documento, se ne presenta qui una descrizione a "black box". Le righe contenute nel blocco manipolano le variabili:
1) la variabile boleana *ROC_20_down_0_current_state* assume valore *True* se la variabile *ROC_20* valutata sulla barra presente ha un valore inferiore a 0, altrimenti *False*.
2) la variabile boleana *ROC_20_down_0_previus_state* assume valore *True* se la variabile *ROC_20* valutata una barra nel passato ha un valore inferiore a 0, altrimenti *False*.
3) la variabile boleana *ROC_20_up_negative5_current_state* assume valore *True* se la variabile *ROC_20* valutata sulla barra presente ha un valore superiore a -5, altrimenti *False*.
4) la variabile boleana *ROC_20_up_negative5_previus_state* assume valore *True* se la variabile *ROC_20* valutata una barra nel passato ha un valore superiore a -5, altrimenti *False*.
