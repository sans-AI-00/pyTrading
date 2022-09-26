# Useful information(eng)

## Simplified description of python code:
line 1-5: We import the global variables to connect to the Meta Trader 5 terminal (***login_environments_variables***) and the operational parameters of the strategy (***strategy_environments_variables***), as well as external libraries containing useful functions that we will use within the code. The ***Metatrader5*** lyricist provides useful functions for financial_commands to the Meta Trader 5 platform, contains functions that implement technical analysis tools that we will use within the strategy, finally the ***time*** strategy module provides useful functions for the arrangement of dates and timetables.

![Cattura_1](https://user-images.githubusercontent.com/105428493/192372882-f93f52ae-fdad-46c8-8391-0d6ca63e36ef.PNG)

line 8-9: you print a video information about the author of the MetaTrader5 library and the current version you are using.

![Cattura_2](https://user-images.githubusercontent.com/105428493/192372914-b465863a-fbd2-489c-a92d-c569fc170b45.PNG)

line 16-19: the following lines of code are used for a connection with the Meta Trader 5 terminal. Personal login variables for the Meta Trader 5 platform are provided as input.

![Cattura_3](https://user-images.githubusercontent.com/105428493/192372930-b8dddd91-85a5-4959-b6ff-5036c9461620.PNG)

line 22-32: in the following lines of code an attempt is made to access the trading platform using the user's personal login variables.

![Cattura_4](https://user-images.githubusercontent.com/105428493/192372957-12589fc2-7837-4252-8f34-8189cb890a82.PNG)

line 37-42: in the following code block you define the variables that the program must "keep in mind" when executing the strategy. The ***cnt*** variable takes into account how many times the strategy has gone to obtain information from the market. The variable ***orders*** is a list in which the 'tickets' relating to the orders placed will be contained. The other variables instead represent the 4 conditions (3 of purchase and 1 of sale) that the strategy will use to operate, these variables are called "boolean" and can assume the logical values "True" and "False".

![Cattura_5](https://user-images.githubusercontent.com/105428493/192372979-8f62c150-d08b-4197-b604-e2db185f868f.PNG)

line 44-169: the entire block contains the actual code that will be executed to perform market operations. It consists of 5 sub-blocks:
1) line 46-56: within this block, useful information is taken, the capital available for operations (***margin free***) and the total capital (***balance***). In addition, the current values of the ROC are taken for the three selected periods (20,50,100 periods).

![Cattura_6](https://user-images.githubusercontent.com/105428493/192373004-ba38f855-cbc9-41f0-9cee-fe08bcd86be9.PNG)

2) line 60-82: the purchase and sale conditions are evaluated in the following lines. In detail, for the purchase conditions, it is observed if the ROC, valued over 100 periods and 50 periods, is greater than zero, and also if the 20-period ROC has crossed upwards the value 0. For the condition of sale, instead, the signal it triggers when the 20-period ROC crosses down the -5 value.

![Cattura_7](https://user-images.githubusercontent.com/105428493/192373038-fec9b22e-f0d6-476b-b473-a19a18aa168e.PNG)

4) line 85-105: the following block contains the lines of code useful for generating the graphic output that shows the current key parameters of the account, for example free margin, total capital, open and closed operations, etc.

![Cattura_8](https://user-images.githubusercontent.com/105428493/192373068-78174767-1732-4174-a39e-6873c3a8d6e8.PNG)

6) line 107-134: in the following lines of code it is evaluated if the purchase conditions are all valid, if so, a purchase order is executed using the amount expressed in "lots" by the global variable ***LOT*** as the amount , with assets on which to operate defined by the variable ***SYMBOL***. Furthermore, for this strategy "stop loss" and "take profit" are absent. If the purchase operation is carried out, the relative ticket is stored to be used when the position is closed.

![Cattura_9](https://user-images.githubusercontent.com/105428493/192373082-367f55bf-b3d3-4864-a24e-329aeffdb793.PNG)

8) line 136-167: in the following lines of code it is evaluated whether the conditions of sale are all valid, if so, the orders identified by the relative "ticket" are closed.

![Cattura_10](https://user-images.githubusercontent.com/105428493/192373114-3bf3a0d8-ee9d-4da9-a712-6323fa4cc678.PNG)

## Full Python code description:
line 1-5: import all the libraries necessary for the correct functioning of the code.
From ***strategy_environments_variables*** we import the global variables ***SYMBOL***, ***LOT*** and ***MAGIC***, which define
the asset on which we operate, the amount of each investment and the identification plate of the EA that we intend to put on the market.
From ***login_environments_variables*** the global variables ***LOGIN*** ***PASSWORD***, ***SERVER*** and ***PATH*** are imported, which define the credentials
access to the user's personal account. From***MetaTrader5*** (renamed as ***mt5***) the functions of the API of Meta Trader 5 are imported, thanks to which it is possible to "communicate" with the terminal
MT5 by converting the python commands into actual actions performed on the Meta Trader 5 platform. From the ***financial_tools.financial_tools*** module, the indicators to be used within the strategy are imported,
in the case in question, only the "ROC" indicator implemented by the ***ROC_from_pos*** function is used.
The ***time*** module is a standard python library module that allows us to work with dates and times.

line 8-9: the variables ***mt5 .__ author __*** and ***mt5 .__ version __*** are printed, which respectively return the author of the MetaTrader5 library and the current version being used.

line 16-19: the command ***mt5.initialize (path = PATH, login = LOGIN, password = PASSWORD, server = SERVER)*** is used to establish a connection with the Meta Trader 5 terminal. It returns ***True*** in case of an adventurous connection, barking ***False***.
If the result is ***False*** then the error message described by the command ***print ("initialize () failed, error code =", mt5.last_error ())*** is printed on the screen, where ***mt5.last_error ()*** is a library function that returns the last error encountered by the
MetaTrader5 library. For more info see https://www.mql5.com/it/docs/integration/python_metatrader5/mt5initialize_py.

line 22-32: the function ***mt5.login (login = LOGIN, password = PASSWORD, server = SERVER)*** makes an attempt to login to the trading platform, returns ***True*** if login is successful, otherwise ***False***. The login result is associated with the Boolean variable ***authorized***.
So if ***authorized*** is ***True*** the following commands are carried out:
1) the ***print (mt5.account_info ()) function*** prints the main information of the personal account of the Meta Trader 5 account on the screen.
2) with the command ***account_info_dict = mt5.account_info () ._ asdict ()*** we associate to the variable ***account_info_dic*** the account information converted into "dictionary" format
3) then with the command ***print ("{} = {}". Format (prop, account_info_dict [prop]))*** let's print this information by extracting it one after the other from the ***account_info_dict*** variable "cycling" on the ***prop*** value which at each cycle takes on the value of the next key of the information dictionary.

If the ***authorized*** variable is ***False*** an error message is printed on the screen using the ***print command ("failure to connect to account # {}, error code: {} ". format (26947266, mt5.last_error ()))***.

For more info see https://www.mql5.com/it/docs/integration/python_metatrader5/mt5login_py, https://www.mql5.com/it/docs/integration/python_metatrader5/mt5accountinfo_py.

line 37-42: We initialize the following variables:
1) ***cnt*** is an "integer" variable that takes into account how many times the script has gone to query the Meta Trader 5 API in order to collect useful information on prices and possibly send commands to be executed by the API itself (for example purchase and sale orders).
2) ***orders*** is a "list" type variable in which the "tickets" of the executed orders are inserted, to keep track of the operations carried out, so as to be able to recall them for any changes or closures in moments subsequent.
3) ***long_condition_1***, ***long_condition_2***, ***long_condition_3*** and ***close_condition***, are boolean variables that represent the long and short conditions of the strategy. Initially they are all initialized with the value ***False***.

