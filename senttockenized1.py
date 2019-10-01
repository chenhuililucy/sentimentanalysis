

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

#https://stackoverflow.com/questions/29423567/python-split-a-string-by-diffrent-full-stops

#".".join(file.split(".")[2:])

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
debug3 = False
#reload(sys)
#sys.setdefaultencoding("ISO-8859-1")

#a.encode('utf-8').strip()


os.chdir("/Users/lucy/Desktop/assortedcodes/assortedcodes/newdictestn/newdic")
#folder containing files you need to find context of words.

file=[]
corpus=[]

###############################################################################
#Debug .DSstore (alternative)
#for files in os.listdir("/Users/lucy/Desktop/newdic")
#if file.endswith(".txt"):
    #print(os.path.join("/mydir", file))
##############################################################################



i=1

for files in glob.glob("/Users/lucy/Desktop/assortedcodes/assortedcodes/newdictestn/newdic/*.txt"):
#copy and paste the directory of the folder containing files you need to find context of words and add /*.txt after it


#alternative: glob.glob(".txt/*"):
    with open('/Users/lucy/Desktop/assortedcodes/assortedcodes/newdictestn/newdic/externalwordlist.csv', newline='') as infile:
        with open('fail12.csv', 'w') as csvfile:
            records = csv.reader(infile)
            for r in records: 
                with open(files) as f: 
                    #lineList=f.split(".")

                    #r[0]=dictionary
        #print(files)
        #files.encode('utf-8').strip()
                    lineList = f.readlines()

                    for line in lineList:
                        #line=line1.split(".")
                        if r[1] in line:
                            print(line)
                            #for r
                            fwriter = csv.writer(csvfile)
                            #for row in line:
                            fwriter.writerow([''] * (i-1) + [line])
                            #fwriter.writerow([line])
                    i=i+1
                    #if debug1:
                        #if i==5: 
                           #csvfile.close()
                            #break


                        
#initially, I was opening each of the file individually and search for words in the dictionary, however, it might be more convenient to open each file and load words from the whole dictionary in