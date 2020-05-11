#import requirements
import json
from utils.utils import getSlotbyName
import urllib.request, json
import urllib.parse

lang = None


def generate_answer():
	global lang
	answer = None
	# generate language specific answer
	if(lang == "de"):
		answer = "Hier sind Bilder "


	if(answer == None):
		answer = "Here are images "

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

	# extract object to search images for
	things = getSlotbyName("things",intents)

	if(things == None):
		return generate_answer()

	# return link to qwant images
	return generate_answer(),"https://www.qwant.com/?q=" + urllib.parse.quote(things) + "&t=images"
