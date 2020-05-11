#import requirements
import json
from fallback import wolfram_Alpha
from utils.utils import getSlotbyName


#beginn function, each skill needs to handle the datas
def beginn(data, intents):
	#load users data into json
	datas = json.loads(data)
	#load nlu data into json
	intents = json.loads(intents)
	# extract name
	name = getSlotbyName("name",intents)
	# if name was not found return False
	if(name == None):
		return False

	# generate question for wolframalpha
	question = "how old is " + name

	# ask wolframalpha
	answer = wolfram_Alpha(question,data)


	# return False if wolframalpha found no answer
	if(answer == False):
		return False
	else:
		return answer
