# def __iter__(internalword): 
#     with open("int.csv","r") as internalfile: 
#         internalwords=csv.reader(internalfile)
#         for row in internalwords: 
#             return row[0].lower()
            

# print(internalword)


#os.chdir("/Users/lucy/Desktop/builddic")



# def internalword: 
#     internalwordlist=[]
#     with open("int.csv","r") as internalfile: 
#         internalwords=csv.reader(internalfile)
#         for row in internalwords: 
#             singleinternalword=row[0].lower()
#             return internalwordlist.append(singleinternalword)

import glob
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize


for files in glob.glob("/Users/lucy/Desktop/assortedcodes/assortedcodes/newdictestn/newdic/*.txt"):
    with open(files) as f: 
        print(files)
        content = f.read()
            #You need to sent-tockenize a string 
        sent=sent_tokenize(content)
        print(sent)