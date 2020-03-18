"""
 * for parts of all relevance 
f for future 
/ for parts del

if contains amplifier/negator, mark, keep 
if performance word is singular, mark all words containing perf words 

change 4 to x 
delete all repeated words 
Get rid of all plurals 

Further: 

truncate common financial words eg. retained earnings


"""

dir1="/Users/lucy/Desktop/assortedcodes/sort/3marchsorted.csv" #classified 
dir2="/Users/lucy/Desktop/assortedcodes/sort/3marchsortfile.csv" #classifying 
originalcsv="/Users/lucy/Desktop/assortedcodes/sort/ngramrel.csv" #labeled perf words 




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


class MANIP: 
 
    def __init__(self): 
        pass

    def read(self): 
        global phraselist
        global tfidf  
        global num 
        global importancerank
        phraselist=[]
        tfidf=[] 
        num=[] 
        importancerank=[]

        with open(dir1,"r") as csvfile: #classified
            freader = csv.reader(csvfile)
            for row in freader: 
                phraselist.append(row[0])
                tfidf.append(row[1])
                num.append(row[2])
                importancerank.append(row[3])
            csvfile.close()

        global classifyingphraselist
        global classifyingtfidf  
        global classifyingnum 
        global classifyingimportancerank
        classifyingphraselist=[]
        classifyingtfidf=[] 
        classifyingnum=[] 
        classifyingimportancerank=[]
                

        with open(dir2,"r") as csvfile: #classfying
            freader = csv.reader(csvfile)
            for row in freader: 
                classifyingphraselist.append(row[0])
                classifyingtfidf.append(row[1])
                classifyingnum.append(row[2])
                classifyingimportancerank.append(row[3])
            csvfile.close()
        

        global ampneghraselist
        global ampnegclassifyingtfidf  
        global ampnegclassifyingnum 
        global ampnegclassifyingimportancerank
        ampneghraselist=[]
        ampnegclassifyingtfidf=[] 
        ampnegclassifyingnum=[] 
        ampnegclassifyingimportancerank=[]
                

        with open(originalcsv,"r") as csvfile: #get amplifiers and negators 
            freader = csv.reader(csvfile)
            for row in freader: 
                ampneghraselist.append(row[0])
                ampnegclassifyingtfidf.append(row[1])
                ampnegclassifyingnum.append(row[2])
                ampnegclassifyingimportancerank.append(row[3])
            csvfile.close()
        return phraselist, tfidf, num, importancerank, classifyingphraselist, classifyingtfidf, classifyingnum,classifyingimportancerank, ampneghraselist, ampnegclassifyingtfidf, ampnegclassifyingnum, ampnegclassifyingimportancerank

    def markallperf(self): 
        self.read() 
        self.change4tox()
        self.convertindex(ampnegclassifyingnum,"x")
        performancewords=[]
        for i in indexlist: 
            performancewords.append(ampneghraselist[i])
        assert len(ampneghraselist)==len(ampnegclassifyingnum)
        for i in range(len(classifyingnum)): 
            for a in performancewords: 
                #for b in classifyingphraselist: 
                if len(classifyingphraselist[i].split(" "))>1:
                    if a==classifyingphraselist[i].split(" ")[0] or a==classifyingphraselist[i].split(" ")[1]: 
                        if "x" not in classifyingnum[i]:
                            classifyingnum[i]=classifyingnum[i]+"x"
                else: 
                    if a==classifyingnum[i]: 
                        if "x" not in classifyingnum[i]:
                            classifyingnum[i]=classifyingnum[i]+"x"


        return classifyingnum 

    def keep(self): 
        #self.read()
        #self.change4tox()
        #self.convertindex()
        self.markallperf()
        self.convertindex(ampnegclassifyingnum,"2")
        amplifierlist=[]
        for i in indexlist: 
            amplifierlist.append(ampneghraselist[i])

        for i in range(len(classifyingnum)): 
            for a in amplifierlist: 
                if "3" in classifyingnum[i]:
                    classifyingnum[i]=classifyingnum[i][1:]
                    classifyingnum[i]=classifyingnum[i]+"ampneg"        
                #for b in classifyingphraselist: 
                if len(classifyingphraselist[i].split(" "))>1:
                        
                    if a==classifyingphraselist[i].split(" ")[0] or a==classifyingphraselist[i].split(" ")[1]: 
                        classifyingnum[i]=classifyingnum[i]+"ampneg"      
                else: 
                    if a==classifyingphraselist[i]: 
                        classifyingnum[i]=classifyingnum[i]+"ampneg"
                    

        """
        Note: Debug 5 March
        (incorrect)
        for a in amplifierlist: 
            for b in classifyingphraselist: 
                if a==b.split(" ")[0] or a==b.split(" ")[1]: 
                    classifyingnum.append("ampneg")

        """

        return classifyingnum 



    def change4tox(self): 
        self.read() 
        self.convertindex(classifyingnum,"4")
        for item in indexlist: 
            classifyingnum[item]="x"
        # classifyingphraselist1=[]
        # classifyingtfidf1=[] 
        # classifyingnum1=[] 
        # classifyingimportancerank1=[]
        # for i in indexlist:
        #     classifyingphraselist1.append(classifyingphraselist[i])
        #     classifyingtfidf1.append(classifyingtfidf[i])
        #     classifyingnum1.append(classifyingnum[i])
        #     classifyingimportancerank1.append(classifyingimportancerank[i])
        return classifyingnum

    def convertindex(self,listcalled,iterable): 

        global indexlist 
        indexlist=[]
        indexPos=0 
        while True: 
            try: 
                indexPos=listcalled.index(iterable,indexPos) #search for item in list from indexPos to end of list
                indexlist.append(indexPos)
                indexPos+=1 
            except ValueError:
                break 
        #debug11 March :nothing wrong with fucntion 
        print(len(indexlist))
        print("convertindex")
        return indexlist

    def getfuture(self): 
        global futures
        global tfidfutures
        global numutures
        global importancerankfutures
        
        self.read()
        self.convertindex(num,"f")
        futures=[]
        tfidfutures=[]
        numutures=[]
        importancerankfutures=[]
        for i in indexlist:
            futures.append(phraselist[i].split(" ")[1]) 
            tfidfutures.append(tfidf[i]) 
            numutures.append(num[i])
            importancerankfutures.append(importancerank[i])


        global futuresngrams
        global tfidfdeletedngramsfutures
        global numdeletedngramsfutures
        global importancerankngramsfutures

        futuresngrams=[]
        tfidfdeletedngramsfutures=[]
        numdeletedngramsfutures=[]
        importancerankngramsfutures=[]


        # Debug 11 March: corrected variable names

        for a in range(len(phraselist)):
            for i in futures: 
                if len(classifyingphraselist[a].split(" "))>1: 
                    if classifyingphraselist[a].split(" ")[0]==i or classifyingphraselist[a].split(" ")[1]==i: 
                        futuresngrams.append(classifyingphraselist[a])
                        importancerankngramsfutures.append(classifyingimportancerank[a])
                        numdeletedngramsfutures.append(classifyingnum[a])
                        tfidfdeletedngramsfutures.append(classifyingtfidf[a])
                else: 
                    if classifyingphraselist[a]==i: 
                        futuresngrams.append(phraselist[a])
                        importancerankngramsfutures.append(classifyingimportancerank[a])
                        numdeletedngramsfutures.append(classifyingnum[a])
                        tfidfdeletedngramsfutures.append(classifyingtfidf[a])
                    

        return futures, tfidfutures, numutures, importancerankfutures, futuresngrams, tfidfdeletedngramsfutures, numdeletedngramsfutures, importancerankngramsfutures

    
    def removeduplicates(self,anylist): 
        global sortedwords 
        dic={}
        for i in range(len(anylist)):
            if anylist[i] in dic: 
                dic[anylist[i]]+=1 
            else: 
                dic.update({anylist[i]:int(1)}) 
        sortedwords=[k for k in dic.keys()] #alternatively, can do list(dic)
        """
        "DEBUG 11 M"
        """
        print("DEBUG 11 M" + "sortedwords" + "\n") 
        print(len(sortedwords))
        #self.convertindex(anylist,sortedwords)
        return sortedwords 

    def delete(self): 

        self.read()
        self.convertindex(num,"/")
        global deleted
        global tfidfdeleted
        global numdeleted
        global importancerankfuturesdeleted

        deleted=[]
        tfidfdeleted=[]
        numdeleted=[]
        importancerankfuturesdeleted=[]
        for i in indexlist:
            deleted.append(phraselist[i].split(" ")[1]) 
            tfidfdeleted.append(tfidf[i]) 
            numdeleted.append(num[i])
            importancerankfuturesdeleted.append(importancerank[i])

        global deletedngrams
        global tfidfdeletedngrams
        global numdeletedngrams
        global importancerankfuturesdeletedngrams


        # Debug 11 March 
        # should be executed on classifying phrase list, not the phraselist 
        # This is fixed, but deletedphraselist still contains words that might be relevant 

        deletedngrams=[]
        tfidfdeletedngrams=[]
        numdeletedngrams=[]
        importancerankfuturesdeletedngrams=[]
        for a in range(len(classifyingphraselist)):
            for i in deleted: 
                if len(classifyingphraselist[a].split(" "))>1: 
                    if classifyingphraselist[a].split(" ")[0]==i or classifyingphraselist[a].split(" ")[1]==i: 
                        deletedngrams.append(classifyingphraselist[a])
                        importancerankfuturesdeletedngrams.append(classifyingimportancerank[a])
                        numdeletedngrams.append(classifyingnum[a])
                        tfidfdeletedngrams.append(classifyingtfidf[a])
                else: 
                    if classifyingphraselist[a]==i: 
                        deletedngrams.append(classifyingphraselist[a])
                        importancerankfuturesdeletedngrams.append(classifyingimportancerank[a])
                        numdeletedngrams.append(classifyingnum[a])
                        tfidfdeletedngrams.append(classifyingtfidf[a])


        return deleted,tfidfdeleted,numdeleted,importancerankfuturesdeleted,deletedngrams,importancerankfuturesdeletedngrams,numdeletedngrams,tfidfdeletedngrams


    def outputfinal(self): 
        """ 
        Not done 
        """
        global newphraselist
        global newtfidf
        global newnum
        global newimportancerank
        self.delete()
        self.getfuture()
        self.ridplurals() 

        newphraselist=[]
        newtfidf=[]
        newnum=[]
        newimportancerank=[]

        reverse_concatenatedlist=deletedngrams+futuresngrams
        newphraselist=list(set(newfinallist)-set(reverse_concatenatedlist))


        """

        Debug 13 March: suboptimal solution, speed issue, see notes. 

        for element in newphraselist:
            while True: 
                try: 
                    indexPos1=classifyingphraselist.index(element,0) #search for item in list from indexPos to end of list
                    indexlist1.append(indexPos1)
                    #indexPos1+=1 
                except ValueError:
                    #print(indexPos1)
                    break


        """

        st=set(newphraselist)
        indexlist1=[newfinallist.index(i) for i in st if i in newfinallist]

        for i in indexlist1:
            newphraselist.append(newfinallist[i])
            newtfidf.append(newclassifyingtfidf[i])
            newnum.append(newclassifyingnum[i])
            newimportancerank.append(newclassifyingimportancerank[i])



        """
        Debug 7 March 
        newtfidf=list(set(tfidf).symmetric_difference(tfidfdeletedngrams+tfidfdeletedngramsfutures))
        newnum=list(set(num).symmetric_difference(numdeletedngrams+numdeletedngramsfutures))
        newimportancerank=list(set(importancerank).symmetric_difference(importancerankfuturesdeletedngrams+importancerankngramsfutures))
        """

        """
        Debug 11 March
        Corrected variable names
        """


        return newphraselist, newtfidf, newnum, newimportancerank

    def ridplurals(self): 
        global newlist
        global newclassifyingtfidf
        global newclassifyingnum
        global newclassifyingimportancerank
        global sortedwords
        global classifyingphraselist
        global hashmapbuilder 
        global hashmapbuilder1
        global indexlist1 
        global newfinallist
        self.keep()
        newlist=[]
        newclassifyingtfidf=[]
        newclassifyingnum=[]
        newclassifyingimportancerank=[]
        newfinallist=[]
        #Begin debug 5 March 
        #for i in classifyingphraselist:
            #i=list(i) 
            #print(i)
            #print(i.split(" ")[0])
        #while len(i.split(" "))>0: try:
        #print(classifyingphraselist)
        hashmapbuilder=[] #list of original phrases
        for item in classifyingphraselist: 
            words=item.split(" ")
            postags=nltk.pos_tag([i for i in words if i]) # rid empty strings 
        #postags1=nltk.pos_tag(classifyingphraselist)
        #print(postags)
        #End debug 5 March 

        #Debug 12 March 
            
            if len(postags)>1:
                word1,word2=postags
                word1,postags1=word1
                word2,postags2=word2
                if (postags1=="NN" or postags1=="NNS") and (postags2!="NN" or postags2!="NNS") : 
                    finalword=pattern.en.singularize(word1)+" "+(word2)
                elif (postags2=="NN" or postags2=="NNS") and (postags1!="NN" or postags1!="NNS"): 
                    finalword=word1+" "+pattern.en.singularize(word2)
                elif (postags2=="NN" or postags2=="NNS") and (postags1=="NN" or postags1=="NNS"):
                    finalword=pattern.en.singularize(word1)+" "+pattern.en.singularize(word2)
                else: 
                    finalword=item 
                hashmapbuilder.append(item)

            else: 
                if len(postags)==1: 
                    word1=postags 
                    #print(postags)
                    for word1[0] in word1: 
                        #print(word1[0])
                        (word1,tag1)=(word1[0])
                    if postags1=="NNS": 
                        finalword=pattern.en.singularize(word1) 
                    else: 
                        finalword=word1
                else: 
                    print("error")
                    finalword=item
                hashmapbuilder.append(item)

            newlist.append(finalword) #except ValueError: pass; at this point, len(newlist)=len(hasmapbuilder)

            #print(newlist)

        assert len(newlist)==len(hashmapbuilder)
        self.removeduplicates(newlist) #returns sorted words 

        """
        #print(len(sortedwords))
        indexlist=[]
        for element in sortedwords:
            while True: 
                try: 
                    indexPos1=newlist.index(element,0) #search for item in list from indexPos to end of list
                    indexlist.append(indexPos1)
                    #indexPos1+=1 
                except ValueError:
                    #print(indexPos1)
                    break

        """

        #firstpass: want to find the words that are in sorted words and in newlist, sortedwordsbeing the smaller
        st=set(sortedwords) # note that some elements in hashmapbuilder are not in sortedwords
        indexlist1=[newlist.index(i) for i in st if i in newlist]
        #second pass: get all indexes of words selected and match with corresponding position in hashmapbuilder
        hashmapbuilder2=[]
        for i in indexlist1: 
            hashmapbuilder2.append(hashmapbuilder[i])
        #self.convertindex(classifyingphraselist,sortedwords) 
        # returns index list 

        #indexlist1=[]

        #indexPos1=0 
        """ 
        There might be some errors with convertindex 
        
        for element in hashmapbuilder2:
            while True: 
                try: 
                    indexPos1=classifyingphraselist.index(element,0) #search for item in list from indexPos to end of list
                    indexlist1.append(indexPos1)
                    #indexPos1+=1 
                except ValueError:
                    #print(indexPos1)
                    break
                    #indexPos1+=1 
                    #print("Value error")
                    #continue 
        #debug11 March :nothing wrong with fucntion, but rather inefficient solution 

        """
        #return indexlist
        st=set(hashmapbuilder2)
        indexlist1=[classifyingphraselist.index(i) for i in st if i in classifyingphraselist]
        print("length hashmap builder2")
        print(len(hashmapbuilder2))
        print("length, sortedwords")
        print(len(sortedwords))
        print(len(indexlist1))

        """ 
        It seems that error is with the lines below 
        """ 
        print(len(classifyingphraselist))
        print(len(classifyingtfidf))
        print(len(classifyingnum))
        print(len(classifyingimportancerank))


        for element in sortedwords: 
            newfinallist.append(element)

        for i in indexlist1: 
            #assert element.isdigit()
            #print(element)
            newclassifyingtfidf.append(classifyingtfidf[i])
            newclassifyingnum.append(classifyingnum[i])
            newclassifyingimportancerank.append(classifyingimportancerank[i])

        
        print(len(newfinallist))
        print(len(newclassifyingtfidf))
        print(len(newclassifyingnum))
        print(len(newclassifyingimportancerank))
        

        return newfinallist, newclassifyingtfidf, newclassifyingnum,newclassifyingimportancerank


