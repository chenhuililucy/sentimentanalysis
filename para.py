import operator 
import nltk
import ssl
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()


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
#nltk.download('punkt')

###################### PLEASE MODIFY THE FOLLOWING DIRECTORIES#####################

######################        YOUR INPUT FILES            #####################

#Change your directory to one which contains all files
#os.chdir("/Users/lucy/Desktop/assortedcodes/builddic")

#The corpus is the main folder that contains all your MD&A files 
corpus="/Users/lichenhuilucy/Desktop/newdic/*.txt"
negator="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/negatorfinal.csv"
amplifier="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/amplifiedfinal.csv"
negative="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/negativelemma.csv"
positive="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/positivelemma.csv"
bad="//Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/bad.csv"
good="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/good.csv"


######################        YOUR OUTPUT FILES            #####################

#csv1 outputs metrics per sentence
csv1="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/name1.csv"
#csv2 outputs metrics per document
csv2="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/name3.csv"
#Output file with all sentence matches
direct="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/examplesentences0.txt"

#####################################################################################

posperdict=defaultdict(list)
negperfdict=defaultdict(list)
amplifierset=set()
negatorset=set()
badset=set()
goodset=set()

o=[]
p=[]

DEBUG=False

posperflist=[]

with open("/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/LMpositive.csv","r") as posfile: 
#with open("posperflist.csv","r") as posfile: 
    poswords=csv.reader(posfile)
    for row in poswords: 
        singleposperword=row[0].lower()
        posperflist.append(singleposperword)
        #print(internalwordlist)

posperflist=set(posperflist)
#load in negative performance word list 

negperflist=[]
with open("/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/LMnegative.csv","r") as negfile: 
#with open("negaperflist.csv","r") as negfile
    negwords=csv.reader(negfile)
    for row in negwords: 
        singlenegperfword=row[0].lower()
        negperflist.append(singlenegperfword)
        #print(internalwordlist)
negperflist=set(negperflist)


