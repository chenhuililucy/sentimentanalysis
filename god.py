""" 
29 Jan
Aim: realign misaligned tfidf and phrases 
""" 

#Too time consuming, used Vlookup instead



import csv 
import os
import itertools

"""

# original file 
list1=[]
# new file 
list2=[]
#deleted words
listrid=[]

"""

originalcsv="intextfinal.csv"
newcsv="asofjan30.csv"

os.chdir("/Users/lucy/Desktop/sort")

row0=[] 
row1=[]
with open(originalcsv, "r",encoding="utf-8", errors="ignore") as csvfile: 
    freader = csv.reader(csvfile)
    for row in freader: 
        row0.append(row[0])
        row1.append(row[1])
    
        #print(mydict)
    csvfile.close()
mydict = zip(row0,row1)


phraselist=[]
with open(newcsv, "r",encoding="utf-8", errors="ignore") as csvfile: 
    freader = csv.reader(csvfile)
    for row in freader:
        phraselist.append(str(row[0]))
    csvfile.close()

#print(phraselist)
phraselist.sort()

"""

#value=[]
for i in phraselist: 
    value=[v for k,v in mydict.items() if k == i]

    #value.append(dict.get(i))

"""


value=[]
for key,values in mydict:
    #print(key)
    #print(i)
    for i in phraselist: 
        #print(i)
        #print(key)
        #print(values)
        if str(key) == str(i):
            #print("y")
            value.append(values)
            
#print(value)

#print(mydict.items())


p=zip(phraselist,value)


with open('finaloutput-111.csv','w') as f:
    w = csv.writer(f)

    for item in p:
        w.writerow(item)

#pd_df = pd.read_csv(originalcsv)
#sp_df = spark.createDataFrame(pd_df, schema=schema)

#sp_df.show()

#myrdd = sc.textFile(originalcsv).map(lambda line: line.split(","))



