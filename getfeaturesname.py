#What this piece of codes does is that it extracts ngrams from a corpus of documents.
#The code called "tfidfvectorizer.py" that I used previously did not perform this function well for several reasons 

#1. Instead of returning values for all vectorizers features name it was mistakingly setting each file as the corpus 
#2. Due to the issue I described it was overwriting my csv file everytime the for loop loops over a new file 
#3. Even after I fixed the issues above by adding an empty list corpus and appending documents in the form of list to the empty list, the tfidf_weights functions uses up too much memory space
# As a result of 3. my anacondas crashes and it results in "killed 9" Error which is a memory error 
# To fix the memory error I instructed csv writer to only print features name 
# However, for some reason it printed features name list in a row and I had to transpose it excel to get the right version of it in columns 
# Printing in columns take up too much memory space in excel so excel stopped printing it after like 10,000 columns 
# I have no idea why this happened 
# Anyways, I decided to set tfidf weights as a dummy null variable and see if it still takes up too much memory space. 

# The tfidf memory space issue is solvable and someone found a solution here: https://stackoverflow.com/questions/25145552/tfidf-for-large-dataset
# I will try to resolve the issue 

###################################################################################################################

#Aside from this issue there is also the issue of random integers appearing in my n-grams 
# I want to get rid of these integers so I first tried to implement this in the comment sections below separated by long #######################################################################
# They did not work as I hoped and I don't know why. 




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
import itertools



debug1 = False 
debug2 = False
debug3 = True

os.chdir("/Users/lucy/Desktop/newdic")

file=[]
corpus=[]

for files in glob.glob("/Users/lucy/Desktop/newdic/*.txt"):
#alternative: glob.glob(".txt/*"):
    with open(files) as f: 
      print(files)
        #files.encode('utf-8').strip()
      lineList = f.readlines()
      if debug1:
        print(lineList)

#######################################################################
      #[x for x in lineList if not any(c.isdigit() for c in x)]
      #filter(re.compile('(?i)[a-z]').match, lineList)=linelist1
#######################################################################

      lines=" ".join(lineList) 
      if debug1:
        print(lines)
      corpus.append(lines)
      if debug2:
        print(corpus)

#######################################################################
      #lines=" ".join(linelist1) 
      #if debug1:
        #print(lines)
      #corpus.append(lines)
      #if debug2:
        #print(corpus)
  #######################################################################



vectorizer = TfidfVectorizer(input=files,stop_words='english', ngram_range=(1,1),analyzer="word",min_df=1)

word_count_vector=vectorizer.fit_transform(corpus)
idf=['null'] * 10000000
#######################################################################
#idf=[itertools.repeat('null')]
#######################################################################
#idf=vectorizer._tfidf.idf_


#######################################################################
#[x for x in vectorizer.get_feature_names() if not any(c.isdigit() for c in x)]=vectorizer1

#######################################################################


#print(vectorizer1)

#p=zip(vectorizer.get_feature_names())

#p=zip(vectorizer.get_feature_names())

p = zip(vectorizer.get_feature_names(), idf)
#p.sort(key = lambda t: t[1])


with open('ngram=1(0).csv', 'w') as csvfile:
  fwriter = csv.writer(csvfile)
  for x in p:
    fwriter.writerow(x)