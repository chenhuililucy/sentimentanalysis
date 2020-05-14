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


#############################  MAIN  #########################################################################################


#You need to have several csv files that store words we are looking for in the dictionary 
#As with the termination of the second for loop, the csv file automatically closes, the first for loop would not run
#The only way to do this is to store the dictionary as several dictionaries each with 1 column

import re 
import glob
import os
import csv
import nltk 
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import RegexpTokenizer


DEBUG=True 
new=True

os.chdir("/Users/lucy/Desktop/assortedcodes/builddic") 

##########################################################################################################################################


#positive performance csv is output by combining amplifier with postperf and negperf with negator

posperdict={}
negperfdict={}


def combine2(): 
    posperflist=[]
    with open("postperf.csv","r") as posfile: 
        records=csv.reader(posfile)
        for row in records:
            posperf=row[0].lower()
            if len(posperf.split(" "))>1: 
                w1=posperf.split(" ")[0]
                w2=posperf.split(" ")[1]
            else: 
                w1=posperf
                w2=""
            with open("amplifier.csv","r") as ampfile: 
                records1=csv.reader(ampfile)
                for row in records1:
                    amplifier=row[0].lower()
                    posperdict.update({w1:{w2:amplifier}})
                    posperdict.update({amplifier:{w1:w2}})

    with open("negperf.csv","r") as negfile: 
        records=csv.reader(negfile)
        for row in records:
            negperf=row[0].lower()
            if len(negperf.split(" "))>1: 
                w1=negperf.split(" ")[0]
                w2=negperf.split(" ")[1]
            else: 
                w1=negperf
                w2=""
            with open("negator.csv","r") as negafile: 
                records1=csv.reader(negafile)
                for row in records1:
                    negator=row[0].lower()
                    posperdict.update({w1:{w2:negator}})
                    posperdict.update({negator:{w1:w2}})


    with open("negperf.csv","r") as negfile: 
        records=csv.reader(negfile)
        for row in records:
            negperf=row[0].lower()
            if len(negperf.split(" "))>1: 
                w1=negperf.split(" ")[0]
                w2=negperf.split(" ")[1]
            else: 
                w1=negperf
                w2=""
            with open("amplifier.csv","r") as ampfile: 
                records1=csv.reader(ampfile)
                for row in records1:
                    amplifier=row[0].lower()
                    negperfdict.update({w1:{w2:amplifier}})
                    negperfdict.update({amplifier:{w1:w2}})


    with open("postperf.csv","r") as posfile: 
        records=csv.reader(posfile)
        for row in records:
            posperf=row[0].lower()
            if len(posperf.split(" "))>1: 
                w1=posperf.split(" ")[0]
                w2=posperf.split(" ")[1]
            else: 
                w1=posperf
                w2=""
            with open("negator.csv","r") as negafile: 
                records1=csv.reader(negafile)
                for row in records1:
                    negator=row[0].lower()
                    negperfdict.update({negator:{w1:w2}})
                    negperfdict.update({w1:{w2:negator}})



##########################################################################################################################################


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



                   ###################

#Clean text

def preprocess(sentence):
    sentence=str(sentence)
    #sentence = sentence.lower()
    sentence=sentence.replace('{html}',"") 
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', sentence)
    rem_url=re.sub(r'http\S+', '',cleantext)
    rem_num = re.sub('[0-9]+', '', rem_url)
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(rem_num)  
    return " ".join(tokens)

                   ###################



direct="/Users/lucy/Desktop/assortedcodes/assortedcodes/examplesentences(1).txt"

# def writesentences(): 

