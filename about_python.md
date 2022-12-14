
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

![Cattura](https://user-images.githubusercontent.com/105428493/192253741-41371f9e-1819-4cf0-b6d1-340c44b798f5.PNG)

Python allows us to manage different types of data, in this lesson we will use two very common types, namely strings and integers. A string type data is defined by the use of quotes as follows:

__'string'
(type enter)__

or similarly through the use of double quotes

__"string"
(type enter)__

the content represented by this type of data is nothing more than a sequence of characters of variable length, ie a text. And it is typically characterized by the green color.

While an integer numeric data will be trivially represented by a sequence of digits. The characteristic color in this case is blue (azure).

__123
(type enter)__

In both cases, typing the data in the command line and pressing enter we obtain, in the line immediately following, the representation of the data itself.


The first concept of fundamental importance in language is the concept of variable. We can imagine it as a container capable of hosting a data among those allowed in the Python language.

The variable itself is represented by the name that we decide to associate with it, it acts as a label thanks to which we can recall at any time the data it hosts inside.

Therefore the correct syntax to associate a data, that is a value, to the variable is the following

__container = 123
(type enter)__

To the left of the "=" sign we have written the name of our variable. we can choose any name of our imagination for the variable, in this case we have decided to call it "container". While to the right of the equal we have written the value that will be inserted inside the variable. The symbol "=" is the fulcrum of this command and is used to make the compiler understand, once the command has been read, that our intention is precisely to associate the numerical data consisting of the digits to the variable named "container" 123.

We can choose any name for our variable, as long as it doesn't contain spaces.

It is interesting to note that, unlike other languages such as "C", it was not necessary to define the type of variable before assigning its value. In fact, the Python compiler is able to automatically detect the type of data that we have decided to insert into it.

Once we type our variable and send the command, it is treated by the compiler just like the data it hosts inside it.

__container
(type enter)__

Therefore there is no difference between the variable and the data we associate with it. It is a powerful tool that allows us to carry a certain data with us while writing a script, without having to remember each time what value it has, but simply calling it by name.

![Cattura](https://user-images.githubusercontent.com/105428493/192258533-d57cc96f-ee96-46e1-8436-a3c490cadebb.PNG)

## Functions

we introduce the concept of function. The functions in programming, conceptually, behave in a completely analogous way to the mathematical functions.
A function requires the insertion of a certain number of input variables, the latter are then manipulated within the function in order to produce a result, called output.

In general we are dealing with three types of functions:
Functions that output data of a certain type, a value that we can subsequently associate with a variable created by us;
Functions whose purpose is to perform internal operations on the computer, such as saving or deleting files;
We can also encounter functions whose purpose is to interact with the user through the screen input output, for example by printing graphics and texts, or by requesting the entry of values from the keyboard.

With the exception of the first type of function, the other two do not necessarily assume a certain output value once executed, in which case the value assumed by the function will be the so-called ???None??? type value, ie literally nothing.

Let's see in practice what it is.

The first function that we observe is called "input", the syntax of the language generally requires that to execute a function you must first write its name, followed by round brackets. It is inside the round brackets that we are going to enter the input values required by the function we are using.

__input()__

The input function requires that a string type value be supplied as input data, so let's insert a representative text, for example the following sentence "write me something:".

__input ("write me something:")__

and finally we associate the result of the function to the variable named "container"

__container = input ("write me something:")
(type enter)__

at this point we send the command. What happens is that this function prints on the screen the phrase we entered in input, waiting for the user to write something to send. So let's literally write "something" and type the "enter" key as always to send the content of what we have written.

What happened at this point? Well it happened that the "input" function returned exactly what we wrote to it, then we subsequently inserted this output value into the "container" variable.

At this point we can observe the content of the "container" variable by typing its name and sending the command.

__Container
(type enter)__

From the presence of the quotes we immediately understand that the content of the "container" variable, that is the output of the "input" function, is of the string type. The value assumed by the output string is exactly what we had typed from the keyboard and fed to the "input" function.

![Cattura_2](https://user-images.githubusercontent.com/105428493/192258555-f11b6b80-2686-44e6-8515-0f651379a386.PNG)

## Utility library

### Pandas:
Pandas is one of the most versatile libraries in the Python world. It is based on NumPy and, in turn, offers the foundation for
many others work environments.

Its operation hinges on two main data structures. The first is the DataFrame, a sort of table, structured on columns where the data is distributed by rows.
It is interesting to note that both the columns and the rows are indexed in order to facilitate access to them individually or in groups. Working in Panda means manipulating data with
DataFrame and related functionalities. The other data structure is the series that is used to represent rows or columns of a DataFrame.

At this point our aim is to become familiar with the DataFrame and learn how to manipulate the data within them.

For more information [click here](https://www.html.it/pag/402840/pandas-series-dataframe/).

### Numpy:

NumPy is one of the most popular, used and appreciated Python modules, to the point of being practically inevitable in any project that has to do with data science, data analysis or machine learning. In this practical guide we will learn to know all its facets, acquiring the necessary knowledge to use it in a professional environment.

For more information [click here](https://www.html.it/guide/numpy-guida/).

### Matplotlib:

Matplotlib is one of the most important libraries in the Data Science scenario not only for its wide use but also because
offers itself as a graphing engine for many other tools.

For more information [click here](https://www.html.it/pag/404701/matplotlib/).

### Tensorflow:

Created by the Google Brain team and initially released to the public in 2015, TensorFlow is an open source library for large-scale numerical computing and machine learning. TensorFlow brings together a number of machine learning and deep learning (aka neural networks) models and algorithms and makes them useful through common programmatic metaphors. It uses Python or JavaScript to provide a convenient front-end API for building applications, while running those applications in high-performance C ++.


TensorFlow, which competes with frameworks such as PyTorch and Apache MXNet, can train and execute deep neural networks for handwritten digit classification, image recognition, word embedding, recurrent neural networks, sequence-to-sequence models for machine translation, natural language processing and PDE-based simulations (partial differential equation). Most importantly, TensorFlow supports large-scale production forecasting, with the same models used for training.


TensorFlow also has an extensive library of pre-trained models that can be used in your own projects. You can also use the code from TensorFlow Model Garden

as examples of best practices for training your models.

For more information [click here](https://www.tensorflow.org/guide).


# Cos'?? Python ?

## Introduzione

Dunque cos????? Python ? Python per definizione ?? un linguaggio di programmazione di "alto livello", orientato a oggetti.
Per saperne meglio sul significato di queste parole, e per scoprire molto altro sul linguaggio e sulla sua storia, ti ho lasciato un link in descrizione dove potrai dare uno sguardo alla pagina wikipedia di Python.
Inoltre i pi?? determinati, sempre in descrizione, potranno travare il link che punta ad un documento pdf molto esaustivo e pratico sulla programmazione in python.

Il miglior modo per comprendere cosa sia Python, oltre ovviamente a praticarlo, ?? capire cosa sarai in grado di fare grazie alla sua conoscenza. Python dispone di una quantit?? enorme di librerie importabili, ognuna specifica per un determinato caso d???uso. Una libreria altro non ?? che un insieme di funzioni che potrai importare e dunque utilizzare all???interno del tuo codice, e vedremo meglio di che si tratta nei video successivi del corso. Di base Python offre una libreria di funzioni gi?? incorporate all???interno del linguaggio, chiamata libreria standard, che non necessita di un processo di importazione. E??? possibile reperire in modo completamente libero e gratuito librerie per ogni utilizzo, ad esempio machine learning ed inteligenza artificiale, automazione web e scriping di dati (ossia i cosiddetti bot), Trading automatico,  blockchain e smart contract, analisi di reti (ad esempio reti social) ed anche sviluppo di interfacce grafiche per webapp, applicazioni smartphone, software e siti web. Questi sono solo alcuni casi d???uso, e potrei restare qui a parlarne per mesi.

Dunque ti lascio solo immaginare le opportunit?? lavorative che si creeranno nel momento in cui saprai maneggiare questo potente linguaggio di programmazione, ovviamente anche in base al livello di conoscenza e utilizzo che hai sviluppato, ma credimi se ti dico che non ?? mai troppo tardi per incominciare. Personalmente mi ?? servito un anno di programmazione per arrivare a livelli professionali, e credo che tu potresti impiegarci anche meno con il giusto impegno.


Un ruolo cruciale ?? svolto dalla documentazione (python 3.9), essa ?? una raccolta di materiale ed informazioni che racchiude tutto ci?? che c????? da sapere sul linguaggio Python. [Cliccando qui](https://docs.python.org/3/) puoi accedere alla documentazione online. 
Osserviamola brevemente per renderci conto di che si tratta. Nel seguente riquadro in alto a destra ?? possibile selezionare la versione di Python, nel nostro caso la 3.9.

![Cattura](https://user-images.githubusercontent.com/105428493/192248391-2d699e21-ea64-4f3f-9803-0b9ce94d8cdd.PNG)

Nella voce [tutorial](https://docs.python.org/3.9/tutorial/index.html) puoi trovare utili esempi di utilizzo del linguaggio di programmazione, mentre nella voce [library reference](https://docs.python.org/3.9/library/index.html) sono contenute informazioni riguardo le operazioni e le funzioni urilizzabili in Python. E dando un primo sguardo potrai renderti conto che sono molte. Invece cliaccando su [language reference](https://docs.python.org/3.9/reference/index.html) si ottengono informazioni riguardo la sintassi del codice, ossia le regole di scrittura da seguire al fine di scrivere un codice privo di errori e dunque eseguibile dal compilatore python. La sintassi ?? sostanzialmente la grammatica del linguaggio, e in quanto tale ?? essenziale.

Il compilatore python, anche detto interprete, ?? l???elemento fondamentale che, appunto, interpreta il codice scritto da noi convertendolo in operazioni concrete eseguite dal nostro computer.

Anche se il contenuto da apprendere sembra essere molto, non ti scoraggiare, ne utilizzerai solo una parte e non serve avere tutto a mente, l???abilit?? del programmatore infatti sta nel saper individuare ci?? che serve all???occorrenza e sfruttare la documentazione disponibile in rete per individuare ed utilizzare lo strumento corretto in base alle proprie esigenze.

Ci tengo a precisare che la rete e le varie comunity che la popolano saranno il tuo principale alleato nell???apprendimento del linguaggio. Ogni qualvolta incontrerai un problema, stai certo che al 99% sar?? stato affrontato gi?? da qualcun???altro, il quale lo avr?? saggiamente esposto su un apposito sito dove molti programmatori di buon cuore hanno provveduto ad offrire la propria soluzione.

Andremo a scrivere ed eseguire il codice python grazie ad un???apposito software di sviluppo, indicato in generale con il termine ???IDE???. Se non sai cosa sia un???IDE te lo spiego brevemente.
Un IDE, o ambiente di sviluppo integrato, in parole povere ?? un software progettato per la realizzazione di applicazioni che unisce strumenti di sviluppo comuni in un'unica interfaccia utente grafica. Dove per strumenti di sviluppo si intende strumenti utili alla scrittura di codice, in questo caso, appunto, codice Python. L???IDE che  utilizzeremo si chiama Pycharm ?? a mio parere ?? una delle migliori per Python, se non forse la migliore IDE in circolazione.

Prima di tutto dovrai scaricare l???ambiente di sviluppo, nei seguenti link potrai trovare la [pagina per lo scaricamento](https://www.jetbrains.com/pycharm/download/#section=windows) e le [istruzioni per l???installazione](https://www.youtube.com/watch?v=SZUNUB6nz3g) di Pycharm. Hai l???opportunit?? di scaricare due versioni differenti, ti consiglio di scaricare la versione ???Community??? in quanto ?? gratuita ma allo stesso tempo completa di tutti gli strumenti necessari per programmare a livello professionale. 

## Variabili

Siamo all???interno di Pycharm , un software di sviluppo, anche detto IDE, che offre strumenti utili per la scrittura di codice nel linguaggio Python. Questa che potete osservare  ??  la console di Python che ci permetter?? di scrivere codice in maniera interattiva, eseguendo un singolo comando alla volta. Come avviene solitamente quando inseriamo comandi all???interno del terminale del nostro computer. Pi?? avanti nel corso inizieremo invece a scrivere veri e propri script, ossia file simili a documenti di testo composti da diversi comandi scritti uno sull???altro, ed eseguiti in modo automatico dal computer seguendo un ordine che va dall???alto verso il basso.

![Cattura](https://user-images.githubusercontent.com/105428493/192253741-41371f9e-1819-4cf0-b6d1-340c44b798f5.PNG)

Python ci permette di gestire diversi tipi di dati,in questa lezione utilizzeremo due tipi molto comuni,  ossia le stringhe e i numeri interi. Un dato di tipo stringa ?? definito mediante l???uso degli apici nel seguente modo:

__???stringa???
(digitare invio)__

o analogamente mediante l???utilizzo di doppi apici

__???stringa???
(digitare invio)__

il contenuto rappresentato da questo tipo di dato altro non ?? che una sequenza di caratteri di lunghezza variabile, ossia un testo. Ed ??  tipicamente caratterizzata dal colore verde.

Mentre un dato di tipo numerico intero sar?? banalmente rappresentato da una sequenza di cifre. Il colore caratteristico in questo caso ?? il blu (azzurro).

__123
(digitare invio)__

In entrambi i casi digitando il dato nella riga di comando e premendo invio otteniamo, nella riga immediatamente successiva, la rappresentazione del dato stesso.


Il primo concetto di fondamentale importanza nel linguaggio ?? il concetto di variabile. Possiamo immaginarla come  un contenitore capace di ospitare un dato tra quelli consentiti nel linguaggio Python.  

La variabile ?? di per s?? rappresentata dal nome che decidiamo di associargli, esso funge come un???etichetta grazie alla quale possiamo richiamare in qualunque momento il dato che ospita al suo interno all???interno. 

Dunque la sintassi corretta per associare un dato, ossia un valore, alla variabile ?? la seguente

__contenitore = 123
(digitare invio)__

Alla sinistra del segno ???=??? abbiamo scritto il nome della nostra variabile. possiamo scegliere un nome qualunque di nostra fantasia per la variabile, in questo caso abbiamo deciso di chiamarla ???contenitore???. Mentre alla destra dell???uguale abbiamo scritto il valore che andr?? inserito all???interno della variabile. Il simbolo ???=??? ?? il fulcro di questo comando ?? serve proprio a far capire al compilatore, una volta letto il comando, che la nostra intenzione ?? proprio quella di associare alla variabile di nome ???contenitore??? il dato di tipo numerico costituito dalle cifre 123.

Possiamo scegliere qualunque nome per la nostra variabile, purch?? non contenga spazi.

E??? interessante osservare che, a differenza di altri linguaggi come il ???C???, non ?? stato necessario definire il tipo di variabile prima dell???assegnazione del suo valore. Infatti il compilatore di Python, ?? in grado di rilevare automaticamente il tipo di dato che abbiamo deciso di inserire al suo interno. 

Una volta che digitiamo la nostra variabile e inviamo il comando, essa ?? trattata dal compilatore proprio come il dato che ospita al suo interno. 

__contenitore
(digitare invio)__

Dunque non vi ?? alcuna differenza tra la variabile e il dato che associamo ad essa. Essa ?? uno strumento potente che ci permette di portarci dietro durante la scrittura di uno script un certo dato, senza doverci ricordare ogni volta che valore abbia, ma chiamandolo semplicemente per nome. 

## Funzioni

introduciamo il concetto di funzione. Le funzioni in programmazione, concettualmente,  si comportano in maniera del tutto analoga alle funzioni matematiche.
Una funzione richiede l???inserimento di un certo numero di variabili in input, queste ultime vengono poi manipolate all???interno della funzione al fine di produrre un risultato, detto output.

In generale ci troviamo ad avere a che fare con tre tipologie di funzioni: 
Funzioni che restituiscono in output un dato di un certo tipo, un valore che successivamente potremo associare ad una variabile da noi creata;
Funzioni il cui scopo ?? quello di eseguire operazioni interne al computer, come ad esempio salvare o eliminare file;
Inoltre possiamo incontrare funzioni il cui scopo ?? quello di interagire con l???utente mediante l???input output dello schermo, ad esempio stampando grafici e testi, oppure richiedendo l???inserimento di valori da tastiera.

Ad eccezione della prima tipologia di funzione, le altre due non necessariamente assumono un certo valore di output un volta eseguite, in tal caso il valore assunto dalla funzione sar?? il cosiddetto valore di tipo ???None??? ossia letteralmente niente.

Andiamo a vedere nel pratico di che si tratta. 

La prima funzione che osserviamo ?? chiamata ???input???, la sintassi del linguaggio generalmente impone che per eseguire una funzione si scriva prima di tutto il suo nome,  seguito poi da parentesi tonde. ?? proprio all???interno delle parentesi tonde che andremo ad inserire i valori di input richiesti dalla funzione che stiamo utilizzando. 

__input()__

La funzione input richiede che venga fornita come dato di input un valore di tipo stringa, andiamo dunque ad inserire una scritta rappresentativa, ad esempio la seguente frase ???scrivimi qualcosa:???.

__input(???scrivimi qualcosa: ???)__

ed infine associamo il risultato della funzione alla variabile di nome ???contenitore???

__contenitore = input(???scrivimi qualcosa: ???)
(digitare invio)__

a questo punto inviamo il comando.  Ci?? che accade ?? che tale funzione stampa a video proprio la frase da noi inserita in input, restando in attesa che l???utente scriva qualcosa da inviare. Dunque scriviamogli letteralmente ???qualcosa??? e digitiamo come sempre il tasto ???invio??? per inviare appunto il contenuto di ci?? che abbiamo scritto.

Cos????? accaduto a questo punto ? Bene ?? accaduto che la funzione ???input??? ha restituito in output proprio ci?? che noi gli abbiamo scritto, poi successivamente abbiamo inserito questo valore di output all???interno della variabile ???contenitore???.

A questo punto possiamo osservare il contenuto della variabile ???contenitore??? digitandone il nome ed inviando il comando. 

__Contenitore
(digitare invio)__

Dalla presenza degli apici comprendiamo subito che il contenuto della variabile ???contenitore???, ossia l???output della funzione ???input??? , ?? di tipo stringa. Il valore assunto dalla stringa di output ?? proprio ci?? che noi avevamo digitato da tastiera e dato in pasto alla funzione ???input???.

## Librerie utili

### Pandas:
Pandas ?? una delle librerie pi?? versatili del mondo Python. Si basa su NumPy e, a sua volta, offre il fondamento per
molti altri ambienti di lavoro.

Il suo funzionamento ?? imperniato su due strutture dati principali. La prima ?? il DataFrame, una sorta di tabella, strutturata su colonne dove i dati sono distribuiti per righe.
Interessante notare che sia le colonne sia le righe sono indicizzate al fine di facilitare l'accesso ad esse singolarmente o a gruppi. Lavorare in Pandas significa essenzialmente manipolare dati con
DataFrame e funzionalit?? ad essi collegate. L'altra struttura dati ?? la Series che viene utilizzata per rappresentare righe o colonne di un DataFrame.

A questo punto il nostro scopo ?? iniziare a prendere confidenza con i DataFrame ed imparare a manipolare i dati al loro interno.

Per maggiori informazioni [cliccare qui](https://www.html.it/pag/402840/pandas-series-dataframe/).

### Numpy:

NumPy ?? uno dei moduli Python pi?? diffusi, usati e apprezzati, al punto da essere praticamente immancabile in ogni progetto che abbia a che fare con data science, analisi dei dati o machine learning. In questa guida pratica impareremo a conoscerne tutte le sfaccettature, acquisendo le conoscenze necessarie per utilizzarlo in ambito professionale.

Per maggiori informazioni [cliccare qui](https://www.html.it/guide/numpy-guida/).

### Matplotlib:

Matplotlib ?? una delle librerie pi?? importanti nello scenario della Data Science non solo per il suo largo utilizzo ma anche perch??
si offre come motore di visualizzazione di grafici per molti altri strumenti. 


Per maggiori informazioni [cliccare qui](https://www.html.it/pag/404701/matplotlib/).

### Tensorflow:

Creata dal team di Google Brain e inizialmente rilasciata al pubblico nel 2015, TensorFlow ?? una libreria open source per il calcolo numerico e l'apprendimento automatico su larga scala. TensorFlow raggruppa una serie di modelli e algoritmi di machine learning e deep learning ( alias reti neurali ) e li rende utili tramite metafore programmatiche comuni. Utilizza Python o JavaScript per fornire una comoda API front-end per la creazione di applicazioni, mentre esegue tali applicazioni in C++ ad alte prestazioni.


TensorFlow, che compete con framework come PyTorch e Apache MXNet, pu?? addestrare ed eseguire reti neurali profonde per la classificazione delle cifre scritte a mano, il riconoscimento di immagini, l'incorporamento di parole, le reti neurali ricorrenti, i modelli da sequenza a sequenza per la traduzione automatica, l'elaborazione del linguaggio naturale e Simulazioni basate su PDE (equazione differenziale parziale). Soprattutto, TensorFlow supporta la previsione della produzione su larga scala, con gli stessi modelli utilizzati per la formazione.


TensorFlow ha anche un'ampia libreria di modelli pre-addestrati che possono essere utilizzati nei propri progetti. Puoi anche utilizzare il codice di TensorFlow Model Garden  

come esempi di best practice per addestrare i tuoi modelli.

Per maggiori informazioni [cliccare qui](https://www.tensorflow.org/guide).


