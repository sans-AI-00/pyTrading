
# What is Python?

## Introduction

So what is Python? Python by definition is a "high-level", object-oriented programming language.
To find out more about the meaning of these words, and to find out much more about the language and its history, I left you a link in the description where you can dare to take a look at the Python wikipedia page.
Furthermore, the more determined, always in the description, can find the link that points to a very exhaustive and practical pdf document on programming in python.

The best way to understand what Python is, besides of course practicing it, is to understand what you will be able to do thanks to its knowledge. Python has a huge amount of importable libraries, each specific to a particular use case. A library is nothing more than a set of functions that you can import and therefore use within your code, and we will better see what it is about in the following videos of the course. Basically Python offers a library of functions already incorporated into the language, called the standard library, which does not require an import process. It is possible to find libraries for every use in a completely free and free way, for example machine learning and artificial intelligence, web automation and data scriping (i.e. the so-called bots), automatic trading, blockchain and smart contracts, network analysis (for example social networks) and also development of graphic interfaces for webapps, smartphone applications, software and websites. These are just a few use cases, and I could stay here talking about them for months.

So I leave you only to imagine the job opportunities that will create when you know how to handle this powerful programming language, obviously also based on the level of knowledge and use you have, but believe me when I tell you that it is never too late to start. Personally, it took me a year of planning to get to professional levels, and I think you should take even less time with the commitment.

