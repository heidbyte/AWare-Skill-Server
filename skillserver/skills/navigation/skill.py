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
	target = getSlotbyName("target",intents)
	answer_type = "answer"

	if(target == None):
		try:
			target = datas["get_adress"]
			intents["target"] = hours
			answer_type = "answer_requested"
		except:
			pass



	if(intention == "search"):
		if(target == None):
			return "Welchen Ort meinen sie ?","https://a-ware.io/wp-content/uploads/2020/02/LOGO.png","get_adress",True,intents


	return "    ","https://a-ware.io/wp-content/uploads/2020/02/LOGO.png",answer_type,False,intents
