#This piece of code will output weights of documents in four categories:posint,negint,posext,negext
#For each time a sentence of the above type occurs, we count one. 

#You need to have several csv files that store words we are looking for in the dictionary 
#As with the termination of the second for loop, the csv file automatically closes, the first for loop would not run
#The only way to do this is to store the dictionary as several dictionaries each with 1 column
  

#key goal in this piece of code is to make stuff immutable 

import re 
import glob
import os
import csv
import nltk 
from nltk.tokenize import sent_tokenize, word_tokenize

DEBUG=True 


os.chdir("/Users/lucy/Desktop/builddic")


#load in positive performance word list

posperflist=[]
with open("postperf.csv","r") as posfile: 
    poswords=csv.reader(posfile)
    for row in poswords: 
        singleposperword=row[0].lower()
        internalword=posperflist.append(singleposperword)
        #print(internalwordlist)

#load in negative performance word list 

negperflist=[]
with open("negperf.csv","r") as negfile: 
    negwords=csv.reader(negfile)
    for row in negwords: 
        singlenegperfword=row[0].lower()
        internalword=negperflist.append(singlenegperfword)
        #print(internalwordlist)


#def internal wordlist 

internalwordlist=[]
with open("int.csv","r") as internalfile: 
    internalwords=csv.reader(internalfile)
    for row in internalwords: 
        singleinternalword=row[0].lower()
        internalword=internalwordlist.append(singleinternalword)
        #print(internalwordlist)


#def external wordlist 

externalwordlist=[]
with open("ext.csv","r") as externalfile: 
    externalwords=csv.reader(externalfile)
    for row in externalwords: 
        singleexternalwords=row[0].lower()
        externalwordlist.append(singleexternalwords)
        #print(externalwordlist)



sentlog_outputfields=['filename','sentno','posperf','negperf','internal','external']

corpus="/Users/lucy/Desktop/assortedcodes/assortedcodes/newdictestn/newdic/*.txt"
csv1="/Users/lucy/Desktop/builddic/sentence.csv"
csv2="/Users/lucy/Desktop/builddic/vector.csv"

externalsent=[]
internalsent=[]
posperfsent=[]
negperfsent=[]
sentnolist=[]
filename=[]


i=1

f_out=open(csv1,"w")
wr=csv.writer(f_out)
wr.writerow(sentlog_outputfields)
for files in glob.glob(corpus):
    #print(files)
    with open(files) as f: 

        i=i+1 
        #print(files)
        content = f.read()
        re.sub("\n","",content)
        


        #Modified sent tokenizer

        #sent=sent_tokenize(content)


        sent = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s|[A-Z].*)',content)
        
        #sent=pat.findall(content)

        #sent.re.sub("\n","")
        #print(sent)
        
        sentno=0
        for sentences in sent:
            print(sentences)
            sentno=sentno+1 
            print(sentno)
            for item in externalwordlist: 
                sentnolist.append(sentno)
                if sentno==1: 
                    filename.append(files)
                else: 
                    filename.append("none")
                if item in sentences: 
                    external=1
                else: 
                    external=0
                    #print(sentences)
                    #wr.writerow("a",newline='') _
                externalsent.append(external)
            for item in internalwordlist: 
                if item in sentences: 
                    internal=1 
                else: 
                    internal=0
                internalsent.append(internal)
            for item in posperflist:
                if item in sentences: 
                    posperf=1 
                else:
                    posperf=0 
                posperfsent.append(posperf)
            for item in negperflist:
                if item in sentences: 
                    negperf=1
                else:
                    negperf=0  
                negperfsent.append(negperf)
           
            
        if DEBUG:
            if i==2:
                break 
                    

p=zip(filename,sentnolist,posperfsent,negperfsent,internalsent,externalsent)
for row in p:
    print(row)
    wr.writerow(row)
