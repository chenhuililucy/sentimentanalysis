
import re 
import glob
import os
import csv
import nltk 
from nltk.tokenize import sent_tokenize, word_tokenize

DEBUG=True 

a=0 

corpus="/Users/lucy/Desktop/assortedcodes/assortedcodes/newdictestn/newdic/*.txt"
csv1="/Users/lucy/Desktop/builddic/sentence.csv"
csv2="/Users/lucy/Desktop/builddic/vector.csv"

posintlist=[]
negintlist=[]
posextlist=[]
negextlist=[]

filenamelist=[]

f_out2 = open(csv2, 'w')
wr2 = csv.writer(f_out2)

with open(csv1,"r"): 
    freader=csv.reader(csv1)
    for row in freader: 
        if row[0] is not "none": 
            if DEBUG:
                if a==2:
                    break 

            a=a+1 
            if a != 1: 
                everyfilename=row[0]
                filenamelist.append(everyfilename)
                posintlist.append(posint)
                negintlist.append(negint)
                posextlist.append(posext)
                negextlist.append(negext)

            posint=0
            negint=0
            posext=0 
            negext=0 
        if row[2]==1 and row[4]==1: 
            posint=posint+1
        if row[3]==1 and row[4]==1: 
            negint=negint+1
        if row[2]==1 and row[5]==1:
            posext=posext+1 
        if row[3]==1 and row[5]==1:
            negext=negext+1
        else:
            if row[2]==1 and row[4]==1: 
                posint=posint+1
            if row[3]==1 and row[4]==1: 
                negint=negint+1
            if row[2]==1 and row[5]==1: 
                posext=posext+1 
            if row[3]==1 and row[5]==1:
                negext=negext+1
            
        
p=zip(filenamelist,posintlist,negintlist,posextlist,negextlist) 
for row in p:
    wr2.writerow(row)

        


