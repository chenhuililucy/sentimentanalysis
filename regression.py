
import csv
import os
import re

dir1= "/Users/lucy/Desktop/assortedcodes/5df8773df51c8ae4.csv"
dir2= "/Users/lucy/Desktop/assortedcodes/builddic/vector1.csv"

allfiles="/Users/lucy/Desktop/others/allfiles"


""" 
Part 1: retrieve all filedates
""" 

item="FILED AS OF DATE:"
item2="FILER"
item3="COMPANY CONFORMED NAME:"
item=item.lower()

s=set()
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]
l7=[]

with open(dir2,"r") as posfile: 
    records=csv.reader(posfile)
    i=0
    for row in records:
        if i==0: 
            pass
        i+=1 
        year=row[1]
        cik=row[2]
        s.add((year,cik))
        
    l1.append(row[0])
    l2.append(row[1])
    l3.append(row[2])
    l4.append(int(row[3])/int(row[7]))
    l5.append(int(row[4])/int(row[7]))
    l6.append(int(row[5])/int(row[7]))
    l7.append(int(row[6])/int(row[7]))

f=[]
for root, dirs, files in os.walk("/Users/lucy/Desktop/others/allfiles"):
    for file in files:
        
        if '.txt' in file:
            year=file[file.find("-")+1:file.find(".")]
            #print(year)
            #print(cik)
            cik=file[:file.find("-")]
            if (year,cik) in s:
                matchedstring=""
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
                            
                f.append(matchedstring.strip())
                print(f)



z=zip(l1,l2,l3,l4,l5,l6,l7,f)
csv2="/Users/lucy/Desktop/assortedcodes/vectorfinal.csv"
f_out2 = open(csv2, 'w')
wr2 = csv.writer(f_out2)
wr2.writerow(["filename","year","cik","posint","negint","posextlist","negextlist","filingdate"])
for i in z: 
    wr2.writerow(i)

#Dummy for filing date

""" 
Part 2: retrieve all filedates
""" 

dic={}
with open(dir1,"r") as posfile: 
    records=csv.reader(posfile)
    i=0
    for row in records:
        if i==0: 
            pass
        i+=1
        cik=row[7]
        datadate=row[2]
        cshoc=row[4]
        eps=row[5]
        prccd=row[6]
        prcod=row[7]
        gsector=row[9]
        dic.update({(cik,datadate):(cshoc,eps,prccd,prcod,gsector)})


l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]
l7=[]

with open(csv2,"r") as e:
    records=csv.reader(e)
    i=0
    for row in records:
        if i==0: 
            pass
        year=row[1]
        cik=row[2]
        if (cik,year) in dic:
            l1=[]
            l2=[]
            l3=[]
            l4=[]
            l5=[]
            l6=[]
            l7.append(dic[(cik:year)])


        #prcod




  

            
             



"""

with open(dir1,"r") as posfile: 
    records=csv.reader(posfile)
    i=0
    for row in records:
        if i==0: 
            pass
        i+=1
        cshoc=row[4]
        eps=row[5]

        i+=1
        year=row[1]
        cik=row[2]
        posint=row[3]
        negint=row[4]
        posextlist=row[5]
        negextlist=row[6]



d={}
with open(dir1,"r") as posfile: 
    records=csv.reader(posfile)
    i=0
    for row in records:
        if i==0: 
            pass
        i+=1
        cshoc=row[4]
        eps=row[5]








        i+=1
        year=row[1]
        cik=row[2]
        posint=row[3]
        negint=row[4]
        posextlist=row[5]
        negextlist=row[6]

        d.update{(year,cik):(posint)}

        posperf=row[0].lower()
        if len(posperf.split(" "))>1: 
            w1=posperf.split(" ")[0]
            w2=posperf.split(" ")[1]

"""


