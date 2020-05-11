#import requirements
import json
from fallback import wolfram_Alpha
from app import detect, translate

lang = None

def generate_answer(answered):
	global lang
	answered = str(answered)
	answer = None
	# generate specific answer for language
	if(lang == "de"):
		answer = "Die Antwort lautet: " + answered


	if(answer == None):
		answer = "The answer is: " + answered

	return answer

#beginn function, each skill needs to handle the datas
def beginn(data, intents):
	global lang
	#load users data into json
	datas = json.loads(data)
	#load nlu data into json
	intents = json.loads(intents)
	question = intents["input"]
	lang = intents["lang"]
	# translations to english if necessary, wolframalpha only understands english
	if(detect(question) != "en"):
		question = translate(question)


	# ask wolframalpha
	answer = wolfram_Alpha(question,data)

	# if wolframalpha fails, return False
	if(answer == False):
		return False
	else:
		return generate_answer(answer),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png"
