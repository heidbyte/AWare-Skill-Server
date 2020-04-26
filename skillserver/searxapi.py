import urllib.request, json
import urllib.parse
import random

def callAPI(question,lang = "en"):
	searxs = ["https://searx.decatec.de/","https://searx.be/","https://searx.my.id/","https://search.snopyta.org/","https://searx.hlfh.space/"]
	engines = ["google","yahoo","duckduckgo","yandex"]
	question = urllib.parse.quote(question)
	try:
		with urllib.request.urlopen("http://127.0.0.1:8888/search?q=:" + lang + "%20" + question + "&format=json&engines=" + random.choice(engines)) as url:
			datas = json.loads(url.read().decode())
			return datas["results"][0]["url"]
	except:
		with urllib.request.urlopen(random.choice(searxs) + "search?q=:" + lang + "%20" + question + "&format=json") as url:
			datas = json.loads(url.read().decode())
			try:
				return datas["results"][0]["url"]
			except:
				return "https://a-ware.io/wp-content/uploads/2020/02/LOGO.png"
