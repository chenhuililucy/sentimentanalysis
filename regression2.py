
# """
# Finalized file, prepare data for regression, this is for your reference. 
# """


import csv
import os
import re
from collections import defaultdict


#FILE OF POSITIVE AND NEGATIVE METRICS FOR EACH DOCUMENT 
dir2= "/Users/lucy/Desktop/assortedcodes/builddic/regposnegvector13.csv"

#DIRECTORY OF ALL 10-Ks, NOT TO BE CONFUSED WITH (CORPUS) DIRECTORY WITH ALL MD&As
allfiles="/Users/lucy/Desktop/others/allfiles"



                    #################################

#PART I: EXTRACTING INFORMATION FROM FILES ON WHARTON DATA SERVICE AND STORING IN DICT 

                    #################################


# EXAMPLE I: 

""" 
Part 1: retrieve all filedates
""" 

item="FILED AS OF DATE:"
item2="FILER"
item3="COMPANY CONFORMED NAME:"
item=item.lower()


dfin="/Users/lucy/Desktop/assortedcodes/1978dd2de17ce8f3.csv" # Debug, 26 June

d=False

d2=defaultdict(list)
with open(dfin,"r") as posfile: 
    records=csv.reader(posfile)
    i=0
    for row in records:
        if i==0: 
            i+=1
            continue
        cik=row[15]
        if len(cik)<10:
            p=10-len(cik)
            cik="0"*p+cik # THE CIK CONSISTS OF 10 DIGITS, FOR CONSISTENCY, IF LENGTH OF CIK IN CSV IS LESS THAN 10, MAKE IT 10
            print("y")
        datadate=row[2]
        ni=row[13]
        at=row[9]

        try:
            float(ni)
            float(at)
            if float(at)!=0:
                ROA=float(ni)/float(at)

                d2.update({(cik,datadate):[ROA]})

        except ValueError:
            print ("Not a float")
            print(ni)
            print(at)


    posfile.close()

d=defaultdict(list)

with open("/Users/lucy/Desktop/assortedcodes/1978dd2de17ce8f3.csv","r") as posfile: 
    #print("u")
    records=csv.reader(posfile)
    i=0
    for row in records:
        if i==0: 
            i+=1
            continue
        cik=row[15]
        at=row[9]
        if len(cik)<10:
            p=10-len(cik)
            cik="0"*p+cik
            print("y1")
            print(cik)
        datadate=row[2]

        if row[17]:
            prcc=row[17]
        else: 
            prcc="."

        if row[10]:
            cshpri=row[10]
        else: 
            cshpri="."

        if cshpri!="." and prcc!=".": 
            marketval=float(cshpri)*float(prcc)
        else: 
            marketval="."

        if row[14]:
            sec=row[14]
        else: 
            sec="."

        if marketval!="." and sec!="." and marketval!=0:
            BOV=float(sec)/float(marketval)
        else: 
            BOV="."

        if row[11]:
            dlc=row[11]
        else: 
            dlc="."

        if row[12]:
            dltt=row[12]
        else: 
            dltt="."

        if dltt!="." and dlc!="." and at!="." and at!=0:
            try:
                lev=(float(dlc)+float(dltt))/float(at)
            except ZeroDivisionError: 
                lev="."
        else: 
            lev="."

        d[(cik,datadate)].extend([marketval,BOV,lev])
    posfile.close()



# EXAMPLE II: 

dfin1="/Users/lucy/Desktop/assortedcodes/49a54bfd0097208b.csv"

#d=defaultdict(list)

with open(dfin1,"r") as posfile: 
    #print("u")
    records=csv.reader(posfile)
    i=0
    for row in records:
        if i==0: 
            i+=1
            continue
        cik=row[11]
        if len(cik)<10:
            p=10-len(cik)
            cik="0"*p+cik
            print(cik)
            print("y2")
        datadate=row[2]
        if row[13]:
            prcc=row[13]
        else: 
            prcc="."
        if row[10]: 
            csho=row[10]
        else: 
            csho="."
        if row[9]:
            ceq=row[9]
        else: 
            ceq="."

        if row[14]:
            gic=row[14]
        else: 
            gic="."
        if prcc not in d[(cik,datadate)]:
            if len(d[(cik,datadate)])==0: 
                d[(cik,datadate)].extend([".",".","."])
                d[(cik,datadate)].extend([prcc,csho,ceq,gic])
            else: 
                d[(cik,datadate)].extend([prcc,csho,ceq,gic])
    posfile.close()



    
                    #################################

