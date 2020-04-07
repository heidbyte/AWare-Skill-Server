import json
from simpletransformers.classification import MultiLabelClassificationModel
import pandas as pd
import logging
from glob import glob

logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

myfile = open("de.keys","r")
keys = myfile.read().split("\n")
myfile.close()
numKeys = len(keys)-1

					
model = MultiLabelClassificationModel('albert', 'de_transformer', num_labels=numKeys, use_cuda = True, args={'reprocess_input_data': True, 'overwrite_output_dir': True, 'num_train_epochs': 1, "train_batch_size": 8,
  "eval_batch_size": 8})


while 1:
	quest = input("Phrase: ")
	predictions, raw_outputs = model.predict([quest])
	for x in range(numKeys):
		if(predictions[0][x] == 1):
			print(keys[x])
	
	print(predictions)


