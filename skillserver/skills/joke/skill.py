#import requirements
import json
import random


def generate_answer(intent, url):
	answer = None
	jokesList = []	
	# return random joke from json file
	with open(url, 'r') as json_file:
		reader = json.load(json_file)
		for row in reader:
			jokesList.append(row["body"])
			
	answer = random.choice(jokesList)

	return answer

#beginn function, each skill needs to handle the datas
def beginn(data, intents):
	#load users data into json
	datas = json.loads(data)
	#load nlu data into json
	intents = json.loads(intents)
	intention = intents["intent"]["intentName"]
	lang = intents["lang"]
	# base path to jokes
	url = "skills//joke//jokes//"	
	
	# append language specific path
	if(lang == "de"):
		url += "de//"
		if(intention == "jokes_blonde"):
			url += "blonde_jokes.json"
		else:
			url += "funny_jokes.json"


	else:
		url += "en//"
		if(intention == "jokes_blonde"):
			url += "blonde_jokes.json"
		else:
			url += "funny_jokes.json"	

	
	return generate_answer(intention, url),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png"
	

	