line 44: with the command ***while (True):*** we define a "while" loop without an interruption rule, therefore ideally able to "loop" indefinitely until the script is closed manually. All commands written with indent inside the body of the duqnue "while" loop will be looped.

line 46: ***time.sleep (1)*** is a command of the library ***time*** which causes the compiler to wait a second before moving on to the following commands, therefore it allows us to adjust a frequency with which the "while" loop will repeat the underlying commands in a loop (in this case one cycle per second).

line 48-51: with the command ***account_info_dict = mt5.account_info () ._ asdict ()***, as already seen, we associate the current information of the account with the dictionary variable ***account_info_dict***. With the ***balance = account_info_dict ["balance"]*** command we associate the information relating to the "balance" key to the ***balance*** variable
which represents the total capital present in the account at the time of the "call". Similarly with the command ***margin_free = account_info_dict ["margin_free"]***, we are going to take the information relating to free capital, that is, available for the marketing of the operations. We will associate this value with the ***margin_free*** variable.

line 54-56: we associate to the variables ***ROC_100***, ***ROC_50*** and ***ROC_20***, the values of the "ROC" evaluated over 100, 50 and 20 periods, respectively.
These variables represent the value of the "ROC" measured at the current instant (decimal variable).
The ***ROC_from_pos (start, stop, symbol, time_frame, timeperiod) function*** returns a list containing the values of the "ROC" measured from the ***start*** index bar (most recent) up to the index bar ***stop*** (previous located in the past), so if ***start - stop = 200*** we get a list containing the 200 values of the" ROC "
measured on each of the 200 bars, chronologically ordered so that the arrow of time points to the right.
The input variable ***symbol*** requires the insertion of the string relating to the asset on which we intend to operate.
The ***time_frame*** input variable requires the insertion of the time frame on which the strategy operates, while the ***time_period*** variable requires the numerical value relating to the period used by the "ROC" indicator.
For example, the following command ***ROC_100 = ROC_from_pos (0, 200, symbol = SYMBOL, time_frame = mt5.TIMEFRAME_H4, timeperiod = 100) [- 1]*** associates the last measured value (present value, list index [-1]) of the "ROC" measurement list. Having considered as input, ***start = 0*** (initial bar corresponding to the present),
***stop = 200*** (200 bars in the past), ***SYMBOL*** which identifies the asset to be used (variable of type string defined in the *strategy_environments_variables.py* script) and editable by the user, a time frame of 4H defined by the variable ***mt5.TIMEFRAME_H4*** (time frame object defined in the MetaTrader5 library), and finally a value of 100 for the period relating to the "ROC" indicator.

