#import requirements
import json

lang = None


def generate_answer(intent):
	global lang
	answer = None
	if(lang == "de"):
		if(intent == "parents"):
			answer = "Ich wurde von dem Aware Team erschaffen"

		if(intent == "creationtime"):
			answer = "Ich bin 2020 auf die Welt gekommen"

		if(intent == "mood"):
			answer = "Mir geht es gut. Danke der Nachfrage"
		
		if(intent == "do_something"):
			answer = "Ich suche nach Optimierungsmöglichkeiten in meinem Code"

		if(intent == "hobby"):
			answer = "Wenn ich nichts zu tun habe, dann schlafe ich für mein Leben gern"

		if(intent == "siblings"):
			answer = "Ich habe keine Geschwister"


	if(answer == None):
		if(intent == "parents"):
			answer = "I was created by the Aware Team"

		if(intent == "creationtime"):
			answer = "I saw the world first time in 2020"

		if(intent == "mood"):
			answer = "I am fine. Thank you for asking" 

		if(intent == "do_something"):
			answer = "I am looking for optimization possibilities in my code"

		if(intent == "hobby"):
			answer = "When I have nothing to do, I'll sleep all day long."

		if(intent == "siblings"):
			answer = "I do not have siblings"


	return answer

#beginn function, each skill needs to handle the datas
def beginn(data, intents):
	global lang
	#load users data into json
	datas = json.loads(data)
	#load nlu data into json
	intents = json.loads(intents)
	intention = intents["intent"]["intentName"]
	lang = intents["lang"]

	if(intention == None):
		return False
	
	return generate_answer(intention),"https://a-ware.io/wp-content/uploads/2020/02/LOGO.png"
	

	