#     if internal!=0 and positive!=0 and negative!=0 and external!=0: 
#         fsent.write("int, ext, pos, neg \n")
#     elif internal!=0 and positive!=0 and negative!=0: 
#         fsent.write("int, pos, neg \n")
#     elif internal!=0 and positive!=0 and external!=0: 
#         fsent.write("int, pos, ext \n")
#     elif external!=0 and positive!=0 and negative!=0: 
#         fsent.write("ext, pos, neg \n")
#     elif external!=0 and negative!=0 and external!=0: 
#         fsent.write("int, pos, neg \n")
#     elif internal!=0 and positive!=0 and external!=0: 
#         fsent.write("int, pos, ext \n")
#     elif internal!=0 and positive!=0: 
#         fsent.write("int, pos \n")
#     elif external!=0 and negative!=0: 
#         fsent.write("ext, neg \n")
#     elif internal!=0 and negative!=0: 
#         fsent.write("int, pos \n")
#     elif external!=0 and positive!=0: 
#         fsent.write("ext, pos \n")
#     fsent.write(sentences)


#write output sentence file




                   ###################
def searchwords(): 
    if new:
        combine()
        combine2()
    posperflist=[]
    


    ########

    #LOAD LM 

    with open("LMpositive.csv","r") as posfile: 
    #with open("posperflist.csv","r") as posfile: 
        poswords=csv.reader(posfile)
        for row in poswords: 
            singleposperword=row[0].lower()
            posperflist.append(singleposperword)
            #print(internalwordlist)

    posperflist=set(posperflist)
    #load in negative performance word list 

    negperflist=[]
    with open("LMnegative.csv","r") as negfile: 
    #with open("negaperflist.csv","r") as negfile
        negwords=csv.reader(negfile)
        for row in negwords: 
            singlenegperfword=row[0].lower()
            negperflist.append(singlenegperfword)
            #print(internalwordlist)
    negperflist=set(negperflist)

    ########

    from collections import defaultdict


    #def internal wordlist 

    internaldict=defaultdict(list)


    def merge(list1, list2): 
        merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))] 
        return merged_list 


    with open("int.csv","r",errors="ignore") as internalfile: 
        w1=[] 
        w2=[]

        internalwords=csv.reader(internalfile)
        for row in internalwords: 
            singleinternalword=row[0].lower()
            if len(singleinternalword.split(" "))>1: 
                w1.append(singleinternalword.split(" ")[0])
                w2.append(singleinternalword.split(" ")[1])
                #print(singleinternalword.split(" "))
                #for word1, word2 in singleinternalword.split(" "):
                #word1=singleinternalword.split(" ")[0]
                #word2=singleinternalword.split(" ")[1]
                #internaldict[word1].append(word2)
                #internaldict.update({word1:word2})
            else: 
                word1=singleinternalword
                internaldict.update({word1:""})
        
    for a, b in list(zip(w1, w2)):
        if a not in internaldict: 
            internaldict[a] = [b]
        else:
            if not isinstance(internaldict[a], str):
                internaldict[a].append(b)
        #internaldict.setdefault(a, []).append(b)

            #print(internalwordlist)
    

    #def external wordlist 

    externaldict=defaultdict(list)
    with open("ext.csv","r",errors="ignore") as externalfile: 
        w1=[]
        w2=[]
        externalwords=csv.reader(externalfile)
        for row in externalwords: 
            singleexternalwords=row[0].lower()
            if len(singleexternalwords.split(" "))>1: 

                w1.append(singleexternalwords.split(" ")[0])
                w2.append(singleexternalwords.split(" ")[1])
                #word1=singleexternalwords.split(" ")[0]
                #word2=singleexternalwords.split(" ")[1]
                #externaldict[word1].append(word2)
                #externaldict.update({word1:word2})
            else: 
                word1=singleexternalwords
                externaldict.update({word1:""})


    for a, b in list(zip(w1, w2)):
        if a not in externaldict: 
            externaldict[a] = [b]
        else:
            if not isinstance(externaldict[a], str):
                externaldict[a].append(b)
            #print(externalwordlist)


    sentlog_outputfields=['filename','sentno','posperf','negperf','internal','external']

    corpus="/Users/lucy/Desktop/others/newdictestn/newdic/*.txt"
    csv1="/Users/lucy/Desktop/assortedcodes/builddic/sentenceLM(1).csv"
    csv2="/Users/lucy/Desktop//assortedcodes/builddic/vector(2).csv"

    externalsent=[]
    internalsent=[]
    posperfsent=[]
    negperfsent=[]
    positiveperformancesent=[]
    negativeperformancesent=[]
    sentnolist=[]
    filename=[]


    filenum=1 #correct as filenum 

    f_out=open(csv1,"w")
    wr=csv.writer(f_out)
    wr.writerow(sentlog_outputfields)
    fsent=open(direct,"w")

    for files in glob.glob(corpus):
        with open(files) as f: 
            filenum=filenum+1 
            content = f.read()
            re.sub("\n","",content)
            sent = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s|[A-Z].*)',content)
            
            
            sentno=0
            for sentences in sent: # ISSUE: need to identify individual words, modify to match regex words
                #print(sentences)
                sentences=preprocess(sentences)
                endext=True 
                endint=True 
                endpos=True 
                endneg=True
                endposperf=True 
                endnegperf=True 
                sentno+=1
                #print(sentno)
                ww=word_tokenize(sentences)
                sentnolist.append(sentno)
                
                if sentno==1: 
                    filename.append(files)
                else: 
                    filename.append("none")


                                    ################################################################################
                                    ################################################################################
                

                if endposperf: 
                    endposperfstring=""
                    #print(posperdict)
                    for i in range(len(ww)-3): 
                        if ww[i].lower() in posperdict:
                            #print(ww[i])
                            #print("y")
                            if posperdict[ww[i]]!="": 
                                assert len(posperdict.get(ww[i]).keys())==1
                                #print(posperdict.get(ww[i]).keys())
                                #for e in posperdict.get(ww[i]).keys(): 
                                    #print(e)
                                    #print("1")
                                for e in posperdict.get(ww[i]).keys():
                                    if e==ww[i+1]: #dict.keys() returns an iterable object
                                        #print("y")
                                    #if posperdict[ww[i]].lower()==ww[i+1]: #match 3 rounds 
                                        y1=True 
                                        y2=True
                                        y3=True 
                                        if i+2>=len(ww): #then list index out of range 
                                            y1=False
                                        if i+3>=len(ww): 
                                            y2=False
                                        if i+4>=len(ww): 
                                            y3=False 
                                        
                                        if y1:

                                            """
                                            Alternative possible method: 
                                            posperdict.get(ww[i].lower(), {}).get(posperdict[ww[i]])

                                            """
                                            #print(posperdict.get(ww[i],{}).get(e))
                                            if posperdict.get(ww[i],{}).get(e)==ww[i+2]:
                                            #if posperdict[ww[i]][posperdict[ww[i]]]==ww[i+2]: 
                                                endposperfstring+=ww[i]+" "
                                                endposperfstring+=ww[i+1]+ " "
                                                endposperfstring+=ww[i+2]+ " "
                                                endposperf=False
                                                break
                                            elif posperdict.get(ww[i],{}).get(e)=="": 
                                                endposperfstring+=ww[i]+ " "
                                                endposperfstring+=ww[i+1]+ " "
                                                endposperf=False
                                                break
                                                
                                        if y2:
                                            if posperdict.get(ww[i],{}).get(e)==ww[i+3]:
                                            #if posperdict[ww[i]][posperdict[ww[i]]]==ww[i+3]: 
                                                endposperfstring+=ww[i]+ " "
                                                endposperfstring+=ww[i+1]+ " "
                                                endposperfstring+=ww[i+3]+ " "
                                                endposperf=False
                                                break
                                            elif posperdict.get(ww[i],{}).get(e)=="": 
                                                endposperfstring+=ww[i]+ " "
                                                endposperfstring+=ww[i+1]+ " "
                                                endposperf=False
                                                break
                                        if y3:
                                            if posperdict.get(ww[i],{}).get(e)==ww[i+4]:
                                                endposperfstring+=ww[i]+ " "
                                                endposperfstring+=ww[i+1]+ " "
                                                endposperfstring+=ww[i+4]+ " "
                                                endposperf=False
                                                break
                                            elif posperdict.get(ww[i],{}).get(e)=="": 
                                                endposperfstring+=ww[i]+ " "
                                                endposperfstring+=ww[i+1]+ " "
                                                endposperf=False
                                                break

                                    if e==ww[i+2]: #match 3 rounds 
                                        y1=True 
                                        y2=True
                                        y3=True 
                                        if i+3>=len(ww): #then list index out of range 
                                            y1=False
                                        if i+4>=len(ww): 
                                            y2=False
                                        if i+5>=len(ww): 
                                            y3=False 
                                        if y1:
                                            if posperdict.get(ww[i],{}).get(e)==ww[i+3]:        
                                                endposperfstring+=ww[i]+ " "
                                                endposperfstring+=ww[i+2]+ " "
                                                endposperfstring+=ww[i+3]+ " "
                                                endposperf=False
                                                break
                                            elif posperdict.get(ww[i],{}).get(e)=="": 
                                                endposperfstring+=ww[i]+ " "
                                                endposperfstring+=ww[i+2]+ " "
                                                endposperf=False
                                                break
                                                
                                        if y2:
                                            if posperdict.get(ww[i],{}).get(e)==ww[i+4]: 
                                                endposperfstring+=ww[i]+ " "
                                                endposperfstring+=ww[i+2]+ " "
                                                endposperfstring+=ww[i+4]+ " "
                                                endposperf=False
                                                break
                                            elif posperdict.get(ww[i],{}).get(e)=="": 
                                                endposperfstring+=ww[i]+ " "
                                                endposperfstring+=ww[i+2]+ " "
                                                endposperf=False
                                                break
                                        if y3:
                                            if posperdict.get(ww[i],{}).get(e)==ww[i+5]:
                                                endposperfstring+=ww[i]+ " "
                                                endposperfstring+=ww[i+2]+ " "
                                                endposperfstring+=ww[i+5]+ " "
                                                endposperf=False
                                                break
                                            elif posperdict.get(ww[i],{}).get(e)=="": 
                                                endposperfstring+=ww[i]+ " "
                                                endposperfstring+=ww[i+2]+ " "
                                                endposperf=False
                                                break

                                    if e==ww[i+3]: 
                                        y1=True 
                                        y2=True
                                        y3=True 
                                        if i+4>=len(ww): #then list index out of range 
                                            y1=False
                                        if i+5>=len(ww): 
                                            y2=False
                                        if i+6>=len(ww): 
                                            y3=False 

                                        if y1:
                                            if posperdict.get(ww[i],{}).get(e)==ww[i+4]:        
                                                endposperfstring+=ww[i]+ " "
                                                endposperfstring+=ww[i+3]+ " "
                                                endposperfstring+=ww[i+4]+ " "
                                                endposperf=False
                                                break
                                            elif posperdict.get(ww[i],{}).get(e)=="": 
                                                endposperfstring+=ww[i]+ " "
                                                endposperfstring+=ww[i+3]+ " "
                                                endposperf=False
                                                break


                                        if y2:
                                            if posperdict.get(ww[i],{}).get(e)==ww[i+5]: 
                                                endposperfstring+=ww[i]+ " "
                                                endposperfstring+=ww[i+3]+ " "
                                                endposperfstring+=ww[i+5]+ " "
                                                endposperf=False
                                                break
                                            elif posperdict.get(ww[i],{}).get(e)=="": 
                                                endposperfstring+=ww[i]+ " "
                                                endposperfstring+=ww[i+3]+ " "
                                                endposperf=False
                                                break

                                        if y3:
                                            if posperdict.get(ww[i],{}).get(e)==ww[i+6]:
                                                endposperfstring+=ww[i]+ " "
                                                endposperfstring+=ww[i+3]+ " "
                                                endposperfstring+=ww[i+6]+ " "
                                                endposperf=False
                                                break
                                            elif posperdict.get(ww[i],{}).get(e)=="": 
                                                endposperfstring+=ww[i]+ " "
                                                endposperfstring+=ww[i+3]+ " "
                                                endposperf=False
                                                break


                            else: #case where the second key does not exist
                                if posperdict.get(ww[i]).keys() is "": 
                                    print("get e")
                                    print(posperdict.get(ww[i])).get(e)
                                    if posperdict.get(ww[i],{}).get(e)==ww[i+1]: 
                                        endposperfstring+=ww[i]+ " "
                                        endposperfstring+=ww[i+1]+ " "
                                        endposperf=False 
                                    if posperdict.get(ww[i],{}).get(e)==ww[i+2]:
                                        endposperfstring+=ww[i]+ " "
                                        endposperfstring+=ww[i+2]+ " "
                                        endposperf=False
                                    if posperdict.get(ww[i],{}).get(e)==ww[i+3]: 
                                        endposperfstring+=ww[i]+ " "
                                        endposperfstring+=ww[i+3]+ " "
                                        endposperf=False

                if endposperf: 
                    positiveperformance=0
                    positiveperformancesent.append(positiveperformance)
                else: 
                    positiveperformance=1 
                    positiveperformancesent.append(positiveperformance)

                if endposperfstring is not "": 
                    print(endposperfstring)


