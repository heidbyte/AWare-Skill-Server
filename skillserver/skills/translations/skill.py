#import requirements
import urllib.request, json
from datetime import datetime
import urllib.parse
from utils.utils import getSlotbyName
from app import translate

lang = None


#beginn function, each skill needs to handle the datas
def beginn(data, intents):
	global lang
	location = None
	time = None
	datas = None
	answer = ""
	#load users data into json
	data = json.loads(data)
	#load nlu data into json
	intents = json.loads(intents)
	answer_type = "answer"
	
	langucode = getSlotbyName("langucode", intents)
	if(langucode != None):
		langucode = str(langucode)
	sentence = getSlotbyName("sentence", intents)
	if(sentence != None):
		sentence = str(sentence)

	if(sentence == None):
		try:
			sentence = data["sentence"]
			intents["sentence"] = sentence
			answer_type = "answer_requested"
		except:
			return "Bitte wiederhole was du übersetzen möchtest","https://a-ware.io/wp-content/uploads/2020/02/LOGO.png","sentence",True,intents

	if(langucode == None):
		return "Ich kann die gewünschte Sprache leider noch nicht übersetzen, aber ich übe täglich um sie zu lernen.","https://a-ware.io/wp-content/uploads/2020/02/LOGO.png"


	return translate(sentence, target  = langucode),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png",answer_type,False