line 60-74: the code block represented by these lines will be described more precisely at the end of the document, a "black box" description is presented here. The lines contained in the block manipulate the variables:
1) the Boolean variable ***ROC_20_down_0_current_state*** takes value ***True*** if the variable ***ROC_20*** evaluated on the present bar has a value lower than 0, otherwise ***False*** .
2) the Boolean variable ***ROC_20_down_0_previus_state*** takes value ***True*** if the variable ***ROC_20*** evaluated a bar in the past has a value less than 0, otherwise ***False***.
3) the Boolean variable ***ROC_20_up_negative5_current_state*** takes value ***True*** if the variable ***ROC_20*** evaluated on the present bar has a value greater than -5, otherwise ***False***.
4) the Boolean variable ***ROC_20_up_negative5_previus_state*** takes value ***True*** if the variable ***ROC_20*** evaluated a bar in the past has a value greater than -5, otherwise ***False***.

line 78-79: the line of code ***long_condition_1 = ROC_100> = 0*** associates the ***long_condition_1*** variable with the value ***True*** if the current value of the variable ***ROC_100*** is greater than or equal to 0, otherwise ***False***.
Similarly, the line of code ***long_condition_1 = ROC_50> = 0*** associates the ***long_condition_1*** variable with the ***True*** value if the current value of the ***ROC_50*** variable is greater than or equal to 0, otherwise ***False***.

line 80-82: the command ***if cnt> 1:*** causes the lines of code contained within its body (81-82) to be executed only if the variable ***cnt*** is greater than 1. This is necessary since the variables ***ROC_20_down_0_previous_state*** and ***ROC_20_up_negative5_previous_state*** at count 0 have not yet assumed any value.
The ***long_condition_3 = ROC_20_down_0_previous_state and not ROC_20_down_0_current_state*** command associates to the boolean variable ***long_condition_3*** the value ***True*** only if ***ROC_20_down_0_previous_state = True*** and ***ROC_20_down_current_0 = False***, that is, if the variable ***ROC_20*** has crossed the value 0 upwards. In all other cases it returns ***False***.
The ***close_condition = ROC_20_up_negative5_previous_state and not ROC_20_up_negative5_current_state*** command associates the value ***True*** with the Boolean variable ***close_condition*** only if ***ROC_20_up_negative5_previous_state*** and ***ROC_20_current_negate5_previous_state*** and ***ROC_20_current_negate = False5***, that is, if the variable ***ROC_20*** has crossed the value -5 downwards. In all other cases it returns ***False***.

line 85-106: lines of code that print on the screen, every 10 seconds, the updated values of the variables and the account information, with any buy/sell signals triggered and the consequent market transactions.

line 107: the statement ***if long_condition_1 and long_condition_2 and long_condition_3:*** causes the lines contained within its body (108-134) to be executed only if all three long conditions are true, that is ***long_condition_1 = True***, ***long_condition_2 = True*** and ***long_condition_3 = True***.

line 109-111: the line of code ***point = mt5.symbol_info (SYMBOL).point*** associates to the variable ***point*** the value of the smallest measurable "point" on the asset defined by the variable input ***SYMBOL*** (remembering that "1 point = 10 pips")
The line of code ***price = mt5.symbol_info_tick (SYMBOL).ask*** associates the ***price*** variable with the current purchase price (ask) relating to the asset defined by the ***SYMBOL*** variable.
The instruction ***deviation = 20*** defines the maximum deviation from the price within which we are willing to buy from the moment the purchase order is sent.

