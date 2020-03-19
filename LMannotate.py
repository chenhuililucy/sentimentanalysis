"""
19 March: 

Some categories of words in LM_annotate are highly relevant to determining whether a phrase is significant
in an internal/external sense. 

also want to get a list of word parts that are marked with the * symbol. 


"""

import collections

import csv 
import os 
import re 
import nltk
import pattern
from pattern.text.en import singularize
from pattern.text.en import pluralize
from pattern.en import pluralize, singularize
from pattern.en import conjugate, lemma, lexeme,PRESENT,SG
import random


labelled="/Users/lucy/Desktop/assortedcodes/sort/labelled18Marchsort.csv"
annotating="/Users/lucy/Desktop/assortedcodes/sort/final3.csv" 
LM="/Users/lucy/Desktop/assortedcodes/sort/LM_annotate.csv"

classifyingphraselist=[]
classifyingtfidf=[]
classifyingnum=[]
classifyingimportancerank=[]

with open(annotating,"r") as csvfile: 
    freader = csv.reader(csvfile)
    for row in freader: 
        classifyingphraselist.append(row[0])
        classifyingtfidf.append(row[1])
        classifyingnum.append(row[2])
        classifyingimportancerank.append(row[3])
    csvfile.close()

wordlist=[]
classfication=[]

with open(LM,"r") as csvfile: 
    freader = csv.reader(csvfile)
    for row in freader: 
        wordlist.append(row[0].lower())
        classfication.append(row[1])
    csvfile.close()

relevantlist=[]
with open(annotating,"r") as csvfile: 
    freader = csv.reader(csvfile)
    for row in freader: 
        if row[2]=="*": 
            if len(row[0].split(" "))==2: 
                ditch,keepphrase=row[0].split(" ")
                relevantlist.append(keepphrase)
            else:
                relevantlist.append(row[0])

                
    csvfile.close()

print("donewithreadingcsv")

st=set(relevantlist)
dictionary=dict(zip(wordlist,classfication))
sorteddict=collections.OrderedDict(sorted(dictionary.items()))

#st=wordlist
indexlist1=[]

for i in range(len(classifyingphraselist)):
    for elem in sorteddict.keys(): 
        if len(classifyingphraselist[i].split(" "))==2: 
            a, b = classifyingphraselist[i].split(" ") 
            if (a not in st) and (b not in st): 
                if a == elem or b == elem: 
                    classifyingnum[i]=classifyingnum[i]+(sorteddict.get(elem))
                    #indexlist1.append(classifyinglist.index(i))
        elif len(classifyingphraselist[i].split(" "))==1:
            if i not in st:
                if i==elem: 
                    classifyingnum[i]=classifyingnum[i]+(sorteddict.get(elem))
                    #indexlist1.append(classifyinglist.index(i))
        else: 
            print (len(classifyingphraselist[i].split(" ")))
            print(classifyingphraselist[i])

#indexlist1=[classifyingphraselist.index(i) for i in st if i in classifyingphraselist]

"""

outphraselist=[classifyingphraselist[i] for i in indexlist] 
outclassifyingtfidf=[classifyingtfidf[i] for i in indexlist]
outclassifyingimportancerank=[classifyingimportancerank[i] for i in indexlist] 
outclassifyingnum = [classifyingnum[i] for i in indexlist]

"""


#modify out classifying num 
#dictionary2=dict(zip(outphraselist,outclassifyingnum))


b=zip(classifyingphraselist,classifyingtfidf,classifyingnum,classifyingimportancerank)
with open("final4.csv","w") as csvfile: 
    fwriter = csv.writer(csvfile)
    for i in b: 
        fwriter.writerow([i])
    csvfile.close()
print("donewithfinal4")

################################################################################################################
################################################################################################################

