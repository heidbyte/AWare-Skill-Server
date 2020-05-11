#import requirements
import json
import io
import requests
import pandas as pd
from utils.utils import getSlotbyName

lang = None


#beginn function, each skill needs to handle the datas
def beginn(data, intents):
	global lang
	#load users data into json
	datas = json.loads(data)
	#load nlu data into json
	intents = json.loads(intents)
	lang = intents["lang"]
	intention = intents["intent"]["intentName"]
	numbered = getSlotbyName("numbered",intents)
	president = getSlotbyName("president",intents)
	answer_type = "answer"
	answer = ""

	# download and read data of american presidents
	col_list = ["Number", "Name","Time"]
	url = "https://raw.githubusercontent.com/flozi00/AWare-Skill-Server/master/skillserver/data/uspresidents.csv"
	s = requests.get(url).content
	df = pd.read_csv(io.StringIO(s.decode('utf-8')), usecols=col_list)


	# check if user want to search by number or name
	if(intention == "presnumber"):
		# if ordinal not found, try with number
		if(numbered == None):
			numbered = getSlotbyName("number",intents)

		# if no number found, return false
		if(numbered == None):
			return False

		# iterate over dataset to find the right entrie
		for index, row in df.iterrows():
			if(int(row["Number"]) == int(numbered)):
				answer = answer + row["Name"] + "\n"


	if(intention == "whichpres"):
		if(president == None):
			return False

		# split name into single names
		president = president.split(" ")
		for index, row in df.iterrows():
			contains = True
			# check if alle single names are in entrie
			for name in president:
				if(name.lower() in row["Name"].lower()):
					contains = True
				else:
					contains = False

			# add entrie to answer
			if(contains):
				answer = answer + row["Name"] + ": " + str(row["Number"]) + "\n"



	if(answer != "" and answer != None):
		"""answer = text you want to speak out,
		second is the url to load in browser,
		third is answer type ( you need to define if you want to have dialogs),
		fourth is boolean if you want to use translator before output or not (this case we dont need translator because only return name or number)"""
		return answer,"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png",answer_type,False
	else:
		# return false, cause no answer found by skill
		return False
