#import requirements
import urllib.request, json
from utils.utils import getSlotbyName


#beginn function, each skill needs to handle the datas
def beginn(data, intents):
	#load users data into json
	data = json.loads(data)
	apiKey = data["newsapi"]
	#load nlu data into json
	intents = json.loads(intents)
	#get intention name
	intention = intents["intent"]["intentName"]
	lang = intents["lang"]
	try:
		lang = data["country"]
	except:
		pass

	thema = getSlotbyName("thema",intents)


	# return all actuall news
	if(intention == "allnews"):
		with urllib.request.urlopen("https://newsapi.org/v2/top-headlines?country=" + str(lang) + "&apiKey=" + apiKey) as url:
			datas = json.loads(url.read().decode())
			articles = datas["articles"]
			answer = ""
			limit = 0
			for x in articles:
				# only return five articles
				if(limit < 5):
					answer += x["description"] + "\n\n"
					limit = limit + 1

			# if articles got added successful, return those
			if(answer != ""):
				return answer
			else:
				return False

	# return news for specific topic
	elif(thema != None):
		with urllib.request.urlopen("https://newsapi.org/v2/everything?q=" + str(thema) + "&language=" + str(lang) + "&apiKey=" + apiKey) as url:
			datas = json.loads(url.read().decode())
			articles = datas["articles"]
			answer = ""
			limit = 0
			for x in articles:
				# only return five articles
				if(limit < 5):
					answer += x["description"] + "\n\n"
					limit = limit + 1

			# if articles got added successful, return those
			if(answer != ""):
				return answer
			else:
				return False

	
	


	#at least one return (no in, if or try) statement has to be not indented
	#this statement is not executed. Necessary for python interpreter tho.
	return False
