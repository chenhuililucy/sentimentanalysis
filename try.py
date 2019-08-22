import re
import sys
import os
import nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer


os.chdir("/Users/lucy/Desktop/down1")

file=[]

for files in os.listdir("/Users/lucy/Desktop/down1"):
    with open(files) as f: 
        lineList=f.readlines()
        lines=" ".join(lineList)
        lines=[lines]
    #data = [line.strip() for line in open(files).readlines()]
    #The TFIDF Vectorizer should expect an array of strings. So if you pass him an array of arrays of tokenz, it crashes.

#texts = [[word.lower() for word in text.split()] for text in data]
    vectorizer=CountVectorizer()
    #[texts]=yes
    word_count_vector=vectorizer.fit_transform(lines)
    #with open(os.path.join(root,files),"r") as auto:
    file.append(word_count_vector)
    #print(file)


print(vectorizer.vocabulary_)