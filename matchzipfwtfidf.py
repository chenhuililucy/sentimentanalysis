
tfidf="/Users/lilucy/Desktop/Data-structure-and-Algo-Notes/ngramis13tfidf.csv"
wordfile="/Users/lilucy/Desktop/Data-structure-and-Algo-Notes/zipfdata<8.csv"
import re
import glob
import os
import csv
import nltk 
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
import re
import glob
import os
import csv
import nltk 
from collections import defaultdict
from collections import Counter
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import ngrams
import matplotlib.pyplot as plt
from scipy.stats import zipf
import csv
import math


d=defaultdict(int)

with open(tfidf,"r") as posfile: 
    records=csv.reader(posfile)
    #records = csv.DictReader((l.replace('\0', '') for l in posfile))
    #try:
    for row in records:
        wordtokens=row[0]
        tfidf=row[1]
        d[wordtokens]=tfidf
    #except csv.Error: 
        #pass

f1=[]
f2=[]
f3=[]
with open(wordfile,"r",encoding="utf-8-sig", errors="ignore") as posfile: 
    records=csv.reader(posfile)
    try:
        for row in records:
            wordtokens=row[0]
            if wordtokens in d: 
                tfidf=d[wordtokens]

            count=row[1]
            f1.append(wordtokens)
            f2.append(count)
            f3.append(tfidf)
            print(row)
    except csv.Error: 
        pass

z=zip(f1,f2,f3)

with open("/Users/lilucy/Desktop/Data-structure-and-Algo-Notes/matched.csv","w") as csvfile: 
    writer=csv.writer(csvfile)
    for i in z: 
        writer.writerow(i)

lessthan3=0
btw3and4=0
btw4and5=0
btw5and6=0
btw6and7=0
btw7and8=0
btw8and9=0
above9=0


lst=[]
with open('/Users/lilucy/Desktop/Data-structure-and-Algo-Notes/matched.csv','r') as csvfile:
    #fieldnames=['word','count']
    records=csv.reader(csvfile)

    for row in records:
        try:
            tfidf=float(str(row[2].lower()))
            count=float(str(row[1].strip()))
        except ValueError: 
            pass
            continue
        try:
            if tfidf<3: 
                lessthan3+=count

            if tfidf<4 and tfidf>=3: 
                btw3and4+=count

            if tfidf<5 and tfidf>=4: 
                btw4and5+=count

            if tfidf<6 and tfidf>=5: 
                btw5and6+=count

            if tfidf<7 and tfidf>=6: 
                btw6and7+=count

            if tfidf<8 and tfidf>=7: 
                btw7and8+=count

            if tfidf<8 and tfidf>=9: 
                btw8and9+=count

            if tfidf>9: 
                above9+=count

            if float(tfidf)<8:
                lst.append((math.log(float(count)),math.log(float(tfidf))))
        except ValueError: pass




print(lessthan3)
print(btw3and4)
print(btw4and5)
print(btw5and6)
print(btw6and7)
print(btw7and8)
print(btw8and9)
print(above9)

lst.sort(key=lambda x:x[1])
#print(lst)
plt.scatter([key for val, key in lst], [val for val, key in lst], color='limegreen')
alpha = 0.5



#total=0
#for p, c in lst: 
    #try:
        #total+=p
    #except ValueError: pass
total = sum([p for p, c in lst])
#except ValueError: pass
    
plt.plot(range(len(lst)), [zipf.pmf(p, alpha) * total for p in range(1, len(lst) + 1)], color='crimson', lw=3)
plt.ylabel("Frequency")
plt.xlabel("TFIDF")
plt.xticks(rotation='vertical')
plt.tight_layout()
plt.show()



# import matplotlib.pyplot as plt
# from scipy.stats import zipf
# import csv
# import math
# lst=[]

# i=0
# with open('/Users/lilucy/Desktop/Data-structure-and-Algo-Notes/zipfdata<8.csv','r') as csvfile:
#     fieldnames=['word','count']
#     records=csv.reader(csvfile)
#     for row in records:
#         wordtokens=row[0].lower()
#         i+=1
#         count=row[1].strip()
#         #lst.append((float(count),i))

#         try:
#             if math.log(float(count))>8:
#                 lst.append((math.log(float(count)),math.log(float(i))))
#         except ValueError: pass


# lst=lst[:-1]
# print(lst)
# plt.bar([key for val, key in lst], [val for val, key in lst], color='limegreen')
# alpha = 0.5

# #total=0
# #for p, c in lst: 
#     #try:
#         #total+=p
#     #except ValueError: pass

# total = sum([p for p, c in lst])
# #except ValueError: pass
    
# plt.plot(range(len(lst)), [zipf.pmf(p, alpha) * total for p in range(1, len(lst) + 1)], color='crimson', lw=3)
# plt.ylabel("Frequency")
# plt.xticks(rotation='vertical')
# plt.tight_layout()
# plt.show()

