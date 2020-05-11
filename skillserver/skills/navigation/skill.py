#import requirements
import json
from utils.utils import getSlotbyName


#beginn function, each skill needs to handle the datas
def beginn(data, intents):
	global lang
	#load users data into json
	datas = json.loads(data)
	#load nlu data into json
	intents = json.loads(intents)
	lang = intents["lang"]
	intention = intents["intent"]["intentName"]
	target = getSlotbyName("target",intents)
	answer_type = "answer"

	# try to get target address
	if(target == None):
		try:
			target = datas["get_adress"]
			intents["target"] = hours
			answer_type = "answer_requested"
		except:
			pass



	if(intention == "search"):
		# ask user whats the target he meaned
		if(target == None):
			return "Welchen Ort meinen sie ?","https://a-ware.io/wp-content/uploads/2020/02/LOGO.png","get_adress",True,intents


	# return extracted data without statement
	return "    ","https://a-ware.io/wp-content/uploads/2020/02/LOGO.png",answer_type,False,intents