#PART II: MATCHING METRICS FROM FILE OF POSITIVE AND NEGATIVE METRICS FOR EACH DOCUMENT WITH ENTRIES IN DICT

                    #################################



s=defaultdict(int)
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



with open(dir2,"r") as posfile: 
    records=csv.reader(posfile)
    i=0
    

    for row in records:
        if i==0: 
            i+=1 
            continue
        i+=1 
        year=row[1]
        cikoriginal=row[2]
        if len(cikoriginal)<10:
            p=10-len(cikoriginal)
            cik="0"*p+cikoriginal


        try:
            year0=int(year)-2 # year 0 being -2 years
            year2=int(year)+1
            year1=int(year)-1
            year3=int(year)+2 # year 3 being +2 years
            year4=int(year)+3 # year 4 being +2 years
            year5=int(year)+4 # year 5 being +2 years
            year6=int(year)+5 # year 6 being +2 years


        except ValueError: 
            pass
            #print(year)

        if d2.get((cik,year)):
            roa=d2[(cik,year)][0]
            l7.append(roa)
        else: 
            l7.append(".")
        if d2.get((cik,str(year1))):
            roa1=d2[(cik,str(year1))][0]
            l9.append(roa1)
        else: 
            l9.append(".")
        if d2.get((cik,str(year2))):
            roa2=d2[(cik,str(year2))][0]
            l11.append(roa2)
        else: 
            l11.append(".")
        if d2.get((cik,str(year0))):
            roa3=d2[(cik,str(year0))][0]
            l21.append(roa3)
        else: 
            l21.append(".")
        if d2.get((cik,str(year3))):
            roa4=d2[(cik,str(year3))][0]
            l22.append(roa4)
        else: 
            l22.append(".")

        if d2.get((cik,str(year4))):
            roa5=d2[(cik,str(year4))][0]
            l23.append(roa5)
        else: 
            l23.append(".")

        if d2.get((cik,str(year5))):
            roa6=d2[(cik,str(year5))][0]
            l24.append(roa6)
        else: 
            l24.append(".")

        if d2.get((cik,str(year6))):
            roa7=d2[(cik,str(year6))][0]
            l25.append(roa7)
        else: 
            l25.append(".")

    
#
        if d.get((cik,year)):

            epspi=d[(cik,year)][0]
            l14.append(epspi)
        else: 
            l14.append(".")



        if d.get((cik,year)):
            epspx=d[(cik,year)][1]
            l15.append(epspx)
        else: 
            l15.append(".")

        if d.get((cik,year)):

            mkvalt=d[(cik,year)][2]
            l16.append(mkvalt)
        else: 
            l16.append(".")

#
        if d.get((cik,year)):
            if len(d[(cik,year)])==7:
                prcc=d[(cik,year)][3]
                l17.append(prcc)

            elif len(d[(cik,year)])==8:
                prcc=d[(cik,year)][4]
                l17.append(prcc)

            elif len(d[(cik,year)])==5:
                prcc=d[(cik,year)][1]
                l17.append(prcc)
            else: 
                l17.append(".")

        else: 
            l17.append(".")

