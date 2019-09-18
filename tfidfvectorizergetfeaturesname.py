import re
import sys
import os
import nltk
import pandas as pd
import csv
import glob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.stem.snowball import SnowballStemmer



debug1 = False 
debug2 = False
debug3 = True

os.chdir("/Users/lucy/Desktop/newdictest1")

file=[]
corpus=[]

for files in glob.glob("/Users/lucy/Desktop/newdictest1/*.txt"):
#alternative: glob.glob(".txt/*"):
    with open(files) as f: 
      print(files)
        #files.encode('utf-8').strip()
      lineList = f.readlines()
      if debug1:
        print(lineList)
      lines=" ".join(lineList for lineList if not lineList.isdigit()) 
      if debug1:
        print(lines)
      corpus.append(lines)
      if debug2:
        print(corpus)


vectorizer = TfidfVectorizer(input=files,stop_words='english', ngram_range=(1,2),analyzer="word",min_df=1)

p=zip(vectorizer.get_feature_names())

with open('ngram=1(1).csv', 'w') as csvfile:
  fwriter = csv.writer(csvfile)
  for row in p:
    fwriter.writerow(row)