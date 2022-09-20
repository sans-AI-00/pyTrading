# pyTrading (eng)

### Prerequisites:

1) Install the Meta Trader 5 trading platform on your computer (preferably windows pc). Download and account creation page (XM broker): https://www.xm.com/it/?gclid=CjwKCAjw4JWZBhApEiwAtJUN0DMsZi3gC2gO2GNoXRsR2njLn6qPL77d6nFdTo8jFkHlUQPIEVBWQnCho
2) Create Meta Trader 5 account accounts (for example through XM or other brokers ...)
3) Identify, on your PC, the path of the Meta Trader 5 terminal, typically in the form
PATH = "path \\\ to \\\ MT5 \\\ terminal64.exe".
4) Obtain the following information regarding the MT5 account:
   1) USER_ID
   2) PASSWORD
   3) SERVER
5) Install the "Python compiler" if not present in the operating system (preferably Python 3.8.x-3.9.x). Download page: https://www.python.org/downloads/.
To check the presence and any version of the python compiler on your pc, follow the instructions on the following page: https://www.wikihow.it/Controlla-la-Versa-di-Python-in-Windows-o-su -Mac
6) Install "Anaconda". Download page: https://www.anaconda.com/products/distribution/download-success-pythonanywhere
7) Install the "ta-lib" python library. Procedure by platform: https://blog.quantinsti.com/install-ta-lib-python/
8) Install the "MetaTrader5" python library (run "pip install MetaTrader5" in the anaconda terminal)
9) Install the "numpy" python library (run "pip install numpy" in the anaconda terminal)
10) Install the python library "pandas" (run "pip install pandas" in the anaconda terminal)
11) Install the "matplotlib" python library (run "pip install matplotlib" in the anaconda terminal)

### Contents description:
* "Examples" directory *: inside you can find various python scripts, each of which shows a practical example of using the functions offered by the "MetaTrader5" library.
For more information visit the official website: https://www.mql5.com/it/docs/integration/python_metatrader5. To use the examples edit the Python file "login_environments_variables.py" (contained in the "examples" directory), which contains the environment variables that the strategy uses to access the Meta Trader 5 account with which you intend to operate. The user must replace the value of the "LOGIN", "PASSWORD", "SERVER" and "PATH" variables with the values ​​of his own account. making sure to insert "LOGIN" in the form of an integer and the other variables in the form of strings.

* Directory "financial_tools" *: inside it it is possible to identify all the function classes that implement the technical indicators and more generally the tools that we will use for the strategies. This directory will be copied into the root directory of any strategy we are going to create and use.

* Directory "strategies' *: inside there are the directories of our strategies, which contain everything you need to make the strategy work. More specifically, each strategy directory consists of the following files:
1) The "financial_tools" directory which contains the technical tools. The user will not have to modify the files contained within it unless he intends to create new indicators or modify existing ones.
2) The Python file "login_environments_variables.py", which contains the environment variables that the strategy uses to access the Meta Trader 5 account with which you intend to operate. The user must replace the value of the "LOGIN", "PASSWORD", "SERVER" and "PATH" variables with the values ​​of his own account. making sure to insert "LOGIN" in the form of an integer and the other variables in the form of strings.
3) the Python file "strategy_environments_variables", which contains the environment variables that describe the main operational parameters of the strategy. The "SYMBOL" variable (string) describes the TAG of the asset in which we intend to invest. "LOT" (decimal) is a number that describes the amount of each investment. On the other hand, the "MAGIC" variable wing (integer) must provide the arbitrary "number plate" that will allow us to distinguish the operations performed by different strategies that operate simultaneously on the emdth account, and obviously helps us to avoid that the different strategies conflict between They.
4) the Python file "name_strategy.py", which will be the script that we would actually execute to make the strategy operational by putting it on the market.
5) the "info_strategy.md" file in which all the information relating to the strategy in question and the optimal setting of the parameters are entered.

### Usage:

Here is the procedure to follow to start the example scripts or strategies:
1) download the project from github and insert it preferably in the path "C: \" (a generic location is fine too).
2) Open "Anaconda powershell prompt" on your pc.
3) Enter the following command in the prompt "cd <path \ to \ pyTrading-main>", where instead of <path \ to \ pyTrading-main> the path of the "pyTrading" project folder must be entered. Note: if the folder has been placed in the path "C: \" the command is "cd C: \ pyTrading-main".
4) If you want to execute a strategy, execute the command "python strategies \ name_strategy \ name_strategy.py", where instead of "name_strategy.py" we will enter the name of the python script relating to the strategy we intend to execute. Note: in the case of the "ROC" strategy, for example, the command will be "python strategies \ ROC_strategy \ ROC_strategy.py".
5) Similarly to run the example scripts enter the following command "python examples \ name_example.py".

### Future additions:

1) new strategies will be periodically added to the "strategies" directory.
2) the "strategy_environments_variables.py" file will be extended in such a way as to allow the adjustment of various parameters with different methodologies, for example the possibility of determining the capital to invest per single operation as a percentage of the available capital (and not only in absolute value as a multiple of "lots")
3) new functions will be developed to simplify the initialization of the strategy and the marketing of the operations, so as to make the code of the strategies "cleaner".
4) BeckTesting functionalities will be included.




# pyTrading(ita) 

### Prerequisiti:

1) Installare la piattaforma di Trading Meta Trader 5 sul proprio computer (preferibilmente pc windows). Pagina Download e creazione conto (broker XM): https://www.xm.com/it/?gclid=CjwKCAjw4JWZBhApEiwAtJUN0DMsZi3gC2gO2GNoXRsR2njLn6qPL77d6nFdTo8jFkHlUQPIEAMnChoCSVkQAvD_BwE 
2) Creare account conto Meta Trader 5 (ad esempio mediante XM o altri broker...)
3) Individuare, nel proprio pc, il path del terminale di Meta Trader 5, tipicamente nella forma 
PATH = "path\\\to\\\MT5\\\terminal64.exe".
4) Ottenere le seguenti informazioni relative all'account MT5:
   1) ID_UTENTE
   2) PASSWORD
   3)  SERVER
5) Installare il "compilatore Python" se non presente nel sistema operativo (preferibilmente Python 3.8.x-3.9.x). Pagina download: https://www.python.org/downloads/ .
Per verificare la presenza e l'eventuale versione del compilatore python nel proprio pc, seguire le istruzioni nella seguente pagina:  https://www.wikihow.it/Controllare-la-Versione-di-Python-in-Windows-o-su-Mac
6) Installare "Anaconda". Pagina Download:  https://www.anaconda.com/products/distribution/download-success-pythonanywhere
7) Installare la libreria python "ta-lib". Procedura in base alla piattaforma : https://blog.quantinsti.com/install-ta-lib-python/
8) Installare la libreria python "MetaTrader5" (run "pip install MetaTrader5" nel terminale anaconda)
9) Installare la libreria python "numpy" (run "pip install numpy" nel terminale anaconda)
10) Installare la libreria python "pandas" (run "pip install pandas" nel terminale anaconda)
11) Installare la libreria python "matplotlib"  (run "pip install matplotlib" nel terminale anaconda)

### Descrizione contenuti:
*Directory "examples"*: al suo interno potrai trovare vari scripts python, ognuno dei quali mostra un esempio pratico di utilizzo delle funzioni che offre la libreria "MetaTrader5".
Per maggiori informazioni visitare il sito ufficiale: https://www.mql5.com/it/docs/integration/python_metatrader5 . Per utilizzare gli esempi modificare il file Python "login_environments_variables.py" (contenuto nella directoy "examples"), il quale contiene le variabili di ambiente che la strategia utilizza per accedere al conto Meta Trader 5 con cui si intende operare. L'utente dovrà sostituire il valore delle variabili "LOGIN", "PASSWORD", "SERVER" e "PATH" con i valori del proprio conto. facendo attenzione a inserire "LOGIN" in forma di numero intero e le altre variabili in forma di stringhe.