class SOLUTIONS(MANIP): 


    def printsolutions(self): 

        self.outputfinal()

        a=zip(futures, tfidfutures, numutures, importancerankfutures)
        with open("futures6march.csv","w") as csvfile: 
            fwriter = csv.writer(csvfile)
            for i in a: 
                fwriter.writerow(i)
            csvfile.close()
        print("donewithfutureswords")

        b=zip(deleted,tfidfdeleted,numdeleted,importancerankfuturesdeleted)
        with open("deleted6march.csv","w") as csvfile: 
            fwriter = csv.writer(csvfile)
            for i in b: 
                fwriter.writerow(i)
            csvfile.close()
        print("donewithdeletedwords")

        
        c=zip(futuresngrams, tfidfdeletedngramsfutures, numdeletedngramsfutures, importancerankngramsfutures)     
        with open("futuresphrases6marchlout.csv","w") as csvfile: 
            fwriter = csv.writer(csvfile)
            for i in c: 
                fwriter.writerow(i)
            csvfile.close()
        print("donewithfuturesphrases")


        d=zip(deletedngrams,importancerankfuturesdeletedngrams,numdeletedngrams,tfidfdeletedngrams)
        with open("deletedphrases6march.csv","w") as csvfile: 
            fwriter = csv.writer(csvfile)
            for i in d: 
                fwriter.writerow(i)
            csvfile.close()
        print("donewithdeletedphrases")

        e=zip(newphraselist, newtfidf, newnum, newimportancerank)
        with open("finalout2.csv","w") as csvfile: 
            fwriter = csv.writer(csvfile)
            for i in e: 
                fwriter.writerow(i)
            csvfile.close()


                
