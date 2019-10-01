

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



"""

#Design

#This portion of the code loops through all files in the corpus 
# and search for key words in our dictionary. 

############################################

# In csv one 
# Want: for each sentence of of dictionary, write the no. of sentence
# For each no. of sentence, output field write posperf,negperf,internal,external 

#Search for the required phrase in each sentence of the document. You need to sent-tockenize a string 


############################################

# In csv two 
# For each file output section posint, negint, posext, negext 
# Match solution in csv one to output regions in csv two 
# Sum the totals of posint-negint, posext-negext for each file



"""




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

f_out=open(csv1,"w")
wr=csv.writer(f_out)
wr.writerow(sentlog_outputfields)
for files in glob.glob(corpus):
    with open(files) as f: 
        #print(files)
        content = f.read()
        re.sub("\n","",content)
        sent=sent_tokenize(content)
        #sent.re.sub("\n","")
        #print(sent)
        i=1
        for sentences in sent:
            sentno=1
            for item in externalwordlist: 
                sentnolist.append(sentno)
                if sentno==1: 
                    filename.append(f)
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
           
                sentno=sentno+1
            i=i+1 
            if DEBUG:
                if i==2:
                    break 
                    

p=zip(filename,sentnolist,posperfsent,negperfsent,internalsent,externalsent)
for row in p:
    print(row)
    wr.writerow(row)


#######################################
#Write csv 2 


a=0 

posintlist=[]
negintlist=[]
posextlist=[]
negextlist=[]

filenamelist=[]

f_out2 = open(csv2, 'w')
wr2 = csv.writer(f_out2)

with open(csv1,"r"): 
    freader=csv.reader(csv1)
    for row in p: 
        if row[0] is not "none": 
            if DEBUG:
                if a==2:
                    break 

            a=a+1 
            if a != 1: 
                everyfilename=row[0]
                filenamelist.append(everyfilename)
                posintlist.append(posint)
                negintlist.append(negint)
                posextlist.append(posext)
                negextlist.append(negext)

            posint=0
            negint=0
            posext=0 
            negext=0 

            if row[2]==1 and row[4]==1: 
                posint=posint+1
            if row[3]==1 and row[4]==1: 
                negint=negint+1
            if row[2]==1 and row[5]==1: 
                posext=posext+1 
            if row[3]==1 and row[5]==1:
                negext=negext+1
        else:
            if row[2]==1 and row[4]==1: 
                posint=posint+1
            if row[3]==1 and row[4]==1: 
                negint=negint+1
            if row[2]==1 and row[5]==1: 
                posext=posext+1 
            if row[3]==1 and row[5]==1:
                negext=negext+1
            
        
p=zip(filenamelist,posintlist,negintlist,posextlist,negextlist) 
for row in p:
    wr2.writerow(row)

        






       