*Directory "financial_tools"*: al suo interno è possibile individuare tutte le classi di funzioni che implementano gli indicatori tecnici e più in generale gli strumenti che andremo ad utilizzare per le strategie. Questa directory andrà copiata all'interno della directory principale di qualunque strategia che andremo a creare ed utilizzare.

*Directory "strategies'*: al suo intrno sono presenti le directory delle nostre strategie, le quali contengono tutto quello che serve per far funzionare la strategia. Più nello specifico ogni directory di strategia consiste nei seguenti file:
1) La directory "financial_tools" che contiene gli strumenti tecnici. L'utente non dovrà modificare i file conttenuti al suo interno a meno che non intenda creare nuovi indicatori o modificare quelli esistenti.
2) Il file Python "login_environments_variables.py", il quale contiene le variabili di ambiente che la strategia utilizza per accedere al conto Meta Trader 5 con cui si intende operare. L'utente dovrà sostituire il valore delle variabili "LOGIN", "PASSWORD", "SERVER" e "PATH" con i valori del proprio conto. facendo attenzione a inserire "LOGIN" in forma di numero intero e le altre variabili in forma di stringhe.
3) il file Python "strategy_environments_variables", il quale contiene le variabili di ambiente che descrivono i parametri operativi principali della strategia. La variabile "SYMBOL" (stringa) descrive il TAG dell'asset sul quale intendiamo investire. "LOT" (decimale) è un numero che descrive l'importo di ogni investimento. Ala variabile "MAGIC" (intero) invece bisogna fornire la "targa numerica" arbitraria che ci permetterà di distinguere le operazioni eseguite da diverse strategie che operano in simultanea sul emdesimo conto, ed ovviamente ci aiuta ad evitare che le diverse strategie vadano in conflitto tra loro.
4) il file Python "name_strategy.py", il quale sarà lo script che andremmo effettivamente ad eseguire per rendere operativa la strategia mettendola a mercato. 
5) il file "info_strategy.md" nel quale sono inserite tutte le informazioni relative alla strategia in questione e sul settaggio ottimale dei parametri.

### Utilizzo:

Di seguito si illustra il procedimento da seguire per avviare gli script di esempio o le strategie:
1) scaricare il progetto da github ed inserirlo preferibilmente nel percorso "C:\" (va bene anche una posizione generica).
2) Aprire "Anaconda powershell prompt" sul proprio pc. 
3) Inserire all'interno del prompt il seguente comando "cd <path\to\pyTrading-main>", dove al posto di <path\to\pyTrading-main> va inserito il path della cartella del progetto "pyTrading". Nota: nel caso la cartella sia stata posizionata nel percorso "C:\" il comando è "cd C:\pyTrading-main".
4) Se si vuole eseguire una startegia eseguire il comando "python strategies\nome_strategia\nome_strategia.py", dove al posto di "nome_strategia.py" andremo ad inserire il nome dello script python relativo alla strategia che intendiamo eseguire. Nota: nel caso della strategia "ROC", per esempio, il comando sarà "python strategies\ROC_strategy\ROC_strategy.py".
5) Analogamente per eseguire gli script di esempio inserire il seguente comando "python examples\nome_esempio.py".

### Aggiunte future:

1) verranno aggiunte periodicamente nuove strategie nella directory "strategies". 
2) il file "strategy_environments_variables.py" verrà esteso in modo tale da permettere la regolazione di diversi parametri con metodologie diverse, ad esempio la possibilità di determinare il capitale da investire per singola operazione in percdentuale al capitale disponibile (e non solo in valore assoluto come multiplo di "lotti")
3) verranno sviluppate nuove funzioni per rendere più semplici le operazioni di inzializzazione della strategia e di messa a mercato delle operazioni, così da rendere il codice delle strategie più "pulito".
4) saranno inserite le funzionalità di BeckTesting.