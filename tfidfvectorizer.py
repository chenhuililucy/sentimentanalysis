

#as3:/usr/local/lib/python2.7/site-packages# cat sitecustomize.py
# encoding=utf8  
#import sys  

#reload(sys)  
#sys.setdefaultencoding('utf8')

import re
import sys
import os
import nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

import sys
#reload(sys)
#sys.setdefaultencoding("ISO-8859-1")

#a.encode('utf-8').strip()

os.chdir("/Users/lucy/Desktop/down2")

file=[]

for files in os.listdir("/Users/lucy/Desktop/down2"):
    with open(files) as f: 
        #files.encode('utf-8').strip()
        lineList = f.readlines()
        lines=b" ".join(lineList) 
    lines=[lines] 
    vectorizer = CountVectorizer(stop_words='english'，ngram_range=(1, 2))
    #[texts]=yes
    #with open(os.path.join(root,files),"r") as auto:
    #print(file)
    
    
    #file.append(lines)
    #file1= " ".join(file)
    word_count_vector=vectorizer.fit_transform(lines)
    lines.append(word_count_vector)



print(vectorizer.vocabulary_)
##
##
##
##for files in os.listdir():
##    for line in open(files).readlines():
##    with open(os.path.join(root,files),"r") as auto:
##        vectorizer = TfidfVectorizer()
##        word_count_vector=vectorizer.fit_transform(line)
##
##
##print(vectorizer.vocabulary)
##
##Error Iterable over raw text documents expected, string object received
##The solution to this problem is because input is just a String, but what is needed is a list (or an iterable) containing a single element (which is nothing but the String itself).

#Error Iterable over raw text documents expected, string object received
#The solution to this problem is because input is just a String, but what is needed is a list (or an iterable) containing a single element (which is nothing but the String itself).

##AttributeError: 'list' object has no attribute 'lower' gensim


  #data = [line.strip() for line in open(files).readlines()]
    #The TFIDF Vectorizer should expect an array of strings. So if you pass him an array of arrays of tokenz, it crashes.

#texts = [[word.lower() for word in text.split()] for text in data]