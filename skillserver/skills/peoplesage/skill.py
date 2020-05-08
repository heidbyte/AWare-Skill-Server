#import requirements
import json
from fallback import wolfram_Alpha
from utils.utils import getSlotbyName


#beginn function, each skill needs to handle the datas
def beginn(data, intents):
	global lang
	#load users data into json
	datas = json.loads(data)
	#load nlu data into json
	intents = json.loads(intents)
	name = getSlotbyName("name",intents)
	if(name == None):
		return False,False
	lang = intents["lang"]
	
	question = "how old is " + name

	answer = wolfram_Alpha(question,data)


	if(answer == False):
		return False
	else:
		return answer
