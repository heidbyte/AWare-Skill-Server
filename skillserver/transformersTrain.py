import json
from simpletransformers.classification import MultiLabelClassificationModel
import pandas as pd
import logging
from glob import glob

import random
import string

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))



logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)


list = glob("*.definition.json")
for fl in list:
	print(fl)
	traindata = []
	numKeys = 0
	with open(fl,"r") as json_file:
		data = json.load(json_file)
		numKeys = len(data["intents"].keys())
		myfile = open(fl.split(".")[0] + ".keys","w+")
		for key in data["intents"].keys():
			myfile.write(key + "\n")
			for datas in data["intents"][key]["utterances"]:
				sentence = ""
				entlist = []
				for texts in datas["data"]:
					sentence = sentence + texts["text"]
					try:
						if("snips/" not in texts["entity"]):
							entlist.append(texts["entity"] + "*" + texts["text"])
					except:
						pass
				
				for entli in entlist:
					enti = entli.split("*")[0]
					repl = entli.split("*")[1]
					counting = 0
					for enti in data["entities"][enti]["data"]:
						counting = counting + 1
						if(counting % 1000 == 0 or counting <= 100):
							repl1 = enti["value"]
							keyList = []
							for label in data["intents"].keys():
								if(label == key):
									keyList.append(1)
								else:
									keyList.append(0)
							for rando in range(random.randint(1,5)):
								traindata.append([randomString(random.randint(1,10)) + " " + sentence.replace(repl,repl1) + " " + randomString(random.randint(1,10)),keyList])
						
						
						
						
						
	#print(traindata)
	myfile.close()
	train_df = pd.DataFrame(traindata, columns=['text', 'labels'])
	model = MultiLabelClassificationModel('albert', 'albert-base-v2', num_labels=numKeys, use_cuda = True, args={'reprocess_input_data': True, 'overwrite_output_dir': True, 'num_train_epochs': 15, "train_batch_size": 16,
  "eval_batch_size": 16})
	model.train_model(train_df, output_dir = fl.split(".")[0] + "_transformer")

	# Evaluate the model
	result, model_outputs, wrong_predictions = model.eval_model(eval_df)
	print(result)
	print(model_outputs)