#
        if d.get((cik,year)):
            if len(d[(cik,year)])==7:               
                csho=d[(cik,year)][4]
                l18.append(csho)

            elif len(d[(cik,year)])==8:   
                csho=d[(cik,year)][5]
                l18.append(csho)

            elif len(d[(cik,year)])==5:
                csho=d[(cik,year)][2]
                l18.append(csho)
            else: 
                l18.append(".")

        else: 
            l18.append(".")
        
        if d.get((cik,year)):

            if len(d[(cik,year)])==7:               
                ceq=d[(cik,year)][5]
                l19.append(ceq)

            elif len(d[(cik,year)])==8:   
                ceq=d[(cik,year)][6]
                l19.append(ceq)

            elif len(d[(cik,year)])==5:
                ceq=d[(cik,year)][3]
                l19.append(ceq)

            else: 
                l19.append(".")

        else: 
            l19.append(".")



        
        if d.get((cik,year)):
            if len(d[(cik,year)])==7:
                giv=d[(cik,year)][6]
                l20.append(giv)

            elif len(d[(cik,year)])==8:
                giv=d[(cik,year)][7]
                l20.append(giv)

            elif len(d[(cik,year)])==5: 
                giv=d[(cik,year)][4]
                l20.append(giv)
            else: 
                l20.append(".")

        else: 
            l20.append(".")



            
        s.update({(cikoriginal,year):i-2})
        directory=row[0]
        l1.append(row[0])
        year=row[1]
        l2.append(row[1])
        cik=row[2]

        l3.append(row[2])
        l4.append(float(row[3])/float(row[6]))
        l5.append(float(row[4])/float(row[6]))
        if float(row[4])!=0:
            l13.append((float(row[3])+float(row[5]))/float(row[4]))
        else: 
            l13.append(".")
        l6.append(".")
        l8.append(float(row[5])/float(row[6]))
        l12.append(row[6])
    posfile.close()


i=i+1
f=[0]*i

    
                    #################################

            #PART III: MATCHING METRICS WITH FILING DATES 

                    #################################




for root, dirs, files in os.walk("/Users/lucy/Desktop/others/allfiles"):
    for file in files:
        
        if '.txt' in file:
            year=file[file.find("-")+1:file.find(".")]
            #print(year)
            #print(cik)
            cik=file[:file.find("-")]
            if (cik,year) in s:
                matchedstring=""
                num=s[(cik,year)]
            #for i in s:
                #year, cik=i
                #if file[file.find("-")+1:file.find(".")]==year and file[:file.find("-")]==cik: 
                with open(os.path.join(root, file), "r") as auto:
                    text = auto.read()
                    text1=text.lower()
                    for m in re.finditer(item, text1): 
                        if not m: 
                            matchedstring=""
                            raise Error
                            #print(file)
                        else:
                            substr1=text[m.start():m.start()+30]
                            #print(substr1)
                            # may be necessary to search for end string  
                            i=0
                            while i< len(substr1) and not substr1[i].isdigit(): 
                                i+=1
                            while i< len(substr1) and substr1[i].isdigit(): 
                                matchedstring+=substr1[i]
                                i+=1
                            break
                            
                f[num]=matchedstring.strip()

#print(f)

import datetime
from datetime import timedelta, date
from datetime import date
from datetime import timedelta



d=defaultdict(list)
pop=[0]*len(f)
l=[0]*len(f)
index=0
for i in zip(l3,f):
    cik,date=i
    print(date)
    if len(cik)<10:
        p=10-len(cik)
        cik="0"*p+cik
    date=str(date).strip()

    if date[:4] is not None or date[4:6] is not None or date[6:8] is not None:
        try:
            mind=datetime.date(int(date[:4]),int(date[4:6]),int(date[6:8]))-timedelta(days=252)
            maxd=datetime.date(int(date[:4]),int(date[4:6]),int(date[6:8]))-timedelta(days=6)

        except ValueError: 
            mind="."
            maxd="."

        
    #maxd=datetime.date(int(date[:4]),int(date[4:6]),int(date[6:8]))-timedelta(days=6)
    d[cik].append([index,date,mind,maxd])
    #print(d)
    index+=1


#print(d)


with open("/Users/lucy/Desktop/assortedcodes/31b3605da3e00c98.csv","r") as posfile: 
    records=csv.reader(posfile)
    i=0
    for row in records:
        if i==0: 
            i+=1 
            continue

        #this works
        try: 
            u=datetime.date(int(row[9][:4]),int(row[9][4:6]),int(row[9][6:8]))
        except ValueError or TypeError:
            pass
            #print(row[9])
            #print("value error with file")


        
        if row[12] in d: 
            for e in d[row[12]]:
                try:
                    b=datetime.date(int(str(e[2])[:4]), int(str(e[2])[5:7]),int(str(e[2])[8:10]))

                    u=datetime.date(int(str(e[3])[:4]), int(str(e[3])[5:7]),int(str(e[3])[8:10]))

                    if b<datetime.date(int(row[9][:4]),int(row[9][4:6]),int(row[9][6:8])) and u>datetime.date(int(row[9][:4]),int(row[9][4:6]),int(row[9][6:8])):
                        try:
                            pop[int(e[0])]+=float(row[11]) # the pop list stores all the matches 
                            #print(float(row[11]))
                            l[int(e[0])]+=int(1)

                        except ValueError: 
                            pop[int(e[0])]+=0
                            l[int(e[0])]+=int(1)
                            #print(row[11])

                    else: 
                        pass

                except ValueError or TypeError: 
                    pass


    posfile.close()

