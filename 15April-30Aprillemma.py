''' 
# 15 April
Want to use heurstics of labelled phrases to batch label unlabeled 
phrases in the dictionary

# 30 April 
Corrected labelled phrases, amended codes 
'''


  #=======================================================================================================================#

import csv
import nltk
import pattern
from pattern.text.en import singularize
from pattern.text.en import pluralize
from pattern.en import pluralize, singularize
from pattern.en import conjugate, lemma, lexeme,PRESENT,SG
import random
#utility functions

"""

def removeduplicates(self,anylist): 
    dic={}
    for i in range(len(anylist)):
        if anylist[i][0] in dic[0]: 
            dic[anylist[i]]+=1 
        else: 
            dic.update({anylist[i]:int(1)}) 
    sortedwords=[k for k in dic.keys()] #alternatively, can do list(dic)
    return sortedwords 

"""


  #=======================================================================================================================#

def firststage():
        

    def ridplurals(e):
        global a
        a=[]
        for i in e:
            words=i.split(" ")
            postags=nltk.pos_tag([i for i in words if i]) # rid empty strings 
            if len(postags)>1:
                word1,word2=postags
                word1,postags1=word1
                word2,postags2=word2
                if (postags1=="NN" or postags1=="NNS") and (postags2!="NN" or postags2!="NNS") : 
                    finalword=pattern.en.singularize(word1)+" "+(word2)
                elif (postags2=="NN" or postags2=="NNS") and (postags1!="NN" or postags1!="NNS"): 
                    finalword=word1+" "+pattern.en.singularize(word2)
                elif (postags2=="NN" or postags2=="NNS") and (postags1=="NN" or postags1=="NNS"):
                    finalword=pattern.en.singularize(word1)+" "+pattern.en.singularize(word2)
                else: 
                    finalword=i 
            else: 
                finalword=i

            a.append(finalword) 
        assert len(a)==len(tfidf)
        return a 

    #=======================================================================================================================#

    src="/Users/lucy/Desktop/assortedcodes/15april.csv"
    ori="/Users/lucy/Desktop/assortedcodes/intext15april.csv"


    external=set()
    internal=set()
    with open(src,"r", encoding="utf-8", errors="ignore") as f: 
        r=csv.reader(f)
        for row in r: 
            if row[2]=="x": 
                if len(row[0].split(" "))>1:
                    external.add(row[0].split(" ")[1])
                else: 
                    external.add(row[0])
            if row[2]=="i": 
                if len(row[0].split(" "))>1:
                    internal.add(row[0].split(" ")[1]) 
                else: 
                    internal.add(row[0])
            if row[2]=="1": 
                if len(row[0].split(" "))>1:
                    internal.add(row[0].split(" ")[0])
                else: 
                    internal.add(row[0])
            if row[2]=="2":
                if len(row[0].split(" "))>1:
                    external.add(row[0].split(" ")[0])
                else: 
                    external.add(row[0])
        f.close()


    # test print external and internal words set 
    def testprint(): 
        with open("testprintintext30April.csv","w", encoding="utf-8", errors="ignore") as f: 
            r=csv.writer(f)
            for element in external: 
                r.writerow([element,"external"])
            for element in internal: 
                r.writerow([element,"internal"])
        f.close()

    testprint()

    external=set()
    internal=set()

    with open("testprintintext30April(1).csv","r", encoding="utf-8", errors="ignore") as f: 
        r=csv.reader(f)
        for row in r: 
            if row[1]=="external": 
                external.add(row[0])
            if row[1]=="internal": 
                internal.add(row[0])
        f.close()


    #testprint()

    plist=[]
    label=[]
    tfidf=[]
    index=[]

    i=0
    with open(ori, "r",encoding="utf-8", errors="ignore") as f: 
        r=csv.reader(f)
        for row in r: 
            i+=1
            plist.append(row[0])
            tfidf.append(row[2])
            index.append(i)
            #print(row[0].split(" "))
            if len(row[0].split(" "))>1: 

                if row[0].split(" ")[0] in external and row[0].split(" ")[0] in internal or row[0].split(" ")[1] in external and row[0].split(" ")[0] in internal: 
                    label.append(".")
                elif row[0].split(" ")[0] in external or row[0].split(" ")[1] in external: 
                    label.append("ext")
                elif row[0].split(" ")[0] in internal or row[0].split(" ")[1] in internal:
                    label.append("int")
                else:
                    label.append(".")
            else: 
                if row[0] in external and row[0] in external in internal or row[0] in external and row[0] in internal: 
                    label.append("int")
                elif row[0] in external: 
                    label.append("ext")
                elif row[0] in internal: 
                    label.append("int")
                else: 
                    label.append(".")
        f.close()
    ridplurals(plist)


    """
    p=[]
    for i in range(len(plist)): 
        z=(plist[i],index[i])
        p.append(z)
    removeduplicates(p)

    """


    final="/Users/lucy/Desktop/assortedcodes/15aprilfinal(1).csv" 

    f=zip(a, label, tfidf)

    with open(final, "w") as file1: 
        fwriter = csv.writer(file1)
        for i in f: 
            fwriter.writerow(i)


"""

For second pass, want to read in annotated changes in 15aprilfinal and the testprinttext file,
output new final sheet 

"""