############################################################################################################################################################################################################################

                if endnegperf: 
                    endnegperfstring=""
                    for i in range(len(ww)-3): 
                        if ww[i].lower() in negperfdict:
                            if negperfdict[ww[i]]!="": 
                                assert len(negperfdict.get(ww[i]).keys())==1
                                for e in negperfdict.get(ww[i]).keys():
                                    if e==ww[i+1]:  #dict.keys() returns an iterable object
                                    #if posperdict[ww[i]].lower()==ww[i+1]: #match 3 rounds 
                                        y1=True 
                                        y2=True
                                        y3=True 
                                        if i+2>=len(ww): #then list index out of range 
                                            y1=False
                                        if i+3>=len(ww): 
                                            y2=False
                                        if i+4>=len(ww): 
                                            y3=False 
                                        
                                        if y1:

                                            """
                                            Alternative possible method: 
                                            posperdict.get(ww[i].lower(), {}).get(posperdict[ww[i]])

                                            """
                                            if negperfdict.get(ww[i],{}).get(e)==ww[i+2]:
                                            #if posperdict[ww[i]][posperdict[ww[i]]]==ww[i+2]: 
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+1]
                                                endnegperfstring+=ww[i+2]
                                                endnegperf=False
                                                break
                                            elif posperdict.get(ww[i],{}).get(e)=="": 
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+1]
                                                endnegperf=False
                                                break
                                                
                                        if y2:
                                            if negperfdict.get(ww[i],{}).get(e)==ww[i+3]:
                                            #if posperdict[ww[i]][posperdict[ww[i]]]==ww[i+3]: 
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+1]
                                                endnegperfstring+=ww[i+3]
                                                endnegperf=False
                                                break
                                            elif negperfdict.get(ww[i],{}).get(e)=="": 
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+1]
                                                endnegperf=False
                                                break
                                        if y3:
                                            if negperfdict.get(ww[i],{}).get(e)==ww[i+4]:
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+1]
                                                endnegperfstring+=ww[i+4]
                                                endnegperf=False
                                                break
                                            elif negperfdict.get(ww[i],{}).get(e)=="": 
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+1]
                                                endnegperf=False
                                                break

                                    if negperfdict.get(ww[i]).keys()==ww[i+2]: #match 3 rounds 
                                        y1=True 
                                        y2=True
                                        y3=True 
                                        if i+3>=len(ww): #then list index out of range 
                                            y1=False
                                        if i+4>=len(ww): 
                                            y2=False
                                        if i+5>=len(ww): 
                                            y3=False 
                                        if y1:
                                            if negperfdict.get(ww[i],{}).get(e)==ww[i+3]:        
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+2]
                                                endnegperfstring+=ww[i+3]
                                                endnegperf=False
                                                break
                                            elif negperfdict.get(ww[i],{}).get(e)=="": 
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+2]
                                                endnegperf=False
                                                break
                                                
                                        if y2:
                                            if negperfdict.get(ww[i],{}).get(e)==ww[i+4]: 
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+2]
                                                endnegperfstring+=ww[i+4]
                                                endnegperf=False
                                                break
                                            elif negperfdict.get(ww[i],{}).get(e)=="": 
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+2]
                                                endnegperf=False
                                                break
                                        if y3:
                                            if negperfdict.get(ww[i],{}).get(e)==ww[i+5]:
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+2]
                                                endnegperfstring+=ww[i+5]
                                                endnegperf=False
                                                break
                                            elif negperfdict.get(ww[i],{}).get(e)=="": 
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+2]
                                                endnegperf=False
                                                break

                                    if posperdict.get(ww[i]).keys()==ww[i+3]: 
                                        y1=True 
                                        y2=True
                                        y3=True 
                                        if i+4>=len(ww): #then list index out of range 
                                            y1=False
                                        if i+5>=len(ww): 
                                            y2=False
                                        if i+6>=len(ww): 
                                            y3=False 

                                        if y1:
                                            if negperfdict.get(ww[i],{}).get(e)==ww[i+4]:        
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+3]
                                                endnegperfstring+=ww[i+4]
                                                endnegperf=False
                                                break
                                            elif negperfdict.get(ww[i],{}).get(e)=="": 
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+3]
                                                endnegperf=False
                                                break


                                        if y2:
                                            if negperfdict.get(ww[i],{}).get(e)==ww[i+5]: 
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+3]
                                                endnegperfstring+=ww[i+5]
                                                endnegperf=False
                                                break
                                            elif negperfdict.get(ww[i],{}).get(e)=="": 
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+3]
                                                endnegperf=False
                                                break

                                        if y3:
                                            if negperfdict.get(ww[i],{}).get(e)==ww[i+6]:
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+3]
                                                endnegperfstring+=ww[i+6]
                                                endnegperf=False
                                                break
                                            elif ponegperfdictsperdict.get(ww[i],{}).get(e)=="": 
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+3]
                                                endnegperf=False
                                                break


                                    else: #case where the second key does not exist
                                        if negperfdict.get(ww[i]).keys()=="": 
                                            if negperfdict.get(ww[i],{}).get(e)==ww[i+1]: 
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+1]
                                                endnegperf=False
                                            if negperfdict.get(ww[i],{}).get(e)==ww[i+2]:
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+2]
                                                endnegperf=False
                                            if negperfdict.get(ww[i],{}).get(e)==ww[i+3]: 
                                                endnegperfstring+=ww[i]
                                                endnegperfstring+=ww[i+3]
                                                endnegperf=False

                if endnegperf: 
                    negativeperformance=0
                    negativeperformancesent.append(negativeperformance)
                else: 
                    negativeperformance=1 
                    negativeperformancesent.append(negativeperformance)

                if endposperfstring is not "": 
                    print(endposperfstring)
                    


