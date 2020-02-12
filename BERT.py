
# attempt with BERT embeddings 

import re
import sys
import os
import nltk
import pandas as pd
import csv
import glob
from nltk import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.stem.snowball import SnowballStemmer
from sentence_transformers import SentenceTransformer
from sentence_transformers import SentenceTransformer, LoggingHandler
import numpy as np
import time

import tqdm
import time
import datetime

"""


#### Just some code to print debug information to stdout
np.set_printoptions(threshold=100)

logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO,
                    handlers=[LoggingHandler()])

"""



corpus="/Users/lucy/Desktop/assortedcodes/assortedcodes/newdictestn/newdic/*.txt"

a=1
total=80000
point = total / 100
increment = total / 20
percent=a/total

sentenceslist=[]
"""
def drawProgressBar(percent, barLen = 20):
    sys.stdout.write("\r")
    progress = ""
    for i in range(barLen):
        if i < int(barLen * percent):
            progress += "="
        else:
            progress += " "
    sys.stdout.write("[ %s ] %.2f%%" % (progress, percent * 100))
    sys.stdout.flush()

"""


for files in glob.glob(corpus):


    with open(files, "r",encoding="utf-8", errors="ignore") as f: 


            
        a+=1 
        content = f.read()
        re.sub("\n","",content)
        sent = sent_tokenize(content)
                #print(sentenceslist)
        for sentences1 in sent: 
            if sentences1 is not " ":
                sentenceslist.append(str(sentences1))
        if a%8783 == 0: 
            sys.stdout.write("\r[" + "=" * int(a/8783) + " "* int((87834-a)/8783) +"]") 
            print("\n"+"all-data-loaded"+datetime.datetime.now())
                


    """for i in range(total):
        if(i % (5 * point) == 0):
            sys.stdout.write("\r[" + "=" * (i / increment) +  " " * ((total - i)/ increment) + "]" +  str(i / point) + "%")
            sys.stdout.flush()
            """



model = SentenceTransformer('bert-base-nli-mean-tokens')

sentence_embeddings = model.encode(sentenceslist[:5000])

p=zip(sentenceslist[:5000], sentence_embeddings)

print("\n"+"all-data-processed"+datetime.datetime.now())

"""

word_embedding_model = models.BERT('bert-base-uncased')

pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension(),
                               pooling_mode_mean_tokens=True,
                               pooling_mode_cls_token=False,
                               pooling_mode_max_tokens=False)

model = SentenceTransformer(modules=[word_embedding_model, pooling_model])

nli_reader = NLIDataReader('datasets/AllNLI')

train_data = SentencesDataset(nli_reader.get_examples('train.gz'), model=model)
train_dataloader = DataLoader(train_data, shuffle=True, batch_size=batch_size)
train_loss = losses.SoftmaxLoss(model=model, sentence_embedding_dimension=model.get_sentence_embedding_dimension(), num_labels=train_num_labels)

sts_reader = STSDataReader('datasets/stsbenchmark')
dev_data = SentencesDataset(examples=sts_reader.get_examples('sts-dev.csv'), model=model)
dev_dataloader = DataLoader(dev_data, shuffle=False, batch_size=train_batch_size)
evaluator = EmbeddingSimilarityEvaluator(dev_dataloader)


model.fit(train_objectives=[(train_dataloader, train_loss)],
         evaluator=evaluator,
         epochs=num_epochs,
         evaluation_steps=1000,
         warmup_steps=warmup_steps,
         output_path=model_save_path
         )


model = SentenceTransformer('bert-base-nli-mean-tokens')

sts_reader = STSDataReader('datasets/stsbenchmark', normalize_scores=True)
train_data = SentencesDataset(sts_reader.get_examples('sts-train.csv'), model)
train_dataloader = DataLoader(train_data, shuffle=True, batch_size=train_batch_size)
train_loss = losses.CosineSimilarityLoss(model=model)

dev_data = SentencesDataset(examples=sts_reader.get_examples('sts-dev.csv'), model=model)
dev_dataloader = DataLoader(dev_data, shuffle=False, batch_size=train_batch_size)
evaluator = EmbeddingSimilarityEvaluator(dev_dataloader)

model.fit(train_objectives=[(train_dataloader, train_loss)],
          evaluator=evaluator,
          epochs=num_epochs,
          evaluation_steps=1000,
          warmup_steps=warmup_steps,
          output_path=model_save_path)

#start_time = time.time()
#main()
#print("--- %s seconds ---" % (time.time() - start_time))
"""