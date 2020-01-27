

"""
To output phrases that have been deleted in the marked fields 
"""

import csv 
import os

# new file 
list1=[]
# original file 
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

with open("ridwords.csv","w",encoding="utf-8", errors="ignore") as csvfile: 
    fwriter=csv.writer(csvfile)
    for word in listrid: 
        fwriter.writerow([word])
    csvfile.close()