A crucial role is played by the documentation (python 3.9), it is a collection of material and information that contains everything there is to know about the Python language. [By clicking here](https://docs.python.org/3/) you can access the online documentation.
Let's look at it briefly to realize what it is. In the following box at the top right you can select the Python version, in our case 3.9.

![Cattura](https://user-images.githubusercontent.com/105428493/192248391-2d699e21-ea64-4f3f-9803-0b9ce94d8cdd.PNG)

In the [tutorial](https://docs.python.org/3.9/tutorial/index.html) item you can find useful examples of using the programming language, while in the [library reference](https://docs.python.org/3.9/library/index.html) item you can find information about the operations and functions that can be used in Python. And taking a first look you will realize that there are many. Instead, clicking on [language reference](https://docs.python.org/3.9/reference/index.html) you get information about the syntax of the code, that is the writing rules to follow in order to write a code without errors and therefore executable by the python compiler. Syntax is basically the grammar of language, and as such it is essential.

The python compiler, also called interpreter, is the fundamental element that, in fact, interprets the code written by us by converting it into concrete operations performed by our computer.

Even if the content to learn seems to be a lot, do not be discouraged, you will only use a part of it and you do not need to have everything in mind, the programmer's ability in fact lies in knowing how to identify what is needed when necessary and take advantage of the documentation available on the net. to identify and use the correct tool according to your needs.

I want to clarify that the network and the various communities that populate it will be your main ally in language learning. Whenever you encounter a problem, you can be sure that 99% will have already been faced by someone else, who will have wisely exposed it on a special site where many kind-hearted programmers have provided their solution.

We will write and execute the python code thanks to a special development software, generally referred to by the term "IDE". If you don't know what an IDE is, I'll explain it to you briefly.
Simply put, an IDE, or integrated development environment, is software designed for building applications that combines common development tools into a single graphical user interface. Where by development tools we mean tools useful for writing code, in this case, in fact, Python code. The IDE we will use is called Pycharm and in my opinion it is one of the best for Python, if not perhaps the best IDE out there.

First of all you will need to download the development environment, in the following links you can find the Pycharm [download page](https://www.jetbrains.com/pycharm/download/#section=windows) and [installation instructions](https://www.youtube.com/watch?v=SZUNUB6nz3g). You have the opportunity to download two different versions, I recommend that you download the "Community" version as it is free but at the same time complete with all the tools you need to program at a professional level.

## Variables

We are inside Pycharm, a development software, also called IDE, which offers useful tools for writing code in the Python language. What you can see is the Python console that will allow us to write code interactively, running a single command at a time. As usually happens when we enter commands inside the terminal of our computer. Later in the course we will instead begin to write real scripts, that is, files similar to text documents composed of different commands written on top of each other, and automatically executed by the computer in an order that goes from top to bottom.

Python allows us to manage different types of data, in this lesson we will use two very common types, namely strings and integers. A string type data is defined by the use of quotes as follows:

__'string'
(type enter) __

or similarly through the use of double quotes

__"string"
(type enter) __

the content represented by this type of data is nothing more than a sequence of characters of variable length, ie a text. And it is typically characterized by the green color.

While an integer numeric data will be trivially represented by a sequence of digits. The characteristic color in this case is blue (azure).

__123
(type enter) __

In both cases, typing the data in the command line and pressing enter we obtain, in the line immediately following, the representation of the data itself.


The first concept of fundamental importance in language is the concept of variable. We can imagine it as a container capable of hosting a data among those allowed in the Python language.

The variable itself is represented by the name that we decide to associate with it, it acts as a label thanks to which we can recall at any time the data it hosts inside.

Therefore the correct syntax to associate a data, that is a value, to the variable is the following

__container = 123
(type enter) __

To the left of the "=" sign we have written the name of our variable. we can choose any name of our imagination for the variable, in this case we have decided to call it "container". While to the right of the equal we have written the value that will be inserted inside the variable. The symbol "=" is the fulcrum of this command and is used to make the compiler understand, once the command has been read, that our intention is precisely to associate the numerical data consisting of the digits to the variable named "container" 123.

We can choose any name for our variable, as long as it doesn't contain spaces.

It is interesting to note that, unlike other languages ​​such as "C", it was not necessary to define the type of variable before assigning its value. In fact, the Python compiler is able to automatically detect the type of data that we have decided to insert into it.

Once we type our variable and send the command, it is treated by the compiler just like the data it hosts inside it.

__container
(type enter) __

Therefore there is no difference between the variable and the data we associate with it. It is a powerful tool that allows us to carry a certain data with us while writing a script, without having to remember each time what value it has, but simply calling it by name.

## Functions









# Cos'è Python ?

## Introduzione

Dunque cos’è Python ? Python per definizione è un linguaggio di programmazione di "alto livello", orientato a oggetti.
Per saperne meglio sul significato di queste parole, e per scoprire molto altro sul linguaggio e sulla sua storia, ti ho lasciato un link in descrizione dove potrai dare uno sguardo alla pagina wikipedia di Python.
Inoltre i più determinati, sempre in descrizione, potranno travare il link che punta ad un documento pdf molto esaustivo e pratico sulla programmazione in python.

Il miglior modo per comprendere cosa sia Python, oltre ovviamente a praticarlo, è capire cosa sarai in grado di fare grazie alla sua conoscenza. Python dispone di una quantità enorme di librerie importabili, ognuna specifica per un determinato caso d’uso. Una libreria altro non è che un insieme di funzioni che potrai importare e dunque utilizzare all’interno del tuo codice, e vedremo meglio di che si tratta nei video successivi del corso. Di base Python offre una libreria di funzioni già incorporate all’interno del linguaggio, chiamata libreria standard, che non necessita di un processo di importazione. E’ possibile reperire in modo completamente libero e gratuito librerie per ogni utilizzo, ad esempio machine learning ed inteligenza artificiale, automazione web e scriping di dati (ossia i cosiddetti bot), Trading automatico,  blockchain e smart contract, analisi di reti (ad esempio reti social) ed anche sviluppo di interfacce grafiche per webapp, applicazioni smartphone, software e siti web. Questi sono solo alcuni casi d’uso, e potrei restare qui a parlarne per mesi.

Dunque ti lascio solo immaginare le opportunità lavorative che si creeranno nel momento in cui saprai maneggiare questo potente linguaggio di programmazione, ovviamente anche in base al livello di conoscenza e utilizzo che hai sviluppato, ma credimi se ti dico che non è mai troppo tardi per incominciare. Personalmente mi è servito un anno di programmazione per arrivare a livelli professionali, e credo che tu potresti impiegarci anche meno con il giusto impegno.


Un ruolo cruciale è svolto dalla documentazione (python 3.9), essa è una raccolta di materiale ed informazioni che racchiude tutto ciò che c’è da sapere sul linguaggio Python. [Cliccando qui](https://docs.python.org/3/) puoi accedere alla documentazione online. 
Osserviamola brevemente per renderci conto di che si tratta. Nel seguente riquadro in alto a destra è possibile selezionare la versione di Python, nel nostro caso la 3.9.

![Cattura](https://user-images.githubusercontent.com/105428493/192248391-2d699e21-ea64-4f3f-9803-0b9ce94d8cdd.PNG)

Nella voce [tutorial](https://docs.python.org/3.9/tutorial/index.html) puoi trovare utili esempi di utilizzo del linguaggio di programmazione, mentre nella voce [library reference](https://docs.python.org/3.9/library/index.html) sono contenute informazioni riguardo le operazioni e le funzioni urilizzabili in Python. E dando un primo sguardo potrai renderti conto che sono molte. Invece cliaccando su [language reference](https://docs.python.org/3.9/reference/index.html) si ottengono informazioni riguardo la sintassi del codice, ossia le regole di scrittura da seguire al fine di scrivere un codice privo di errori e dunque eseguibile dal compilatore python. La sintassi è sostanzialmente la grammatica del linguaggio, e in quanto tale è essenziale.

Il compilatore python, anche detto interprete, è l’elemento fondamentale che, appunto, interpreta il codice scritto da noi convertendolo in operazioni concrete eseguite dal nostro computer.

Anche se il contenuto da apprendere sembra essere molto, non ti scoraggiare, ne utilizzerai solo una parte e non serve avere tutto a mente, l’abilità del programmatore infatti sta nel saper individuare ciò che serve all’occorrenza e sfruttare la documentazione disponibile in rete per individuare ed utilizzare lo strumento corretto in base alle proprie esigenze.

Ci tengo a precisare che la rete e le varie comunity che la popolano saranno il tuo principale alleato nell’apprendimento del linguaggio. Ogni qualvolta incontrerai un problema, stai certo che al 99% sarà stato affrontato già da qualcun’altro, il quale lo avrà saggiamente esposto su un apposito sito dove molti programmatori di buon cuore hanno provveduto ad offrire la propria soluzione.

Andremo a scrivere ed eseguire il codice python grazie ad un’apposito software di sviluppo, indicato in generale con il termine “IDE”. Se non sai cosa sia un’IDE te lo spiego brevemente.
Un IDE, o ambiente di sviluppo integrato, in parole povere è un software progettato per la realizzazione di applicazioni che unisce strumenti di sviluppo comuni in un'unica interfaccia utente grafica. Dove per strumenti di sviluppo si intende strumenti utili alla scrittura di codice, in questo caso, appunto, codice Python. L’IDE che  utilizzeremo si chiama Pycharm è a mio parere è una delle migliori per Python, se non forse la migliore IDE in circolazione.

Prima di tutto dovrai scaricare l’ambiente di sviluppo, nei seguenti link potrai trovare la [pagina per lo scaricamento](https://www.jetbrains.com/pycharm/download/#section=windows) e le [istruzioni per l’installazione](https://www.youtube.com/watch?v=SZUNUB6nz3g) di Pycharm. Hai l’opportunità di scaricare due versioni differenti, ti consiglio di scaricare la versione “Community” in quanto è gratuita ma allo stesso tempo completa di tutti gli strumenti necessari per programmare a livello professionale. 

## Variabili

Siamo all’interno di Pycharm , un software di sviluppo, anche detto IDE, che offre strumenti utili per la scrittura di codice nel linguaggio Python. Questa che potete osservare  è  la console di Python che ci permetterà di scrivere codice in maniera interattiva, eseguendo un singolo comando alla volta. Come avviene solitamente quando inseriamo comandi all’interno del terminale del nostro computer. Più avanti nel corso inizieremo invece a scrivere veri e propri script, ossia file simili a documenti di testo composti da diversi comandi scritti uno sull’altro, ed eseguiti in modo automatico dal computer seguendo un ordine che va dall’alto verso il basso.

Python ci permette di gestire diversi tipi di dati,in questa lezione utilizzeremo due tipi molto comuni,  ossia le stringhe e i numeri interi. Un dato di tipo stringa è definito mediante l’uso degli apici nel seguente modo:

__‘stringa’
(digitare invio)__

o analogamente mediante l’utilizzo di doppi apici

__“stringa”
(digitare invio)__

il contenuto rappresentato da questo tipo di dato altro non è che una sequenza di caratteri di lunghezza variabile, ossia un testo. Ed è  tipicamente caratterizzata dal colore verde.

Mentre un dato di tipo numerico intero sarà banalmente rappresentato da una sequenza di cifre. Il colore caratteristico in questo caso è il blu (azzurro).

__123
(digitare invio)__

In entrambi i casi digitando il dato nella riga di comando e premendo invio otteniamo, nella riga immediatamente successiva, la rappresentazione del dato stesso.


Il primo concetto di fondamentale importanza nel linguaggio è il concetto di variabile. Possiamo immaginarla come  un contenitore capace di ospitare un dato tra quelli consentiti nel linguaggio Python.  

La variabile è di per sé rappresentata dal nome che decidiamo di associargli, esso funge come un’etichetta grazie alla quale possiamo richiamare in qualunque momento il dato che ospita al suo interno all’interno. 

Dunque la sintassi corretta per associare un dato, ossia un valore, alla variabile è la seguente

__contenitore = 123
(digitare invio)__

Alla sinistra del segno “=” abbiamo scritto il nome della nostra variabile. possiamo scegliere un nome qualunque di nostra fantasia per la variabile, in questo caso abbiamo deciso di chiamarla “contenitore”. Mentre alla destra dell’uguale abbiamo scritto il valore che andrà inserito all’interno della variabile. Il simbolo “=” è il fulcro di questo comando è serve proprio a far capire al compilatore, una volta letto il comando, che la nostra intenzione è proprio quella di associare alla variabile di nome “contenitore” il dato di tipo numerico costituito dalle cifre 123.

Possiamo scegliere qualunque nome per la nostra variabile, purché non contenga spazi.

E’ interessante osservare che, a differenza di altri linguaggi come il “C”, non è stato necessario definire il tipo di variabile prima dell’assegnazione del suo valore. Infatti il compilatore di Python, è in grado di rilevare automaticamente il tipo di dato che abbiamo deciso di inserire al suo interno. 

Una volta che digitiamo la nostra variabile e inviamo il comando, essa è trattata dal compilatore proprio come il dato che ospita al suo interno. 

__contenitore
(digitare invio)__

Dunque non vi è alcuna differenza tra la variabile e il dato che associamo ad essa. Essa è uno strumento potente che ci permette di portarci dietro durante la scrittura di uno script un certo dato, senza doverci ricordare ogni volta che valore abbia, ma chiamandolo semplicemente per nome. 

## Funzioni


