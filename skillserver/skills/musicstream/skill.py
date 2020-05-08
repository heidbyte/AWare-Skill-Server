#import requirements
import json
import urllib.request, json
import urllib.parse
from utils.utils import getSlotbyName

lang = None


# for this function you will need an selfhosted searx instance on the same machine
def geturl(song):
	song = urllib.parse.quote("!youtube " + song)
	with urllib.request.urlopen("http://localhost:8888/?category_videos=1&q=" + song + "&pageno=1&time_range=None&format=json") as url:
		datas = json.loads(url.read().decode())
		for url in range(10):
			if("youtube.com" in datas["results"][url]["url"]):
				return datas["results"][url]["url"]
	
	return None


def generate_answer():
	global lang
	answer = None
	if(lang == "de"):
		answer = "Hier ist die Musik"


	if(answer == None):
		answer = "Here is the music"

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
	
	song = ""

	artist = getSlotbyName("artist",intents)
	track = getSlotbyName("track",intents)

	if(artist):
		song += artist

	if(track):
		song += track

	if(artist == None and track == None):
		return False

	song = geturl(song)

	if(song == None):
		return False

	return generate_answer(),song
