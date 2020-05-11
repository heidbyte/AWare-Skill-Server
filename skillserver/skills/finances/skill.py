#import requirements
import json
from utils.utils import getSlotbyName
import urllib.request, json
import urllib.parse

lang = None


#beginn function, each skill needs to handle the datas
def beginn(data, intents):
	global lang
	#load users data into json
	datas = json.loads(data)
	#load nlu data into json
	intents = json.loads(intents)
	question = intents["input"]
	lang = intents["lang"]

	answer = ""

	# extract name and quantity
	appnames = getSlotbyName("appnames",intents)
	quantity = getSlotbyName("quantity",intents)

	if(appnames == None):
		return False

	# remove last characters to solve bug with search, bitcoin's --> bitcoin
	appnames = appnames[:-2]

	try:
		# search for names
		with urllib.request.urlopen("https://financialmodelingprep.com/api/v3/search?query=" + urllib.parse.quote(appnames) + "&limit=5=") as url:
					datas = json.loads(url.read().decode())
					# get price for each name
					for x in datas:
						with urllib.request.urlopen("https://financialmodelingprep.com/api/v3/quote/" + x["symbol"]) as url2:
							datas2 = json.loads(url2.read().decode())
							prices = datas2[0]["price"]
							if(quantity != None):
								prices = prices * float(quantity)
							prices = str(prices)
							# format prices, for text to speech
							price1 = prices.split(".")[0]
							price2 = prices.split(".")[1]
							price2 = price2[0] + price2[1]
							prices = price1 + "." + price2
							# append to answer
							answer += x["name"] + ": " + prices + " $\n\n"

	except Exception as e:
		print(e)
		return False

	# return if correct answer is generated
	if(answer != ""):
		return answer
	else:
		return False
