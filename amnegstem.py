

import csv 
import os 

os.chdir("/Users/lucy/Desktop/assortedcodes")
import nltk
from textblob import TextBlob


detect=False 

def grammarfix():
    finwordlist=[]
    with open("new2jan.csv", "r") as csvfile:
      freader = csv.reader(csvfile)
      for row in freader:
        wordlist=str(row[0]).split(" ")
    
        for word in wordlist: 
            finwordlist.append(word)
    
    with open("outnew2Jan.csv","w") as csvfile:
        fwriter=csv.writer(csvfile)
        for word in finwordlist: 
            fwriter.writerow([word])
        
            print(word)
        if detect:
            i=0
            for i in range(0,10):
                print("###########################")
                i+=1
            finallist=[w for (w, pos) in TextBlob(word).pos_tags if pos[0] != 'N']
            for word in finallist: 
                print(word)

def findword(): 
    with open("amnegstem2.csv", "r") as csvfile:
        row1=[]
        row2=[]
        freader = csv.reader(csvfile)
        for row in freader:
            row1.append(row[0])
        for row in freader:
            row2.append(row[1])
        
        list1=[item for item in row1 if item not in row2] 
        for item1 in list1: 
            print(item1)

 

#grammarfix()


def sortaaronswords():
    with open("aftersort.csv", "r") as csvfile: 
        freader = csv.reader(csvfile)
        originalword=[]
        first=[]
        second=[]
        tfidf=[]
        for row in freader:
            originalword.append(str(row[0]))
            wordlist=str(row[0]).split(" ")
            first.append(wordlist[0])
            tfidf.append(row[1])
            if len(wordlist) is int(2):
                second.append(wordlist[1])
            else: 
                second.append(".")
        
        p=zip(originalword,first,second,tfidf)    
    csvfile.close()

    with open("aaronintext.csv","w") as csvfile:
        fwriter = csv.writer(csvfile)
        for word in p: 
            fwriter.writerow(word)




sortaaronswords()  
    
    
    

    

            
            


        
        
