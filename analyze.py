

"""
To output phrases that have been deleted in the marked fields 
"""
import csv 
import os
import itertools

# original file 
list1=[]
# new file 
list2=[]
#deleted words
listrid=[]


os.chdir("/Users/lucy/Desktop/sort")

with open("original.csv", "r",encoding="utf-8", errors="ignore") as csvfile: 
    freader = csv.reader(csvfile)
    for row in freader:
        wordlist=str(row[0])
        list1.append(wordlist)
    csvfile.close()


with open("intextfinal.csv", "r",encoding="utf-8", errors="ignore") as csvfile: 
    freader = csv.reader(csvfile)
    for row in freader:
        wordlist=str(row[0])
        list2.append(wordlist)
    csvfile.close()

# print(list1)
# print(list2)

print(len(list1))
print(len(list2))
listrid= list(set(list1) - set(list2))
"""
optimal performance solution 
see discussion in https://stackoverflow.com/questions/3462143/get-difference-between-two-lists
"""

#print(listrid)

listrid.sort()
with open("ridwords.csv","w",encoding="utf-8", errors="ignore") as csvfile: 
    fwriter=csv.writer(csvfile)
    for word in listrid: 
        fwriter.writerow([word])
    csvfile.close()



# find how many % of a given phrase given a starting word are deleted 


count=[]
elements=[] 
eli1=[]


# for element in new file 
for element in list2:
    if len(element.split(" "))==2: 
        el1,el2=element.split(" ")
    else: 
        el1=element
   

    eli1.append(el1)

eli1.sort()

a=1
for n in range(0,len(eli1)): 
    if n<len(list2)-1:
        second=eli1[n+1]
        first=eli1[n]
        if second==first:
            a+=1
        else: 
            count.append(a)
            elements.append(first)
            a=1


dic1=dict(zip(elements,count))


#dic1={elements[i]:count[i] for i in range(len(count))}



count1=[]
elements1=[] 
eli2=[]

for element in list1:
    if len(element.split(" "))==2: 
        el1,el2=element.split(" ")
    else: 
        el1=element
   

    eli2.append(el1)

#print(eli2)

eli2.sort()


a=1
for n in range(0,len(eli2)): 
    if n<len(eli2)-1:
        second=eli2[n+1]
        #print(second)
        first=eli2[n]
        #print(first)
        if second==first:
            a+=1
        else: 
            count1.append(a)
            elements1.append(first)
            a=1


dic2=dict(zip(elements1,count1))

#dic2=[{elements[i]:count[i] for i in range(len(count))}]

print(dic2)

shared_items = {k: dic2[k] for k in dic1 if k in dic2}


list=[] 
for k in dic1:
    if k in dic2: 
        list.append(dic1[k])

print(list)


list1=[]
for k in dic1: 
    if k in dic2: 
        list1.append(dic2[k])


ratio = {k:float(dic1[k])/(float(dic2[k])+0.0000000001) for k in dic1 if k in dic2}



thing1=[]
thing2=[]

with open('finaloutput.csv','w') as f:
    w = csv.writer(f)
    
    for item in ratio.keys():
        thing1.append(item)
    for item1 in ratio.values():
        thing2.append(item1)

    for item in zip(thing1,thing2,list,list1):
        w.writerow(item)










            







    