##################################################################################################################################################################################################################

                if endext: 
                    endextstring=""
                    for i in range(len(ww)-3): 
                        if ww[i].lower() in externaldict:
                            for el in externaldict[ww[i]]:
                                if el!="": 
                                    if el.lower()==ww[i+1]: 
                                        endextstring+=ww[i]+" "
                                        endextstring+=ww[i+1]+" "
                                        endext=False
                                    if el.lower()==ww[i+2]: 
                                        endextstring+=ww[i]+" "
                                        endextstring+=ww[i+2]+" "
                                        endext=False
                                    if el.lower()==ww[i+3]: 
                                        endextstring+=ww[i]+" "
                                        endextstring+=ww[i+3]+" "
                                        #print(internaldict[ww[i]])
                                        endext=False
                                else: 
                                    endextstring+=ww[i]
                                    endext=False


                """
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
                """ 
     
                if endext:      
                    external=0
                    externalsent.append(external)

                else: 
                    external=1
                    externalsent.append(external)
                
                #
                if endint: 
                    internalstring=""
                    for i in range(len(ww)-3): 
                        if ww[i].lower() in internaldict:
                            a=ww[i].lower()
                            for el in internaldict[ww[i]]:
                                if el!="": 
                                    if el.lower()==ww[i+1]: 
                                        internalstring+=ww[i]+" "
                                        internalstring+=ww[i+1]+" "
                                        endint=False
                                    if el.lower()==ww[i+2]: 
                                        internalstring+=ww[i]+" "
                                        internalstring+=ww[i+2]+" "
                                        endint=False
                                    if el.lower()==ww[i+3]: 
                                        internalstring+=ww[i]+" "
                                        internalstring+=ww[i+3]+" "
                                        #print(externaldict[ww[i]])
                                        endint=False
                                else: 
                                    internalstring+=ww[i]
                                    endint=False


                """
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
                """

                if endint:      
                    internal=0
                    internalsent.append(internal)

                else: 
                    internal=1
                    internalsent.append(internal)
            
                #
                if endpos: 
                    endposting=""
                    for item in ww: 
                        if item in posperflist: 
                            endposting+=item
                            endpos=False 
                
                    """
                    for item in posperflist :   
                        item=" "+item+" "
                        if item in sentences: 
                            #print(item)
                            endpos=False      
                    """    
                if endpos:      
                    positive=0
                    posperfsent.append(positive)

                else: 
                    positive=1
                    posperfsent.append(positive)
            
                #
                if endneg: 
                    endnegstring=""
                    for item in ww: 
                        if item in negextlist: 
                            endnegstring+=item
                            endneg=False 
                    """
                    for item in negperflist :  
                        item=" "+item+" " 
                        if item in sentences: 
                            #print(item)
                            endneg=False   

                    """

                if endneg:      
                    negative=0
                    negperfsent.append(negative)

                else: 
                    negative=1
                    negperfsent.append(negative)        
        
                # can definitely simplify this section: cuz senpai says so


                
                Y=True
                # Debug 14th of May
                fsent.write(files)
                sentno=int(sentno)
                fsent.write(str(sentno))
                if endnegperfstring is not "" and internal!=0:
                    
                    fsent.write("endnegperf, int \n")
                    fsent.write(internalstring+"\n")
                    fsent.write(endnegperfstring+"\n")
                    fsent.write("\n")
                    fsent.write(sentences + "\n"+ "\n")
                    
                elif endnegperfstring is not "": 
                    fsent.write("negperf \n")
                    fsent.write(endnegperfstring+"\n")
                    fsent.write(sentences + "\n"+ "\n")
                    Y=False 
                    
                if endnegperfstring is not "" and external!=0 : 
                    fsent.write("endnegperf, ext \n")
                    fsent.write(endextstring+"\n")
                    fsent.write(endnegperfstring+"\n")
                    fsent.write("\n")
                    fsent.write(sentences + "\n"+ "\n")
                elif endnegperfstring is not "": 
                    if Y:
                        fsent.write("negperf, int \n")
                        fsent.write("\n")
                        fsent.write(sentences + "\n"+ "\n")

                Z=True
                if endposperfstring is not "" and internal!=0 : 
                    fsent.write("endposperf, int \n")
                    fsent.write(internalstring+"\n")
                    fsent.write(endposperfstring+"\n")
                    fsent.write("\n")
                    fsent.write(sentences + "\n"+ "\n")

                elif endposperfstring is not "": 
                    fsent.write("endposperf \n")
                    fsent.write("\n")
                    fsent.write(endposperfstring+"\n")
                    fsent.write(sentences + "\n"+ "\n")
                    Z=False 
        
                if endposperfstring is not "" and external!=0 : 
                    fsent.write("endposperf, ext \n")
                    fsent.write(endextstring+"\n")
                    fsent.write(endposperfstring+"\n")
                    fsent.write("\n")
                    fsent.write(sentences + "\n"+ "\n")

                elif endposperfstring is not "": 
                    if Z:
                        fsent.write("endposperf \n")
                        fsent.write("\n")
                        fsent.write(endposperfstring+"\n")
                        fsent.write(sentences + "\n"+ "\n")

                if internal!=0 and positive!=0 and negative!=0 and external!=0: 
                    fsent.write("int, ext, pos, neg \n")
                    fsent.write(internalsent+"\n")
                    fsent.write("\n")
                    fsent.write(endposting+"\n")
                    fsent.write("\n")
                    fsent.write(endnegstring+"\n")
                    fsent.write("\n")
                    fsent.write(endextstring+"\n") 
                    fsent.write("\n")
                    fsent.write(sentences + "\n" + "\n")

                elif internal!=0 and positive!=0 and negative!=0: 
                    fsent.write("int, pos, neg \n" )
                    fsent.write(internalstring+ "\n")
                    fsent.write("\n")
                    fsent.write(endposting+ "\n")
                    fsent.write("\n")
                    fsent.write(endnegstring+ "\n")
                    fsent.write("\n")
                    fsent.write(sentences + "\n"+ "\n")

                elif internal!=0 and positive!=0 and external!=0: 
                    fsent.write("int, pos, ext \n")
                    fsent.write(internalstring+"\n")
                    fsent.write(endposting+"\n")
                    fsent.write(endextstring+"\n")
                    fsent.write(sentences + "\n" + "\n")
                elif external!=0 and positive!=0 and negative!=0: 
                    fsent.write("ext, pos, neg \n")
                    fsent.write(endnegstring+"\n")
                    fsent.write(endposting+"\n")
                    fsent.write(endextstring+"\n")
                    fsent.write(sentences + "\n"  + "\n")
                elif external!=0 and negative!=0 and internal!=0: 
                    fsent.write("int, pos, neg \n")
                    fsent.write(endnegstring+"\n")
                    fsent.write(internalstring+"\n")
                    fsent.write(endextstring+"\n")
                    fsent.write(sentences+ "\n"  + "\n")
                elif internal!=0 and positive!=0 and external!=0: 
                    fsent.write("int, pos, ext \n")
                    fsent.write(endposting+"\n")
                    fsent.write(internalstring+"\n")
                    fsent.write(endextstring+"\n")
                    fsent.write(sentences + "\n" + "\n")
                elif internal!=0 and positive!=0: 
                    fsent.write("int, pos \n")
                    fsent.write(endposting+"\n")
                    fsent.write(internalstring+"\n")
                    fsent.write(sentences + "\n" + "\n")
                elif external!=0 and negative!=0: 
                    fsent.write("ext, neg \n")
                    fsent.write(endposting+"\n")
                    fsent.write(endextstring+"\n")
                    fsent.write(sentences + "\n" + "\n")
                elif internal!=0 and negative!=0: 
                    fsent.write("int, pos \n" + "\n")
                    fsent.write(endnegstring+"\n")
                    fsent.write(internalstring+"\n")
                    fsent.write(sentences + "\n")
                elif external!=0 and positive!=0: 
                    fsent.write("ext, pos \n" + "\n")
                    fsent.write(endextstring+"\n")
                    fsent.write(endposting+"\n")
                    fsent.write(sentences + "\n")


            """
                if negative==1 and external==1: 
                    print(sentences)

            """ 


            if DEBUG:
                if filenum==1000:
                    break 
                        
            
    print(filename)  
    print(len(sentnolist))           
    print(len(posperflist))    
    print(len(internalsent))
    print(len(externalsent))
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
csv1="/Users/lucy/Desktop/assortedcodes/builddic/sentenceLM(1).csv"
csv2="/Users/lucy/Desktop/assortedcodes/builddic/vector(1).csv"

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