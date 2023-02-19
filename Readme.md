## webscraping from Tehran Stock Exchange website

* IN This program has been attempted to scrap NAV(Net asset Value) & final TXN(Transaction) of desired funds in real time form as it should be executed when 
the Tehran market is open and data of investment funds varies online .
* As we are facing a dynamic website , this code entails Selenium libs obviously.
* The final intention is to compile datas(NAV , final TXN) every 2 minutes from the given lists of funds and return them in a csv dataframe which has a column with exact time of scraping as well.
* columns' name:
namad : the name of investment fund
p     : final transaction value

* The web link for scraping : tsetmc.com/