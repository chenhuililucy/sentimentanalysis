""" 

Clean useless words 
Rid the corpus of any useless words, rid currencies, rid numbers 

""" 



""" 

Remove currencies

""" 



import csv
import pandas as pd 
import os

import pattern
from pattern.text.en import singularize
from pattern.text.en import pluralize
from pattern.en import pluralize, singularize
from pattern.en import conjugate, lemma, lexeme,PRESENT,SG
import random


list=["total", "totaled", "percent", "pared", "parcel", "paperwork", "papers", "paper", "net"]

os.chdir("/Users/lucy/Desktop/sort")
def removecurrencies(): 
    global listcur
    listcur=[]
    with open("currencies1.csv", "r") as csvfile: #read in currency list csv 
        freader = csv.reader(csvfile)
        for row in freader:
            currency=row[0].split(' ')[-1]
            listcur.append(currency) 
            listcur.append(pattern.en.pluralize(currency))

        csvfile.close()

list1=[] 
list2=[] 
list3=[] 
list4=[] 

removecurrencies()

for i in list:
    listcur.append(pattern.en.pluralize(i))
    listcur.append(pattern.en.singularize(i))

    listcur.append(i) 


def removenumbers():
     with open("numbers1.csv", "r") as csvfile: #read in currency list csv 
        freader = csv.reader(csvfile)
        for row in freader:
            currency=row[0].strip().lower()
            listcur.append(currency) 
            listcur.append(pattern.en.pluralize(currency))

        csvfile.close()

removenumbers()



    

with open("25janprogress1.csv", "r") as csvfile:
    freader = csv.reader(csvfile)
    for row in freader:

        if str(row[0]).split(" ")[0] in listcur: 
            pass
            #print(str(row[0]).split(" ")[0])

        elif len(str(row[0]).split(" "))==2:
            if str(row[0]).split(" ")[1] in listcur: 
                pass
                #print(str(row[0]).split(" ")[1])
            else: 
                list1.append(row[0]) 
                list2.append(row[1]) 
                list3.append(row[2])
                #list4.append(row[3])
            
        else: 

            list1.append(row[0]) 
            list2.append(row[1]) 
            list3.append(row[2])
            #list4.append(row[3])
    csvfile.close()

p=zip(list1,list2,list3)

with open("27janprogress.csv", "w") as csvfile:

    fwriter = csv.writer(csvfile)
    for i in p: 
        fwriter.writerow(i)


                
