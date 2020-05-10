






import csv
import nltk
import pattern
from pattern.text.en import singularize
from pattern.text.en import pluralize
from pattern.en import pluralize, singularize, conjugate
from pattern.en import conjugate, lemma, lexeme,PRESENT,SG
import os
import re
import operator

#modify!!!!
src= "/Users/lucy/Desktop/assortedcodes/afile(1).csv"

"""
References
dict1 = {"a":0.6, "b":0.3, "c":0.9, "d":1.2, "e":0.2}
dict2 = {"a":1.4, "b":7.7, "c":9.0, "d":2.5, "e":2.0}
k1 = sorted(dict1, key=dict1.get)
k2 = sorted(dict2, key=dict2.get)
diffs = dict((k, k2.index(k) - k1.index(k)) for k in dict1)
"""


classifyingphraselist=[]
l1=[]
l2=[]
l3=[] 
l4=[]

dic={}
with open(src,"r", encoding="utf-8", errors="ignore") as f: 
    r=csv.reader(f)
    for row in r: 
        if len(row[0].split(" "))==2:
            if row[0].split(" ")[0] not in dic: 
                dic.update({row[0].split(" ")[0]:1})
            else:
                dic[row[0].split(" ")[0]]+=1 
            if row[0].split(" ")[1] not in dic: 
                dic.update({row[0].split(" ")[1]:1})
            else:
                dic[row[0].split(" ")[1]]+=1 
        else: 
            if row[0].split(" ")[0] not in dic: 
                dic.update({row[0].split(" ")[0]:1})
            else:
                dic[row[0].split(" ")[0]]+=1 

    f.close() 

n = sorted(dic.items(), key=operator.itemgetter(1))
#n=sorted(dic,key=dic.get)
l=[]

for k, value in dic.items():
    print(k)
    l.append(k)

#for k in n.keys(): 
   # l.append(k)


l1=[]
l2=[] 
l3=[]
l4=[]
i=0
tockens=set()


while i<len(l):
    with open(src,"r", encoding="utf-8", errors="ignore") as f: 
        r=csv.reader(f) 
        a=0
        for row in r: 
            a+=1
            if len(row[0].split(" "))>1:
                if row[0].split(" ")[0]==l[i]: 
                    if a not in tockens:
                        l1.append(row[0])
                        l2.append(row[1])
                        l3.append(row[2])
                        if len(row)>3:
                            l4.append(row[3])
                        tockens.add(a)
                elif row[0].split(" ")[1]==l[i]: 
                    if a not in tockens:
                        l1.append(row[0])
                        l2.append(row[1])
                        l3.append(row[2])
                        if len(row)>3:
                            l4.append(row[3])
                        tockens.add(a)

            elif len(row[0].split(" "))==1: 
                if row[0].split(" ")[0]==l[i]: 
                    if a not in tockens:
                        l1.append(row[0])
                        l2.append(row[1])
                        l3.append(row[2])
                        if len(row)>3:
                            l4.append(row[3])
                        tockens.add(a)
    i+=1


fin= "/Users/lucy/Desktop/assortedcodes/afile(1)final.csv"
z=zip(l1,l2,l3,l4)
with open(fin,"w", encoding="utf-8", errors="ignore") as f: 
    fwriter = csv.writer(csvfile)
    for i in z:
        fwriter.writerow(i)
    csvfile.close()



