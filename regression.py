
import csv
import os
import re

#dir1= "/Users/lucy/Desktop/assortedcodes/5df8773df51c8ae4.csv"
dir2= "/Users/lucy/Desktop/assortedcodes/regression2.csv"

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


d=defaultdict(list)
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
                d.update({(cik,datadate):ROA})
        except ValueError:
            print ("Not a float")
            print(ni)
            print(at)

        #print(ROA)
       # i+=1

    posfile.close()


with open(dfin,"r") as posfile: 
    #print("u")
    records=csv.reader(posfile)
    i=0
    for row in records:
        if i==0: 
            i+=1
            continue
        cik=row[12]


print(d)

s=defaultdict(int)
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
l6=[]
l7=[]
l8=[]

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
        if d.get((cik,year)):
            ROA=d[(cik,year)]
            l7.append(ROA)
        else: 
            l7.append(".")

        s.update({(cikoriginal,year):i-2})
        
        l1.append(row[0])
        l2.append(row[1])
        l3.append(row[2])
        l4.append(float(row[3])/float(row[5]))
        l5.append(float(row[4])/float(row[5]))
        l6.append(row[6])
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



z=zip(l1,l2,l3,l4,l5,l6,l7,f)
csv2="/Users/lucy/Desktop/assortedcodes/vectorfinal.csv"
f_out2 = open(csv2, 'w')
wr2 = csv.writer(f_out2)
wr2.writerow(["filename","year","cik","posl","negl","spreturns","roa","filedate"])

#wr2.writerow(["filename","year","cik","posint","negint","posextlist","negextlist","filingdate"])
for i in z: 
    wr2.writerow(i)

#Dummy for filing date

""" 
Part 2: retrieve all filedates
""" 


# d="/Users/lucy/Desktop/assortedcodes/91e17c1ef257fb31.csv"

# d=defaultdict(list)
# with open(d,"r") as posfile: 
#     records=csv.reader(posfile)
#     i=0
#     for row in records:
#         if i==0: 
#             pass
#         i+=1
#         cik=row[7]
#         datadate=row[2]
#         cshoc=row[4]
#         eps=row[5]
#         prccd=row[6]
#         prcod=row[7]
#         gsector=row[9]
#         dic.update({(cik,datadate):(cshoc,eps,prccd,prcod,gsector)})


# d=defaultdict(list)
# with open(d,"r") as posfile: 
#     records=csv.reader(posfile)
#     i=0
#     for row in records:
#         if i==0: 
#             pass
#         i+=1
#         cik=row[12]
#         datadate=row[2]
#         ni=row[11]
#         at=row[10]
#         ROA=ni/at
#         dic.update({(cik,datadate):ROA})




# with open()
# l1=[]
# l2=[]
# l3=[]
# l4=[]
# l5=[]
# l6=[]
# l7=[]

# with open(csv2,"r") as e:
#     records=csv.reader(e)
#     i=0
#     for row in records:
#         if i==0: 
#             pass
#         year=row[1]
#         cik=row[2]
#         if (cik,year) in dic:
#             l1=[]
#             l2=[]
#             l3=[]
#             l4=[]
#             l5=[]
#             l6=[]
#             l7.append(dic[(cik:year)])


#         #prcod




  

            
             



# """

# with open(dir1,"r") as posfile: 
#     records=csv.reader(posfile)
#     i=0
#     for row in records:
#         if i==0: 
#             pass
#         i+=1
#         cshoc=row[4]
#         eps=row[5]

#         i+=1
#         year=row[1]
#         cik=row[2]
#         posint=row[3]
#         negint=row[4]
#         posextlist=row[5]
#         negextlist=row[6]



# d={}
# with open(dir1,"r") as posfile: 
#     records=csv.reader(posfile)
#     i=0
#     for row in records:
#         if i==0: 
#             pass
#         i+=1
#         cshoc=row[4]
#         eps=row[5]








#         i+=1
#         year=row[1]
#         cik=row[2]
#         posint=row[3]
#         negint=row[4]
#         posextlist=row[5]
#         negextlist=row[6]

#         d.update{(year,cik):(posint)}

#         posperf=row[0].lower()
#         if len(posperf.split(" "))>1: 
#             w1=posperf.split(" ")[0]
#             w2=posperf.split(" ")[1]

# """