x=SOLUTIONS() 
x.printsolutions()

##############################################################################################################################
##############################################################################################################################
##############################################################################################################################
##############################################################################################################################

"""
Due to potential indexing error, want to relabel everything in 3rdmarchsortfile. Then take intersection of 3marchsortfile and final2. 
Whereby final2 is a subset of 3rdmarchsortfile

"""


dir1="/Users/lucy/Desktop/assortedcodes/sort/3marchsorted.csv" #classified 
dir2="/Users/lucy/Desktop/assortedcodes/finalout2.csv" #classifying, needs correction 
dir3="/Users/lucy/Desktop/assortedcodes/sort/3marchsortfile.csv" #classifying 
originalcsv="/Users/lucy/Desktop/assortedcodes/sort/ngramrel.csv" #labeled perf words 


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


phraselist=[]
tfidf=[] 
num=[] 
importancerank=[]

with open(dir1,"r") as csvfile: #classified
    freader = csv.reader(csvfile)
    for row in freader: 
        phraselist.append(row[0])
        tfidf.append(row[1])
        num.append(row[2])
        importancerank.append(row[3])
    csvfile.close()

finallist=[]

with open(dir2,"r") as csvfile: #classified
    freader = csv.reader(csvfile)
    for row in freader: 
        finallist.append(row[0])
    csvfile.close()

