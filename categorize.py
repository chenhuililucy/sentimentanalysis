

import csv
from collections import defaultdict

csv1="/Users/lichenhuilucy/Desktop/dictionaries/intcat1.csv"
csv2="/Users/lichenhuilucy/Desktop/dictionaries/intcat2.csv"
csv3="/Users/lichenhuilucy/Desktop/dictionaries/intcat3.csv"
csv4="/Users/lichenhuilucy/Desktop/dictionaries/intcat4.csv"
csv5="/Users/lichenhuilucy/Desktop/dictionaries/extcat1.csv"
csv6="/Users/lichenhuilucy/Desktop/dictionaries/extcat2.csv"
intc="/Users/lichenhuilucy/Desktop/dictionaries/internalfinal.csv"
extc="/Users/lichenhuilucy/Desktop/dictionaries/externalfinal.csv"


l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]

s=set()
with open(csv1,"r") as csvfile: 
    freader=csv.reader(csvfile)
    for row in freader:
        s.add(str(row[0].strip().lower()))

print(s)

s2=set()

with open(csv2,"r") as csvfile: 
    freader=csv.reader(csvfile)
    for row in freader:
        s2.add(str(row[0].strip().lower()))


s3=set()

with open(csv3,"r") as csvfile: 
    freader=csv.reader(csvfile)
    for row in freader:
        s3.add(str(row[0].strip().lower()))


s4=set()

with open(csv4,"r") as csvfile: 
    freader=csv.reader(csvfile)
    for row in freader:
        s4.add(str(row[0].strip().lower()))



s5=set()

with open(csv5,"r") as csvfile: 
    freader=csv.reader(csvfile)
    for row in freader:
        s5.add(str(row[0].strip().lower()))


s6=set()

with open(csv6,"r") as csvfile: 
    freader=csv.reader(csvfile)
    for row in freader:
        s6.add(str(row[0].strip().lower()))

for e in s: 
    with open(intc,"r") as csvfile: 
        freader=csv.reader(csvfile)
        for row in freader:
            if e in str(row[0]):
                l1.append(str(row[0]))
    
for e in s2: 
    with open(intc,"r") as csvfile: 
        freader=csv.reader(csvfile)
        for row in freader:
            if e in str(row[0]):
                l2.append(str(row[0]))

for e in s3: 
    with open(intc,"r") as csvfile: 
        freader=csv.reader(csvfile)
        for row in freader:
            if e in str(row[0]):
                l3.append(str(row[0]))


for e in s4: 
    with open(intc,"r") as csvfile: 
        freader=csv.reader(csvfile)
        for row in freader:
            if e in str(row[0]):
                l4.append(str(row[0]))


for e in s5:
    with open(extc,"r") as csvfile: 
        freader=csv.reader(csvfile)
        for row in freader:
            if e in str(row[0]):
                l5.append(str(row[0]))


for e in s6:
    with open(extc,"r") as csvfile: 
        freader=csv.reader(csvfile)
        for row in freader:
            if e in str(row[0]):
                l6.append(str(row[0]))



with open("/Users/lichenhuilucy/Desktop/dictionaries/cat1.csv","w") as csvfile: 
    wr=csv.writer(csvfile)
    for row in l1:
        wr.writerow([row])

with open("/Users/lichenhuilucy/Desktop/dictionaries/cat2.csv","w") as csvfile: 
    wr=csv.writer(csvfile)
    for row in l2:
        wr.writerow([row])

with open("/Users/lichenhuilucy/Desktop/dictionaries/cat3.csv","w") as csvfile: 
    wr=csv.writer(csvfile)
    for row in l3:
        wr.writerow([row])


with open("/Users/lichenhuilucy/Desktop/dictionaries/cat4.csv","w") as csvfile: 
    wr=csv.writer(csvfile)
    for row in l4:
        wr.writerow([row])


with open("/Users/lichenhuilucy/Desktop/dictionaries/cat5.csv","w") as csvfile: 
    wr=csv.writer(csvfile)
    for row in l5:
        wr.writerow([row])

with open("/Users/lichenhuilucy/Desktop/dictionaries/cat6.csv","w") as csvfile: 
    wr=csv.writer(csvfile)
    for row in l6:
        wr.writerow([row])