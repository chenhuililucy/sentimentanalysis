
"""
Final cleaning of performance dictionary as of 31 May

"""



import csv
import nltk
import pattern
from pattern.text.en import singularize
from pattern.text.en import pluralize
from pattern.en import pluralize, singularize, conjugate
from pattern.en import conjugate, lemma, lexeme,PRESENT,SG
import os
import re



# fix amp neg dictionary
def ampneg():
# Just to make it a bit more readable
    WN_NOUN = 'n'
    WN_VERB = 'v'
    WN_ADJECTIVE = 'a'
    WN_ADJECTIVE_SATELLITE = 's'
    WN_ADVERB = 'r'
    
    def convert(word, from_pos, to_pos):    
        """ Transform words given from/to POS tags """
    
        synsets = wn.synsets(word, pos=from_pos)
    
        # Word not found
        if not synsets:
            return []
    
        # Get all lemmas of the word (consider 'a'and 's' equivalent)
        # the logic is the following
        # for s in synsets: 
        # for l i s.lemmas


        for s in synsets: 
            print(s.name())
        
        lemmas = [l for s in synsets
                    for l in s.lemmas() 
                    if s.name().split('.')[1] == from_pos
                        or from_pos in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE)
                            and s.name().split('.')[1] in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE)]
    
        # Get related forms=> nested list
        derivationally_related_forms = [(l, l.derivationally_related_forms()) for l in lemmas]
        #print(derivationally_related_forms)
        #debug 
        related_noun_lemmas=[]
        for drf in derivationally_related_forms: #list in nested list 
            #print(drf)
            for l in drf[1]: 
                if checklemma(l.name(),to_pos): 
                    print(l.name())
                    return l.name()



    import nltk
    from nltk.corpus import brown
    from collections import Counter, defaultdict


    def checklemma(wordspecific, to_pos): 
        # x is a dict which will have the word as key and pos tags as values 
        x = defaultdict(list)

        # looping for first 100 words and its pos tags
        for word, pos in brown.tagged_words()[1:100]:
            if pos not in x[word]:        # to append one tag only once
                x[word].append(pos)       # adding key-value to x

        if (x[wordspecific])==to_pos:
    # to print the pos tags for the word 'further'
            return True
    #['RBR']


            

        """
                #print(l.lemmas())
                #print(l.name()) #l.name returns the actual word
                if len(l.split("."))>=2:
                    if l.split(".")[1]==to_pos or to_pos in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE) and l.split('.')[1] in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE): 
                        related_noun_lemmas.append(l)
                else: #debug
                    pass#print(l)

        '''           
        # filter only the desired pos (consider 'a' and 's' equivalent)
        related_noun_lemmas = [l for drf in derivationally_related_forms
                                for l in drf[1] 
                                if synsets(l).name().split('.')[1] == to_pos
                                    or to_pos in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE)
                                        and l.synsets().name().split('.')[1] in (WN_ADJECTIVE, WN_ADJECTIVE_SATELLITE)]
    

        '''

        # Extract the words from the lemmas
        words = [l.name() for l in related_noun_lemmas] 
        len_words = len(words)
    
        # Build the result in the form of a list containing tuples (word, probability)
        result = [(w, float(words.count(w))/len_words) for w in set(words)]
        result.sort(key=lambda w: -w[1])
    
        print(result)
        # return all the possibilities sorted by probability
        return result.name().split(" ")[0]


        """

    #utility function: converting adverbs to their root adjetive
    def adverbtoadjective(word): 
        possible_adj = []
        for ss in wn.synsets(word):
            for lemmas in ss.lemmas(): # all possible lemmas
                for ps in lemmas.pertainyms(): # all possible pertainyms
                    possible_adj.append(ps.name())
        print("advtoadj")
        print(possible_adj[0])
        return possible_adj[0]


    #utility function: converting adjectives to their adverb
    from difflib import SequenceMatcher
    from gensim.models.keyedvectors import KeyedVectors
    glove_filename = '/Users/lucy/Desktop/assortedcodes/glove-word2vec.6B.100d.txt'
    model = KeyedVectors.load_word2vec_format(glove_filename, binary=False)

    def close_adv(input, num=5, model_topn=50):
        positive = [input, 'happily']
        negative = [       'happy']
        input=re.match("/^[A-Z]+$/i",input)
        if input not in model.wv.vocab: 
            return None
        all_similar = model.most_similar(positive, negative, topn=model_topn)

    def score(candidate):
        ratio = SequenceMatcher(None, candidate, input).ratio()
        looks_like_adv = 1.0 if candidate.endswith('ly') else 0.0
        return ratio + looks_like_adv

    close = sorted([(word, score(word)) for word, _ in all_similar], key=lambda x: -x[1])
    print(close[:num])
    print("close_adv")
    return close[:num]



    src= "/Users/lucy/Desktop/assortedcodes/afile(1).csv"
    src= "/Users/lucy/Desktop/assortedcodes/intext15april.csv"



    classifyingphraselist=[]

    with open(src,"r", encoding="utf-8", errors="ignore") as f: 
        r=csv.reader(f)
        for row in r: 
            classifyingphraselist.append(row[0])




    """
    Pos tag output phrases and words and write them to a new csv file 

    Dependencies: 
    * csv file with list of performance words 
    """

    # def posttagperformance(): 
    #     list=[]
    #     word1list=[] 
    #     word2list=[]
    #     tag1list=[]
    #     tag2list=[]
    #     with open(src, "r",encoding="utf-8", errors="ignore") as csvfile: 
    #         freader = csv.reader(csvfile)
    #         for row in freader: 
    #             words=row[0].split(" ")
    #             postags=nltk.pos_tag(words)
    #             if len(postags)>1: 
    #                 word1,word2=postags
    #                 word1,tag1=word1
    #                 word2,tag2=word2
    #             else: 
    #                 word1=postags
    #                 #print(word1)
    #                 n=0
    #                 for word1[n] in word1: 
    #                     #print(word1[n])
    #                     (word1,tag1)=(word1[n])
    #                     word2="."
    #                     tag2="."
    #                     n+=1
    #             word1list.append(word1)
    #             word2list.append(word2)
    #             tag1list.append(tag1)
    #             tag2list.append(tag2)
    #             result= [(word, tag) for word, tag in postags]
    #             list.append(result)
            
    #         p=zip(word1list,tag1list,word2list,tag2list)    

                
    #         csvfile.close()
            
        # with open("afile(1)postagged.csv","w",encoding="utf-8", errors="ignore") as csvfile:
        #     fwriter = csv.writer(csvfile)
        #     for i in p:
        #         fwriter.writerow(i)
        #     csvfile.close()




    from word_forms.word_forms import get_word_forms


    a=set()
    b=set()

    with open("/Users/lucy/Desktop/assortedcodes/finalperfdict.csv","r") as c:
        records=csv.reader(c)
        for row in records: 
            if row[2]=="1": 
                a.add(row[0])
            elif row[2]=="2": 
                b.add(row[0])
            elif row[2]=="3": 
                a.add(row[0].split(" ")[1])
            elif row[2]=="4": 
                b.add(row[0].split(" ")[1])
                if IndexError: 
                    print(row[0])
            elif row[2]=="5": 
                a.add(row[0].split(" ")[0])
            elif row[2]=="6": 
                b.add(row[0].split(" ")[0])
            elif row[2]=="p": 
                a.add(row[0])
            elif row[2]=="m": 
                a.add(row[0])

    l=[]
    for i in a:
        i=i.lower()
        postags=nltk.pos_tag([i]) # rid empty strings
        word1=postags
        print(word1)
        for w in word1:
            (word1,tag1)=w
        if tag1=="NN": 
            f1=pattern.en.pluralize(word1)
            l.append(f1)
            l.append(word1)


        elif tag1=="NNS": 
            f1=pattern.en.singularize(word1)
            l.append(f1)
            l.append(word1)

        elif tag1=="VBG" or tag1=="VBN" or tag1=="VBZ" or tag1=="VB" or  tag1=="VBZ": 
            #finalword1=lemmatize(word1)
            f1=conjugate(word1,tense="past")
            f4=conjugate(word1,tense="past",person=2)
            f2=conjugate(word1,tense="infinitive")
            f3=conjugate(word1,tense="present",person=3)
            f5=conjugate(word1,tense="present",person=2)
            l.extend([f1,f2,f3,f4,f5])
            l.append(word1)

        elif tag1=="JJ": 
            f1=close_adv(word1) 
            l.append(word1)
            l.append(f1)

        elif tag1=="RB":
            f1=close_adv(word1) 
            l.append(word1)
            l.append(f1)

        #for k,v in get_word_forms(i).items():
            #l.append(v)
        
    p=[]
    for i in b:
        i=i.lower()
        postags=nltk.pos_tag([i]) # rid empty strings
        word1=postags
        print(word1)
        for w in word1:
            (word1,tag1)=w
        if tag1=="NN": 
            f1=pattern.en.pluralize(word1)
            p.append(f1)
            p.append(word1)


        elif tag1=="NNS": 
            f1=pattern.en.singularize(word1)
            p.append(f1)
            p.append(word1)

        elif tag1=="VBG" or tag1=="VBN" or tag1=="VBZ" or tag1=="VB" or  tag1=="VBZ": 
            #finalword1=lemmatize(word1)
            f1=conjugate(word1,tense="past")
            f4=conjugate(word1,tense="past",person=2)
            f2=conjugate(word1,tense="infinitive")
            f3=conjugate(word1,tense="present",person=3)
            f5=conjugate(word1,tense="present",person=2)
            p.extend([f1,f2,f3,f4,f5])
            p.append(word1)

        elif tag1=="JJ": 
            f1=close_adv(word1) 
            p.append(word1)
            p.append(f1)

        elif tag1=="RB":
            f1=close_adv(word1) 
            p.append(word1)
            p.append(f1)

    """

    for i in b: 
        for o in get_word_forms(i).items():
            k,v=o
            if v is not None:
                for item in v:
                    p.append(item)

    """

    """

    with open("amplifiedfinal(1).csv","w",encoding="utf-8", errors="ignore") as csvfile:
        fwriter = csv.writer(csvfile)
        for i in l:
            if i is not None:
                fwriter.writerow([i])
        csvfile.close()

    """


    with open("negatorfinal(1).csv","w",encoding="utf-8", errors="ignore") as csvfile:
        fwriter = csv.writer(csvfile)
        for i in p:
            if i is not None:   
                fwriter.writerow([i])
        csvfile.close()