class secondpass: 
    def __init__(self):
        self.a="/Users/lucy/Desktop/assortedcodes/testprintintext30April(1).csv" 
        #a: phrases
        self.b="/Users/lucy/Desktop/assortedcodes/testprintintextupdatednew.csv"
        #b: words
        self.internal=set()
        self.external=set()

    def genvocab(self): 
        with open(self.a, "r",encoding="utf-8", errors="ignore") as f: 
            r=csv.reader(f)
            for i in r: 
                
                if i[1]=="nt": 
                    if len(i[0].split(" "))>0:
                        self.internal.add(i[0].split(" ")[1])
                    else: 
                        self.internal.add(i[0])
                elif i[1]=="xt": 
                    if len(i[0].split(" "))>0:
                        self.external.add(i[0].split(" ")[1])
                    else:
                        self.external.add(i[0]) 

                if i[1]=="n": 
                    if len(i[0].split(" "))>1:
                        self.internal.add(i[0].split(" ")[1])
                    else: 
                        self.internal.add(i[0].split(" ")[0])

                elif i[1]=="x": 
                    if len(i[0].split(" "))>1:
                        self.external.add(i[0].split(" ")[0])
                    else: 
                        self.external.add(i[0].split(" ")[0])

            f.close()
        with open(self.b, "r",encoding="utf-8", errors="ignore") as f: 
            r=csv.reader(f)
            for i in r: 
                if i[1]=="internal": 

                    self.internal.add(i[0])
                elif i[1]=="external": 
                    self.external.add(i[0])
            f.close()

    #completed adding elements to the internal and external categories, 
    #want to correct inflection error with pattern.en and 
    def output(self): 
        setofallphrases=set()
        self.genvocab()
        list1=[]
        list2=[]
        list3=[]
        with open(self.a, "r",encoding="utf-8", errors="ignore") as f: 
            r=csv.reader(f)
            for i in r: 
                if i[0].split(" ")[0] not in setofallphrases: 
                    setofallphrases.add(i[0].split(" ")[0])
                if len(i[0].split(" "))>1:
                    if i[0].split(" ")[1] not in setofallphrases: 
                        setofallphrases.add(i[0].split(" ")[0])
                # correct mistake 
                if i[0].split(" ")[0].endswith("s"): 
                    x=i[0].split(" ")[0]+"s"
                    if x in setofallphrases: 
                        i[0]=x+" "+i[0].split(" ")[1]
                else: 
                    pass 

                if len(i[0].split(" "))>1:
                    if i[0].split(" ")[1].endswith("s"): 
                        x=i[0].split(" ")[1]+"s"
                        if x in setofallphrases: 
                            i[0]=i[0].split(" ")[0]+" "+x
                        else: 
                            pass
                    else: 
                        pass

                else: 
                    if i[0].split(" ")[0].endswith("s"): 
                        x=i[0].split(" ")[0]+"s"
                        if x in setofallphrases: 
                            i[0]=i[0].split(" ")[0]+" "+x
                        else: 
                            pass
                    else: 
                        pass


                #
                if len(i[0].split(" "))>1:

                    if (i[0].split(" ")[0] in self.internal and i[0].split(" ")[0] in self.external) or (i[0].split(" ")[1] in self.internal and i[0].split(" ")[1] in self.external): 
                        list1.append(i[0])
                        list2.append(".")
                        list3.append(i[2])
                        print(i[0])

                    elif i[0].split(" ")[0] in self.internal:
                        list1.append(i[0])
                        list2.append("internal")
                        list3.append(i[2])

                    elif i[0].split(" ")[0] in self.external:
                        list1.append(i[0])
                        list2.append("external")
                        list3.append(i[2])
                    elif i[0].split(" ")[1] in self.external:
                        list1.append(i[0])
                        list2.append("external")
                        list3.append(i[2])
                    elif i[0].split(" ")[1] in self.internal: 
                        list1.append(i[0])
                        list2.append("internal")
                        list3.append(i[2])
                    else: 

                        list1.append(i[0])
                        list2.append(".")
                        list3.append(i[2])

                else: 
                    if i[0].split(" ")[0] in self.external:
                        list1.append(i[0])
                        list2.append("external")
                        list3.append(i[2])
                    
                    if i[0].split(" ")[0] in self.internal: 
                        list1.append(i[0])
                        list2.append("internal")
                        list3.append(i[2])

                    else: 
                        list1.append(i[0])
                        list2.append(".")
                        list3.append(i[2])



            f.close()


        #CAUTION

        #!!!!!!!!!!!!!!
        #CHANGE EVERYTIME
        d="/Users/lucy/Desktop/assortedcodes/bfile(1).csv"
        y=zip(self.internal,["internal"]*len(self.internal))
        v=zip(self.external,["external"]*len(self.external))
        with open(d, "w",encoding="utf-8", errors="ignore") as f: 
            fwriter = csv.writer(f)
            for e in y: 
                fwriter.writerow(e)
            for e in v: 
                fwriter.writerow(e)
            f.close()

        # final output file 

        
        c="/Users/lucy/Desktop/assortedcodes/afile(1).csv"
        z=zip(list1,list2,list3)
        with open(c, "w",encoding="utf-8", errors="ignore") as f: 
            fwriter = csv.writer(f)
            for e in z: 
                fwriter.writerow(e)
            f.close()

        
            
x=secondpass() 
x.output()
                    


                


        




         


            

                