classifyingphraselist=[]
classifyingtfidf=[] 
classifyingnum=[] 
classifyingimportancerank=[]
        
with open(dir3,"r") as csvfile: #classfying
    freader = csv.reader(csvfile)
    for row in freader: 
        classifyingphraselist.append(row[0])
        classifyingtfidf.append(row[1])
        classifyingnum.append(row[2])
        classifyingimportancerank.append(row[3])
    csvfile.close()

ampneghraselist=[]
ampnegclassifyingtfidf=[] 
ampnegclassifyingnum=[] 
ampnegclassifyingimportancerank=[]
        
with open(originalcsv,"r") as csvfile: #get amplifiers and negators 
    freader = csv.reader(csvfile)
    for row in freader: 
        ampneghraselist.append(row[0])
        ampnegclassifyingtfidf.append(row[1])
        ampnegclassifyingnum.append(row[2])
        ampnegclassifyingimportancerank.append(row[3])
    csvfile.close()

def convertindex(listcalled,iterable): 
    global indexlist
    indexlist=[]
    indexPos=0 
    while True: 
        try: 
            indexPos=listcalled.index(iterable,indexPos) #search for item in list from indexPos to end of list
            indexlist.append(indexPos)
            indexPos+=1 
        except ValueError:
            break 
    #debug11 March :nothing wrong with fucntion 
    print(len(indexlist))
    print("convertindex")
    return indexlist

