
"""
Finalized file, prepare data for regression

"""


import csv
import os
import re

#dir1= "/Users/lucy/Desktop/assortedcodes/5df8773df51c8ae4.csv"
dir2= "/Users/lucy/Desktop/assortedcodes/regposnegvector.csv"

allfiles="/Users/lucy/Desktop/others/allfiles"

from collections import defaultdict

""" 
Part 1: retrieve all filedates
""" 

item="FILED AS OF DATE:"
item2="FILER"
item3="COMPANY CONFORMED NAME:"
item=item.lower()

dfin="/Users/lucy/Desktop/assortedcodes/91e17c1ef257fb31.csv" # for ROA data 
dfin2=""

d=False

d2=defaultdict(list)
with open(dfin,"r") as posfile: 
    #print("u")
    records=csv.reader(posfile)
    i=0
    for row in records:
        if i==0: 
            i+=1
            continue
        cik=row[12]
        if len(cik)<10:
            p=10-len(cik)
            cik="0"*p+cik
            print("y")
        datadate=row[2]
        ni=row[11]
        at=row[9]
        #print(ni)
        #if ni.isnumeric() and at.isnumeric():
        try:
            float(ni)
            float(at)
            if float(at)!=0:
                ROA=float(ni)/float(at)
                for e in d2[(cik,datadate)]:
                    if e==ROA: 
                        d=True 

                if not d:
                    d2[(cik,datadate)].append(ROA)
                    d=False
                #d.update({(cik,datadate):[ROA]})
        except ValueError:
            print ("Not a float")
            print(ni)
            print(at)

        #print(ROA)
       # i+=1

    posfile.close()

d1=defaultdict(list)

dfin1="/Users/lucy/Desktop/assortedcodes/dfb333d6ddf9d922.csv" # for ROA data 


with open("/Users/lucy/Desktop/assortedcodes/dfb333d6ddf9d922.csv","r") as posfile: 
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
            print("y1")
            print(cik)
        datadate=row[2]
        if row[9]:
            epspi=row[9]
        else: 
            epspi="."
        if row[10]:
            epspx=row[10]
        else: 
            epspx="."

        if row[13]:
            mkvalt=row[13]
        else: 
            mkvalt="."
        if epspi not in d1[(cik,datadate)]:
            d1[(cik,datadate)].extend([epspi,epspx,mkvalt])
    posfile.close()



dfin1="/Users/lucy/Desktop/assortedcodes/49a54bfd0097208b.csv"

d=defaultdict(list)

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



    
#print(d)

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

with open(dir2,"r") as posfile: 
    records=csv.reader(posfile)
    i=0
    
    

#epspi,epspx,mkvalt, prcc, csho, ceq, gic

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


        if year.isdigit():
            year2=int(year)+1
            year1=int(year)-1

        if d2.get((cik,year)):
            roa=d2[(cik,year)][0]
            l7.append(roa)
        else: 
            l7.append(".")
        if d2.get((cik,year1)):
            roa1=d2[(cik,year1)][0]
            l9.append(roa1)
        else: 
            l9.append(".")
        if d2.get((cik,year2)):
            roa2=d2[(cik,year2)][0]
            l11.append(roa2)
        else: 
            l11.append(".")

        

        # if d.get((cik,year)):
        #     if len(d[(cik,year)])==1 or len(d[(cik,year)])==4 or len(d[(cik,year)])==5 or len(d[(cik,year)])==8:
        #         if d[(cik,year)][0]:

        #             ROA=d[(cik,year)][0]
        #             l7.append(ROA)
        #         else:
        #             l7.append(".")
        #     else: 
        #         l7.append(".")
        # else: 
        #     l7.append(".")


        # if year.isdigit():
        #     year2=int(year)+1
        #     year1=int(year)-1

        # if d.get((cik,str(year1))):
        #     if len(d[(cik,year1)])==1 or len(d[(cik,year1)])==4 or len(d[(cik,year1)])==5 or len(d[(cik,year1)])==8:
        #         if d[(cik,year1)][0]:

        #             ROA1=d[(cik,year1)][0]
        #             l9.append(ROA1)
        #         else:
        #             l9.append(".")
        #     else: 
        #         l9.append(".")
        # else: 
        #     l9.append(".")


        # if d.get((cik,str(year2))):
        #     if len(d[(cik,year2)])==1 or len(d[(cik,year2)])==4 or len(d[(cik,year2)])==5 or len(d[(cik,year2)])==8:
        #         if d[(cik,year2)][0]:

        #             ROA2=d[(cik,year2)][0]
        #             l11.append(ROA2)
        #         else:
        #             l11.append(".")
        #     else: 
        #         l11.append(".")
        # else: 
        #     l11.append(".")



