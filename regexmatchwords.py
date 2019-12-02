
"""
One of the issues with our dictionary is that sometimes, amplifier/negator are not connected together with performance indicator 
In order to resolve this, we introduced a regular expression match between amplifier/negator and performance indicator and write out the match, together with the amplifier and negator

###################################################################################################################
Data Dependencies:

postperf.csv -------- csv with all positive performance ngrams 
negperf.csv -------- csv with all negative performance ngrams  
amplifier.csv  -------- csv with all amplifiers ngrams  
negator.csv --------csv with all negators ngrams  

##########################################################################################################################################
This program outputs: 

negateposper.csv
amplifyposper.csv
negatenegper.csv
amplifynegper.csv

negateposper.csv and amplifynegper.csv can be dumped into negperflist.csv --------   csv with  amplifier & negator adjusted negative performance ngrams 
amplifyposper.csv and negatenegper.csv can be dumped into posperflist.csv -------- csv with amplifier & negator adjusted positive performance ngrams 




"""




import re 
import glob
import os
import csv
import nltk 
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 



debug=False

os.chdir("/Users/lucy/Desktop/builddic")

posperflist=[]
with open("postperf.csv","r") as posfile: 
#with open("posperflist.csv","r") as posfile: 
    poswords=csv.reader(posfile)
    for row in poswords: 
        singleposperword=row[0].lower()
        posperflist.append(singleposperword)
        #print(internalwordlist)

#load in negative performance word list 

negperflist=[]
with open("negperf.csv","r") as negfile: 
#with open("negaperflist.csv","r") as negfile
    negwords=csv.reader(negfile)
    for row in negwords: 
        singlenegperfword=row[0].lower()
        negperflist.append(singlenegperfword)
        #print(internalwordlist)


#def internal wordlist 

amplist=[]
with open("amplifier.csv","r") as ampfile: 
    ampwords=csv.reader(ampfile)
    for row in ampwords: 
        singleampword=row[0].lower()
        amplist.append(singleampword)
        #print(internalwordlist)


#def external wordlist 

neglist=[]
with open("negator.csv","r") as negfile: 
    negwords=csv.reader(negfile)
    for row in negwords: 
        singlenegword=row[0].lower()
        neglist.append(singlenegword)
        #print(externalwordlist)


corpus="/Users/lucy/Desktop/assortedcodes/assortedcodes/newdictestn/newdic/*.txt"





for files in glob.glob(corpus):
    with open(files) as f: 
        print(files)
        content = f.read()
        re.sub("\n","",content)
        sent = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s|[A-Z].*)',content)
        sentno=0

        for sentences in sent: #need to identify individual words, modify to match regex words

#negateposper

            for negword in neglist: 
                for posword in posperflist: 
                    if negword and posword in sentences:
                        matchfound=re.findall(negword+'(.*)'+posword,sentences)
                        if matchfound: 
                             #print(matchfound)
                            match="".join(matchfound)
                            a=0
                            words=match.split()
                            matchlist=[]
                            for word in words: 
                                if word not in stopwords.words("english"):
                                    matchlist.append(word)
                                    a=a+1 
                            if a<4: 
                                matched=" ".join(matchlist)
                                if debug: 
                                    print([negword+" "+matched+" "+posword])
                                    print("a")

                                with open("negateposper.csv","a") as f_out:
                                    wr=csv.writer(f_out)
                                    wr.writerow([negword+" "+matched+" "+posword]) 
                               

#amplifyposper

            for ampword in amplist: 
                for posword in posperflist: 
                    if ampword and posword in sentences:
                        matchfound=re.findall(ampword+'(.*)'+posword,sentences)
                        if matchfound: 
                             #print(matchfound)
                            match="".join(matchfound)
                            a=0
                            words=match.split()
                            matchlist=[]
                            for word in words: 
                                if word not in stopwords.words("english"):
                                    matchlist.append(word)
                                    a=a+1 
                            if a<4: 
                                matched=" ".join(matchlist)
                                if debug: 
                                    print([ampword+" "+matched+" "+posword])
                                    print("b")

                                with open("amplifyposper.csv","a") as f_out1:
                                    wr1=csv.writer(f_out1)
                                    wr1.writerow([ampword+" "+matched+" "+posword]) 

#negatenegper

            for negword in neglist: 
                for negperword in negperflist: 
                    if negword and negperword in sentences:
                        matchfound=re.findall(negword+'(.*)'+negperword,sentences)
                        if matchfound: 
                             #print(matchfound)
                            match="".join(matchfound)
                            a=0
                            words=match.split()
                            matchlist=[]
                            for word in words: 
                                if word not in stopwords.words("english"):
                                    matchlist.append(word)
                                    a=a+1 
                            if a<4: 
                                matched=" ".join(matchlist)
                                if debug: 
                                    print([negword+" "+matched+" "+negperword])
                                    print("c")

                                with open("negatenegper.csv","a") as f_out2:
                                    wr2=csv.writer(f_out2)
                                    wr2.writerow([negword+" "+matched+" "+negperword]) 
                                    

#amplifynegper

            for ampword in amplist: 
                for negperword in negperflist: 
                    if ampword and negperword in sentences:
                        matchfound=re.findall(ampword+'(.*)'+negperword,sentences)
                        if matchfound: 
                             #print(matchfound)
                            match="".join(matchfound)
                            a=0
                            words=match.split()
                            matchlist=[]
                            for word in words: 
                                if word not in stopwords.words("english"):
                                    matchlist.append(word)
                                    a=a+1 
                            if a<4: 
                                matched=" ".join(matchlist)
                                if debug: 
                                    print([ampword+" "+matched+" "+negperword])
                                    print("d")

                                with open("amplifynegper.csv","a") as f_out3:
                                    wr3=csv.writer(f_out3)
                                    wr3.writerow([ampword+" "+matched+" "+negperword]) 

#add performance + "" + negator 
#Put a space before and after each negator/amplifer/performance 