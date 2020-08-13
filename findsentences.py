
import re 
import glob
import os
import csv
import nltk 
from collections import defaultdict
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import ngrams

#Change your directory to one which contains all files
os.chdir("/Users/lucy/Desktop/assortedcodes/builddic")

#The corpus is the main folder that contains all your MD&A files 
corpus="/Users/lucy/Desktop/others/newdictestn/newdic/*.txt"

#The corpus is the main folder that contains all your MD&A files 
unsure="/Users/lucy/Desktop/assortedcodes/AA2ndpass.csv"

d=defaultdict(list)

idex=0
with open(unsure,"r") as f: 
    records=csv.reader(f)
    for row in records:
        #print(row)
        idex+=1
        index=str(row[0])
        #print(index)
        #if "?" in index: 
        if len(row[1].lower().split(" "))>1:
            if row[1].lower().split(" ")[0] in d:
                d[row[1].lower().split(" ")[0]].append([row[1].lower().split(" ")[1], idex])
            else: 
                d[row[1].lower().split(" ")[0]]=[[row[1].lower().split(" ")[1], idex]]
        else: 
            if row[1].lower().split(" ")[0] in d:
                d[row[1].lower().split(" ")[0]].append(["",idex])
            else: 
                d[row[1].lower().split(" ")[0]]=[["",idex]]
            
            #d.add(row[0].lower().split(" "))
    maximum=idex
    f.close()

print(d)

filenum=0
l=["none"]*maximum
for files in glob.glob(corpus):
    year=files[files.find("-")+1:files.find(".")]
    cik=files[:files.find("-")]
    with open(files) as f: 
        filenum+=1
        content = f.read()
        text1=content.lower()
       
        totalnumberofsent=0        
        re.sub("\n","",content)
        sent = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s|[A-Z].*)',content)
        posperfcnt=0 
        negperfcnt=0
        doubleneg=0
        
        sentno=0
        for sentences in sent: # ISSUE: need to identify individual words, modify to match regex words
            #print(sentences)
            ww=[]
            #print(sentences)
            for r in word_tokenize(sentences): 
                if r.isalpha(): 
                    ww.append(r)

            for i in range(len(ww)-3): 
                y=False
                if ww[i] in d:

                    if any(ww[i+1] in a for a in d[ww[i]]):
                        #indexlist=(ww[i+1] in a for a in d[ww[i]])
                        #indexed_sevens=enumerate(indexlist)
                        #seven_indexes = (index for index, value in indexed_sevens if value)
                        #index=d[ww[i]].index(ww[i+1])
                        num=-1
                        for a,b in d[ww[i]]: 
                            num+=1
                            if a==ww[i+1]: 
                                index=num
                                break
                        try:
                            if l[d[ww[i]][index][1]]=="none":
                                l[d[ww[i]][index][1]]=[ww[i],ww[i+1],ww]
                            else: 
                                l[d[ww[i]][index][1]].append([ww[i],ww[i+1],ww])
                        except IndexError: 
                            print(index)
                        y=True

                    if any(ww[i+2] in a for a in d[ww[i]]) and not y:

                        num=-1
                        for a,b in d[ww[i]]: 
                            num+=1
                            if a==ww[i+2]: 
                                index=num
                                break
                        #index=d[ww[i]].index(ww[i+2])
                        try:
                            if l[d[ww[i]][index][1]]=="none":
                                l[d[ww[i]][index][1]]=[ww[i],ww[i+2],ww]
                            else: 
                                l[d[ww[i]][index][1]].append([ww[i],ww[i+2],ww])

                        except IndexError: 
                            print(index)
                        y=True 

                    if any(ww[i+3] in a for a in d[ww[i]]) and not y:

                        num=-1
                        for a,b in d[ww[i]]: 
                            num+=1
                            if a==ww[i+3]: 
                                index=num
                                break               
                        #index=d[ww[i]].index(ww[i+3])
                        try:
                            if l[d[ww[i]][index][1]]=="none":
                                l[d[ww[i]][index][1]]=[ww[i],ww[i+3],ww]
                            else: 
                                l[d[ww[i]][index][1]].append([ww[i],ww[i+3],ww])
                        except IndexError: 
                            print(index)
                            #print(d[ww[i]][index])
                        y=True 
                            
                        #print(ww[i])
                        #print(ww[i+1])
                        #print(sentences)

                #else: 
                    #print(".")

        #if filenum==10000:
            #break 


csv2="/Users/lucy/Desktop/assortedcodes/example.csv"
f_out2 = open(csv2, 'w')
wr2 = csv.writer(f_out2)
for r in l:
    wr2.writerow(r)

