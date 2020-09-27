
from collections import defaultdict
import csv

with open("/Users/lucy/Desktop/task1.csv","r") as posfile: 
    records=csv.reader(posfile)
    d=defaultdict(list)
    for row in records:
        cik=row[3].lower()
        year=row[5].lower()
        l1=row[0]
        l2=row[1]
        l3=row[2]
        l4=row[4]
        l5=row[6]
        l6=row[7]
        l7=row[8]
        l8=row[9]
        l9=row[10]
        d[(cik,year)]=[l1,l2,l3,l4,l5,l6,l7,l8,l9]

print("done")

cikl=[]
yearl=[]
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]
l7=[]
l8=[]
l9=[]
l10=[]
l11=[]
l12=[]
l13=[]
l14=[]
l15=[]
l16=[]
l17=[]
l18=[]
l19=[]
l20=[]
l21=[]
l22=[]
l23=[]
l24=[]
l25=[]
l26=[]
l27=[]
l28=[]
l29=[]
l30=[]
l31=[]
l32=[]
l33=[]
l34=[]
l35=[]
l36=[]
l37=[]
l38=[]

with open("/Users/lucy/Desktop/assortedcodes/vectorfinalv7finalv.csv","r") as posfile: 
    records=csv.reader(posfile)
    #di=defaultdict(list)
    for row in records:
        cik=row[2].lower()
        year=row[1].lower()
        if (cik,year) in d:
            cikl.append(row[2])
            yearl.append(row[1])
            l1.append(row[0])
            l2.append(row[3])
            l3.append(row[4])
            l4.append(row[5])
            l5.append(row[6])
            l6.append(row[7])
            l7.append(row[8])
            l8.append(row[9])
            l9.append(row[10])
            l10.append(row[11])
            l11.append(row[12])
            l12.append(row[13])
            l13.append(row[14])
            l14.append(row[15])
            l15.append(row[16])
            l16.append(row[17])
            l17.append(row[18])
            l18.append(row[19])
            l19.append(row[20])
            l20.append(row[21])
            l21.append(row[22])
            l22.append(row[23])
            l23.append(row[24])
            l24.append(row[25])
            l34.append(row[26])
            l35.append(row[27])
            l36.append(row[28])
            l37.append(row[29])
            l38.append(row[30])
            l25.append(d[(cik,year)][0])
            l26.append(d[(cik,year)][1])
            l27.append(d[(cik,year)][2])
            l28.append(d[(cik,year)][3])
            l29.append(d[(cik,year)][4])
            l30.append(d[(cik,year)][5])
            l31.append(d[(cik,year)][6])
            l32.append(d[(cik,year)][7])
            l33.append(d[(cik,year)][8])


z=zip(cikl, yearl, l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l34,l35,l36,l37,l38,l25,l26,l27,l28,l29,l30,l31,l32,l33)


#z=zip([i for i in d.values()],[r for r in d.keys()])

with open("/Users/lucy/Desktop/assortedcodes/vectorfinalversion8.csv","w") as wr2: 
    records=csv.writer(wr2)
    for i in z: 
        records.writerow(i)

    