"""

PART II

"""

    #with open("negatorfinal(1).csv","w",encoding="utf-8", errors="ignore") as csvfile:


from collections import defaultdict

d=defaultdict(int)

with open("/Users/lucy/Desktop/assortedcodes/Ngramreljames.csv","r",encoding="utf-8", errors="ignore") as csvfile:
    freader = csv.reader(csvfile)
    for i in freader:
        if i[0] is None: 
            pass
        if len(i[0].split(" "))>1:
            d[i[0].split(" ")[0]]+=1
            d[i[0].split(" ")[1]]+=1
        elif len(i[0].split(" "))==1: 
            d[i[0].split(" ")[0]]+=1

    csvfile.close()
di=[k for k, v in sorted(d.items(), key=lambda item: item[1])][::-1]


"""

with open("performancelabeling.csv","w",encoding="utf-8", errors="ignore") as csvfile:
    fwriter = csv.writer(csvfile)
    for i in di:
        if i is not None:   
            fwriter.writerow([i])
    csvfile.close()

"""

negimp=set()
posimp=set()
neg=set()
pos=set()

with open("/Users/lucy/Desktop/assortedcodes/performancelabellingpass1.csv","r",encoding="utf-8", errors="ignore") as csvfile:
    freader = csv.reader(csvfile)
    for i in freader:
        if i[0] is None: 
            pass
        if i[1]=="4": 
            negimp.add(i[0])
        if i[1]=="3": 
            posimp.add(i[0])
        if i[1]=="2": 
            neg.add(i[0])
        if i[1]=="1": 
            pos.add(i[0])

        """     
        if len(i[0].split(" "))>1:

            d[i[0].split(" ")[0]]+=1
            d[i[0].split(" ")[1]]+=1
        elif len(i[0].split(" "))==1: 
            d[i[0].split(" ")[0]]+=1
        """


