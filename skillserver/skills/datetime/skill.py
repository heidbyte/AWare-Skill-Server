from datetime import date, datetime
import json

lang = None

def generate_answer(h,m,date):
	global lang
	h = str(h)
	m = str(m)
	date = str(date)
	answer = None
	if(lang == "de"):
		answer = "Es ist " + h + ":"  + m + " Uhr"


	if(answer == None):
		answer = "It is " + h + ":"  + m + " o'clock"
	return answer




def beginn(data, intents):
	global lang
	data = json.loads(data)
	intents = json.loads(intents)
	intention = intents["intent"]["intentName"]
	lang = intents["lang"]


	if(intention == "date"):
		h = int(datetime.now().strftime('%H'))
		m = int(datetime.now().strftime('%M'))
		answer = generate_answer(h,m,datetime.now().strftime('%d.%m.%Y'))
		return answer,"https://www.uhrzeit.org/weltzeit.php"
		


	return False