line 112-125: line 112-125: in the following lines we build the dictionary that defines the variables of the order request to be sent to the Meta Trader 5 API. It is made up of the following "key - value" pairs.
1) ***action***: Type of trading operation. The value can be one of the ***TRADE_REQUEST_ACTIONS*** enumeration values (see https://www.mql5.com/en/docs/integration/python_metatrader5/mt5ordercheck_py#trade_request_actions).
2) ***symbol***: The name of the trading instrument (asset), for which the order is placed. Not required to change orders and close positions.
3) ***volume***: Required volume of a deal in lots. Actual volume when making a deal depends on the type of order execution.
4) ***type***: Type of order. The value can be one of the ***ORDER_TYPE*** enumeration values (see https://www.mql5.com/it/docs/integration/python_metatrader5/mt5ordercalcmargin_py#order_type).
5) ***price***: Price at which to execute an order.
6) ***sl***: A price for which a Stop Loss order is triggered when the price moves in an unfavorable direction.
7) ***tp***: A price for which a Take Profit order is triggered when the price moves in a favorable direction
8) ***deviation***: Maximum acceptable deviation from the asking price, specified in "points".
9) ***magic***: EA ID. It allows you to organize the analytical management of trading orders. Each EA can set a unique ID when submitting a trade request.
10) ***comment***: Comment on an order.
11) ***type_time***: Type of order by expiration. The value can be one of the ***ORDER_TYPE_TIME*** values (see https://www.mql5.com/it/docs/integration/python_metatrader5/mt5ordercheck_py#order_type_time).
12) ***type_filling***: Order filling type. The value can be one of the ***ORDER_TYPE_FILLING*** values (see https://www.mql5.com/it/docs/integration/python_metatrader5/mt5ordercheck_py#order_type_filling).

line 128-130: the line ***result = mt5.order_send (request)*** sends the order configured by the input variable ***request*** and associates the result of the request (in the form of an identification code ) to the variable ***result***.
line 130 prints the information relating to the order just sent on the screen. For more information see https://www.mql5.com/it/docs/integration/python_metatrader5/mt5ordersend_py.

line 131-134: the following lines print the result of the order on the screen in the event of an error, otherwise if the order is successful, the value of the "ticket" (order identification value) is added to the list ***orders***.

line 136: the instruction ***if close_condition and orders:*** executes the lines contained within its body (138-154) only if ***close_condition = True*** and the list ***orders*** is not empty, i.e. only if the sell signal is activated and there are still unclosed buy orders.

line 138: the instruction ***for order in orders:*** executes a loop by iterating on the elements of the list ***orders***, that is the list containing the "tickets" of the open orders. At each iteration, the ***For*** instruction executes the lines contained within the body of the instruction (139-154).

line 139-141: the line of code ***position_id = order*** ssociates the value of the order ticket considered to the variable ***position_id***.
The ***price = mt5.symbol_info_tick (SYMBOL).bid*** command associates the current sales price (bid) with the variable ***price***.
The ***deviation*** variable as already seen defines the price variation that we are willing to tolerate.

line 142-154: As seen previously, we define the input variables of the order request, but we are dealing with an order of sale and not of purchase. An additional parameter is the "key-value" pair defined by the ***position*** key, which takes as input the ticket of the order to be closed (essential to uniquely distinguish the order).

line 157-167: similarly to the block consisting of lines 127-134, it sends the order and prints any negative result on the screen, while in the event of a positive outcome it closes the order identified by the ticket and removes the related ticket from the list ***orders***.

line 169: the command ***cnt + = 1*** at the end of each cycle increases by 1 the variable ***cnt*** which takes into account the cycles performed.



# Informazioni utili(ita)

## Descrizione semplificata codice python:
riga 1-5: Si importano le variabili globali per effettuare la connessione al terminale di Meta Trader 5 (__login_environments_variables__) e i parametri operativi della strategia (__strategy_environments_variables__), oltre alle librerie esterne contenenti funzioni utili che utilizzeremo all'interno del codice. La lireria __Metatrader5__ mette a disposizione funzioni utili per inviare comandi alla piattaforma Meta Trader 5, __financial_tools__ contiene funzioni che implementano strumenti di analisi tecnica che andremo ad utilizzare all'interno della strategia, infine il modulo __time__ mette a disposizione funzioni utili per la manipolazione di date ed orari.

![Cattura_1](https://user-images.githubusercontent.com/105428493/192372882-f93f52ae-fdad-46c8-8391-0d6ca63e36ef.PNG)

riga 8-9: si stampano a video informazioni riguardanti l'autore della libreria MetaTrader5 e la versione corrente che si sta utilizzando.

![Cattura_2](https://user-images.githubusercontent.com/105428493/192372914-b465863a-fbd2-489c-a92d-c569fc170b45.PNG)

riga 16-19: le seguenti righe di codice sono utilizzate per stabilire una connessione con il terminale di Meta Trader 5. Sono fornite in input le variabili personali di login alla piattaforma Meta Trader 5.

![Cattura_3](https://user-images.githubusercontent.com/105428493/192372930-b8dddd91-85a5-4959-b6ff-5036c9461620.PNG)

riga 22-32: nelle seguenti righe di codice si effettua un tentativo di accesso alla piattaforma di trading utilizzando le variabili di login personali dell'utente.

![Cattura_4](https://user-images.githubusercontent.com/105428493/192372957-12589fc2-7837-4252-8f34-8189cb890a82.PNG)

riga 37-42: nel seguente blocco di codice si definiscono le variabili che il programma dovrà "tenere a mente" durante l'esezucione della strategia. La variabile ***cnt*** tiene il conto di quante volte la strategia è andata a prelevare informazioni dal mercato. La variabile ***orders*** è una lista all'interno della quale saranno contenuti i 'tickets' relativi a gli ordini effettuati. Le altre variabili invece rappresentato le 4 condizioni (3 di acquisto e 1 di vendita) che la startegia utilizzerà per operare, tali variabili sono dette "boleane" è possono assumere i valori logici "True" e "False".

![Cattura_5](https://user-images.githubusercontent.com/105428493/192372979-8f62c150-d08b-4197-b604-e2db185f868f.PNG)

riga 44-169: l'intero blocco contiene il codice effettivo che verrà eseguito per effettuare operazioni a mercato. Esso si compone di 5 sotto blocchi:
1) riga 46-56: all'interno di questo questo blocco si prelevano informazioni utili, il capitale disponibile per le operazioni (***margin free***) ed il capitale totale (***balance***). Inoltre si prelevano i valori attuali del ROC per i tre periodi selezionati (20,50,100 periodi).

![Cattura_6](https://user-images.githubusercontent.com/105428493/192373004-ba38f855-cbc9-41f0-9cee-fe08bcd86be9.PNG)

3) riga 60-82: nelle seguenti righe si valutano le condizioni di acquisto e di vendita. Nel dettaglio per le condizioni di acquisto si osserva se il ROC, valutato su 100 periodi e 50 periodi, è maggiore di zero, ed inoltre se il ROC a 20 periodi ha incrociato a rialzo il valore 0. Per la condizione di vendita invece il segnale scatta quando il ROC a 20 periodi incrocia a ribasso il valore -5.

![Cattura_7](https://user-images.githubusercontent.com/105428493/192373038-fec9b22e-f0d6-476b-b473-a19a18aa168e.PNG)

5) riga 85-105: nel seguente blocco sono contenute le righe di codice utili alla generazione dell'output grafico che riporta i parametri chiave attuali del conto, ad esmepio margine libero, capitale totale, operazioni aperte e chiuse etc.. 

![Cattura_8](https://user-images.githubusercontent.com/105428493/192373068-78174767-1732-4174-a39e-6873c3a8d6e8.PNG)

7) riga 107-134: nelle seguenti righe di codice si valuta se le condizioni di acquisto sono tutte valide, in caso affermativo si esegue un ordine di acquisto utilizzando come importo quello espresso in "lotti" dalla variabile globale ***LOT***, con asset su cui operare definito dalla variabile ***SYMBOL***. Inoltre per tale strategia "stop loss" e "take profit" sono assenti. Se l'operazione di acquisto viene effettuata il relativo tickets viene memorizzato per essere poi utilizzato al momento della chiusura della posizione.

![Cattura_9](https://user-images.githubusercontent.com/105428493/192373082-367f55bf-b3d3-4864-a24e-329aeffdb793.PNG)

9) riga 136-167: nelle seguenti righe di codice si valuta se le condizioni di vendita sono tutte valide, in caso affermativo si effettua la chiusura degli ordini identificati dal relativo "ticket".

![Cattura_10](https://user-images.githubusercontent.com/105428493/192373114-3bf3a0d8-ee9d-4da9-a712-6323fa4cc678.PNG)



## Descrizione completa codice python:
riga 1-5: si ffettua l'importazione di tutte le librerie necessarie per il corretto funzionamento del codice. 
Da ***strategy_environments_variables*** si importano le varibili globali ***SYMBOL***, ***LOT*** e ***MAGIC***, le quali definiscono 
l'asset sul quale operiamo, l'importo di ogni investimento e la targa identificativa dell'EA che si intende mettere a mercato.
Da ***login_environments_variables*** si importano le variabili globali ***LOGIN*** ***PASSWORD***, ***SERVER*** e ***PATH***, le quali definiscono le credenziali 
di accesso al conto personale dell'utente. Da ***MetaTrader5*** (rinominato come ***mt5***) si importano le funzioni dell'API di Meta Trader 5, grazie alle quali è possibile "comunicare" con il terminale
MT5 convertendo i comandi python in azioni effettive eseguite sulla piattaforma Meta Trader 5. Dal modulo ***financial_tools.financial_tools*** si importano gli indicatori da utilizzare all'interno della strategia,
nel caso in esame si fa utilizzo del solo indicatore "ROC" implementato dalla funzione ***ROC_from_pos***.
Il modulo ***time*** è un modulo della libreira standard di python che ci permette di lavorare con date e orari.

riga 8-9: si stampano a video le variabili ***mt5.__author__*** e ***mt5.__version__*** che restituiscono rispettivamente l'autore della libreria MetaTrader5 e la versione corrente che si sta utilizzando.

riga 16-19: il comando ***mt5.initialize(path=PATH, login=LOGIN, password=PASSWORD, server=SERVER)*** è utilizzato per stabilire una connessione con il terminale di Meta Trader 5. Esso restituisce ***True*** in caso di connessione avventuta, latrimenti ***False***.
Se l'esito è ***False*** allora viene stampato a video il messaggio di errore descritto dal comando ***print("initialize() fallito, error code =", mt5.last_error())***, dove ***mt5.last_error()*** è una funzione della libreria che restituisce l'ultimo errore rilevato dalla 
libreria MetaTrader5. Per maggiori info vedere https://www.mql5.com/it/docs/integration/python_metatrader5/mt5initialize_py .

riga 22-32: la funzione ***mt5.login(login=LOGIN, password=PASSWORD, server=SERVER)*** effettua un tentativo di login alla piattaforma di trading, restituisce in output ***True***  se il login avviene corretamente, altrimenti ***False***. L'esito del login viene associato alla variabile boleana ***authorized***.
Dunque se ***authorized*** è ***True*** si effettuano i seguenti comandi:
1) la funzione ***print(mt5.account_info())*** stampa a video le informazioni principali dell'account personale del conto Meta Trader 5.
2) con il comando ***account_info_dict = mt5.account_info()._asdict()*** associamo alla variabile ***account_info_dic*** le informazioni dell'account convertite in formato di "dizionario"
3) dunque con il comando ***print("  {}={}".format(prop, account_info_dict[prop]))*** andiamo a stampare tali informazioni estraendole una dopo l'altra dalla variabile ***account_info_dict*** "ciclando" sul valore ***prop*** che ad ogni ciclo assume il valore della chiave successiva del dizionario delle informazioni.

Se la variabile ***authorized*** è ***False*** viene stampato a video un messaggio di errore mediante il comando ***print("fallimento nella connessione all'account #{}, error code: {}".format(26947266, mt5.last_error()))***.

Per maggiori info vedere https://www.mql5.com/it/docs/integration/python_metatrader5/mt5login_py , https://www.mql5.com/it/docs/integration/python_metatrader5/mt5accountinfo_py .

riga 37-42: Inizializiamo le seguenti variabili:
1) ***cnt*** è una variabile di tipo "intero" che tiene il conto di quante volte lo script è andato ad ***interrogare*** l'API di Meta Trader 5 al fine di prelevare le informazioni utili sui prezzi ed eventualmente inviare comandi da fa eseguire all'API stessa (ad esempio ordini di acquisto e vendita). 
2) ***orders*** è una variabile di tipo "lista" all'interno della quale si inseriscono i "ticket" degli ordini eseguiti, per tenere traccia delle operazioni effettuate, così da poterle richiamare per eventuali modifiche o chiusure in momenti successivi.
3) ***long_condition_1***, ***long_condition_2***, ***long_condition_3*** e ***close_condition***, sono variaibli boleane che rappresentano le condizioni long e short della strategia. Inizialmente esse sono tutte inizializzate con valore ***False***.

