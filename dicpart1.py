''' 
This piece of code, together with dicpart2.py, dicpar3.py are used to generate weights of documents in four categories: posint,negint,posext,negext

dicpart1.py will permute amplifier and negator with positive & negative performance words and write output to csv file. 

##########################################################################################################################################

Data Dependencies: 

postperf.csv -------- csv with all positive performance ngrams 
negperf.csv -------- csv with all negative performance ngrams  
amplifier.csv  -------- csv with all amplifiers ngrams  
negator.csv --------csv with all negators ngrams  

##########################################################################################################################################
This program outputs: 

posperflist.csv -------- csv with amplifier & negator adjusted positive performance ngrams 
negperflist.csv --------   csv with  amplifier & negator adjusted negative performance ngrams 


'''




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



#positive performance csv is output by combining amplifier with postperf and negperf with negator

posperflist=[]

with open("postperf.csv","r") as posfile: 
    records=csv.reader(posfile)
    for row in records:
        posperf=row[0]
        with open("amplifier.csv","r") as ampfile: 
            records1=csv.reader(ampfile)
            for row in records1:
                amplifier=row[0].lower()
                new=posperf+" "+amplifier
                new2=amplifier+" "+posperf   
                posperflist.append(new)
                posperflist.append(new2)
                #print(posperflist)

with open("negperf.csv","r") as negfile: 
    records=csv.reader(negfile)
    for row in records:
        negperf=row[0].lower()
        with open("negator.csv","r") as negafile: 
            records1=csv.reader(negafile)
            for row in records1:
                negator=row[0].lower()
                new=negperf+" "+negator
                new2=negator+" "+negperf   
                posperflist.append(new)
                posperflist.append(new2)
                #print(posperflist)

with open("posperflist.csv","w") as posperffile: 
    filewriter0 = csv.writer(posperffile)
    for item in posperflist: 
        filewriter0.writerow([item])
       

negperflist=[]

with open("negperf.csv","r") as negfile: 
    records=csv.reader(negfile)
    for row in records:
        negperf=row[0].lower()
        with open("amplifier.csv","r") as ampfile: 
            records1=csv.reader(ampfile)
            for row in records1:
                amplifier=row[0].lower()
                new=negperf+" "+amplifier
                new2=amplifier+" "+negperf   
                negperflist.append(new)
                negperflist.append(new2)
                #print(posperflist)

with open("postperf.csv","r") as posfile: 
    records=csv.reader(posfile)
    for row in records:
        posperf=row[0].lower()
        with open("negator.csv","r") as negafile: 
            records1=csv.reader(negafile)
            for row in records1:
                negator=row[0].lower()
                new=posperf+" "+negator
                new2=negator+" "+posperf   
                negperflist.append(new)
                negperflist.append(new2)
                #print(posperflist)

with open("negperflist.csv","w") as negperffile: 
    filewriter1 = csv.writer(negperffile)
    for item in negperflist: 
        filewriter1.writerow([item])

#def internal wordlist 
