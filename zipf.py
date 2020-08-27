corpus="/Users/lucy/Desktop/others/newdictestn/newdic/*.txt"
wordfile="/Users/lucy/Desktop/assortedcodes/initial/ngramis13tfidf.csv"

import re
import glob
import os
import csv
import nltk 
from nltk.corpus import stopwords
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



s=set()

with open(wordfile,"r") as posfile: 
    records=csv.reader(posfile)
    s=set()
    for row in records:
        wordtokens=row[0].lower()
        if len(wordtokens.split(" "))==2: 
            a,b=wordtokens.split(" ")[0],wordtokens.split(" ")[1]
        elif len(wordtokens.split(" "))==1: 
            a=str(wordtokens.split(" "))[0]
            b=""
        s.add((a,b))


#print(s)

C=Counter()

i=0
for files in glob.glob(corpus):
    #year=files[files.find("-")+1:files.find(".")]
    #cik=files[:files.find("-")]
    with open(files) as f: 
        content = f.read()
        text1=content.lower()
        text_tokens=word_tokenize(text1)
        tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
        for i in range(len(tokens_without_sw)-1): 
            #if tokens_without_sw[i] in d: 

            """
            if d[tokens_without_sw[i]]==tokens_without_sw[i+1]: 
                C[tuple(tokens_without_sw[i:i+2])]+=1
            elif d[tokens_without_sw[i]]=="": 
                C[tuple(tokens_without_sw[i])]+=1
            Counter[list(tokens_without_sw[i:i+2])]+=1
            """ 

            if (tokens_without_sw[i],"") in s:
                C[tokens_without_sw[i]]+=1
            if (tokens_without_sw[i],tokens_without_sw[i+1]) in s: 
                C[tokens_without_sw[i]+" "+tokens_without_sw[i+1]]+=1
        if (tokens_without_sw[-1],"") in s:
            C[tokens_without_sw[-1]]+=1
        i+=1
        if i==10: 
            break

final=sorted(C.items(),key=lambda i:i[1])
#final=[(l,k) for k,l in sorted([(j,i) for i,j in C.items()])]


with open('/Users/lucy/Desktop/assortedcodes/zipfdata.csv','w') as csvfile:
    fieldnames=['word','count']
    writer=csv.writer(csvfile)
    writer.writerow(fieldnames)
    for r in final: 
        writer.writerow(r)