riga 44: con il comando ***while(True):*** definiamo un ciclo "while" senza regola di interruzione, dunque idealmente capace di "ciclare" all'infinito finchè non avviene la chiusura manuale dello script. Tutti i comandi scritti con indentatura all'interno del corpo del ciclo "while" duqnue saranno ripetuti a loop.

riga 46: ***time.sleep(1)*** è un comando della libreira ***time*** che fa si che il compilatore attenda un secondo prima di passare ai comandi successivi, esso dunque ci permette di regolare una frequenza con la quale il ciclo "while" andrà a ripetere a loop i comandi sottostanti (in questo caso un cilco al seocondo).

riga 48-51: con il comando ***account_info_dict = mt5.account_info()._asdict()***, come già visto, associamo le informazioni correnti del conto alla variabile dizionario ***account_info_dict***. Con il comando ***balance = account_info_dict["balance"]*** associamo l'informazione relativa alla chiave "balance" alla variabile ***balance***
che rappresenta appunto il capitale totale presente sul conto al momento della "chiamata". Analogamente con il comando ***margin_free = account_info_dict["margin_free"]***, andiamo a prelevare l'informazione relativa al capitale libero, ossia disponibile per la messa a mercato delle operazioni. Assoceremo tale valore alla variabile ***margin_free***.

