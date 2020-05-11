#import requirements
import json
import random
from utils.utils import getSlotbyName



#beginn function, each skill needs to handle the datas
def beginn(data, intents):
	#load users data into json
	datas = json.loads(data)
	#load nlu data into json
	intents = json.loads(intents)
	intention = intents["intent"]["intentName"]
	answer_type = "answer"


	if(intention == "choice"):
		slots = ["0"]
		for xy in range(1):
			# get slots with ID's from zero to five
			for x in range(6):
				slot = getSlotbyName("slot" + str(x),intents)
				if(slot != None):
					slots.append(slot)

		# more than one slot could get extracted
		if(len(slots) > 1):
			choice = random.choice(slots)
			# choose random element untils it is not the first one
			while(choice == "0"):
				choice = random.choice(slots)

			return choice,"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png"
		else:
			return False

	if(intention == "randomint"):
		# extract range numbers
		num1 = getSlotbyName("number1",intents)
		num2 = getSlotbyName("number2",intents)

		# if first number is not given, set to zero
		if(num1 == None):
			num1 = 0

		# second number is not given, set to ten
		if(num2 == None):
			num2 = 10

		# check if first number is bigger than seconds
		if(num1 >= num2):
			return random.randint(num2,num1),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png",answer_type,False

		# check if first number is smaller than seconds
		if(num1 <= num2):
			return random.randint(num1,num2),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png",answer_type,False
		
		
	# return random number between one and six as it is a real dice
	if(intention == "diceroll"):
		return random.randint(1,6),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png",answer_type,False

	# return head or number as it is on coin
	if(intention == "coinflip"):
		return random.choice(["kopf","zahl","zahl","kopf"]),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png"

