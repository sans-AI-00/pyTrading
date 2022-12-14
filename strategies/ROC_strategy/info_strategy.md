# Useful information (eng)

## Strategy description:

In the previous Youtube lessons (if you missed them visit the youtube channel: New Horizon) we understood the concept of automatic trading and we understood how to generate a winning trading strategy in the long run. Now, we will try to merge these two aspects in order to create a robot that inserts the “market” operations in our place. To make automated trading strategies as profitable as possible, you need to eliminate discretion from the strategy. Elements such as "POC", resistances, supports and all large-scale patterns outperform only if they are used with manual trading strategies, precisely because they are not elements of objective interpretation. That is, any trader on these patterns will be able to take ideas and positions different.
There are several ways to build an automated trading system, and each trader uses a different one. This depends a lot on the characteristics of the analyst and his needs.
In our case we will use the Pro Real Time and Metatrader 5 platforms. Both platforms have their own programming language that can be easily explored within their official websites.
The strategy that we will mention can also be programmed through the Python language.
Ours is a strategy optimized for the stock market, mainly on “CAMTEK” and “TESLA” stocks. The time horizon used is two days. This means that the graph on which buy and sell signals will be obtained will have a two-day "time frame".
The strategy is from Momentum, that is, it evaluates the strength of the market in place. It is carried out considering a single indicator organized over three different time horizons.
The strategy is very simple and easy to interpret, this does not mean that it will be less profitable than other strategies, on the contrary the complexity of creating a strategy is precisely to make it as simple as possible. All of this will also make programming easier.
The strategy involves the use of the "Price Rate Of Change", ie the "ROC". The ROC is a momentum indicator and therefore indicates whether the prices of the last session are higher or lower than the chosen period, that is, compared to the prices of "x" sessions ago.
For example, if we consider the period equal to twenty candles, then the ROC will show us where the prices are today compared to the prices of twenty sessions ago. If the prices are higher than twenty sessions then the ROC will be positive. If the prices are lower than twenty sessions then the ROC will be negative. A "Price Rate Of Change" rising above the zero line indicates that prices are growing fast. A ROC, on the other hand, below the zero line leads us to believe that the price action is slowing down, that is, they are accelerating downwards.
A ROC that falls above the zero line means that prices are rising but slowing down, while a ROC that rises below the zero line implies that prices are slowing their descent.
The first phase is based on the development of the trading system. It starts from a theoretical concept and materializes in a mathematical language by identifying the set of rules that underlie our strategy.

The indicators used will be:
1) “Price Rate Of Change” with 20 periods, which gives us information on the short term trend
2) “Price Rate Of Change” with 50 periods, which gives us information on the medium-term trend
3) “Price Rate Of Change” with 100 periods, which gives us information about the long-term trend.

The period, in our case, is two days.
Basically the concept is based on going for bullish operations when the long-term and medium-term ROC indicate that there is an uptrend. The "market" entry signal is realized when the short-term ROC crosses the zero line upwards, this is because it means that there is a change in trend from bearish to bullish.
The exit from the market of the operation occurs when the short-term ROC crosses down the line set at minus five. This exit function will represent our "stop loss" or our "take profit", depending on whether the transaction will be positive or negative.

## Back Test

From Charles Dow's theory of trends, we now know that the more we decrease the observation time horizon, the more the margin of error on identifying the dominant trend will increase. It would therefore be counterproductive to waste time testing our trading program on shorter time intervals than the daily one. In this case we will use the two days as the time frame as seen in the figure.
First you need to download the application from the official “Pro real time” website. Once the screen is open, you need to implement the strategy on a chart you want to start from. Normally, momentum strategies, which indicate the strength of a trend, are used on the stock markets. Therefore, we will consider, in the backtest phase, the CAMTEK title.