riga 54-56: associamo alle variabili ***ROC_100***, ***ROC_50*** e ***ROC_20***, i valori del "ROC" valutato su 100,50 e 20 periodi, rispettivamente.
Tali variabili rappresentato il valore del "ROC" misurato all'instante attuale (variabile decimale). 
La funzione ***ROC_from_pos(start, stop, symbol, time_frame, timeperiod)*** restituisce una lista contenente i valori del "ROC" misurati a partire dalla barra di indice "start" (più recente) fino alla barra di indice "stop" (precedente situata nel passato), duqnue se "start - stop = 200" otteniamo una lista contenente i 200 valori del "ROC" 
misurati su ognuna delle 200 barre, cronologicamente ordinati in modo tale che la freccia del tempo punti verso destra.
La variabile di input ***symbol*** richiede l'inserimento della stringa relativa all'asset sul quale intendiamo operare.
La variabile di input ***time_frame*** richiede l'inseriemnto del time frame sul quale opera la strategia, mentre la variabile ***time_period*** necessita del valore numerico relativo al periodo utilizzato dall'indicatore "ROC".
Ad esempio il seguente comando ***ROC_100 = ROC_from_pos(0, 200, symbol=SYMBOL, time_frame=mt5.TIMEFRAME_H4, timeperiod=100)[-1]*** associa alla variabile ***ROC_100*** l'ultimo valore misurato (valore presente, indice della lista [-1]) della lista delle misurazioni del "ROC" . Avendo considerato come input, ***start = 0*** (barra iniziale corrispondente al presente),
***stop = 200*** (200 barre nel passato), ***SYMBOL*** che identifica l'asset da utilizzare (variabile di tipo stringa definita nello script ***strategy_environments_variables.py***) e modificabile dall'utente, un time frame di 4H definita dalla variabile ***mt5.TIMEFRAME_H4*** (oggetto time frame definito nella libreria MetaTrader5), ed infine un valore di 100 per il periodo relativo all'indicatore "ROC". 

