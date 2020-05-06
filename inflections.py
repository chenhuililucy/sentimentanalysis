


""" 
Find all possible inflections of a phrase 

""" 

src= "/Users/lucy/Desktop/assortedcodes/afile(1).csv"

l1=[]
l2=[] 
l3=[]
l4=[]

with open(src,"r", encoding="utf-8", errors="ignore") as f: 
    r=csv.reader(f)
    for row in r: 
        l1.append(row[0])
        l2.append(row[1])
        l3.append(row[2])
        l4.append(row[3])

def transformintobothpluralsandsingular(classifyingphraselist): 
    finalphrase=[]
    cha=[]
    for item in classifyingphraselist: 
        words=item.split(" ")
        postags=nltk.pos_tag([i for i in words if i]) # rid empty strings 
        if len(postags)>1:
            word1,word2=postags
            word1,postags1=word1
            word2,postags2=word2
            if postags1=="NN": 
                finalword1=pattern.en.pluralize(word1)
                if postags2=="NN": 
                    finalword2=pattern.en.pluralize(word2)
                    finalphrase1=finalword1+" "+finalword2
                    finalphrase2=finalword1+" "+word2
                else: 
                    if postags2=="NN": 
                        finalword2=pattern.en.pluralize(word2)
                        finalphrase1= word1+" "+finalword2
                    else: 
                        pass
                        #unfinihsed














