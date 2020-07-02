


"""
Backtesting the performance dictionary 

"""


# ''' 

# The first part of this piece of code 


# ##########################################################################################################################################

               # Data Dependencies: 

                 #  CSV FILES #

# postperf.csv -------- csv with all positive performance ngrams 
# negperf.csv -------- csv with all negative performance ngrams  
# amplifier.csv  -------- csv with all amplifiers ngrams  
# negator.csv --------csv with all negators ngrams  
# bad.csv ------ csv with all words of which, when appended to performance words, result in a negative performance

                  #  CORPUS  #

# Corpus where all MD&A files are stored


# ##########################################################################################################################################


"""

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


            
# Libraries imported

import re 
import glob
import os
import csv
import nltk 
from collections import defaultdict
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import ngrams

###################### PLEASE MODIFY THE FOLLOWING DIRECTORIES#####################

######################        YOUR INPUT FILES            #####################

#Change your directory to one which contains all files
os.chdir("/Users/lucy/Desktop/assortedcodes/builddic")

#The corpus is the main folder that contains all your MD&A files 
corpus="/Users/lucy/Desktop/others/newdictestn/newdic/*.txt"
negator="/Users/lucy/Desktop/assortedcodes/builddic/negatorfinal.csv"
amplifier="/Users/lucy/Desktop/assortedcodes/builddic/amplifiedfinal.csv"
negative="/Users/lucy/Desktop/assortedcodes/builddic/negativeperf.csv"
positive="/Users/lucy/Desktop/assortedcodes/builddic/positiveperfcsv.csv"
bad="/Users/lucy/Desktop/assortedcodes/builddic/bad.csv"


######################        YOUR OUTPUT FILES            #####################

#csv1 outputs metrics per sentence
csv1="/Users/lucy/Desktop/assortedcodes/builddic/name1.csv"
#csv2 outputs metrics per document
csv2="/Users/lucy/Desktop//assortedcodes/builddic/name2.csv"
#Output file with all sentence matches
direct="/Users/lucy/Desktop/assortedcodes/assortedcodes/examplesentences0.txt"

#####################################################################################

posperdict=defaultdict(list)
negperfdict=defaultdict(list)
amplifierset=set()
negatorset=set()
badset=set()

o=[]
p=[]

DEBUG=True

def combine2(): 
    o=[]
    p=[]
    amplifier="/Users/lucy/Desktop/assortedcodes/builddic/amplifiedfinal.csv"
    negative="/Users/lucy/Desktop/assortedcodes/builddic/negativeperf.csv"
    positive="/Users/lucy/Desktop/assortedcodes/builddic/positiveperfcsv.csv"
    os.chdir("/Users/lucy/Desktop/assortedcodes/builddic")
    posperflist=[]
    with open(positive,"r") as posfile: 
        records=csv.reader(posfile)
        for row in records:
            posperf=row[0].lower()
            if len(posperf.split(" "))>1: 
                w1=posperf.split(" ")[0]
                w2=posperf.split(" ")[1]
            else: 
                w1=posperf
                w2="."
            
            posperdict[w1].append(w2)


    with open(negative,"r") as negfile: 
        records=csv.reader(negfile)
        for row in records:
            negperf=row[0].lower()
            if len(negperf.split(" "))>1: 
                w1=negperf.split(" ")[0]
                w2=negperf.split(" ")[1]
            else: 
                w1=negperf
                w2="."
            
            negperfdict[w1].append(w2)

    with open(bad,"r") as badf: 
        records1=csv.reader(badf)
        for row in records1:
            badf1=row[0].lower()
            badset.add(badf1)


    with open(amplifier,"r") as ampfile: 
        records1=csv.reader(ampfile)
        for row in records1:
            amplifier1=row[0].lower()
            amplifierset.add(amplifier1)
    
    with open(negator,"r") as negfile: 
        records1=csv.reader(negfile)
        for row in records1:
            negator1=row[0].lower()
            negatorset.add(negator1)
                



f1=[]


                   ###################
def searchwords(): 
    
    global sentlist
    combine2()
    posperflist=[]
    

    """
    def c(i,a,b,ww,d,cnt,BOOL): 
        if dict[ww[i+b]] is not None:
            if ww[i+a+b] in d[ww[i+b]]: 
                # print(ww[i:i+a+b+1])
                # print(ww[i])
                # print(ww[i+b])
                # print(ww[i+a+b])
                cnt+=sum([a,b])
                i=i+a+b 
                BOOL=False
                return cnt,BOOL,i
        return None 

    def b(i,a,b,ww,s,cnt,BOOL):
        if fww[i+a+b] in s:
            # print(ww[i:i+a+b+1]) 
            # print(ww[i])
            # print(ww[i+b])
            # print(ww[i+a+b])
            i=i+a+b 
            negperfcnt+=a+b
            BOOl=False
            return cnt, BOOL, i
        return None

    """


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


    #print(negperfdict)

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


    

    sentlog_outputfields=["filename","sentnolist","positiveperformancesent","negativeperformancesent","negneg","sentlen"]


    externalsent=[]
    internalsent=[]
    doublenegsent=[]
    posperfsent=[]
    negperfsent=[]
    positiveperformancesent=[]
    negativeperformancesent=[]
    sentnolist=[]
    filename=[]
    sentlist=[]
    sentlen=[]


    item="FILED AS OF DATE:"
    filenum=1 #correct as filenum 

    f_out=open(csv1,"w")
    wr=csv.writer(f_out)
    wr.writerow(sentlog_outputfields)
    fsent=open(direct,"w")

    for files in glob.glob(corpus):
        year=files[files.find("-")+1:files.find(".")]
        cik=files[:files.find("-")]
        with open(files) as f: 
            content = f.read()
            text1=content.lower()
            matchedstring=""
            for m in re.finditer(item.lower(), text1): 
                if not m: 
                    matchedstring="."
                    raise Error
                    #print(file)
                else:
                    substr1=text[m.start():m.start()+30]
                    #print(substr1)
                    # may be necessary to search for end string  
                    i=0
                    while i< len(substr1) and not substr1[i].isdigit(): 
                        i+=1
                    while i< len(substr1) and substr1[i].isdigit(): 
                        matchedstring+=substr1[i]
                        i+=1
                    break
            if matchedstring:
                f1.append(matchedstring.strip())

            totalnumberofsent=0
            filenum=filenum+1 
            
            re.sub("\n","",content)
            sent = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s|[A-Z].*)',content)
            posperfcnt=0 
            negperfcnt=0
            doubleneg=0
            
            sentno=0
            for sentences in sent: # ISSUE: need to identify individual words, modify to match regex words
                #print(sentences)
                
                sentno+=1
                fsent.write(files)
                fsent.write(str(sentno))
                fsent.write("\n")
                ww=[]
                for r in word_tokenize(sentences): 
                    if r.isalpha(): 
                        ww.append(r)
                #ww=[w in word_tokenize(sentences) if isalpha(w)]
                #ww=[w in ww if w.isalpha()]
                if len(ww)>=1:
                    #print(ww)
                    sentnolist.append(sentno)
                    if sentno==1: 
                        filename.append(files)
                    else: 
                        filename.append("none")
                    a=0
                    i=0
                    b=0

                    while i+a+b<len(ww):
                        BOOL=True
                        for b in range(1,3):
                            for a in range(1,3):
                                if BOOL:
                                    if ww[i].lower() in negatorset and i+a+b<len(ww) :
                                        if negperfdict.get(ww[i+b]):
                                        
                                            if ww[i+a+b] in negperfdict[ww[i+b]]: 
                                                fsent.write("doubleneg")
                                                fsent.write(str(ww[i:i+a+b+1]))
                                                #print(ww[i])
                                                #print(ww[i+b])
                                                #print(ww[i+a+b])
                                                doubleneg+=sum([a,b])
                                                i=i+a+b 
                                                BOOl=False
                                                break 

                                            elif "." in negperfdict[ww[i+b]] :
                                                fsent.write("doubleneg")
                                                fsent.write(str(ww[i:i+b+1]))                                               #print(ww[i:i+a+b+1])
                                                #print(ww[i])
                                                # print(ww[i+b])
                                                # print(ww[i+a+b])
                                                doubleneg+=b
                                                i=i+b
                                                BOOl=False
                                                break
                                          
                                        if posperdict.get(ww[i+b]):

                                            if ww[i+a+b] in posperdict[ww[i+b]]: 
                                                fsent.write("negative")
                                                fsent.write(str(ww[i:i+a+b+1]))                                               # print(ww[i:i+a+b+1])
                                                # print(ww[i])
                                                # print(ww[i+b)
                                                # print(ww[i+a+b])
                                                negperfcnt+=sum([a,b])
                                                i=i+a+b 
                                                BOOl=False
                                                break 

                                            elif "." in posperdict[ww[i+b]] :
                                                fsent.write("negative")
                                                fsent.write(str(ww[i:i+b+1]))
                                                #print(ww[i:i+a+b+1])
                                                #print(ww[i])
                                                # print(ww[i+b])
                                                # print(ww[i+a+b])
                                                negperfcnt+=b
                                                i=i+b
                                                BOOl=False
                                                break
                                            

                                    elif ww[i].lower() in amplifierset and i+a+b<len(ww): 
                                        if posperdict.get(ww[i+b]):

                                            if ww[i+a+b] in posperdict[ww[i+b]]: 
                                                # print(ww[i:i+a+b+1])
                                                # print(ww[i])
                                                # print(ww[i+b])
                                                # print(ww[i+a+b])   
                                                fsent.write("positive")                                                
                                                fsent.write(str(ww[i:i+a+b+1]))
                                                posperfcnt+=sum([a,b])
                                                i=i+a+b 
                                                BOOl=False
                                                break

                                            elif "." in posperdict[ww[i+b]]:
                                                fsent.write("positive")                                                
                                                fsent.write(str(ww[i:i+b+1]))
                                                posperfcnt+=b                                         
                                                i=i+b
                                                BOOl=False
                                                break
                                            
                                            
                                            # elif c(i,a,b,ww,negperfdict,negperfcnt,BOOL) is not None: 
                                            #     negperfcnt,BOOL,i=c(i,a,b,ww,negperfdict,negperfcnt,BOOL)
                                            #     break

                                        if negperfdict.get(ww[i+b]):  
                                            if ww[i+a+b] in negperfdict[ww[i+b]]: 
                                                # print(ww[i:i+a+b+1])
                                                # print(ww[i])
                                                # print(ww[i+b])
                                                # print(ww[i+a+b])
                                                fsent.write("negative")                                                
                                                fsent.write(str(ww[i:i+a+b+1]))                                            
                                                negperfcnt+=sum([a,b])
                                                i=i+a+b 
                                                BOOl=False
                                                break 

                                            elif "." in negperfdict[ww[i+b]]: 
                                                fsent.write("negative")                                                
                                                fsent.write(str(ww[i:i+b+1]))                                                
                                                negperfcnt+=b 
                                                i=i+b
                                                BOOL=False
                                                break
                                        
                                    elif ww[i].lower() in badset and i+a+b<len(ww): 
                                        if posperdict.get(ww[i+b]):
                                            # if c(i,a,b,ww,posperdict,posperfcnt,BOOL) is not None: 
                                            #     posperfcnt,BOOL,i=c(i,a,b,ww,posperdict,posperfcnt,BOOL)
                                            #     break

                                           
                                            #if negperfdict[ww[i+b]] is not None:
                                            if ww[i+a+b] in posperdict[ww[i+b]]: 
                                                    # print(ww[i:i+a+b+1])
                                                    # print(ww[i])
                                                    # print(ww[i+b])
                                                    # print(ww[i+a+b])    
                                                fsent.write("negative")                                                
                                                fsent.write(str(ww[i:i+b+a+1]))                                 
                                                negperfcnt+=sum([a,b])
                                                i=i+a+b 
                                                BOOl=False
                                                break

                                            elif "." in posperdict[ww[i+b]]:
                                                fsent.write("negative")                                                
                                                fsent.write(str(ww[i:i+b+1]))                                                    
                                                negperfcnt+=b                                         
                                                i=i+b
                                                BOOl=False
                                                break
                                            
                                            
                                            # elif c(i,a,b,ww,negperfdict,negperfcnt,BOOL) is not None: 
                                            #     negperfcnt,BOOL,i=c(i,a,b,ww,negperfdict,negperfcnt,BOOL)
                                            #     break

                                        if negperfdict.get(ww[i+b]):  
                                            if ww[i+a+b] in negperfdict[ww[i+b]]: 
                                                # print(ww[i:i+a+b+1])
                                                # print(ww[i])
                                                # print(ww[i+b])
                                                # print(ww[i+a+b])
                                                fsent.write("negative")                                                
                                                fsent.write(str(ww[i:i+b+1]))                                                 
                                                negperfcnt+=sum([a,b])
                                                i=i+a+b 
                                                BOOl=False
                                                break 

                                            elif "." in negperfdict[ww[i+b]]: 
                                                fsent.write("negative")                                                
                                                fsent.write(str(ww[i:i+b+1]))                                                
                                                negperfcnt+=b 
                                                i=i+b
                                                BOOL=False
                                                break
                                        
                    
                                            # else:
                                            #     #print(ww[i:i+b+a+1])   
                                            #     #print(ww[i])
                                            #     #print(ww[i+b])
                                            #     #print(ww[i+a+b])
                                            #     i=i+b+a
                                            #     BOOl=False
                                            #     break
                                            

                                    elif negperfdict.get(ww[i].lower()) and i+a+b<len(ww): 
                                        #print(i+b)
                                        #print(len(ww))
                                        # if b(i,a,b,ww,amplifierset,negperfcnt,BOOL) is not None: 
                                        #     negperfcnt,BOOL,i=b(i,a,b,ww,amplifierset,negperfcnt,BOOL)
                                        
                                        
                                        if ww[i+b] in negperfdict[ww[i].lower()]:
                                            #if negperfdict[ww[i+b]] is not None:
                                            if ww[i+a+b] in amplifierset: 
                                                # print(ww[i:i+a+b+1]) 
                                                # print(ww[i])
                                                # print(ww[i+b])
                                                # print(ww[i+a+b])
                                                fsent.write("negative")                                                
                                                fsent.write(str(ww[i:i+b+a+1]))  
                                                i=i+a+b 
                                                negperfcnt+=a+b
                                                BOOl=False
                                                break 
                                        
                                       
                                        # elif b(i,a,b,ww,negatorset,posperfcnt,BOOL) is not None:
                                        #     posperfcnt,BOOL,i=b(i,a,b,ww,negatorset,posperfcnt,BOOL)
                                        
                                            elif ww[i+a+b] in negatorset: 
                                                # print(ww[i:i+a+b+1]) 
                                                # print(ww[i])
                                                # print(ww[i+b])
                                                # print(ww[i+a+b])
                                                fsent.write("doubleneg")                                                
                                                fsent.write(str(ww[i:i+b+1]))      
                                                i=i+a+b 
                                                doubleneg+=a+b
                                                BOOl=False
                                                break 

                                            elif ww[i+a+b] in badset: 
                                                # print(ww[i:i+a+b+1]) 
                                                # print(ww[i])
                                                # print(ww[i+b])
                                                # print(ww[i+a+b])
                                                fsent.write("negative")                                                
                                                fsent.write(str(ww[i:i+a+b+1]))
                                                i=i+a+b 
                                                negperfcnt+=a+b
                                                BOOl=False
                                                break 
                                      

                                        #elif b(i,a,b,ww,negatorset,posperfcnt,BOOL):

                                        elif "." in negperfdict[ww[i].lower()]:
                                            if ww[i+b] in amplifierset:
                                                negperfcnt+=sum([b,a])
                                                # print(ww[i])
                                                # print(ww[i+b])
                                                # print(ww[i+a+b])
                                                # print(ww[i:i+b+a+1]) 
                                                fsent.write("negative")                                                
                                                fsent.write(str(ww[i:i+a+b+1]))                                             
                                                i=i+b+a
                                                BOOl=False
                                                break
                                            if ww[i+b] in negatorset:
                                                posperfcnt+=sum([b,a])
                                                # print(ww[i])
                                                # print(ww[i+b])
                                                # print(ww[i+a+b])
                                                # print(ww[i:i+b+a+1]) 
                                                fsent.write("positive")                                                
                                                fsent.write(str(ww[i:i+a+b+1]))                                                   
                                                i=i+b+a
                                                BOOl=False
                                                break
                                            if ww[i+b] in badset:
                                                posperfcnt+=sum([b,a])
                                                # print(ww[i])
                                                # print(ww[i+b])
                                                # print(ww[i+a+b])
                                                # print(ww[i:i+b+a+1]) 
                                                fsent.write("positive")                                                
                                                fsent.write(str(ww[i:i+a+b+1]))                                                 
                                                i=i+b+a
                                                BOOl=False
                                                break
                                            


                                    elif  posperdict.get(ww[i].lower()) and i+a+b<len(ww): 
                                        if ww[i+b] in posperdict[ww[i].lower()]:
                                            #if negperfdict[ww[i+b]] is not None:
                                            if ww[i+a+b] in amplifierset: 
                                                fsent.write("positive")                                                
                                                fsent.write(str(ww[i:i+a+b+1]))                                                
                                                #print(ww[i:i+a+b+1]) 
                                                i=i+a+b 
                                                posperfcnt+=a+b
                                                BOOl=False
                                                break 
                                            
                                            elif ww[i+a+b] in negatorset: 
                                                #print(ww[i:i+a+b+1]) 
                                                fsent.write("negative")                                                
                                                fsent.write(str(ww[i:i+a+b+1]))                                               
                                                i=i+a+b 
                                                negperfcnt+=a+b
                                                BOOl=False
                                                break 
                                            elif ww[i+a+b] in badset: 
                                                #print(ww[i:i+a+b+1]) 
                                                fsent.write("negative")                                                
                                                fsent.write(str(ww[i:i+a+b+1]))  
                                                i=i+a+b 
                                                negperfcnt+=a+b
                                                BOOl=False
                                                break 
                                            
                                        elif "." in negperfdict[ww[i].lower()]:
                                            if ww[i+b] in amplifierset:
                                                negperfcnt+=sum([a,b])
                                                fsent.write("negative")                                                
                                                fsent.write(str(ww[i:i+a+b+1]))                                             
                                                #print(ww[i:i+b+a+1]) 
                                                i=i+b+a
                                                BOOl=False
                                                break
                                            if ww[i+b] in negatorset:
                                                doubleneg+=sum([a,b])
                                                fsent.write("doubleneg")                                                
                                                fsent.write(str(ww[i:i+a+b+1]))                                                 
                                                #print(ww[i:i+b+a+1]) 
                                                i=i+b+a
                                                BOOl=False
                                                break
                                            if ww[i+b] in badset:
                                                fsent.write("negative")                                                
                                                fsent.write(str(ww[i:i+a+b+1]))                                                     
                                                negperfcnt+=sum([a,b])
                                                #print(ww[i:i+b+a+1]) 
                                                i=i+b+a
                                                BOOl=False
                                                break
                        i+=1
                
            
                    positiveperformancesent.append(posperfcnt)
                    negativeperformancesent.append(negperfcnt)
                    doublenegsent.append(doubleneg)
                    posperfcnt=0
                    negperfcnt=0
                    doubleneg=0
                    
                    sentlen.append(len(ww))

                else:
                    sentno-=1   

            if DEBUG:
                if filenum==10:
                    break 
                        
                        
   # print(filename)  
   # print(len(sentnolist))           
   # print(len(posperflist))    
   # print(len(sentlen))



    p=zip(filename,sentnolist,positiveperformancesent,negativeperformancesent,doublenegsent,sentlen)
    for row in p:
        #print(row)
        wr.writerow(row)
    print(len(f1))
    return f1




a=0 


poslist=[]
neglist=[]


filenamelist=[]
yearlist=[]
ciklist=[]
llist=[] 
doublenegall=[]

#print(len(f1))

def finalcount(f1):
    a=0 
    f1=searchwords()
    print(len(f1))
    f_out2 = open(csv2, 'w')
    wr2 = csv.writer(f_out2)
    pos=0
    neg=0
    l=0
    doubleneg=0

    with open(csv1,"r") as csvfile: 

        freader=csv.reader(csvfile)
        for row in freader:
            if "none" not in row[0] and "lucy" in row[0]: #matches a component in directory name, please change accordingly
                #print(row[0])
                everyfilename=row[0]
                #
                y=row[0][row[0].find("-")+1:row[0].find("-")+5]
                yearlist.append(y)
                st=""
                for e in row[0]: 
                    if e.isalpha() or e=="/": 
                        continue
                    elif e !="-": 
                        st+=e
                    elif e=="-": 
                        break

                cik=st
                ciklist.append(cik)

                #everyfilename=
                filenamelist.append(everyfilename)
                a=a+1
                
                if a > 1: #if more than one file has been loaded and the next line is the actual filename 
                    poslist.append(pos)
                    #print(posintlist)
                    neglist.append(neg)
                    llist.append(l)
                    doublenegall.append(doubleneg)

                pos=0
                neg=0
                l=0
                doubleneg=0


            if row[2].isdigit():
                pos+=int(row[2])
            if row[3].isdigit(): 
                neg+=int(row[3])
            if row[4].isdigit():
                doubleneg+=int(row[4])
            if row[5].isdigit():
                l+=int(row[5])
            """
            if "1" in row[2] and "1" in row[4]: 
                posint=posint+1
            if "1" in row[3] and "1" in row[4]: 
                negint=negint+1
            if "1" in row[2] and "1" in row[5]:
                posext=posext+1 
            if "1" in row[3] and "1" in row[5]:
                negext=negext+1

            """ 

            
    p=zip(filenamelist,yearlist,ciklist,poslist,neglist,doublenegall,llist) 
    wr2.writerow(["filename","year","cik","pos","neg","doublenegall","l","filedate"])
    for row in p:
        wr2.writerow(row)


finalcount(f1)