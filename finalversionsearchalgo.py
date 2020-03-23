''' 
This piece of code is used to generate weights of documents in four categories: posint,negint,posext,negext

The first part of this piece of code permutes amplifier and negator with positive & negative performance words and write output to csv file. 

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

import re 
import glob
import os
import csv
import nltk 
from nltk.tokenize import sent_tokenize, word_tokenize

DEBUG=True 


os.chdir("/Users/lucy/Desktop/assortedcodes/builddic") 



#positive performance csv is output by combining amplifier with postperf and negperf with negator

def combine(): 
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
    




"""

part 2 will count if posperf,negperf,internal,external n-grams exist in every sentence of a file

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


#load in positive performance word list

def searchwords(): 
    combine()
    posperflist=[]
    with open("LMpositive.csv","r") as posfile: 
    #with open("posperflist.csv","r") as posfile: 
        poswords=csv.reader(posfile)
        for row in poswords: 
            singleposperword=row[0].lower()
            internalword=posperflist.append(singleposperword)
            #print(internalwordlist)

    posperflist=set(posperflist)
    #load in negative performance word list 

    negperflist=[]
    with open("LMnegative.csv","r") as negfile: 
    #with open("negaperflist.csv","r") as negfile
        negwords=csv.reader(negfile)
        for row in negwords: 
            singlenegperfword=row[0].lower()
            internalword=negperflist.append(singlenegperfword)
            #print(internalwordlist)

    negperflist=set(negperflist)

    #def internal wordlist 

    internalwordlist=[]
    with open("int.csv","r") as internalfile: 
        internalwords=csv.reader(internalfile)
        for row in internalwords: 
            singleinternalword=row[0].lower()
            internalword=internalwordlist.append(singleinternalword)
            #print(internalwordlist)

    internalwordlist=set(internalwordlist)

    #def external wordlist 

    externalwordlist=[]
    with open("ext.csv","r") as externalfile: 
        externalwords=csv.reader(externalfile)
        for row in externalwords: 
            singleexternalwords=row[0].lower()
            externalwordlist.append(singleexternalwords)
            #print(externalwordlist)

    externalwordlist=set(externalwordlist)


    sentlog_outputfields=['filename','sentno','posperf','negperf','internal','external']

    corpus="/Users/lucy/Desktop/assortedcodes/assortedcodes/newdictestn/newdic/*.txt"
    csv1="/Users/lucy/Desktop/assortedcodes/builddic/sentenceLM.csv"
    csv2="/Users/lucy/Desktop//assortedcodes/builddic/vector.csv"

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
                #print(sentences)
                endext=True 
                endint=True 
                endpos=True 
                endneg=True
                sentno=sentno+1 
                #print(sentno)
                sentnolist.append(sentno)
                if sentno==1: 
                    filename.append(files)
                else: 
                    filename.append("none")

                if endext: 
                   
                    for item in externalwordlist :   
                        item=" "+item+" "
                        if len(item.strip().split(" "))>1: 
                            if item.split(" ")[0] in sentences: 
                                mini_string=sentences.find(item.split(" ")[0])+len(str(item.split(" ")))
                                stringend=mini_string+12 
                                if item.split(" ")[1] in sentences[mini_string:stringend]: 
                                    endext=False      
                                    #print(item)

                        else: 
                            if item in sentences: 
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
                        item=" "+item+" "
                        if len(item.strip().split(" "))>1: 
                            if item.split(" ")[0] in sentences: 
                                mini_string=sentences.find(item.split(" ")[0])+len(str(item.split(" ")))
                                stringend=mini_string+12 
                                if item.split(" ")[1] in sentences[mini_string:stringend]: 
                                    endint=False      


                        else: 
                            if item in sentences: 
                                #print(item)
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
                        item=" "+item+" "
                        if item in sentences: 
                            #print(item)
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
                        item=" "+item+" " 
                        if item in sentences: 
                            #print(item)
                            endneg=False           
                if endneg:      
                    negative=0
                    negperfsent.append(negative)

                else: 
                    negative=1
                    negperfsent.append(negative)        
        


            """
                if negative==1 and external==1: 
                    print(sentences)

            """ 

            if DEBUG:
                if i==3:
                    break 
                        
            

    p=zip(filename,sentnolist,posperfsent,negperfsent,internalsent,externalsent)
    for row in p:
        #print(row)
        wr.writerow(row)



'''

part 3 will take sentences.csv written by dicpart2 and add together the number of sentences in one file that are in the categories posint,negint,posext,negext

###################################################################################################################
Data Dependencies:

sentence.csv

###################################################################################################################

Output file: 

vector.csv 

Outputn fields: 

filename,posint,negint,posext,negext

'''


#This piece of code will output weights of documents in four categories:posint,negint,posext,negext
#For each time a sentence of the above type occurs, we count one. 




a=0 

corpus="/Users/lucy/Desktop/assortedcodes/assortedcodes/newdictestn/newdic/*.txt"
csv1="/Users/lucy/Desktop/assortedcodes/builddic/sentenceLM.csv"
csv2="/Users/lucy/Desktop/assortedcodes/builddic/vector.csv"

posintlist=[]
negintlist=[]
posextlist=[]
negextlist=[]

filenamelist=[]




def finalcount(): 
    global a 
    a=0 
    searchwords()
    f_out2 = open(csv2, 'w')
    wr2 = csv.writer(f_out2)

    with open(csv1,"r") as csvfile: 
        freader=csv.reader(csvfile)
        for row in freader:
            if "none" not in row[0] and "lucy" in row[0]: #matches a component in directory name, please change accordingly
                #print(row[0])
                everyfilename=row[0]
                filenamelist.append(everyfilename)
                a=a+1
                
                if a > 1: #if more than one file has been loaded and the next line is the actual filename 
                    posintlist.append(posint)
                    #print(posintlist)
                    negintlist.append(negint)
                    posextlist.append(posext)
                    negextlist.append(negext)
                posint=0
                negint=0
                posext=0 
                negext=0
                    
            if "1" in row[2] and "1" in row[4]: 
                posint=posint+1
            if "1" in row[3] and "1" in row[4]: 
                negint=negint+1
            if "1" in row[2] and "1" in row[5]:
                posext=posext+1 
            if "1" in row[3] and "1" in row[5]:
                negext=negext+1
        

    
            
    p=zip(filenamelist,posintlist,negintlist,posextlist,negextlist) 
    for row in p:
        wr2.writerow(row)

finalcount()