
"""

This piece of code, together with dicpart1.py, dicpart3.py are used to generate weights of documents in four categories: posint,negint,posext,negext

dicpart 2 will count if posperf,negperf,internal,external n-grams exist in every sentence of a file

###################################################################################################################
Data Dependencies:

posperflist.csv -------- csv with amplifier & negator adjusted positive performance ngrams 
negperflist.csv --------   csv with  amplifier & negator adjusted negative performance ngrams 
int.csv -------- csv with internal ngrams 
ext.csv -------- csv with external ngrams 


###################################################################################################################
Directory(User-specific directory to all scrubbed input MD&A files): 

Corpus where all MD&A filings are stored  

###################################################################################################################
Output file: sentence.csv 

# Want: for each sentence of of dictionary, write the no. of sentence in the doc 
# For each no. of sentence, output field write posperf,negperf,internal,external 


filename-------- write filename for every first sentence of the file, for the following sentences after the first, shows "none" 
sentnolist-------- outputs the no. of the sentence in the file 
posperfsent-------- outputs 1 or 0 depending on whether the sentence contains ngrams in posperflist.csv
negperfsent-------- outputs 1 or 0 depending on whether the sentence contains ngrams in negperflist.csv
internalsent-------- outputs 1 or 0 depending on whether the sentence contains ngrams in int.csv
externalsent-------- outputs 1 or 0 depending on whether the sentence contains ngrams in ext.csv



"""




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
with open("LMpositive.csv","r") as posfile: 
#with open("posperflist.csv","r") as posfile: 
    poswords=csv.reader(posfile)
    for row in poswords: 
        singleposperword=row[0].lower()
        internalword=posperflist.append(singleposperword)
        #print(internalwordlist)

#load in negative performance word list 

negperflist=[]
with open("LMnegative.csv","r") as negfile: 
#with open("negaperflist.csv","r") as negfile
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
csv1="/Users/lucy/Desktop/builddic/sentenceLM.csv"
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
    with open(files) as f: 
        i=i+1 
        content = f.read()
        re.sub("\n","",content)
        sent = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s|[A-Z].*)',content)
        sentno=0
        for sentences in sent: # ISSUE: need to identify individual words, modify to match regex words, DONNOT use the  
            print(sentences)
            endext=True 
            endint=True 
            endpos=True 
            endneg=True
            sentno=sentno+1 
            print(sentno)
            sentnolist.append(sentno)
            if sentno==1: 
                filename.append(files)
            else: 
                filename.append("none")

            if endext: 
                for item in externalwordlist :   
                    if item in sentences: 
                        print(item)
                        endext=False           
            if endext:      
                external=0
                externalsent.append(external)

            else: 
                external=1
                externalsent.append(external)
             
            #
            if endint: 
                for item in internalwordlist :   
                    if item in sentences: 
                        print(item)
                        endint=False           
            if endint:      
                internal=0
                internalsent.append(internal)

            else: 
                internal=1
                internalsent.append(internal)
        
            #
            if endpos: 
                for item in posperflist :   
                    if item in sentences: 
                        print(item)
                        endpos=False           
            if endpos:      
                positive=0
                posperfsent.append(positive)

            else: 
                positive=1
                posperfsent.append(positive)
        
            #
            if endneg: 
                for item in negperflist :   
                    if item in sentences: 
                        print(item)
                        endneg=False           
            if endneg:      
                negative=0
                negperfsent.append(negative)

            else: 
                negative=1
                negperfsent.append(negative)        
    
            
        if DEBUG:
            if i==2:
                break 
                    

p=zip(filename,sentnolist,posperfsent,negperfsent,internalsent,externalsent)
for row in p:
    print(row)
    wr.writerow(row)
