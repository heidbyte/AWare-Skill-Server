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
	hours = getSlotbyName("hours",intents)
	minutes = getSlotbyName("minutes",intents)
	seconds = getSlotbyName("seconds",intents)
	answer_type = "answer"

	if(hours == None):
		try:
			hours = datas["get_hours"]
			intents["hours"] = int(hours)
			answer_type = "answer_requested"
		except:
			pass
	if(minutes == None):
		try:
			minutes = datas["get_minutes"]
			intents["minutes"] = int(minutes)
			answer_type = "answer_requested"
		except:
			pass

	if(seconds == None):
		try:
			seconds = datas["get_seconds"]
			intents["seconds"] = int(seconds)
			answer_type = "answer_requested"
		except:
			pass



	if(intention == "alarm"):
		if(hours == None):
			return "Wieviel Stunden möchten sie Einstellen ?","https://a-ware.io/wp-content/uploads/2020/02/LOGO.png","get_hours",True,intents

		if(minutes == None):
			return "Wieviel Minuten möchten sie Einstellen ?","https://a-ware.io/wp-content/uploads/2020/02/LOGO.png","get_minutes",True,intents
	else:
		if(hours == None and hours == None and hours == None):
			return "Bitte sag mir die Zeit, die ich einstellen soll","https://a-ware.io/wp-content/uploads/2020/02/LOGO.png"


	return generate_answer(intention),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png",answer_type,True,intents
