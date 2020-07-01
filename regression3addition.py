




import csv
import os
import re

#dir1= "/Users/lucy/Desktop/assortedcodes/5df8773df51c8ae4.csv"
dir2= "/Users/lucy/Desktop/assortedcodes/builddic/regposnegvector13.csv"

allfiles="/Users/lucy/Desktop/others/allfiles"

from collections import defaultdict


l1=[]
l2=[]
A=[]
l3=[]
l4=[]
l5=[]
l8=[]
l6=[]
l7=[]
l9=[]
l11=[]
l21=[]
l22=[]
l23=[]
l24=[]
l25=[]
l12=[]
l13=[]
l14=[]
l15=[]
l16=[]
l17=[]
l18=[]
l19=[]
l20=[]
f=[]
pop=[]

# Want to write out metrics for the past 5 years 

with open("/Users/lucy/Desktop/assortedcodes/vectorfinal(7).csv","r") as posfile: 
    #print("u")
    d=defaultdict(list)
    records=csv.reader(posfile)
    i=0
    for row in records:
        if i==0: 
            i+=1
            continue


        try:
            year=int(row[1])
            cik=int(row[2])
        except ValueError: 
            pass

        l1.append(row[0])
        l2.append(row[1])
        A.append(row[2])
        l3.append(row[3])
        l4.append(row[4])
        l5.append(row[5])
        l8.append(row[6])
        l6.append(row[7])
        l7.append(row[8])
        l9.append(row[9])
        l11.append(row[10])
        l21.append(row[11])
        l22.append(row[12])
        l23.append(row[13])
        l24.append(row[14])
        l25.append(row[15])
        l12.append(row[16])
        l13.append(row[17])
        l14.append(row[18])
        l15.append(row[19])
        l16.append(row[20])
        l17.append(row[21])
        l18.append(row[22])
        l19.append(row[23])
        l20.append(row[24])
        f.append(row[25])

        if row[3]: 
            pass
        else: 
            row[3]=="."
        if row[4]: 
            pass
        else: 
            row[4]=="."
        if row[5]: 
            pass
        else: 
            row[5]=="."

        d[(year,cik)].extend([row[3],row[4],row[5]])
        print(len(d[(year,cik)]))

    posfile.close()

print(d)
with open("/Users/lucy/Desktop/assortedcodes/vectorfinal(7).csv","r") as posfile: 
    #print("u")
    pos1=[]
    neg1=[]
    negneg1=[]
    pos2=[]
    neg2=[] 
    negneg2=[]
    pos3=[]
    neg3=[] 
    negneg3 =[]
    pos4=[]
    neg4 =[]
    negneg4=[]
    pos5=[]
    neg5 =[]
    negneg5=[]
    records=csv.reader(posfile)
    i=0
    for row in records:
        if i==0: 
            i+=1
            continue
        try: 

            year=int(row[1])
        except ValueError: 
            year=0
        
        try: 
            cik=int(row[2])

        except ValueError: 
            cik=0


        if (int(year-1),cik) in d: 
            pos1.append(d[(year-1,cik)][0])
            neg1.append(d[(year-1, cik)][1])
            negneg1.append(d[(year-1,cik)][2])
        else: 
            pos1.append(".")
            neg1.append(".")
            negneg1.append(".")
        if (int(year-2),cik) in d: 
            pos2.append(d[(year-2,cik)][0])
            neg2.append(d[(year-2,cik)][1])
            negneg2.append(d[(year-2,cik)][2])
        else: 
            pos2.append(".")
            neg2.append(".")
            negneg2.append(".")
        if (int(year-3),cik) in d: 
            pos3.append(d[(year-3,cik)][0])
            neg3.append(d[(year-3,cik)][1])
            negneg3.append(d[(year-3,cik)][2])
        else: 
            pos3.append(".")
            neg3.append(".")
            negneg3.append(".")
        if (int(year-4),cik) in d: 
            pos4.append(d[(year-4,cik)][0])
            neg4.append(d[(year-4,cik)][1])
            negneg4.append(d[(year-4,cik)][2])
        else: 
            pos4.append(".")
            neg4.append(".")
            negneg4.append(".")
        if (int(year-5),cik) in d: 
            pos5.append(d[(year-5,cik)][0])
            neg5.append(d[(year-5,cik)][1])
            negneg5.append(d[(year-5,cik)][2])
        else: 
            pos5.append(".")
            neg5.append(".")
            negneg5.append(".")
        
    posfile.close()



z=zip(l1,l2,A,l3,l4,l5,l8,pos1,neg1,negneg1,pos2,neg2,negneg2,pos3,neg3,negneg3,pos4,neg4,negneg4,pos5,neg5,negneg5,l6,l7,l9,l11,l21,l22,l23,l24,l25,l12,l13,l14,l15,l16,l17,l18,l19,l20,f)
csv2="/Users/lucy/Desktop/assortedcodes/vectorfinalfinal.csv"
f_out2 = open(csv2, 'w')
wr2 = csv.writer(f_out2)
#wr2.writerow(["filename","year","cik","posl","negl","negneg","spreturns","roa","filedate"])
wr2.writerow(["filename","year","cik","posl","negl","negneg","posllag1","negllag1","negneglag1","posllag2","negllag2","negneglag2","posllag3","negllag3","negneglag3","posllag4","negllag4","negneglag4","posllag5","negllag5","negneglag5","spreturns","roa","roat-1","roat+1","roat-2","roat+2","roat+3","roat+4","roat+5","length","percwrds","marketval","BOV","lev","prcc","csho","ceq","gic","filedate","shareturnover"])

#wr2.writerow(["filename","year","cik","posint","negint","posextlist","negextlist","filingdate"])
for i in z: 
    wr2.writerow(i)