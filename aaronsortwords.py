

"""
Section 1: Check if existing int/ext word list contains useless words 
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


os.chdir("/Users/lucy/Desktop/sort")

list=[]
with open("uselesswords1.csv", "r") as csvfile: #read in useless words csv 
    freader = csv.reader(csvfile)
    for row in freader:
        if str(row[4])=="x": 
            list.append(row[0]) 

    csvfile.close()


print(list)


list1=[] 
list2=[] 
list3=[] 
list4=[] 

with open("final2.csv", "r") as csvfile: #read in int/ext word list 
    freader = csv.reader(csvfile)
    for row in freader:

        if str(row[0]).split(" ")[0] in list: 
            pass
            #print(str(row[0]).split(" ")[0])

        elif len(str(row[0]).split(" "))==2:
            if str(row[0]).split(" ")[1] in list: 
                pass
                #print(str(row[0]).split(" ")[1])
            else: 
                list1.append(row[0]) 
                list2.append(row[1]) 
                list3.append(row[2])
                list4.append(row[3])
            
        else: 

            list1.append(row[0]) 
            list2.append(row[1]) 
            list3.append(row[2])
            list4.append(row[3])
    csvfile.close()

p=zip(list1,list2,list3,list4)

with open("final3.csv", "w") as csvfile:

    fwriter = csv.writer(csvfile)
    for i in p: 
        fwriter.writerow(i)



######################


""" 

Remove currencies

""" 



os.chdir("/Users/lucy/Desktop/sort")
def removecurrencies(): 
    global listcur
    listcur=[]
    with open("currencies1.csv", "r") as csvfile: #read in currency list csv 
        freader = csv.reader(csvfile)
        for row in freader:
            currency=row[1].split(' ')[-1]
            listcur.append(currency) 
            listcur.append(pattern.en.pluralize(currency))

        csvfile.close()

list1=[] 
list2=[] 
list3=[] 
list4=[] 

removecurrencies()


with open("final3.csv", "r") as csvfile:
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
                list4.append(row[3])
            
        else: 

            list1.append(row[0]) 
            list2.append(row[1]) 
            list3.append(row[2])
            list4.append(row[3])
    csvfile.close()

p=zip(list1,list2,list3,list4)

with open("final4.csv", "w") as csvfile:

    fwriter = csv.writer(csvfile)
    for i in p: 
        fwriter.writerow(i)


                

