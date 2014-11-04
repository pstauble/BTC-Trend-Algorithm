import requests
import time

localtime=time.strftime("%H:%M:%S")

def getlast():
	bitstamp=requests.get("https://www.bitstamp.net/api/ticker/")
	print "The price at " + localtime + " is " + bitstamp.json()["last"]+ " EUR"

def purchase():
	eurwallet=100
	btcwallet=0
	loopvar=0
	while loopvar < 5:
		lastprice=requests.get("https://www.bitstamp.net/api/ticker/")
		lastpricenum=float(lastprice.json()["last"])
		time.sleep(150)
		currentprice=requests.get("https://www.bitstamp.net/api/ticker/")
		currentpricenum=float(currentprice.json()["last"])
		print currentpricenum
		purchasebtc=eurwallet/currentpricenum
		
		if (currentpricenum/lastpricenum)-1 > 0.1:
			btcwallet=purchasebtc
			eurwallet=0
			print localtime+ " BUY: "+purchasebtc+ " BTC at "+currentpricenum+" EUR."
		elif(currentpricenum/lastpricenum)<0.93:
			eurwallet=btcwallet*currentpricenum
			btcwallet=0
			print localtime+ " SELL: "+btcwallet+ " BTC at "+currentpricenum+" EUR for "+eurwallet+" EUR."
		else:
			print "Loop run, no change."
		loopvar=loopvar + 1
		
purchase()