l=[]
l1=[]
l2=[]
l3=[]
l4=[]

with open("/Users/lucy/Desktop/assortedcodes/Ngramreljames.csv","r",encoding="utf-8", errors="ignore") as csvfile:
    freader = csv.reader(csvfile)
    for i in freader:
        if i[0] is None: 
            pass
#        
        if len(i[0].split(" "))>1:
            if i[0].split(" ")[0] in negimp or i[0].split(" ")[1] in negimp:
                l1.append(i[0])
                l2.append(i[1])
                l3.append(i[2])
                l.append(i[3])
                l4.append("neg")
                continue

            elif i[0].split(" ")[0] in posimp or i[0].split(" ")[1] in posimp:
                l1.append(i[0])
                l2.append(i[1])
                l3.append(i[2])
                l4.append(i[4])
                l.append("pos")
                continue

            elif i[0].split(" ")[0] in neg or i[0].split(" ")[1] in neg:
                l1.append(i[0])
                l2.append(i[1])
                l3.append(i[2])
                l.append(i[3])
                l4.append("neg")

                continue

            elif i[0].split(" ")[0] in pos or i[0].split(" ")[1] in pos:
                l1.append(i[0])
                l2.append(i[1])
                l3.append(i[2])
                l.append(i[3])
                l4.append("pos")

                continue

            else:
                l1.append(i[0])
                l2.append(i[1])
                l3.append(i[2])
                l.append(i[3])
                l4.append(".")

        else: 
            if i[0] in negimp or i[0] in neg:
                l1.append(i[0])
                l2.append(i[1])
                l3.append(i[2])
                l.append(i[3])
                l4.append("neg")
                

            elif i[0] in posimp or i[0] in pos:
                l1.append(i[0])
                l2.append(i[1])
                l3.append(i[2])
                l.append(i[3])
                l4.append("pos")

            else:
                l1.append(i[0])
                l2.append(i[1])
                l3.append(i[2])
                l.append(i[3])
                l4.append(".")
        """ 

            d[i[0].split(" ")[0]]+=1
            d[i[0].split(" ")[1]]+=1
        elif len(i[0].split(" "))==1: 
            d[i[0].split(" ")[0]]+=1

        """

z=zip(l1,l2,l3,l,l4)

with open("performancelabeling(f).csv","w",encoding="utf-8", errors="ignore") as csvfile:
    fwriter = csv.writer(csvfile)
    for i in z:
        if i is not None:   
            fwriter.writerow(i)
    csvfile.close()
