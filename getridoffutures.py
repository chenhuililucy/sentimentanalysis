""" 

Aimed at getting rid of words referring to future performance
Outputs 


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
inputfile="27janprogress.csv"
outputfilefuture="future.csv"
outputfilepast="past.csv"
outputfileseasons="seasons.csv" 
finaloutputfile="27cleaned.csv"




futurelist=["future","next","coming","anticipated","anticipate", "forthcoming", "eventual", "imminent", "impending", "prospective", "ultimate", "approaching", "unfolding"]
pastlist=["former","previous","past","historical"]
seasonalitylist=["season","seasons","spring","summer","autumn","winter"] 



futurephrase=[]
pastphrase=[]
seasonsphrase=[]
list11=[] 
list21=[] 
list31=[] 
list12=[] 
list22=[] 
list32=[] 
list13=[] 
list23=[] 
list33=[] 
list01=[]
list02=[] 
list03=[]


            #################################################


ist11=[] 
ist21=[] 
ist31=[] 
ist12=[] 
ist22=[] 
ist32=[] 
ist31=[] 
ist23=[] 
ist33=[] 




with open(inputfile, "r") as csvfile:
    freader = csv.reader(csvfile)
    for row in freader:
        for item in futurelist: 
            if item in str(row[0]).split(): 
                futurephrase.append(str(row[0]))
                list01.append(row[0])
                list11.append(row[1])
                list21.append(row[2])
                #list31.append(row[3])

            # else:

            #     ist11.append(row[1])
            #     ist21.append(row[2])
            #     ist31.append(row[3])


                
    csvfile.close()

a=zip(list01, list11,list21) #list of futures phrase 


with open(inputfile, "r") as csvfile:
    freader = csv.reader(csvfile)
    for row in freader:
        for item in pastlist: 
            if item in str(row[0]): 
                pastphrase.append(str(row[0]))
                list02.append(row[0])
                list12.append(row[1])
                list22.append(row[2])
                #list32.append(row[3])



            # else:

            #     ist11.append(row[1])
            #     ist21.append(row[2])
            #     ist31.append(row[3])

                
    csvfile.close()



c=zip(list02, list12,list22)

with open(inputfile, "r") as csvfile:
    freader = csv.reader(csvfile)
    for row in freader:
        for item in seasonalitylist: 
            if item in str(row[0]): 
                seasonsphrase.append(str(row[0]))
                list03.append(row[0])
                list13.append(row[1])
                list23.append(row[2])
                #list33.append(row[3])

            

            # else:

            #     ist11.append(row[1])
            #     ist21.append(row[2])
            #     ist31.append(row[3])



    csvfile.close()

e=zip(list03, list13,list23)



with open(outputfilefuture, "w") as csvfile:

    fwriter = csv.writer(csvfile)
    for i in a: 
        fwriter.writerow(i)

with open(outputfilepast, "w") as csvfile:

    fwriter = csv.writer(csvfile)
    for i in c: 
        fwriter.writerow(i)


with open(outputfileseasons, "w") as csvfile:

    fwriter = csv.writer(csvfile)
    for i in e: 
        fwriter.writerow(i)



################################

""" 

Get rid of these words in the main file 

""" 

ridlist=[]
list1=[] 
list2=[] 
list3=[] 
list4=[] 

with open(outputfilefuture, "r") as csvfile:

    freader = csv.reader(csvfile)
    for row in freader:
        ridlist.append(row[0])
    csvfile.close()
        

with open(outputfilepast, "r") as csvfile:

    freader = csv.reader(csvfile)
    for row in freader:
        ridlist.append(row[0])
    csvfile.close()

        

with open(outputfileseasons, "r") as csvfile:

    freader = csv.reader(csvfile)
    for row in freader:
        ridlist.append(row[0])
    csvfile.close()

        

with open(inputfile, "r") as csvfile:

    
    freader = csv.reader(csvfile)
    for row in freader:
        if str(row[0]) not in ridlist:
            list1.append(row[0]) 
            list2.append(row[1]) 
            list3.append(row[2])
            #list4.append(row[3])
    csvfile.close()

z=zip(list1,list2,list3)
    
with open(finaloutputfile, "w") as csvfile: 
    fwriter = csv.writer(csvfile)
    for item in z: 
        fwriter.writerow(item)

        






