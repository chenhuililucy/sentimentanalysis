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
import time

from torch.utils.data import DataLoader
import math
from sentence_transformers import models, losses
from sentence_transformers import SentencesDataset, LoggingHandler, SentenceTransformer
from sentence_transformers.evaluation import EmbeddingSimilarityEvaluator
from sentence_transformers.readers import *
import logging
from datetime import datetime


import tqdm
import time




corpus="/Users/lucy/Desktop/assortedcodes/assortedcodes/newdictestn/newdic/*.txt"

a=1
total=80000
point = total / 100
increment = total / 20
percent=a/total

sentenceslist=[]



for files in glob.glob(corpus):


    with open(files,"r",encoding="utf-8", errors="ignore") as f: 




            
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

                    

#model = SentenceTransformer('bert-base-nli-mean-tokens')

#sentence_embeddings = model.encode(sentenceslist)

#p=zip(sentences, sentence_embeddings)

n=int((len(sentenceslist)+1)/2)
print(n)



word_embedding_model = models.BERT('bert-base-uncased') # model is not defined 

pooling_model = models.Pooling(word_embedding_model.get_word_embedding_dimension(),
                               pooling_mode_mean_tokens=True,
                               pooling_mode_cls_token=False,
                               pooling_mode_max_tokens=False)

model = SentenceTransformer(modules=[word_embedding_model, pooling_model])


train_dataloader = DataLoader(sentenceslist[:n], shuffle=True, batch_size=batch_size)
train_loss = losses.SoftmaxLoss(model=model, sentence_embedding_dimension=model.get_sentence_embedding_dimension(), num_labels=train_num_labels)

#will change
dev_data = SentencesDataset(examples=sentenceslist[:n], model=model)
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


train_dataloader = DataLoader(sentenceslist[n:], shuffle=True, batch_size=train_batch_size)
train_loss = losses.CosineSimilarityLoss(model=model)

#will change

dev_data = SentencesDataset(examples=sentenceslist[n:], model=model)
dev_dataloader = DataLoader(dev_data, shuffle=False, batch_size=train_batch_size)
evaluator = EmbeddingSimilarityEvaluator(dev_dataloader)

model.fit(train_objectives=[(train_dataloader, train_loss)],
          evaluator=evaluator,
          epochs=num_epochs,
          evaluation_steps=1000,
          warmup_steps=warmup_steps,
          output_path=model_save_path)