def combine2(): 
    o=[]
    p=[]
    amplifier="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/amplifiedfinal.csv"
    negative="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/negativelemma.csv"
    positive="/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/positivelemma.csv"
    os.chdir("/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001")
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


    with open(good,"r") as goodf: 
        records1=csv.reader(goodf)
        for row in records1:
            goodf1=row[0].lower()
            goodset.add(goodf1)


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

    with open("/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/LMpositive.csv","r") as posfile: 
    #with open("posperflist.csv","r") as posfile: 
        poswords=csv.reader(posfile)
        for row in poswords: 
            singleposperword=row[0].lower()
            posperflist.append(singleposperword)
            #print(internalwordlist)

    posperflist=set(posperflist)
    #load in negative performance word list 

    negperflist=[]
    with open("/Users/lichenhuilucy/Desktop/drive-download-20201106T151715Z-001/LMnegative.csv","r") as negfile: 
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


    # with open("int.csv","r",errors="ignore") as internalfile: 
    #     w1=[] 
    #     w2=[]

    #     internalwords=csv.reader(internalfile)
    #     for row in internalwords: 
    #         singleinternalword=row[0].lower()
    #         if len(singleinternalword.split(" "))>1: 
    #             w1.append(singleinternalword.split(" ")[0])
    #             w2.append(singleinternalword.split(" ")[1])
    #             #print(singleinternalword.split(" "))
    #             #for word1, word2 in singleinternalword.split(" "):
    #             #word1=singleinternalword.split(" ")[0]
    #             #word2=singleinternalword.split(" ")[1]
    #             #internaldict[word1].append(word2)
    #             #internaldict.update({word1:word2})
    #         else: 
    #             word1=singleinternalword
    #             internaldict.update({word1:""})
        
    # for a, b in list(zip(w1, w2)):
    #     if a not in internaldict: 
    #         internaldict[a] = [b]
    #     else:
    #         if not isinstance(internaldict[a], str):
    #             internaldict[a].append(b)
    #     #internaldict.setdefault(a, []).append(b)

    #         #print(internalwordlist)
    

    # #def external wordlist 

    # externaldict=defaultdict(list)
    # with open("ext.csv","r",errors="ignore") as externalfile: 
    #     w1=[]
    #     w2=[]
    #     externalwords=csv.reader(externalfile)
    #     for row in externalwords: 
    #         singleexternalwords=row[0].lower()
    #         if len(singleexternalwords.split(" "))>1: 

    #             w1.append(singleexternalwords.split(" ")[0])
    #             w2.append(singleexternalwords.split(" ")[1])
    #             #word1=singleexternalwords.split(" ")[0]
    #             #word2=singleexternalwords.split(" ")[1]
    #             #externaldict[word1].append(word2)
    #             #externaldict.update({word1:word2})
    #         else: 
    #             word1=singleexternalwords
    #             externaldict.update({word1:""})


    # for a, b in list(zip(w1, w2)):
    #     if a not in externaldict: 
    #         externaldict[a] = [b]
    #     else:
    #         if not isinstance(externaldict[a], str):
    #             externaldict[a].append(b)
    #         #print(externalwordlist)


    

    sentlog_outputfields=["filename","sentnolist","positiveperformancesent","negativeperformancesent","positivewordscount","negativewordscount","doublenegsent","sentlen","LMposall","LMnegall","positiveLMlist","negativeLMlist","possentcount","neggsentcount"]


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
    LMposall=[]
    LMnegall=[]
    possentcount=[]
    neggsentcount=[]
    positivewordscount=[]
    negativewordscount=[]
    positiveLMlist=[]
    negativeLMlist=[]


    maximum1=-1*float("inf")
    maximum2=-1*float("inf")
    maximum3=-1*float("inf")
    maximum4=-1*float("inf")

    # changes on 6 nov: append the top 2 entries to maxmimumpara where least LM and most count in our dictionary
    maximumpara1=""
    maximumpara2=""
    maximumpara3=""
    maximumpara4=""
    

    dictcount=defaultdict(int)

    item="FILED AS OF DATE:"
    filenum=1 #correct as filenum 

    f_out=open(csv1,"w")
    wr=csv.writer(f_out)
    wr.writerow(sentlog_outputfields)
    fsent=open(direct,"w")

    #print("x")
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
                    substr1=text1[m.start():m.start()+30]
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
            #sent = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s|[A-Z].*)',content)
            sent = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s|[A-Z].*)',content) # list 
            # want to accumlate 5 sentences 
            posperfcnt=0 
            negperfcnt=0
            doubleneg=0
            LMpos=0
            LMneg=0
            sentno=0
            negativewordscnt=0
            positivewordscnt=0
            accumulate=0
            l=[]
            temp=""
            for i in range(len(sent)): # increment this by 5 sentences at a time
                accumulate+=1
                temp+=sent[i]
                if accumulate%5==0: 
                    l.append(temp)
                    temp=""
            for sentences in l:
                #print(sentences)
                #print(sentences)
                if "liquidity and capital resources" in sentences:
                    print("Y") #skip sentences with "liquidity and capital resources" since it may be categorized into the wrong thing 
                    continue
                sentno+=1
                fsent.write(files)
                fsent.write(str(sentno))
                fsent.write("\n")
                ww=[]
                #for r in word_tokenize(sentences): 
                for r in sentences.split(" "):
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
                    
                    for item in ww: 
                        if item in posperflist: 
                            LMpos+=1
                        if item in negperflist: 
                            LMneg+=1
                    
                    while i+a+b<len(ww):
                        BOOL=True
                        for b in range(1,4):
                            for a in range(1,4):
                                if BOOL:

                                    if negperfdict.get(ww[i].lower()) and i+a+b<len(ww): 
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
                                                dictcount[str(ww[i:i+b+a+1])]+=1
                                                i=i+a+b 
                                                negperfcnt+=1
                                                negativewordscnt+=sum([a,b])
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
                                                fsent.write(str(ww[i:i+a+b+1]))   
                                                dictcount[str(ww[i:i+a+b+1])]+=1
                                                i=i+a+b 
                                                posperfcnt+=1
                                                positivewordscnt+=sum([a,b])
                                                BOOl=False
                                                break 

                                            elif ww[i+a+b] in badset: 
                                                # print(ww[i:i+a+b+1]) 
                                                # print(ww[i])
                                                # print(ww[i+b])
                                                # print(ww[i+a+b])
                                                fsent.write("negative")                                                
                                                fsent.write(str(ww[i:i+a+b+1]))
                                                dictcount[str(ww[i:i+a+b+1])]+=1
                                                i=i+a+b 
                                                negperfcnt+=1
                                                negativewordscnt+=sum([a,b])
                                                BOOl=False
                                                break 

                                            elif ww[i+a+b] in goodset: 
                                                # print(ww[i:i+a+b+1]) 
                                                # print(ww[i])
                                                # print(ww[i+b])
                                                # print(ww[i+a+b])
                                                fsent.write("positive")                                                
                                                fsent.write(str(ww[i:i+a+b+1]))
                                                dictcount[str(ww[i:i+a+b+1])]+=1
                                                i=i+a+b 
                                                posperfcnt+=1
                                                positivewordscnt+=sum([a,b])
                                                BOOl=False
                                                break 
                                      
                                        #elif b(i,a,b,ww,negatorset,posperfcnt,BOOL):

                                        elif "." in negperfdict[ww[i].lower()] and b==3:
                                            # changed to reflect greedy appraoch 28 Sept
                                            for x in range(1,4):
                                                if ww[i+x] in amplifierset:
                                                    negperfcnt+=1
                                                    fsent.write("negative")                                                
                                                    fsent.write(str(ww[i:i+x+1]))  
                                                    dictcount[str(ww[i:i+x+1])]+=1   
                                                    negativewordscnt+=x                           
                                                    i=i+x
                                                    BOOl=False
                                                    break
                                                if ww[i+x] in negatorset:
                                                    posperfcnt+=1
                                                    fsent.write("positive")                                                
                                                    fsent.write(str(ww[i:i+x+1]))  
                                                    dictcount[str(ww[i:i+x+1])]+=1
                                                    positivewordscnt+=x
                                                    i=i+x
                                                    BOOl=False
                                                    break
                                                if ww[i+x] in badset:
                                                    negperfcnt+=1
                                                    fsent.write("negative")                                                
                                                    fsent.write(str(ww[i:i+x+1]))  
                                                    dictcount[str(ww[i:i+x+1])]+=1 
                                                    negativewordscnt+=x 
                                                    i=i+x
                                                    BOOl=False
                                                    break
                                                if ww[i+x] in goodset:
                                                    posperfcnt+=1
                                                    fsent.write("positive")                                                
                                                    fsent.write(str(ww[i:i+x+1]))  
                                                    dictcount[str(ww[i:i+x+1])]+=1  
                                                    positivewordscnt+=x
                                                    i=i+x
                                                    BOOl=False
                                                    break


                                    if posperdict.get(ww[i].lower()) and i+a+b<len(ww): 
                                        if ww[i+b] in posperdict[ww[i].lower()]:
                                            #if negperfdict[ww[i+b]] is not None:
                                            if ww[i+a+b] in amplifierset: 
                                                fsent.write("positive")                                                
                                                fsent.write(str(ww[i:i+a+b+1]))  
                                                dictcount[str(ww[i:i+a+b+1])]+=1
                                                i=i+a+b 
                                                posperfcnt+=1
                                                positivewordscnt+=sum([a,b])
                                                BOOl=False
                                                break 
                                            
                                            elif ww[i+a+b] in negatorset: 
                                                #print(ww[i:i+a+b+1]) 
                                                fsent.write("negative")                                                
                                                fsent.write(str(ww[i:i+a+b+1]))    
                                                dictcount[str(ww[i:i+a+b+1])]+=1
                                                negativewordscnt+=sum([a,b])
                                                i=i+a+b 
                                                negperfcnt+=1
                                                BOOl=False
                                                break 
                                            elif ww[i+a+b] in badset: 
                                                #print(ww[i:i+a+b+1]) 
                                                fsent.write("negative")                                                
                                                fsent.write(str(ww[i:i+a+b+1]))  
                                                dictcount[str(ww[i:i+a+b+1])]+=1
                                                negativewordscnt+=sum([a,b])
                                                i=i+a+b 
                                                negperfcnt+=1
                                                BOOl=False
                                                break 

                                            elif ww[i+a+b] in goodset: 
                                                #print(ww[i:i+a+b+1]) 
                                                fsent.write("positive")                                                
                                                fsent.write(str(ww[i:i+a+b+1]))  
                                                dictcount[str(ww[i:i+a+b+1])]+=1
                                                i=i+a+b 
                                                positivewordscnt+=sum([a,b])
                                                posperfcnt+=1
                                                BOOl=False
                                                break 
                                            
                                        elif "." in negperfdict[ww[i].lower()] and b==3:
                                            for x in range(1,4):
                                                if ww[i+x] in amplifierset:
                                                    negperfcnt+=1
                                                    fsent.write("negative")                                                
                                                    fsent.write(str(ww[i:i+x+1]))      
                                                    dictcount[str(ww[i:i+x+1])]+=1
                                                    negativewordscnt+=sum([a,b])
                                                    negativewordscnt+=x
                                                    i=i+x
                                                    BOOl=False
                                                    break
                                                if ww[i+x] in negatorset:
                                                    posperfcnt+=1
                                                    fsent.write("doubleneg")                                                
                                                    fsent.write(str(ww[i:i+x+1]))    
                                                    dictcount[str(ww[i:i+x+1])]+=1
                                                    positivewordscnt+=x
                                                    #print(ww[i:i+b+a+1]) 
                                                    i=i+x
                                                    BOOl=False
                                                    break
                                                if ww[i+x] in badset:
                                                    fsent.write("negative")                                                
                                                    fsent.write(str(ww[i:i+x+1]))                                                     
                                                    negperfcnt+=1
                                                    dictcount[str(ww[i:i+x+1])]+=1
                                                    #print(ww[i:i+b+a+1]) 
                                                    negativewordscnt+=x
                                                    i=i+x
                                                    BOOl=False
                                                    break
                                                if ww[i+x] in goodset:
                                                    fsent.write("positive")                                                
                                                    fsent.write(str(ww[i:i+x+1]))                                                     
                                                    posperfcnt+=1
                                                    dictcount[str(ww[i:i+x+1])]+=1
                                                    positivewordscnt+=x
                                                    #print(ww[i:i+b+a+1]) 
                                                    i=i+x
                                                    BOOl=False
                                                    break


                                    if ww[i].lower() in negatorset and i+a+b<len(ww) :
                                        if negperfdict.get(ww[i+b]):
                                            if ww[i+a+b] in negperfdict[ww[i+b]]: 
                                                fsent.write("doubleneg")
                                                fsent.write(str(ww[i:i+a+b+1]))
                                                #freq count increment
                                                dictcount[str(ww[i:i+a+b+1])]+=1
                                                # alternative sol
                                                positivewordscnt+=sum([a,b])
                                                posperfcnt+=1
                                                i=i+a+b 
                                                BOOl=False
                                                break 

                                            elif "." in negperfdict[ww[i+b]] :
                                                fsent.write("doubleneg")
                                                fsent.write(str(ww[i:i+b+1]))     
                                                dictcount[str(ww[i:i+b+1])]+=1
                                                posperfcnt+=1
                                                i=i+b
                                                negativewordscnt+=b
                                                BOOl=False
                                                break
                                          
                                        if posperdict.get(ww[i+b]):

                                            if ww[i+a+b] in posperdict[ww[i+b]]: 
                                                fsent.write("negative")
                                                fsent.write(str(ww[i:i+a+b+1]))       
                                                dictcount[str(ww[i:i+a+b+1])]+=1
                                                negperfcnt+=1
                                                i=i+a+b 
                                                negativewordscnt+=sum([a,b])
                                                BOOl=False
                                                break 

                                            elif "." in posperdict[ww[i+b]] :
                                                fsent.write("negative")
                                                fsent.write(str(ww[i:i+b+1]))
                                                dictcount[str(ww[i:i+b+1])]+=1
                                                negativewordscnt+=sum([a,b])
                                                negperfcnt+=1
                                                i=i+b
                                                BOOl=False
                                                break
                                            

                                    if ww[i].lower() in amplifierset and i+a+b<len(ww): 
                                        if posperdict.get(ww[i+b]):

                                            if ww[i+a+b] in posperdict[ww[i+b]]: 
                                                fsent.write("positive")                                                
                                                fsent.write(str(ww[i:i+a+b+1]))
                                                dictcount[str(ww[i:i+a+b+1])]+=1
                                                positivewordscnt+=sum([a,b])
                                                posperfcnt+=1
                                                i=i+a+b
                                                BOOl=False
                                                break

                                            elif "." in posperdict[ww[i+b]]:
                                                fsent.write("positive")                                                
                                                fsent.write(str(ww[i:i+b+1]))
                                                dictcount[str(ww[i:i+b+1])]+=1
                                                positivewordscnt+=b
                                                posperfcnt+=1                                      
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
                                                dictcount[str(ww[i:i+a+b+1])]+=1
                                                negperfcnt+=1 
                                                negativewordscnt+=sum([a,b])
                                                i=i+a+b 
                                                BOOl=False
                                                break 

                                            elif "." in negperfdict[ww[i+b]]: 
                                                fsent.write("negative")                                                
                                                fsent.write(str(ww[i:i+b+1]))  
                                                dictcount[str(ww[i:i+b+1])]+=1
                                                negperfcnt+=1
                                                negativewordscnt+=b
                                                i=i+b
                                                BOOL=False
                                                break
                                        
                                    if ww[i].lower() in badset and i+a+b<len(ww): 
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
                                                dictcount[str(ww[i:i+b+a+1])]+=1
                                                negperfcnt+=1
                                                i=i+a+b 
                                                negativewordscnt+=sum([a,b])
                                                BOOl=False
                                                break

                                            elif "." in posperdict[ww[i+b]]:
                                                fsent.write("negative")                                                
                                                fsent.write(str(ww[i:i+b+1]))
                                                dictcount[str(ww[i:i+b+1])]+=1
                                                negativewordscnt+=b
                                                negperfcnt+=1                                         
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
                                                dictcount[str(ww[i:i+a+b+1])]+=1
                                                negperfcnt+=1
                                                negativewordscnt+=sum([a,b])
                                                i=i+a+b 
                                                BOOl=False
                                                break 

                                            elif "." in negperfdict[ww[i+b]]: 
                                                fsent.write("negative")                                                
                                                fsent.write(str(ww[i:i+b+1]))
                                                dictcount[str(ww[i:i+b+1])]+=1
                                                negativewordscnt+=b
                                                negperfcnt+=1
                                                i=i+b
                                                BOOL=False
                                                break


                                    if ww[i].lower() in goodset and i+a+b<len(ww): 
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
                                                fsent.write("positive")                                                
                                                fsent.write(str(ww[i:i+b+a+1]))    
                                                dictcount[str(ww[i:i+b+a+1])]+=1
                                                positivewordscnt+=sum([a,b])
                                                posperfcnt+=1
                                                i=i+a+b 
                                                BOOl=False
                                                break

                                            elif "." in posperdict[ww[i+b]]:
                                                fsent.write("positive")                                                
                                                fsent.write(str(ww[i:i+b+1]))
                                                dictcount[str(ww[i:i+b+1])]+=1
                                                positivewordscnt+=b
                                                posperfcnt+=1                                         
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
                                                fsent.write("positive")                                                
                                                fsent.write(str(ww[i:i+a+b+1])) 
                                                dictcount[str(ww[i:i+a+b+1])]+=1
                                                positivewordscnt+=sum([a,b])
                                                posperfcnt+=1
                                                i=i+a+b 
                                                BOOl=False
                                                break 

                                            elif "." in negperfdict[ww[i+b]]: 
                                                fsent.write("positive")                                                
                                                fsent.write(str(ww[i:i+b+1]))
                                                dictcount[str(ww[i:i+b+1])]+=1
                                                positivewordscnt+=b
                                                posperfcnt+=1
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
                                            
                    
                                   
                        i+=1
                

                    """
                    Nov 6 modifications
                    """

                    if LMneg>LMpos: 
                        positiveLM=1
                    else: 
                        positiveLM=0
                    if LMneg<LMpos: 
                        negativeLM=1
                    else: 
                        negativeLM=0

                    lmdiff=LMpos/(LMneg+0.01) # diff in words frequency LM (words level)
                    # now want diff in words freq porportion to be highest
                    if (positivewordscnt-negativewordscnt)/(lmdiff+0.01)>maximum1: 
                        maximum1=(positivewordscnt-negativewordscnt)/(lmdiff+0.01)
                        maximumpara1=sentences
                        positiveoverall=positivewordscnt
                        negativeoverall=negativewordscnt
                        lmpositiveoverall=LMpos
                        lmnegativeoverall=LMneg

                    
                    lmdiff2=positiveLM/(negativeLM+0.01) # diff in sentence level frequency 
                    if (posperfcnt-negperfcnt)/(lmdiff2+0.01)>maximum2: 
                        maximum2=(posperfcnt-negperfcnt)/(lmdiff2+0.01)
                        maximumpara2=sentences
                        positiveoverall2=positivewordscnt
                        negativeoverall2=negativewordscnt
                        lmpositiveoverall2=LMpos
                        lmnegativeoverall2=LMneg


                    lmdiff3=LMneg/(LMpos+0.01) # diff in words frequency LM (words level)
                    if (negativewordscnt-positivewordscnt)/(lmdiff3+0.01)>maximum3: 
                        maximum3=(negativewordscnt-positivewordscnt)/(lmdiff3+0.01)
                        maximumpara3=sentences
                        positiveoverall3=positivewordscnt
                        negativeoverall3=negativewordscnt
                        lmpositiveoverall3=LMpos
                        lmnegativeoverall3=LMneg
                    
                    lmdiff4=negativeLM/(positiveLM+0.01)# diff in sentence level frequency 
                    if (negperfcnt-posperfcnt)/(lmdiff4+0.01)>maximum4: 
                        maximum4=(negperfcnt-posperfcnt)/(lmdiff4+0.01)
                        maximumpara4=sentences
                        positiveoverall4=positivewordscnt
                        negativeoverall4=negativewordscnt
                        lmpositiveoverall4=LMpos
                        lmnegativeoverall4=LMneg

                    if posperfcnt>negperfcnt: 
                        possent=1
                    else: 
                        possent=0
                    if posperfcnt<negperfcnt: 
                        neggsent=1
                    else: 
                        neggsent=0



                    neggsentcount.append(neggsent)
                    possentcount.append(possent)
                    positiveperformancesent.append(posperfcnt)
                    negativeperformancesent.append(negperfcnt)
                    doublenegsent.append(doubleneg)
                    LMposall.append(LMpos)
                    LMnegall.append(LMneg)
                    positivewordscount.append(positivewordscnt)
                    negativewordscount.append(negativewordscnt)
                    positiveLMlist.append(positiveLM)
                    negativeLMlist.append(negativeLM)
                    positivewordscnt=0
                    negativewordscnt=0
                    posperfcnt=0
                    negperfcnt=0
                    doubleneg=0
                    LMpos=0
                    LMneg=0
                    positiveLM=0
                    negativeLM=0
                    sentlen.append(len(ww))

                else:
                    sentno-=1   

            if DEBUG:
                if filenum==10:
                    break 
    
    print(maximumpara1)
    print(positiveoverall)
    print(negativeoverall)
    print(lmpositiveoverall)
    print(lmnegativeoverall)
    print(maximumpara2)
    print(positiveoverall2)
    print(negativeoverall2)
    print(lmpositiveoverall2)
    print(lmnegativeoverall2)
    print(maximumpara3)
    print(positiveoverall3)
    print(negativeoverall3)
    print(lmpositiveoverall3)
    print(lmnegativeoverall3)
    print(maximumpara4)
    print(positiveoverall4)
    print(negativeoverall4)
    print(lmpositiveoverall4)
    print(lmnegativeoverall4)

    sorted_x = sorted(dictcount.items(), key=operator.itemgetter(1))
    print(sorted_x)
    p=zip(filename,sentnolist,positiveperformancesent,negativeperformancesent,positivewordscount,negativewordscount,doublenegsent,sentlen,LMposall,LMnegall,positiveLMlist,negativeLMlist,possentcount,neggsentcount)
    for row in p:
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
lmposoverall=[]
lmnegoverall=[]
posall=[]
negall=[]
positiveoverall=[]
negativeoverall=[]
numberofsentences=[]
poswordcount=[]
negwordcount=[]
poswordcountlist=[]
negwordcountlist=[]
lmsentencespos=[]
lmsentencesneg=[]