riga 60-74: il blocco di codice rappresentato da queste righe verrà descritto con maggiore precisione al termine del documento, se ne presenta qui una descrizione a "black box". Le righe contenute nel blocco manipolano le variabili:
1) la variabile boleana ***ROC_20_down_0_current_state*** assume valore ***True*** se la variabile ***ROC_20*** valutata sulla barra presente ha un valore inferiore a 0, altrimenti ***False***.
2) la variabile boleana ***ROC_20_down_0_previus_state*** assume valore ***True*** se la variabile ***ROC_20*** valutata una barra nel passato ha un valore inferiore a 0, altrimenti ***False***.
3) la variabile boleana ***ROC_20_up_negative5_current_state*** assume valore ***True*** se la variabile ***ROC_20*** valutata sulla barra presente ha un valore superiore a -5, altrimenti ***False***.
4) la variabile boleana ***ROC_20_up_negative5_previus_state*** assume valore ***True*** se la variabile ***ROC_20*** valutata una barra nel passato ha un valore superiore a -5, altrimenti ***False***.

riga 78-79: la riga di codice ***long_condition_1 = ROC_100 >= 0*** associa alla variabile ***long_condition_1*** il valore ***True*** se il valore corrente della variabile ***ROC_100*** è superiore o uguale a 0, altrimenti ***False***.
Analogamente la riga di codice ***long_condition_1 = ROC_50 >= 0*** associa alla variabile ***long_condition_1*** il valore ***True*** se il valore corrente della variabile ***ROC_50*** è superiore o uguale a 0, altrimenti ***False***.

riga 80-82: il comando ***if cnt > 1:*** fa sì che le righe di codice contenute all'interno del suo corpo (81-82) vengano eseguite solo se la variabile ***cnt*** è maggiore di 1. Questo si rende necessario in quanto al conteggio 0 le variabili ***ROC_20_down_0_previous_state*** e ***ROC_20_up_negative5_previous_state*** non assunto ancora alcun valore.
Il comando ***long_condition_3 = ROC_20_down_0_previous_state and not ROC_20_down_0_current_state*** associa alla variabile boleana ***long_condition_3*** il valore ***True*** solo se ***ROC_20_down_0_previous_state = True*** e ***ROC_20_down_0_current_state = False***, ossia se la variabile ***ROC_20*** ha incrociato a rialzo il valore 0. In tutti gli altri casi restituisce ***False***.
Il comando ***close_condition = ROC_20_up_negative5_previous_state and not ROC_20_up_negative5_current_state*** associa alla variabile boleana ***close_condition*** il valore ***True*** solo se ***ROC_20_up_negative5_previous_state*** e ***ROC_20_up_negative5_current_state = False***, ossia se la variabile ***ROC_20*** ha incrociato a ribasso il valore -5. In tutti gli altri casi restituisce ***False***.

riga 85-106: righe di codice che si occupano di stampare a video, ogni 10 secondi, i valori aggiornati delle varibili e le informazioni del conto, con eventuali segnali di buy/sell scattati e le conseguenti operazioni effettuate a mercato.

riga 107: l'istruzione ***if long_condition_1 and long_condition_2 and long_condition_3:*** fa sì che vegano eseguite le righe contenute all'interno del suo corpo (108-134) solo se tutte e tre le condizioni long risultano essere vere, ossia ***long_condition_1 = True***, ***long_condition_2 = True*** e ***long_condition_3 = True***.

riga 109-111: la riga di codice ***point = mt5.symbol_info(SYMBOL).point*** associa alla variabile ***point*** il valore del "point" più piccolo misurabile sull'asset definito dalla variabile di input ***SYMBOL*** (ricordando che "1 point = 10 pips")
La riga di codice ***price = mt5.symbol_info_tick(SYMBOL).ask*** associa alla variabile ***price*** il prezzo corrente di acquisto (ask) relativo all'asset definito dalla variabile ***SYMBOL***.
L'istruzione ***deviation = 20*** definisce la deviazione massima dal prezzo entro il quale siamo disposti ad acquistare dal momento in cui è partito l'ordine di acquisto.

