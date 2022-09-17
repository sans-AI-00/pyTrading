# pyTrading 

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

### Utilizzo:

Di seguito si illustra il procedimento da seguire per avviare gli script di esempio o le strategie:
1) scaricare il progetto da github ed inserirlo preferibilmente nel percorso "C:\" (va bene anche una posizione generica).
2) Aprire "Anaconda powershell prompt" sul proprio pc. 
3) Inserire all'interno del prompt il seguente comando "cd <path\to\pyTrading-main>", dove al posto di <path\to\pyTrading-main> va inserito il path della cartella del progetto "pyTrading". Nota: nel caso la cartella sia stata posizionata nel percorso "C:\" il comando è "cd C:\pyTrading-main".
4) Se si vuole eseguire una startegia eseguire il comando "python strategies\nome_strategia\nome_strategia.py", dove al posto di "nome_strategia.py" andremo ad inserire il nome dello script python relativo alla strategia che intendiamo eseguire. Nota: nel caso della strategia "ROC", per esempio, il comando sarà "python strategies\ROC_strategy\ROC_strategy.py".
5) Analogamente per eseguire gli script di esempio inserire il seguente comando "python examples\nome_esempio.py".