#print(len(f1))

poslist=[]
neglist=[]
filenamelist=[]
yearlist=[]
ciklist=[]
llist=[] 
doublenegall=[]
lmposoverall=[]
lmnegoverall=[]
posall=[]
negall=[]
positiveoverall=[]
negativeoverall=[]
numberofsentences=[]
poswordcount=[]
negwordcount=[]
poswordcountlist=[]
negwordcountlist=[]
lmsentencespos=[]
lmsentencesneg=[]

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
    lmpos=0
    lmneg=0
    lmsentencespos=0
    lmsentencesneg=0
    poscount=0
    poswordcount=0
    negwordcount=0
    negcount=0
    sentencescount=0
    


poslist=[]
neglist=[]
filenamelist=[]
yearlist=[]
ciklist=[]
llist=[] 
doublenegall=[]
lmposoverall=[]
lmnegoverall=[]
posall=[]
negall=[]
positiveoverall=[]
negativeoverall=[]
numberofsentences=[]
poswordcount=[]
negwordcount=[]
poswordcountlist=[]
negwordcountlist=[]
lmsentencespos=[]
lmsentencesneg=[]

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
    lmpos=0
    lmneg=0
    lmsentencespos=0
    lmsentencesneg=0
    poscount=0
    poswordcount=0
    negwordcount=0
    negcount=0
    sentencescount=0
    


