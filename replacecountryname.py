

import csv 
import os 
import re 
import pattern
from pattern.text.en import singularize
from pattern.text.en import pluralize
from pattern.en import pluralize, singularize
from pattern.en import conjugate, lemma, lexeme,PRESENT,SG
import random



os.chdir("/Users/lucy/Desktop/sort")

uselesswordsfile="uselesswords2.csv"
countrynamefile="stopwordscountrynames.csv"
stopwordsdates="stopwordsdates.csv"

def getriduselesswords(): 

    list=[]
    with open(uselesswordsfile, "r") as csvfile: #read in useless words csv 
        freader = csv.reader(csvfile)
        for row in freader:
            if str(row[4])=="x": 
                list.append(row[0]) 

        csvfile.close()


    #print(list)


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

    with open("finalv3.csv", "w") as csvfile:

        fwriter = csv.writer(csvfile)
        for i in p: 
            fwriter.writerow(i)


getriduselesswords()

########################################################################


def getridofcountrynames(): 

    countrynames=[]
    with open(countrynamefile,"r") as csvfile: 

        freader = csv.reader(csvfile)
        for row in freader:
            countrynames.append(row[0].lower())
        
        csvfile.close()


    list1=[] 
    list2=[] 
    list3=[] 
    list4=[] 

    with open('finalv3.csv',"r") as csvfile: 

        freader = csv.reader(csvfile)
        for row in freader:
            
            i=str(row[0]).split(" ")[0] 
            if len(row[0].split(" "))>1:
                epsilon=str(row[0]).split(" ")[1]
            else:
                epsilon=None 
            if i in countrynames:
                if epsilon in countrynames: 
                    list1.append("* *")
                    list2.append(row[1]) 
                    list3.append(row[2])
                    list4.append(row[3])
            

                else: 
                    if len(str(row[0]).split(" "))>1: 
                        list1.append("*"+str(row[0]).split(" ")[1]) 
                        list2.append(row[1]) 
                        list3.append(row[2])
                        list4.append(row[3])
                
                    elif len(str(row[0]).split(" "))==1: 
                        list1.append("*")
                        list2.append(row[1]) 
                        list3.append(row[2])
                        list4.append(row[3])




                

                #i.replace(countrynames, '*')

                #words = [w.replace(str(row[0]).split(" ")[0], '*') for w in words]

                
                #print(str(row[0]).split(" ")[0])

            elif len(str(row[0]).split(" "))==2:
                if str(row[0]).split(" ")[1] in countrynames: 
                    list1.append(str(row[0]).split(" ")[0]+"*")
                    
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


    with open('finalv4.csv','w') as f:
        w = csv.writer(f)

        for item in p:
            w.writerow(item)
        f.close()


getridofcountrynames()

############################################


def getridoftime():

    time=[]
    with open(stopwordsdates,"r", encoding="utf-8", errors="ignore") as csvfile: 

        freader = csv.reader(csvfile)
        for row in freader:
            time.append(row[0].lower())
            time.append(pattern.en.pluralize(row[0])) 
        
        csvfile.close()


    list1=[] 
    list2=[] 
    list3=[] 
    list4=[] 

    with open('finalv4.csv',"r") as csvfile: 

        freader = csv.reader(csvfile)
        for row in freader:
            
            i=str(row[0]).split(" ")[0] 
            if len(row[0].split(" "))>1:
                epsilon=str(row[0]).split(" ")[1]
            else:
                epsilon=None 
            if i in time:
                if epsilon in time: 
                    list1.append("@ @")
                    list2.append(row[1]) 
                    list3.append(row[2])
                    list4.append(row[3])
            

                else: 
                    if len(str(row[0]).split(" "))>1: 
                        list1.append("@"+str(row[0]).split(" ")[1]) 
                        list2.append(row[1]) 
                        list3.append(row[2])
                        list4.append(row[3])
                
                    elif len(str(row[0]).split(" "))==1: 
                        list1.append("@")
                        list2.append(row[1]) 
                        list3.append(row[2])
                        list4.append(row[3])




            
            elif len(str(row[0]).split(" "))==2:
                if str(row[0]).split(" ")[1] in time: 
                    list1.append(str(row[0]).split(" ")[0]+"@")
                    
     
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


    with open('finalv6.csv','w') as f:
        w = csv.writer(f)

        for item in p:
            w.writerow(item)
        f.close()

getridoftime()



