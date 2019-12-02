"""
Oct 19 2019
This piece of code fixes the search dictionary problem and I will append it to the search dictionary codes
"""


import re 
import glob
import os
import csv
import nltk 
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 


os.chdir("/Users/lucy/Desktop/builddic")


wordlist=[]
with open("ngram13edit2.csv", "r") as csvfile:
    words=csv.reader(csvfile)
    for row in words: 
        newword=" "+row[0]+" "
        wordlist.append(newword)

with open("ngram13edit2final.csv","w") as csvfile2: 
    words2=csv.writer(csvfile2)
    for element in wordlist: 
        words2.writerow([element])

    

