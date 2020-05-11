#import requirements
import json
from utils.utils import getSlotbyName

lang = None


def generate_answer(appnames):
	global lang
	answer = None
	# generate language specific answer
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
	lang = intents["lang"]

	# extract name to call
	appnames = getSlotbyName("name",intents)

	# return False if no name to call was found
	if(appnames == None):
		return False

	return generate_answer(appnames),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png"
