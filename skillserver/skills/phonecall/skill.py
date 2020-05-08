#import requirements
import json
from utils.utils import getSlotbyName

lang = None


def generate_answer(appnames):
	global lang
	answer = None
	if(lang == "de"):
		answer = "Ich versuche " + appnames + " anzurufen"


	if(answer == None):
		answer = "I try to call " + appnames

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
	
	song = ""

	appnames = getSlotbyName("name",intents)

	if(appnames == None):
		return False

	return generate_answer(appnames),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png"
