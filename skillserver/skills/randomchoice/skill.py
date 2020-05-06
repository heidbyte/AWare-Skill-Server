#import requirements
import json
import random


lang = None

def getSlotbyName(slotname, datas, datakey = "value"):
	try:
		slots = datas["slots"]
		for x in slots:
			if x["slotName"] == slotname:
				return x["value"][datakey]

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
	answer_type = "answer"


	if(intention == "choice"):
		slots = ["0"]
		for xy in range(1):
			for x in range(6):
				slot = getSlotbyName("slot" + str(x),intents)
				if(slot != None):
					slots.append(slot)

		if(len(slots) > 1):
			choice = random.choice(slots)
			while(choice == "0"):
				choice = random.choice(slots)

			return choice,"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png"
		else:
			return False

	if(intention == "randomint"):
		num1 = getSlotbyName("number1",intents)
		num2 = getSlotbyName("number2",intents)

		if(num1 == None):
			num1 = 0

		if(num2 == None):
			num2 = 10

		if(num1 >= num2):
			return random.randint(num2,num1),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png",answer_type,False

		if(num1 <= num2):
			return random.randint(num1,num2),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png",answer_type,False
		
		

	if(intention == "diceroll"):
		return random.randint(1,6),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png",answer_type,False

	if(intention == "coinflip"):
		return random.choice(["kopf","zahl","zahl","kopf"]),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png"

