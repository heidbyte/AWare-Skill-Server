import urllib.request, json
import urllib.parse

def callAPI(question,lang = "en"):
	question = urllib.parse.quote(question)
	try:
		with urllib.request.urlopen("http://127.0.0.1:8888/search?q=:" + lang + "%20" + question + "&format=json") as url:
			datas = json.loads(url.read().decode())
			for url in range(10):
				if("youtube.com" in datas["results"][url]["url"] == False):
					return datas["results"][url]["url"]
	except:
		with urllib.request.urlopen("https://searx.decatec.de/search?q=:" + lang + "%20" + question + "&format=json") as url:
			datas = json.loads(url.read().decode())
			for url in range(10):
				if("youtube.com" in datas["results"][url]["url"] == False):
					return datas["results"][url]["url"]