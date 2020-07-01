





import csv
import os
import re
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
#h=[]

# Want to write out metrics for the past 5 years 

with open("/Users/lucy/Desktop/assortedcodes/builddic/regposnegvector11.csv","r") as posfile: 
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
        #h.append(row[26])


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
        if row[6]: 
            pass
        else: 
            row[6]=="."          
            
              
        d[(year,cik)].extend([row[3],row[4],row[5],row[6],row[8]])

    posfile.close()

with open("/Users/lucy/Desktop/assortedcodes/builddic/regposnegvector11.csv","r") as posfile: 
    #print("u")
    posint1=[]
    negint1=[]
    posext1=[]
    negext1=[]
    posint2=[]
    negint2=[]
    posext2=[]
    negext2=[]
    posint3=[]
    negint3=[]
    posext3=[]
    negext3=[]
    posint4=[]
    negint4=[]
    posext4=[]
    negext4=[]
    posint5=[]
    negint5=[]
    posext5=[]
    negext5=[]
    ROAl1=[]
    ROAl2=[]
    ROAl3=[]
    ROAl4=[]
    ROAl5=[]





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
            posint1.append(d[(year-1,cik)][0])
            negint1.append(d[(year-1,cik)][1])
            posext1.append(d[(year-1,cik)][2])
            negext1.append(d[(year-1,cik)][3])
            ROAl1.append(d[(year-1,cik)][4])

        else: 
            posint1.append(".")
            negint1.append(".")
            posext1.append(".")
            negext1.append(".")
            ROAl1.append(".")


        if (int(year-2),cik) in d: 
            posint2.append(d[(year-2,cik)][0])
            negint2.append(d[(year-2,cik)][1])
            posext2.append(d[(year-2,cik)][2])
            negext2.append(d[(year-2,cik)][3])
            ROAl2.append(d[(year-2,cik)][4])


        else: 
            posint2.append(".")
            negint2.append(".")
            posext2.append(".")
            negext2.append(".")
            ROAl2.append(".")




        if (int(year-3),cik) in d: 
            posint3.append(d[(year-3,cik)][0])
            negint3.append(d[(year-3,cik)][1])
            posext3.append(d[(year-3,cik)][2])
            negext3.append(d[(year-3,cik)][3])
            ROAl3.append(d[(year-3,cik)][4])


        else: 
            posint3.append(".")
            negint3.append(".")
            posext3.append(".")
            negext3.append(".")
            ROAl3.append(".")



        if (int(year-4),cik) in d: 
            posint4.append(d[(year-4,cik)][0])
            negint4.append(d[(year-4,cik)][1])
            posext4.append(d[(year-4,cik)][2])
            negext4.append(d[(year-4,cik)][3])
            ROAl4.append(d[(year-4,cik)][4])


        else: 
            posint4.append(".")
            negint4.append(".")
            posext4.append(".")
            negext4.append(".")
            ROAl4.append(".")


        if (int(year-5),cik) in d: 
            posint5.append(d[(year-5,cik)][0])
            negint5.append(d[(year-5,cik)][1])
            posext5.append(d[(year-5,cik)][2])
            negext5.append(d[(year-5,cik)][3])
            ROAl5.append(d[(year-5,cik)][4])

        else: 
            posint5.append(".")
            negint5.append(".")
            posext5.append(".")
            negext5.append(".")
            ROAl5.append(".")

        


    posfile.close()



z=zip(l1,l2,A,l3,l4,l5,l8,posint1,negint1,posext1,negext1,posint2,negint2,posext2,negext2,posint3,negint3,posext3,negext3,posint4,negint4,posext4, negext4,posint5,negint5,posext5,negext5,l6,l7,l9,l11,l21,l22,l23,l24,l25,l12,l13,l14,l15,l16,l17,l18,l19,l20,f,ROAl1,ROAl2,ROAl3,ROAl4,ROAl5)
csv2="/Users/lucy/Desktop/assortedcodes/vectorfinalinternalexternal.csv"
f_out2 = open(csv2, 'w')
wr2 = csv.writer(f_out2)
#wr2.writerow(["filename","year","cik","posl","negl","negneg","spreturns","roa","filedate"])
wr2.writerow(["filename","year","cik","posint","negint","posext","negext","posint1","negint1","posext1","negext1","posint2","negint2","posext2","negext2","posint3","negint3","posext3","negext3","posint4","negint4","posext4","negext4","posint5","negint5","posext5","negext5","spreturns","roa","roat-1","roat+1","roat-2","roat+2","roat+3","roat+4","roat+5","length","marketval","BOV","lev","prcc","csho","ceq","gic","filedate","shareturnover","ROAl1","ROAl2","ROAl3","ROAl4","ROAl5"])

#wr2.writerow(["filename","year","cik","posint","negint","posextlist","negextlist","filingdate"])
for i in z: 
    wr2.writerow(i)