poslist=[]
neglist=[]
filenamelist=[]
yearlist=[]
ciklist=[]
llist=[] 
doublenegall=[]
lmposoverall=[]
lmnegoverall=[]
posall=[]
negall=[]
positiveoverall=[]
negativeoverall=[]
numberofsentences=[]
poswordcount=[]
negwordcount=[]
poswordcountlist=[]
negwordcountlist=[]
lmsentencespos=[]
lmsentencesneg=[]

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
    lmpos=0
    lmneg=0
    lmsentencespos1=0
    lmsentencesneg1=0
    poscount=0
    poswordcount=0
    negwordcount=0
    negcount=0
    sentencescount=0
    


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
                    #doublenegall.append(doubleneg)
                    lmposoverall.append(lmpos)
                    lmnegoverall.append(lmneg)
                    positiveoverall.append(poscount)
                    negativeoverall.append(negcount)
                    numberofsentences.append(sentencescount)
                    lmsentencespos.append(lmsentencespos1)
                    lmsentencesneg.append(lmsentencesneg1)
                    poswordcountlist.append(poswordcount)
                    negwordcountlist.append(negwordcount)

                pos=0
                neg=0
                l=0
                doubleneg=0
                lmpos=0
                lmneg=0
                poscount=0
                negcount=0
                sentencescount=0
                poswordcount=0
                negwordcount=0
                lmsentencespos1=0
                lmsentencesneg1=0

            if row[2].isdigit():
                poswordcount+=int(row[2])
            if row[3].isdigit(): 
                negwordcount+=int(row[3])
            if row[4].isdigit():
                pos+=int(row[4])
            if row[5].isdigit(): 
                neg+=int(row[5])
            #if row[4].isdigit():
                #doubleneg+=int(row[4])
            if row[7].isdigit():
                l+=int(row[7])
            if row[8].isdigit():
                lmpos+=int(row[8])
            if row[9].isdigit():
                lmneg+=int(row[9])
            if row[10].isdigit():
                lmsentencespos1+=int(row[10])
            if row[11].isdigit():
                lmsentencesneg1+=int(row[11])
            if row[12].isdigit():
                poscount+=int(row[12])
            if row[13].isdigit():
                negcount+=int(row[13])

            sentencescount+=1          
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

            
    p=zip(filenamelist,yearlist,ciklist,poslist,neglist,poswordcountlist,negwordcountlist,lmposoverall,lmnegoverall,lmsentencespos,lmsentencesneg,llist,positiveoverall,negativeoverall,numberofsentences) 
    wr2.writerow(["filename","year","cik","pos","neg","poscount","negcount","lmpositive","lmnegative","lmpos","lmneg","l","poscount","negcount","sentences"])
    for row in p:
        wr2.writerow(row)


finalcount(f1)