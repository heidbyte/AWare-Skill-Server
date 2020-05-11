#import requirements
import json
from utils.utils import getSlotbyName

lang = None


def generate_answer(appnames):
	global lang
	answer = None
	# generate answer for specific language
	if(lang == "de"):
		answer = "Ich versuche " + appnames + " für dich zu öffnen"


	if(answer == None):
		answer = "I try to open " + appnames + " for you"

	return answer

#beginn function, each skill needs to handle the datas
def beginn(data, intents):
	global lang
	#load users data into json
	datas = json.loads(data)
	#load nlu data into json
	intents = json.loads(intents)
	# get language
	lang = intents["lang"]

	# get app name
	appnames = getSlotbyName("appnames",intents)

	# return False if appname could not get extracted
	if(appnames == None):
		return False

	return generate_answer(appnames),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png"
