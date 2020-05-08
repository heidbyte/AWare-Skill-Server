#import requirements
import json
from utils.utils import getSlotbyName

lang = None


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
	time = getSlotbyName("time",intents)
	answer_type = "answer"

	print(time)


	if(intention == "alarm"):
		time = getSlotbyName("time",intents)
		if(time == None):
			return "Ich habe die Zeit leider nicht verstanden","https://a-ware.io/wp-content/uploads/2020/02/LOGO.png"

		time = time.split(" ")
		time = time[1]
		time = time.split(":")
		intents["hours"] = time[0]
		intents["minutes"] = time[1]
		intents["seconds"] = time[2]

	else:
		hours = getSlotbyName("time",intents, "hours")
		minutes = getSlotbyName("time",intents, "minutes")
		seconds = getSlotbyName("time",intents, "seconds")
		if(hours == None and minutes == None and seconds == None):
			return "Ich habe die Zeit leider nicht verstanden","https://a-ware.io/wp-content/uploads/2020/02/LOGO.png"

		if(hours == None):
			intents["hours"] = 0
		else:
			intents["hours"] = hours
		
		if(minutes == None):
			intents["minutes"] = 0
		else:
			intents["minutes"] = minutes

		if(seconds == None):
			intents["seconds"] = 0
		else:
			intents["seconds"] = seconds


	return generate_answer(intention),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png",answer_type,True,intents