def markallperf(): 
    convertindex(ampnegclassifyingnum,"x")
    performancewords=[]
    for i in indexlist: 
        performancewords.append(ampneghraselist[i])
    assert len(ampneghraselist)==len(ampnegclassifyingnum)
    for i in range(len(classifyingnum)): 
        for a in performancewords: 
            if len(classifyingphraselist[i].split(" "))>1:
                if a==classifyingphraselist[i].split(" ")[0] or a==classifyingphraselist[i].split(" ")[1]: 
                    if "x" not in classifyingnum[i]:
                        classifyingnum[i]=classifyingnum[i]+"x "
            else: 
                if a==classifyingnum[i]: 
                    if "x" not in classifyingnum[i]:
                        classifyingnum[i]=classifyingnum[i]+"x "
    return classifyingnum

def keep(): 
    markallperf()
    convertindex(ampnegclassifyingnum,"2")
    amplifierlist=[]
    for i in indexlist: 
        amplifierlist.append(ampneghraselist[i])
    for i in range(len(classifyingnum)): 
        for a in amplifierlist: 
            if "3" in classifyingnum[i]:
                classifyingnum[i]=re.sub(r'[3]', "ampneg x",classifyingnum[i])
            if "ampneg" not in classifyingnum[i]: 
                if len(classifyingphraselist[i].split(" "))>1:
                    if a==classifyingphraselist[i].split(" ")[0] or a==classifyingphraselist[i].split(" ")[1]: 
                        classifyingnum[i]=classifyingnum[i]+"ampneg"      
                else: 
                    if a==classifyingphraselist[i]: 
                        classifyingnum[i]=classifyingnum[i]+"ampneg"
    return classifyingnum

