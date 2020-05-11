#import requirements
import urllib.request, json
from datetime import datetime
import urllib.parse
from utils.utils import getSlotbyName

lang = None


#beginn function, each skill needs to handle the datas
def beginn(data, intents):
	global lang
	location = None
	time = None
	datas = None
	answer = ""
	#load users data into json
	data = json.loads(data)
	#load nlu data into json
	intents = json.loads(intents)
	#get intention name
	intention = intents["intent"]["intentName"]
	slots = intents["slots"]
	lang = intents["lang"]
	apikey = data["owmapi"]
	answer_type = "answer"



	# extract time and location
	# TODO: replace with new global function from utils
	try:
		for x in slots:
			if x["slotName"] == "city":
				location = x["value"]["value"]

			if x["slotName"] == "datetime":
				time = x["value"]["value"]
				time = time.split(" ")[0]
			
			
	except Exception as e:
		print(e)
		# return false, so the server can try to use fallback skills to generate an answer
		return False

	# try to extract location and ask user if not given
	if(location == None):
		try:
			location = data["get_location"]
			intents["city"] = location
			answer_type = "answer_requested"
		except:
			return "Für welchen Ort möchtest du das Wetter wissen ?","https://a-ware.io/wp-content/uploads/2020/02/LOGO.png","get_location",True,intents


	location2 = location
	location = urllib.parse.quote(location)


	try:	

		# return actual weather
		if(time == None):
			with urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + apikey + "&units=metric&lang=" + lang) as url:
				datas = json.loads(url.read().decode())


			answer = generate_answer(datas["weather"][0]["description"],datas["main"]["temp"],location2)

			return answer,None,answer_type

		# return weather for specific time
		else:
			with urllib.request.urlopen("https://api.openweathermap.org/data/2.5/forecast?q=" + location + "&appid=" + apikey + "&units=metric&lang=" + lang) as url:
				datas = json.loads(url.read().decode())


			for x in datas["list"]:
				# get weather at 15 o clock
				if(x["dt_txt"].split(" ")[0] == time and x["dt_txt"].split(" ")[1] == "15:00:00"):
					answer = generate_answer(x["weather"][0]["description"],str(int(x["main"]["temp_min"])),location2)
					return answer,None,answer_type

		return False


	except Exception as e:
		print(e)
		return False


	#at least one return (no in, if or try) statement has to be not indented
	#this statement is not executed. Necessary for python interpreter tho.
	return str(intents)