riga 112-125: riga 112-125: nelle seguenti righe si va a costruire il dizionario che definisce le variabili della richiesta di ordine da affettuare all'API di Meta Trader 5. Essa è composta dalle seguenti coppie "chiave - valore".
1) ***action***: Tipo di operazione di trading. Il valore può essere uno dei valori dell'enumerazione ***TRADE_REQUEST_ACTIONS*** (vedere https://www.mql5.com/it/docs/integration/python_metatrader5/mt5ordercheck_py#trade_request_actions).
2) ***symbol***: Il nome dello strumento di trading (asset), per il quale viene piazzato l'ordine. Non richiesto per modificare ordini e chiudere posizioni.
3) ***volume***: Volume richiesto di un affare(deal) in lotti. Un volume reale quando si fa un affare(deal) dipende dal tipo di esecuzione dell'ordine.
4) ***type***: Tipo di ordine. Il valore può essere uno dei valori dell'enumerazione ***ORDER_TYPE*** (vedere https://www.mql5.com/it/docs/integration/python_metatrader5/mt5ordercalcmargin_py#order_type).
5) ***price***: Prezzo al quale eseguire un ordine.
6) ***sl***: Un prezzo per cui viene attivato un ordine Stop Loss quando il prezzo si sposta in una direzione sfavorevole.
7) ***tp***: Un prezzo per cui viene attivato un ordine Take Profit quando il prezzo si muove in una direzione favorevole
8) ***deviation***: Deviazione massima accettabile dal prezzo richiesto, specificata in "points".
9) ***magic***: EA ID. Consente di organizzare la gestione analitica degli ordini di trading. Ogni EA può impostare un ID univoco quando invia una richiesta di trading.
10) ***comment***: Commento ad un ordine.
11) ***type_time***: Tipo di ordine per scadenza. Il valore può essere uno dei valori ***ORDER_TYPE_TIME*** ( vedere https://www.mql5.com/it/docs/integration/python_metatrader5/mt5ordercheck_py#order_type_time).
12) ***type_filling***: Tipo di riempimento dell'ordine. Il valore può essere uno dei valori ***ORDER_TYPE_FILLING*** (vedere https://www.mql5.com/it/docs/integration/python_metatrader5/mt5ordercheck_py#order_type_filling).

riga 128-130: la riga ***result = mt5.order_send(request)*** invia l'ordine configurato dalla variabile di input ***request*** ed associa l'esito della richiesta (sotto forma di codice identificativo) alla variabile ***result***.
la riga 130 stampa a video le informazioni relative all'ordine appena inviato. Per maggiori informazioni vedere https://www.mql5.com/it/docs/integration/python_metatrader5/mt5ordersend_py .

riga 131-134: le seguenti righe stampano a video l'esito dell'ordine in caso di errore, altrimenti se l'rdine va a buon fine viene aggiunto il valore del "ticket" (valore identificativo dell'ordine) alla lista ***orders***.

riga 136: l'istruzione ***if close_condition and orders:*** esegue le righe contenuti all'interno del suo corpo (138-154) solo se ***close_condition = True*** e la lista ***orders*** non è vuota, ossia solo se si attiva il segnale di vendita e sono presenti ordini di acquisto ancora non chiusi.

riga 138: l'istruzione ***for order in orders:*** esegue un ciclo iterando sugli elementi della lista ***orders***, ossia la lista contenente i "tickets" degli ordini aperti. Ad ogni iterazione l'istruzione ***For*** esegue le righe contenute all'interno del corpo dell'istruzione (139-154).

riga 139-141: la riga di codice ***position_id = order*** ssocia il valore del ticket dell'ordine considerato alla variabile ***position_id***.
Il comando ***price = mt5.symbol_info_tick(SYMBOL).bid*** associa alla variabile ***price*** il prezzo attuale di venidta (bid).
La variabile ***deviation*** come già visto definisce la variazione di prezzo che siamo disposti a tollerare.

riga 142-154: Come visto in precedenza definiamo le variabili di input della richiesta di ordine, stavoltà trattando però un oridne di vendità e non di acquisto. Un parametro aggiuntivo è la coppia "chiave-valore" definita dalla chiave ***position***, la quale prende in input il ticket dell'ordine che si intende chiudere (fondamentale per distinguere in maniera univoca l'ordine).

riga 157-167: analogamente al blocco costituito dalle righe 127-134 esso invia l'ordine e stampa a video un eventuale esito negativo, mentre nel caso di esito positivo chiude l'ordine identificato da ticket e rimuove il relativo ticket dalla lista ***orders***.

riga 169: il comando ***cnt += 1*** al termine di ogni ciclo incrementa di 1 la variabile ***cnt*** che tiene il conto dei cicli eseguiti.
