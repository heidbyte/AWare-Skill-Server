import json

def getSlotbyName(slotname, datas, datakey = "value"):
	try:
		slots = datas["slots"]
		for x in slots:
			if x["slotName"] == slotname:
				return x["value"][datakey]

		return None

			
	except Exception as e:
		print(e)
		return None