#
        if d1.get((cik,year)):

            epspi=d1[(cik,year)][0]
            l14.append(epspi)
        else: 
            l14.append(".")



        if d1.get((cik,year)):
            epspx=d1[(cik,year)][2]
            l14.append(epspx)
        else: 
            l14.append(".")

        if d1.get((cik,year)):

            mkvalt=d1[(cik,year)][2]
            l14.append(mkvalt)
        else: 
            l14.append(".")

        #     if len(d[(cik,year)])==4 or len(d[(cik,year)])==8:
        #         epspi=d[(cik,year)][1]
        #         l14.append(epspi)
        #     elif len(d[(cik,year)])==7:
        #         epspi=d[(cik,year)][0]
        #         l14.append(epspi)
        #     elif len(d[(cik,year)])==3:
        #         epspi=d[(cik,year)][0]
        #         l14.append(epspi)
        #     else:
        #         l14.append(".")
        # else: 
        #     l14.append(".")

#

        # if d.get((cik,year)):
        #     if len(d[(cik,year)])==4 or len(d[(cik,year)])==8:
        #         epspx=d[(cik,year)][2]
        #         l15.append(epspx)
        #     elif len(d[(cik,year)])==7:
        #         epspx=d[(cik,year)][1]
        #         l15.append(epspx)
        #     elif len(d[(cik,year)])==3:
        #         epspx=d[(cik,year)][1]
        #         l15.append(epspx)
        #     else: 
        #         l15.append(".")

        # else: 
        #     l15.append(".")


        # if d.get((cik,year)):
        #     if len(d[(cik,year)])==4 or len(d[(cik,year)])==8:
        #         mkvalt=d[(cik,year)][3]
        #         l16.append(mkvalt)
        #     elif len(d[(cik,year)])==7:
        #         mkvalt=d[(cik,year)][2]
        #         l16.append(mkvalt)
        #     elif len(d[(cik,year)])==3:
        #         mkvalt=d[(cik,year)][2]
        #         l16.append(mkvalt)
        #     else: 
        #         l16.append(".")
        # else: 
        #     l16.append(".")


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
            l13.append(float(row[3])+float(row[5])/float(row[4]))
        else: 
            l13.append(".")
        l6.append(".")
        l8.append(float(row[5])/float(row[6]))
        l12.append(row[6])
    posfile.close()
    #l6.append(int(row[5])/int(row[7]))
    #l7.append(int(row[6])/int(row[7]))

i=i+1
f=[0]*i

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

print(f)



z=zip(l1,l2,l3,l4,l5,l8,l6,l7,l9,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,f)
csv2="/Users/lucy/Desktop/assortedcodes/vectorfinal(7).csv"
f_out2 = open(csv2, 'w')
wr2 = csv.writer(f_out2)
#wr2.writerow(["filename","year","cik","posl","negl","negneg","spreturns","roa","filedate"])
wr2.writerow(["filename","year","cik","posl","negl","negneg","spreturns","roa","roat-1","roat+1","length","percwrds","epspi","epspx","mkvalt","prcc","csho","ceq","gic","filedate"])

#wr2.writerow(["filename","year","cik","posint","negint","posextlist","negextlist","filingdate"])
for i in z: 
    wr2.writerow(i)

#Dummy for filing date
