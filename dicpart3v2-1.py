
'''
This piece of code, together with dicpart1.py, dicpart2.py are used to generate weights of documents in four categories: posint,negint,posext,negext

dicpart 3 will take sentences.csv written by dicpart2 and add together the number of sentences in one file that are in the categories posint,negint,posext,negext

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


a=0 

f_out2 = open(csv2, 'w')
wr2 = csv.writer(f_out2)

with open(csv1,"r") as csvfile: 
    freader=csv.reader(csvfile)
    for row in freader:
        if "none" not in row[0] and "lucy" in row[0]: 
            print(row[0])
            everyfilename=row[0]
            filenamelist.append(everyfilename)
            a=a+1
            
            if a > 1: #if more than one file has been loaded and the next line is the actual filename 
                posintlist.append(posint)
                print(posintlist)
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
