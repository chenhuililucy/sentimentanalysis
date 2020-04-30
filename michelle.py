import csv 

final="/Users/lucy/Desktop/assortedcodes/michelle.csv" 

l1=[] 
l2=[]
l3=[]

with open(final,"r", encoding="utf-8", errors="ignore") as f: 
    r=csv.reader(f)
    for row in r: 
        if row[2]=="External": 
            l1.append(row[0])
            l2.append("external")
            l3.append(row[1])

        if row[2]=="Internal": 
            l1.append(row[0])
            l2.append("internal")
            l3.append(row[1])

    f.close()



final1="/Users/lucy/Desktop/assortedcodes/michelle1.csv" 

z=zip(l1,l2,l3)
with open(final1,"w", encoding="utf-8", errors="ignore") as f: 
    fwriter=csv.writer(f)
    for i in z: 
        fwriter.writerow(i)
    f.close()



