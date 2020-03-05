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
        self.convertindex(classifyingnum,"x")
        performancewords=[]
        for i in indexlist: 
            performancewords.append(classifyingphraselist[i])
        assert len(classifyingphraselist)==len(classifyingnum)
        for i in range(len(classifyingnum)): 
            for a in performancewords: 
                #for b in classifyingphraselist: 
                if a==classifyingphraselist[i].split(" ")[0] or a==classifyingphraselist[i].split(" ")[1]: 
                    classifyingnum[i].append("x")
        return classifyingnum 

    def keep(self): 
        #self.read()
        #self.change4tox()
        #self.convertindex()
        self.markallperf()
        amplifierlist=[]
        for i in indexlist: 
            amplifierlist.append(ampneghraselist[i])

        for i in range(len(classifyingnum)): 
            for a in amplifierlist: 
                #for b in classifyingphraselist: 
                if a==classifyingphraselist[i].split(" ")[0] or a==classifyingphraselist[i].split(" ")[1]: 
                    classifyingnum[i].append("ampneg")

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

        for a in range(len(newlist)):
            for i in futures: 
                if newlist[a].split(" ")[0]==i or newlist[a].split(" ")[1]==i: 
                    deletedngrams.append(newlist[a])
                    importancerankfuturesdeletedngrams.append(newclassifyingimportancerank[a])
                    numdeletedngrams.append(newclassifyingnum[a])
                    tfidfdeletedngrams.append(newclassifyingtfidf[a])

        return futures, tfidfutures, numutures, importancerankfutures

    
    def removeduplicates(self,anylist): 
        global sortedwords 
        dic={}
        for i in len(range(anylist)): 
            dic.append(phranylistaselist[i]) 
            dic[anylist[i]]+=1 
        sortedwords=[k for k in dic]
        convertindex(anylist,sortedwords)
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
        importancerankfutures=[]
        for i in indexlist:
            deleted.append(phraselist[i].split(" ")[1]) 
            tfidfdeleted.append(tfidf[i]) 
            numdeleted.append(num[i])
            importancerankfuturesdeleted.append(importancerank[i])

        global deletedngrams
        global tfidfdeletedngrams
        global numdeletedngrams
        global importancerankfuturesdeletedngrams

        deletedngrams=[]
        tfidfdeletedngrams=[]
        numdeletedngrams=[]
        importancerankfuturesdeletedngrams=[]
        for a in range(len(newlist)):
            for i in deleted: 
                if newlist[a].split(" ")[0]==i or newlist[a].split(" ")[1]==i: 
                    deletedngrams.append(newlist[a])
                    importancerankfuturesdeletedngrams.append(newclassifyingimportancerank[a])
                    numdeletedngrams.append(newclassifyingnum[a])
                    tfidfdeletedngrams.append(newclassifyingtfidf[a])

        return deleted,tfidfdeleted,numdeleted,importancerankfuturesdeleted,deletedngrams,importancerankfuturesdeletedngrams,numdeletedngrams,tfidfdeletedngrams


    def outputfinal(self): 
        """ 
        Not done 
        """
        self.ridplurals() 
        self.delete()
        self.getfuture()

        reverse_concatenatedlist=deleted+futures
        newphraselist=set(phraselist).symmetric_difference((deleted+futures))
        newtfidf=set(tfidf).symmetric_difference(tfidfdeleted+tfidfutures)
        newnum=set(num).addsymmetric_difference(numdeleted+numutures)
        newimportancerank=set(importancerank).symmetric_difference(importancerankfutures+importancerankfutures)
        return newphraselist, newtfidf, newnum, newimportancerank


    def ridplurals(self): 
        global newlist
        global newclassifyingtfidf
        global newclassifyingnum
        global newclassifyingimportancerank
        self.keep()
        newlist=[]
        #Begin debug 5 March 
        #for i in classifyingphraselist:
            #i=list(i) 
            #print(i)
            #print(i.split(" ")[0])
        #while len(i.split(" "))>0: try:
        #print(classifyingphraselist)
        for item in classifyingphraselist: 
            words=item.split(" ")
            postags=nltk.pos_tag([i for i in words if i]) # rid empty strings 
        #postags1=nltk.pos_tag(classifyingphraselist)
        #print(postags)
        #End debug 5 March 
            if len(postags)>1: 
                word1,word2=postags
                word1,postags1=word1
                word2,postags2=word2
                if postags1=="NN" and postags2!="NN": 
                    finalword=pattern.en.singularize(word1)+" "+(word2)
                elif postags2=="NN" and postags1!="NN": 
                    finalword=word1+" "+pattern.en.singularize(word2)
                elif postags2=="NN" and postags1=="NN": 
                    finalword=pattern.en.singularize(word1)+" "+pattern.en.singularize(word2)
                else: 
                    finalword=item 
            else: 
                if len(postags)==1: 
                    word1=postags 
                    #print(postags)
                    for word1[0] in word1: 
                        #print(word1[0])
                    (word1,tag1)=(word1[0])
                    if postags1=="NN": 
                        finalword=pattern.en.singularize(word1) 
                    else: 
                        finalword=word1
        newlist.append(finalword) #except ValueError: pass 
        removeduplicates(newlist)
        convertindex(classifyingphraselist,sortedwords)
        newclassifyingtfidf=[classifyingtfidf[element] for element in indexlist]
        newclassifyingnum=[classifyingnum[element] for element in indexlist]
        newclassifyingimportancerank=[classifyingimportancerank[element] for element in indexlist]
        return newlist, newclassifyingtfidf, newclassifyingnum,newclassifyingimportancerank


class SOLUTIONS(MANIP): 


    def printsolutions(self): 
        self.getfuture()
        self.ridplurals()
        p=zip(futures, tfidfutures, numutures, importancerankfutures)
        with open("futures4march.csv","w") as csvfile: 
            fwriter = csv.writer(csvfile)
            for i in p: 
                fwriter.writerow(i)
            csvfile.close()
        print("done")
        with open("deleted4march.csv","w") as csvfile: 
            fwriter = csv.writer(csvfile)
            for i in a: 
                fwriter.writerow(i)
            csvfile.close()
        with open("finalout.csv","w") as csvfile: 
            fwriter = csv.writer(csvfile)
            for i in a: 
                fwriter.writerow(i)
            csvfile.close()


                
x=SOLUTIONS() 
x.printsolutions()