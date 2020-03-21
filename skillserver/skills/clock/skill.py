#import requirements
import json
from app import detect, translate
import urllib.request, json
import urllib.parse

lang = None

def getSlotbyName(slotname, datas):
	try:
		slots = datas["slots"]
		for x in slots:
			if x["slotName"] == slotname:
				return x["value"]["value"]

		return None

			
	except Exception as e:
		print(e)
		return None


def generate_answer(intent):
	global lang
	answer = None
	if(lang == "de"):
		if(intent == "alarm"):
			answer = "Wecker wird gesetzt"
		else:
			answer = "Countdown wird gestartet"

	if(answer == None):
		if(intent == "alarm"):
			answer = "Alarm set"
		else:
			answer = "Countdown started"

	return answer

#beginn function, each skill needs to handle the datas
def beginn(data, intents):
	global lang
	#load users data into json
	datas = json.loads(data)
	#load nlu data into json
	intents = json.loads(intents)
	question = intents["input"]
	lang = intents["lang"]
	intention = intents["intent"]["intentName"]

	if(intention == "alarm" and getSlotbyName("hours") == None):
		return False

	return generate_answer(intention),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png"
