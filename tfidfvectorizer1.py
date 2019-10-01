
# -*- coding: utf-8 -*-

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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

import sys
#reload(sys)
#sys.setdefaultencoding("ISO-8859-1")

#a.encode('utf-8').strip()

os.chdir("/Users/lucy/Desktop/dictionary")

file=[]

for files in os.listdir("/Users/lucy/Desktop/dictionary"):
    with open(files) as f: 
        #files.encode('utf-8').strip()
        lineList = f.readlines()
        lines=" ".join(lineList) 
    lines=[lines] 
    vectorizer = TfidfVectorizer(input='f',stop_words=None, ngram_range=(1,2),analyzer="word")
    #[texts]=yes
    #with open(os.path.join(root,files),"r") as auto:
    #print(file)
    

    #Calling fit_transform() on either vectorizer with our list of documents, [a,b], as the argument in each case, returns the same type of object – a 2x6 sparse matrix with 8 stored elements in Compressed Sparse Row format. The only difference is that the TfidfVectorizer() returns floats while the CountVectorizer() returns ints. And that’s to be expected – as explained in the documentation quoted above, TfidfVectorizer() assigns a score while CountVectorizer() counts.


    #file.append(lines)
    #file1= " ".join(file)
    word_count_vector=vectorizer.fit_transform(lines)
    file.append(word_count_vector)
    #print(vectorizer.vocabulary_)

    file2=[]

    from sklearn.feature_extraction.text import TfidfTransformer
    lines.append(file2)
    list(file2)
    tf_transformer = TfidfTransformer(use_idf=False).fit(word_count_vector)
    X_train_tf = tf_transformer.transform(word_count_vector)

    #print(vectorizer.get_feature_names())
    
    idf=vectorizer._tfidf.idf_
    #print(idf)
    p =zip(vectorizer.get_feature_names(),idf)
    # p.sort(key = lambda t: t[1])


    import csv

    with open('ngram=1or2version2.csv', 'w') as csvfile:
      fwriter = csv.writer(csvfile)
      for row in p:
          fwriter.writerow(row)


    ##  This piece of codes below was what I tried out but unsuccessfully 
    #writer = csv.writerow(p, delimiter=';', lineterminator='\n')


    #This piece of codes write out the words in the form of a .txt file, I dont know if this is of any use
    with open('daemons.txt', 'w') as fp:
      fp.write('\n'.join('%s %s' % x for x in p))

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