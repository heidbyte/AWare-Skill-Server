#import requirements
import json
import io
import requests
import pandas as pd

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
	numbered = getSlotbyName("numbered",intents)
	president = getSlotbyName("president",intents)
	answer_type = "answer"
	answer = ""

	col_list = ["Number", "Name","Time"]
	url = "https://raw.githubusercontent.com/flozi00/AWare-Skill-Server/master/skillserver/data/uspresidents.csv"
	s = requests.get(url).content
	df = pd.read_csv(io.StringIO(s.decode('utf-8')), usecols=col_list)



	if(intention == "presnumber"):
		if(numbered == None):
			return False

		for index, row in df.iterrows():
			if(int(row["Number"]) == int(numbered)):
				answer = answer + row["Name"] + "\n"


	if(intention == "whichpres"):
		if(president == None):
			return False

		president = president.split(" ")
		for index, row in df.iterrows():
			contains = True
			for name in president:
				if(name.lower() in row["Name"].lower()):
					contains = True
				else:
					contains = False

			if(contains):
				answer = answer + row["Name"] + ": " + str(row["Number"]) + "\n"



	if(answer != "" and answer != None):
		return answer,"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png",answer_type,False
	else:
		return False