![image](https://user-images.githubusercontent.com/105428493/192235039-3f2ca3b6-6982-4494-9ea3-207e7f3fc0c9.png)

Using the "add" item seen in the figure, we insert the three Momentum indicators: the Price Rate of Change

![image](https://user-images.githubusercontent.com/105428493/192235614-fd293b80-bcd9-4e9e-9f8d-20a48ddc1d3d.png)

From Charles Dow's theory of trends, we now know that the more we decrease the observation time horizon, the more the margin of error on identifying the dominant trend will increase. It would therefore be counterproductive to waste time testing our trading program on shorter time intervals than the daily one. In this case we will use the two days as the time frame as seen in the figure.

![image](https://user-images.githubusercontent.com/105428493/192236110-1d247d00-622a-4b3c-afd9-cf8e4d9535fd.png)

Now we just have to manually check the goodness of our strategy. The strategy profited twice out of three times. The blue arrows represent trades closed in profit, while the orange “xs” represent lost trades. (see figure) Since the strategy does not seem to have a high frequency, we will pass to the backtest automatically in order to evaluate its effectiveness, which seems apparently positive.

![image](https://user-images.githubusercontent.com/105428493/192236318-124bae92-bdd9-4c4e-a4b6-0d6defdfcca3.png)



# Informazioni utili(ita)

## Descrizione strategia:

Nelle lezioni su Youtube precedenti (se te le sei perse visita il canale youtube: New Horizon) abbiamo compreso il concetto di trading automatico ed abbiamo capito come generare una strategia di trading vincente sul lungo periodo. Ora, proveremo a fondere questi due aspetti al fine di creare un robot che inserisca le operazioni “a mercato” al posto nostro. Per rendere le strategie di trading automatico più profittevoli possibili bisogna eliminare la discrezionalità dalla strategia. Elementi  come "POC”, le resistenze, i supporti e tutti i pattern in grande scala sovraperformano solo se vengono utilizzati con strategie di trading manuali, proprio perché essi non sono elementi di oggettiva interpretazione. Cioè ogni trader su questi pattern potrà assumere idee e posizioni diverse.
Ci sono diversi modi per costruire un trading system automatizzato, ed ogni trader ne usa uno differente. Ciò dipende molto dalle caratteristiche dell’analista e dalle sue esigenze.
Nel nostro caso utilizzeremo le piattaforme Pro Real Time e Metatrader 5. Entrambe le piattaforme hanno un proprio linguaggio di programmazione che può essere facilmente approfondito all’interno dei loro siti web ufficiali. 
La strategia che menzioneremo potrà essere programmata anche attraverso il linguaggio Python.
La nostra è una strategia ottimizzata per il mercato azionario, principalmente sui titoli “CAMTEK” e “TESLA”. L’orizzonte temporale utilizzato è pari a due giorni. Ciò significa che il grafico sul quale si conseguiranno dei segnali di acquisto e vendita avrà un “time frame” bigiornaliero.
La strategia è di Momentum, cioè valuta la forza del mercato in essere. Essa è realizzata considerando un unico indicatore organizzato su tre diversi orizzonti temporali.
La strategia è molto semplice e di facile interpretazione , ciò non significa che sarà meno profittevole di altre strategie, anzi la complessità di quando si crea una strategia è proprio quella di renderla il più semplice possibile. Tutto questo agevolerà anche la programmazione.
La strategia prevede l’uso del “Price Rate Of Change”, cioè il “ROC”. Il ROC è un indicatore di momentum e quindi ci indica  se i prezzi dell’ ultima seduta sono superiori oppure inferiori rispetto al periodo scelto, cioè rispetto ad i prezzi di “x” sedute fa.
Se per esempio consideriamo il periodo uguale a venti candele, allora il ROC ci indicherà dove sono i prezzi oggi rispetto ad i prezzi di venti sedute fa. Se i prezzi risulteranno superiori alle venti sedute allora il ROC sarà positivo. Se i prezzi risulteranno inferiori alle venti sedute allora il ROC sarà negativo. Un “Price Rate Of Change”che cresce sopra la linea dello zero ci indica che i prezzi stanno crescendo velocemente. Un ROC, invece al di sotto della linea dello zero ci induce a credere che la price action sta rallentando, cioè stanno accellerando al ribasso.
Un ROC che scende sopra la linea dello zero vuol dire che i prezzi stanno salendo ma stanno rallentando, mentre invece, un ROC che sale sotto la linea dello zero implica che i prezzi stanno rallentando la loro discesa.
La prima fase si basa sullo sviluppo del trading system. Si parte da un concetto teorico e si materializza in un linguaggio matematico identificando il set delle regole che stanno alla base della nostra strategia.

Gli indicatori utilizzati saranno :
1) “Price Rate Of Change” con 20 periodi, che ci da informazioni sul trend di breve termine
2) “Price Rate Of Change” con 50 periodi, che ci da informazioni sul trend di medio termine
3) “Price Rate Of Change” con 100 periodi, che ci fornisce informazioni circa il trend di lungo termine.

Il periodo, nel nostro caso, vale due giorni.
Di base il concetto si basa sull’andare a fare operazioni rialziste quando il ROC di lungo termine e di medio termine indicano che c’è un trend rialzista. Il segnale di ingresso “a mercato” si realizza quando il ROC di breve termine incrocia la linea dello zero a rialzo, questo perché significa che c’è un cambiamento di trend da ribassista a rialzista.
L’uscita dal mercato dell’operazione si verifica quando il ROC di breve termine incrocia a ribasso la linea impostata a meno cinque. Tale funzione di uscita rappresenterà il nostro “stop loss” o il nostro “take profit”, a seconda se l’operazione sarà positiva o negativa.

## Back Test

Prima di avviare un codice di programmazione bisognerebbe verificare la validità della strategia manualmente, cosi da dedicarsi principalmente alla fase di backtest.
Nel capitolo precedente abbiamo utilizzato la piattaforma “Trading View”. Ora proveremo ad effettuare gli stessi ragionamenti sulla piattaforma Pro Real Time, che ci consentirà  attraverso il linguaggio “Pro Builder” di generare il nostro Expert Advisor e quindi il software di programmazione.
Per prima cosa bisogna scaricare l’applicazione dal sito web ufficiale “Pro real time”. Una volta aperta la schermata bisogna implementare la strategia su un grafico da cui si vuole partire. Normalmente, le strategie di momentum, che indicano la forza di un trend, vengono utilizzate sui mercati azionari. Pertanto, considereremo , in fase di backtest, il titolo CAMTEK. 

![image](https://user-images.githubusercontent.com/105428493/192235039-3f2ca3b6-6982-4494-9ea3-207e7f3fc0c9.png)

Attraverso la voce “aggiungi” vista in figura  inseriamo i tre indicatori di Momentum : i Price Rate of Change

![image](https://user-images.githubusercontent.com/105428493/192235614-fd293b80-bcd9-4e9e-9f8d-20a48ddc1d3d.png)

Dalla teoria di Charles Dow dei trend,  sappiamo ormai che più diminuiamo l’orizzonte temporale di osservazione più il margine di errore sull’individuazione del trend dominante aumenterà. Risulterebbe, quindi controproducente perdere tempo nel  testare il nostro programma di trading su intervalli di tempo minori di quello giornaliero. In questo caso utilizzeremo come time frame i due giorni come visto in figura.

![image](https://user-images.githubusercontent.com/105428493/192236110-1d247d00-622a-4b3c-afd9-cf8e4d9535fd.png)

Ora non ci resta che verificare manualmente la bontà della nostra strategia. La strategia è andata in profitto due volte su tre. Le frecce blu rappresentano le operazioni chiuse in profitto, mentre le “x” arancioni rappresentano i trade persi. (vedi figura) Dato che la strategia non sembra avere un elevata frequenza passeremo al backtest in forma automatica cosi da valutarne l’efficacia, che sembra apparentemente positiva.

![image](https://user-images.githubusercontent.com/105428493/192236318-124bae92-bdd9-4c4e-a4b6-0d6defdfcca3.png)

## Sviluppo codice e analisi risultati

Dopo aver ideato una strategia e dopo averla testata manualmente non resta che generare un trading system automatizzato. Ci sono diverse teorie su questa materia, in quanto vasta e molto affascinante. L’idea di poter far eseguire ad una macchina le proprie operazioni, annichilendo gli aspetti emotivi è qualcosa di altrettanto sorprendente. Per la creazione di un robot automatico c’è bisogno di avere dimestichezza con diversi linguaggi di programmazione. In questo capitolo tratteremo i linguaggi ProBuilder e Python. 

ProBuilder è un linguaggio di programmazione utilizzato sulla piattaforma ProRealTime. 
Questo è molto facile da usare ed è definito il linguaggio dei trader, infatti, ci consente di costruire svariate strategie di trading in poco tempo. Tutto ciò grazie al fatto che tutte le funzioni e gli indicatori di trading sono inglobati in esso. Ciò non è banale e semplifica molto il nostro approccio, tant’è che in poche righe di codice potremmo sviluppare strategie complesse ed efficaci. Questo approccio viene preferito da molti analisti in quanto con esso si riesce a preservare il miglior investimento : il tempo! 
ProBuilder è un linguaggio di programmazione che  consente l’utilizzo di numerosi comandi classici e più elaborati, specifici dell’analisi
tecnica, che ci daranno la possibilità di programmare indicatori e trading system dai più semplici ai più sofisticati.
Attraverso ProBuilder:
Le variabili possono anche non essere dichiarate e definite
Il tipo di variabile può non essere definito
Minuscole e Maiuscole hanno lo stesso significato
Viene usato un segno uguale per l’uguaglianza e l’attribuzione matematica

Per costruire un robot automatico bisognerebbe quantomeno avere dimestichezza con le funzioni base del trading. Di seguito vengono elencate tutte quelle funzioni e tutti quei comandi  che stanno alla base di un trading program di successo e che ci serviranno per generare il nostro codice attraverso ProBuilder .
Open : funzione che ci indica il valore di apertura della barra 
Close: funzione che ci indica il valore di chiusura della barra 
High: valore massimo di periodo
Low: valore minimo di periodo
Volume: Numero di contrattazioni scambiati in quel periodo
Buy: consente di entrare a mercato in posizione di acquisto (long)
SELL consente di chiudere a mercato una posizione di acquisto 
SELLSHORT consente di entrare a mercato in posizione di vendita ( short)
EXITSHORT consente di chiudere a mercato una posizione di vendita

Ciò differenzia questo approccio rispetto ai più comuni. Infatti, queste funzioni non esistono in altri linguaggi di programmazione, pertanto probuilder risulta essere uno dei linguaggi preferiti dai trader.

![image](https://user-images.githubusercontent.com/105428493/192370871-21351b81-3a6d-4aee-8d62-f923f6b59662.png)

ProBuilder inoltre mette a disposizione tutti gli indicatori principali dell’analisi tecnica. Essi, possono essere utilizzati senza doverli andare a generare in maniera autonoma.
La sintassi degli indicatori è costituita da tre elementi fondamentali quali il nome della funzione, il periodo considerato ed il valore della barra. Essi vengono riportati su un apposito Expert Advisor in questa modalità:
Nome della Funzione [periodo] (valore della barra)

Una volta selezionato il nostro Expert Advisor, cioè il foglio di programmazione del trading program attraverso  "Inserisci Funzione" si ricerca un indicatore, e quindi una funzione ProBuilder. Essa avrà dei valori preimpostati
per il periodo e per il valore della barra. Se consideriamo la funzione media mobile avremo:
***Average[20](Close)***
I valori tra le parentesi possono essere cambiati.  Nel nostro caso Average[20](Close) significa media mobile è settata a 20 periodi e sul valore della chiusura della barra precedente . Come descritto è possibile cambiare il periodo(es: Average[50], Average[100], Average[200]. E’ altresi possibile
sostituire "Close" con "Open”.

 Questi strumenti di trading su ProBuilder consentono di costruire trading system personalizzati attraverso la programmazione. 


La schermata di generazione  di un  trading system é formata principalmente da due finestre:
1) La finestra di generazione per programmazione 
2) La finestra di Backtesting di un sistema di di trading. 