finpop=[] 
finitem=[]


z=zip(l1,l2,l3,l4,l5,l8,l6,l7,l9,l11,l21,l22,l23,l24,l25,l12,l13,l14,l15,l16,l17,l18,l19,l20,f,pop)
csv2="/Users/lucy/Desktop/assortedcodes/vectorfinal(12).csv"
f_out2 = open(csv2, 'w')
wr2 = csv.writer(f_out2)
#wr2.writerow(["filename","year","cik","posl","negl","negneg","spreturns","roa","filedate"])
wr2.writerow(["filename","year","cik","posl","negl","negneg","spreturns","roa","roat-1","roat+1","roat-2","roat+2","roat+3","roat+4","roat+5","length","percwrds","marketval","BOV","lev","prcc","csho","ceq","gic","filedate","shareturnover"])

#wr2.writerow(["filename","year","cik","posint","negint","posextlist","negextlist","filingdate"])
for i in z: 
    wr2.writerow(i)

# #Dummy for filing date


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
        except ValueError: 
            pass
        d[year].extend([row[3],row[4],row[5]])

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
    if int(year-1) in d: 
        pos1.append(d[year-1][1])
        neg1.append(d[year-1][2])
        negneg1.append(d[year-1][3])
    else: 
        pos1.append(".")
        neg1.append(".")
        negneg1.append(".")
    if int(year-2) in d: 
        pos2.append(d[year-2][1])
        neg2.append(d[year-2][2])
        negneg2.append(d[year-2][3])
    else: 
        pos2.append(".")
        neg2.append(".")
        negneg2.append(".")
    if int(year-3) in d: 
        pos3.append(d[year-3][1])
        neg3.append(d[year-3][2])
        negneg3.append(d[year-3][3])
    else: 
        pos3.append(".")
        neg3.append(".")
        negneg3.append(".")
    if int(year-4) in d: 
        pos4.append(d[year-4][1])
        neg4.append(d[year-4][2])
        negneg4.append(d[year-4][3])
    else: 
        pos4.append(".")
        neg4.append(".")
        negneg4.append(".")
    if int(year-5) in d: 
        pos5.append(d[year-5][1])
        neg5.append(d[year-5][2])
        negneg5.append(d[year-5][3])
    else: 
        pos5.append(".")
        neg5.append(".")
        negneg5.append(".")
        
    posfile.close()



z=zip(l1,l2,l3,l4,l5,l8,pos1,neg1,negneg1,pos2,neg2,negneg2,pos3,neg3,negneg3,pos4,neg4,negneg4,pos5,neg5,negneg5,l6,l7,l9,l11,l21,l22,l23,l24,l25,l12,l13,l14,l15,l16,l17,l18,l19,l20,f,pop)
csv2="/Users/lucy/Desktop/assortedcodes/vectorfinalfinal.csv"
f_out2 = open(csv2, 'w')
wr2 = csv.writer(f_out2)
#wr2.writerow(["filename","year","cik","posl","negl","negneg","spreturns","roa","filedate"])
wr2.writerow(["filename","year","cik","posl","negl","negneg","posllag1","negllag1","negneglag1","posllag2","negllag2","negneglag2","posllag3","negllag3","negneglag3","posllag4","negllag4","negneglag4","posllag5","negllag5","negneglag5""spreturns","roa","roat-1","roat+1","roat-2","roat+2","roat+3","roat+4","roat+5","length","percwrds","marketval","BOV","lev","prcc","csho","ceq","gic","filedate","shareturnover"])

#wr2.writerow(["filename","year","cik","posint","negint","posextlist","negextlist","filingdate"])
for i in z: 
    wr2.writerow(i)