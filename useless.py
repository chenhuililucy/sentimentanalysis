

""" 

Purpose: get all useless words 

output useless words (ie. removed because containing a certain part) 

Dependencies: 

1. ridwords.csv 
2. intextfinal.csv 

Want to output csv with columns in the form of: unique word, percentage of words that Aaron got rid of: percentage of words Aaron kept, number of words Aaron kept, number of words Aaron got rid of


Output: 

1. uselesswords1.csv


""" 


import csv 
import os


list=[]

os.chdir("/Users/lucy/Desktop/sort")


with open("ridwords.csv","r") as csvfile: 
    freader = csv.reader(csvfile)
    for row in freader:
        if len(row[0].split(" "))>1:
            item1,item2=row[0].split(" ")
            list.append(item1) 
            list.append(item2) 
        elif len(row[0].split(" "))==1: 
            item1=row[0]
            list.append(item1) 


list.sort()

count=0
counts=[]
uniquewords=[]
for i in range(len(list)-1): 
    if list[i]==list[i+1]: #add 1 count to the same word occuring more than once 
        count+=1
    else: # if different word seen, dump list of words to uniquewords and counts 
        count+=1
        uniquewords.append(list[i]) 
        counts.append(count)
        count=0


dic1=dict(zip(uniquewords,counts)) 
print(dic1)

##################################################

list1=[]


with open("intextfinal.csv","r") as csvfile: 
    freader = csv.reader(csvfile)
    for row in freader:
        if len(row[0].split(" "))==2:
            item1,item2=row[0].split(" ")
            list1.append(item1) 
            list1.append(item2) 
        elif len(row[0].split(" "))==1: 
            item1=row[0]
            list1.append(item1) 

list1.sort()

count1=0
counts1=[]
uniquewords1=[]
for i in range(len(list1)-1): 
    if list1[i]==list1[i+1]:
        count1+=1
    else:
        uniquewords1.append(list1[i])
        counts1.append(count1)
        count1=0


dic2=dict(zip(uniquewords1,counts1)) 
print(dic2)

shared_items = {k: dic2[k] for k in dic1 if k in dic2}
ratio = {k:float(dic1[k])/(float(dic2[k])+0.0000000001) for k in dic1 if k in dic2}


thing1=[] 
thing2=[]

list1=[]
for k in dic1: 
    if k in dic2: 
        list1.append(dic2[k]) #the ones we kept 


list2=[]
for k in dic2: 
    if k in dic1: 
        list2.append(dic1[k]) #the ones we got rid of 


with open("uselesswords1.csv","w") as csvfile: 
    w = csv.writer(csvfile)
        
    for item in ratio.keys():
        thing1.append(item)
    for item1 in ratio.values():
        thing2.append(item1)
    for item in zip(thing1,thing2,list1,list2):
        w.writerow(item)






 