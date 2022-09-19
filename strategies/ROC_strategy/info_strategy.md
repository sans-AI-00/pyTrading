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

riga 78-79: la riga di codice *long_condition_1 = ROC_100 >= 0* associa alla variabile *long_condition_1* il valore *True* se il valore corrente della variabile *ROC_100* è superiore o uguale a 0, altrimenti *False*.
Analogamente la riga di codice *long_condition_1 = ROC_50 >= 0* associa alla variabile *long_condition_1* il valore *True* se il valore corrente della variabile *ROC_50* è superiore o uguale a 0, altrimenti *False*.

riga 80-82: il comando *if cnt > 1:* fa sì che le righe di codice contenute all'interno del suo corpo (81-82) vengano eseguite solo se la variabile *cnt* è maggiore di 1. Questo si rende necessario in quanto al conteggio 0 le variabili *ROC_20_down_0_previous_state* e *ROC_20_up_negative5_previous_state* non assunto ancora alcun valore.
Il comando *long_condition_3 = ROC_20_down_0_previous_state and not ROC_20_down_0_current_state* associa alla variabile boleana *long_condition_3* il valore *True* solo se *ROC_20_down_0_previous_state = True* e *ROC_20_down_0_current_state = False*, ossia se la variabile *ROC_20* ha incrociato a rialzo il valore 0. In tutti gli altri casi restituisce *False*.
Il comando *close_condition = ROC_20_up_negative5_previous_state and not ROC_20_up_negative5_current_state* associa alla variabile boleana *close_condition* il valore *True* solo se *ROC_20_up_negative5_previous_state* e *ROC_20_up_negative5_current_state = False*, ossia se la variabile *ROC_20* ha incrociato a ribasso il valore -5. In tutti gli altri casi restituisce *False*.

riga 85-106: righe di codice che si occupano di stampare a video, ogni 10 secondi, i valori aggiornati delle varibili e le informazioni del conto, con eventuali segnali di buy/sell scattati e le conseguenti operazioni effettuate a mercato.

riga 107: l'istruzione *if long_condition_1 and long_condition_2 and long_condition_3:* fa sì che vegano eseguite le righe contenute all'interno del suo corpo (108-134) solo se tutte e tre le condizioni long risultano essere vere, ossia *long_condition_1 = True*, *long_condition_2 = True* e *long_condition_3 = True*.

riga 109-111: la riga di codice *point = mt5.symbol_info(SYMBOL).point* associa alla variabile *point* il valore del "point" più piccolo misurabile sull'asset definito dalla variabile di input *SYMBOL* (ricordando che "1 point = 10 pips")
La riga di codice *price = mt5.symbol_info_tick(SYMBOL).ask* associa alla variabile *price* il prezzo corrente di acquisto (ask) relativo all'asset definito dalla variabile *SYMBOL*.
L'istruzione *deviation = 20* definisce la deviazione massima dal prezzo entro il quale siamo disposti ad acquistare dal momento in cui è partito l'ordine di acquisto.

riga 112-125: riga 112-125: nelle seguenti righe si va a costruire il dizionario che definisce le variabili della richiesta di ordine da affettuare all'API di Meta Trader 5. Essa è composta dalle seguenti coppie "chiave - valore".
1) *action*: Tipo di operazione di trading. Il valore può essere uno dei valori dell'enumerazione *TRADE_REQUEST_ACTIONS* (vedere https://www.mql5.com/it/docs/integration/python_metatrader5/mt5ordercheck_py#trade_request_actions).
2) *symbol*: Il nome dello strumento di trading (asset), per il quale viene piazzato l'ordine. Non richiesto per modificare ordini e chiudere posizioni.
3) *volume*: Volume richiesto di un affare(deal) in lotti. Un volume reale quando si fa un affare(deal) dipende dal tipo di esecuzione dell'ordine.
4) *type*: Tipo di ordine. Il valore può essere uno dei valori dell'enumerazione *ORDER_TYPE* (vedere https://www.mql5.com/it/docs/integration/python_metatrader5/mt5ordercalcmargin_py#order_type).
5) *price*: Prezzo al quale eseguire un ordine.
6) *sl*: Un prezzo per cui viene attivato un ordine Stop Loss quando il prezzo si sposta in una direzione sfavorevole.
7) *tp*: Un prezzo per cui viene attivato un ordine Take Profit quando il prezzo si muove in una direzione favorevole
8) *deviation*: Deviazione massima accettabile dal prezzo richiesto, specificata in "points".
9) *magic*: EA ID. Consente di organizzare la gestione analitica degli ordini di trading. Ogni EA può impostare un ID univoco quando invia una richiesta di trading.
10) *comment*: Commento ad un ordine.
11) *type_time*: Tipo di ordine per scadenza. Il valore può essere uno dei valori *ORDER_TYPE_TIME* ( vedere https://www.mql5.com/it/docs/integration/python_metatrader5/mt5ordercheck_py#order_type_time).
12) *type_filling*: Tipo di riempimento dell'ordine. Il valore può essere uno dei valori *ORDER_TYPE_FILLING* (vedere https://www.mql5.com/it/docs/integration/python_metatrader5/mt5ordercheck_py#order_type_filling).

riga 128-130: la riga *result = mt5.order_send(request)* invia l'ordine configurato dalla variabile di input *request* ed associa l'esito della richiesta (sotto forma di codice identificativo) alla variabile *result*.
la riga 130 stampa a video le informazioni relative all'ordine appena inviato.

riga 131-134: le seguenti righe stampano a video l'esito dell'ordine in caso di errore, altrimenti se l'rdine va a buon fine viene aggiunto il valore del "ticket" (valore identificativo dell'ordine) alla lista *orders*.

riga 136: l'istruzione *if close_condition and orders:* esegue le righe contenuti all'interno del suo corpo (138-154) solo se *close_condition = True* e la lista *orders* non è vuota, ossia solo se si attiva il segnale di vendita e sono presenti ordini di acquisto ancora non chiusi.

riga 138: l'istruzione *for order in orders:* esegue un ciclo iterando sugli elementi della lista *orders*, ossia la lista contenente i "tickets" degli ordini aperti. Ad ogni iterazione l'istruzione *For* esegue le righe contenute all'interno del corpo dell'istruzione (139-154).

riga 139-141: la riga di codice *position_id = order* ssocia il valore del ticket dell'ordine considerato alla variabile *position_id*.
Il comando *price = mt5.symbol_info_tick(SYMBOL).bid* associa alla variabile *price* il prezzo attuale di venidta (bid).
La variabile *deviation* come già visto definisce la variazione di prezzo che siamo disposti a tollerare.

riga 142-154: Come visto in precedenza definiamo le variabili di input della richiesta di ordine, stavoltà trattando però un oridne di vendità e non di acquisto. Un parametro aggiuntivo è la coppia "chiave-valore" definita dalla chiave *position*, la quale prende in input il ticket dell'ordine che si intende chiudere (fondamentale per distinguere in maniera univoca l'ordine).

riga 157-167: analogamente al blocco costituito dalle righe 127-134 esso invia l'ordine e stampa a video un eventuale esito negativo, mentre nel caso di esito positivo chiude l'ordine identificato da ticket e rimuove il relativo ticket dalla lista *orders*.

riga 169: il comando *cnt += 1* al termine di ogni ciclo incrementa di 1 la variabile *cnt* che tiene il conto dei cicli eseguiti.