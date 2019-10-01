
# -*- coding: utf-8 -*-

#use explode in excel to generate different columns of words 
#VLOOKUP() look up internal words in your dictionary 
#as3:/usr/local/lib/python2.7/site-packages# cat sitecustomize.py
# encoding=utf8  
#import sys  

#reload(sys)  
#sys.setdefaultencoding('utf8')
#The thing above destroys a bit of your codes in the the original nlp corpus. Don't use it!!! 

#https://stackoverflow.com/questions/34449127/sklearn-tfidf-transformer-how-to-get-tf-idf-values-of-given-words-in-document
#http://wordlist.aspell.net/12dicts-readme/#classic


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
#reload(sys)
#sys.setdefaultencoding("ISO-8859-1")

#a.encode('utf-8').strip()

os.chdir("/Users/lucy/Desktop/assortedcodes/assortedcodes/newdictestn/newdic")

file=[]
corpus=[]

###############################################################################
#Debug .DSstore (alternative)
#for files in os.listdir("/Users/lucy/Desktop/newdic")
#if file.endswith(".txt"):
    #print(os.path.join("/mydir", file))
##############################################################################

for files in glob.glob("/Users/lucy/Desktop/assortedcodes/assortedcodes/newdictestn/newdic/*.txt"):
#alternative: glob.glob(".txt/*"):
    with open(files) as f: 

      print(files)
        #files.encode('utf-8').strip()
      lineList = f.readlines()
      if debug1:
        print(lineList)
      lines1="".join(lineList) 
      lines = re.sub(r'\d', '', lines1)
      if debug1:
        print(lines)
      corpus.append(lines)
      if debug2:
        print(corpus)

        
      #lines=[lines] 

############################################

#I decided not to introduce the Stemmer at first 

      #stemmer = SnowballStemmer("english")
      #build_tokenizer(self)

      #def tockenizer_stemmer(lines): 
        #return[tockenizer_stemmer(word) for word in lines.split()]
        #print(tockenizer_stemmer(lines))

########################################################################################



vectorizer = TfidfVectorizer(input=files,stop_words='english', ngram_range=(1,2),analyzer="word",min_df=1)
#if debug: 
  #print(vectorizer)


######################################################################

    #irrelevant trying out stuff

    #[texts]=yes
    #with open(os.path.join(root,files),"r") as auto:
    #print(file)
    #vectorizer =  TfidfVectorizer('input='filename'')

    #I think the issue with tfidf.vectorizer here is that you are opening these files and appending the lines one by one, which is not
    #A viable solution; you should instead try to use vectorizer.fit.transform() on a file 
    

    #Calling fit_transform() on either vectorizer with our list of documents, [a,b], as the argument in each case, returns the same type of object – a 2x6 sparse matrix with 8 stored elements in Compressed Sparse Row format. The only difference is that the TfidfVectorizer() returns floats while the CountVectorizer() returns ints. And that’s to be expected – as explained in the documentation quoted above, TfidfVectorizer() assigns a score while CountVectorizer() counts.


    #file.append(lines)
    #file1= " ".join(file)
    #lines=[lines] 
########################################################################################

word_count_vector=vectorizer.fit_transform(corpus)
    #file.append(word_count_vector)
    #print(vectorizer.vocabulary_)

    #file2=[]
    #lines.append(file2)
    #list(file2)
tf_transformer = TfidfTransformer(use_idf=True).fit(word_count_vector)
X_train_tf = tf_transformer.transform(word_count_vector)

    #print(vectorizer.get_feature_names())

######################################################################
    #I have no idea as to what the thing below means
    #Is it the same as .toarray()?
      #idf=vectorizer._tfidf.idf_
########################################################################


#idf=X_train_tf.toarray()
idf=vectorizer._tfidf.idf_
if debug3: 
  print(vectorizer.get_feature_names(),idf)
    #print(idf)
p =zip(vectorizer.get_feature_names(),idf)
    # p.sort(key = lambda t: t[1])


with open('ngram=1or2version2.csv', 'w') as csvfile:
  fwriter = csv.writer(csvfile)
  for row in p:
    fwriter.writerow(row)


    ##  This piece of codes below was what I tried out but unsuccessfully 
    #writer = csv.writerow(p, delimiter=';', lineterminator='\n')


    #This piece of codes write out the words in the form of a .txt file, I dont know if this is of any use
#with open('daemons2.txt', 'w') as fp:
  #fp.write('\n'.join('%s %s' % x for x in p))

    #with open("tfidf.txt","w") as t:
      #for x in p:
        #t.print(x)
        #t.close()
      



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