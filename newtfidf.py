
import re
import sys
import os
import nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import locale 
import codecs
locale.getpreferredencoding(False)


os.chdir("/Users/lucy/Desktop/down1")

file=[]

for files in os.listdir("/Users/lucy/Desktop/down1"):
    with open(files) as f: 
        lineList = f. readlines()
        lines="".join(lineList) #joins list into text
    #data = [line.strip() for line in open(files).readlines()]
    #The TFIDF Vectorizer should expect an array of strings. So if you pass him an array of arrays of tokenz, it crashes.

#texts = [[word.lower() for word in text.split()] for text in data]
        lines=[lines] #convert intostring.
        os.chdir("/Users/lucy/Desktop/summer/datacollection")
        stopwords = [x.strip() for x in open('stopwords.txt','r').read().split('\n')]
        vectorizerCOUNT = CountVectorizer(stop_words='english')
        vectorizerTFIDF = TfidfVectorizer(stop_words='english',ngram_range=(1, 2),analyzer='char')
        os.chdir("/Users/lucy/Desktop/down1")
        #[texts]=yes
        word_count_vector=vectorizerCOUNT.fit_transform(lines)
        X = vectorizerTFIDF.fit_transform(lines)
        #with open(os.path.join(root,files),"r") as auto:
        file.append(word_count_vector)
        output= vectorizerTFIDF.get_feature_names()
        print(type(output))
        target= open(files, mode='w+')
        for line in output: 
            target.write(line)
            target.close()
            print(target)
    #print(file)




#In order to convert your str (aka unicode) object into bytes to be written to the file, 
# Python needs to encode it using some encoding. For some reason (either due to your system's default
#  encoding or because of some code you haven't pasted here), Python is using the ASCII encoding, which cannot handle some of the code points in your object.


#f=open("dictionary.csv","w+")
#f.write(str(vectorizer.vocabulary_))
#f.close()


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