def change4tox(): 
    keep()
    convertindex(classifyingnum,"4")
    for item in indexlist: 
        classifyingnum[item]="x"
        classifyingnum[item]=re.sub(r'[4]', "x",classifyingnum[item])
    return classifyingnum

def intersection():
    change4tox()
    assert len(classifyingnum)==len(classifyingphraselist)
    st=set(finallist)

    global outphraselist
    global outclassifyingnum
    global outclassifyingtfidf
    global outclassifyingimportancerank
    global newwords

    indexlist=[classifyingphraselist.index(i) for i in st if i in classifyingphraselist]
    outphraselist=[classifyingphraselist[i] for i in indexlist]
    outclassifyingnum=[classifyingnum[i] for i in indexlist]
    outclassifyingtfidf=[classifyingtfidf[i] for i in indexlist]
    outclassifyingimportancerank=[classifyingimportancerank[i] for i in indexlist] 
    newwords=[item for item in finallist if item not in classifyingphraselist]

    return outphraselist,outclassifyingtfidf,outclassifyingnum,outclassifyingimportancerank

def solution():
    intersection()
    a=zip(classifyingphraselist, classifyingtfidf,classifyingnum, classifyingimportancerank)
    with open("debug1.csv","w") as csvfile: 
        fwriter = csv.writer(csvfile)
        for i in a: 
            fwriter.writerow(i)
        csvfile.close()
    print("donewithdebug1")

    b=zip(outphraselist,outclassifyingtfidf,outclassifyingnum,outclassifyingimportancerank)
    with open("final3.csv","w") as csvfile: 
        fwriter = csv.writer(csvfile)
        for i in b: 
            fwriter.writerow(i)
        for i in newwords: 
            fwriter.writerow([i])
        csvfile.close()
    print("donewithfinal3")

"""
    with open("newwords.csv","w") as csvfile: 
        fwriter=csv.write(csvfile)
        for i in newwords: 
            fwriter.writerow([i])
        csvfile.close() 
    
"""

solution()
