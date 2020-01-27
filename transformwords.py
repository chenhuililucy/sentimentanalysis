
"""

Modelling based on context free grammar: Phrase-Structure-Grammars or BackusNaur Form or BNF 

* Subcategorizations and dependency relations:  eg "want" + infinitive

NOUNS

* A noun phrase is often surrounded by a group of noun words sometimes called the "noun group"
* Noun phrase + verb
* Preoposed or postposed sentences (ie. you can say that 'On September 17th, I'd like tofly from Atlanta to Denver": On September 17th can be anywhere in the sentence
                                    whereas a sentence that says 'On September, I'd like to fly seventeenth from Atalanta to Denver does not make sense)

* A typical noun phrase consists of a noun (the head of the phrase) together with zero or more dependents of various types. (These dependents, since they modify a noun, are called adnominal.) The chief types of these dependents are:

*determiners, such as the, this, my, some, Jane's
*attributive adjectives, such as large, beautiful, sweeter
*adjective phrases and participial phrases, such as extremely large, hard as nails, made of wood, sitting on the step
*noun adjuncts, such as college in the noun phrase a college student
*nouns in certain oblique cases, in languages which have them, such as German des Mannes ("of the man"; genitive form)
*prepositional phrases, such as in the drawing room, of his aunt
*adnominal adverbs and adverbials, such as (over) there in the noun phrase the man (over) there
*relative clauses, such as which we noticed
*other clauses serving as complements to the noun, such as that God exists in the noun phrase the belief that God exists
*infinitive phrases, such as to sing well and to beat in the noun phrases a desire to sing well and the man to beat
                                              


1.Amplifier/Negator: Transform verbs into nouns, adjectives,

                     OR Transform adjectives into verbs, nouns 


"""

import nltk 
import csv
from nltk.corpus import wordnet as wn
import pattern
from pattern.text.en import singularize
from pattern.text.en import pluralize
from pattern.en import pluralize, singularize
from pattern.en import conjugate, lemma, lexeme,PRESENT,SG
import random




"""
Pos tag output phrases and words and write them to a new csv file 

Dependencies: 
* csv file with list of performance words 
"""

def posttagperformance(): 
    list=[]
    word1list=[] 
    word2list=[]
    tag1list=[]
    tag2list=[]
    

    with open("postag.csv", "r",encoding="utf-8", errors="ignore") as csvfile: 
        freader = csv.reader(csvfile)
        for row in freader: 
            words=row[0].split(" ")
            postags=nltk.pos_tag(words)
            if len(postags)>1: 
                word1,word2=postags
                word1,tag1=word1
                word2,tag2=word2
                
            else: 
                word1=postags
                print(word1)
                n=0
                for word1[n] in word1: 
                    print(word1[n])
                    (word1,tag1)=(word1[n])
                    word2="."
                    tag2="."
                    n+=1

                
            word1list.append(word1)
            word2list.append(word2)
            tag1list.append(tag1)
            tag2list.append(tag2)

            result= [(word, tag) for word, tag in postags]

            #print(word1)
            #if word2: 
                #print(word2)

            list.append(result)
         
        p=zip(word1list,tag1list,word2list,tag2list)    

            
        csvfile.close()
        
    with open("ngramrel2csvout.csv","w",encoding="utf-8", errors="ignore") as csvfile:
        fwriter = csv.writer(csvfile)
        for i in p:
            fwriter.writerow(i)
        csvfile.close()


"""
Want to convert NNS to NN and vice versa and store in a new csv
Want to convert VBG and VBN to every tense possible to observe possible relationships
"""




def convertsingular(): 

    testVBG=False  

    newword1list=[] 
    newword2list=[]
    newtag1list=[]
    newtag2list=[]
    VBG=[]
    VBG1=[]
    VBGorVBN=[]
    
    with open("ngramrel2csvout.csv","r",encoding="utf-8", errors="ignore") as csvfile:
        freader = csv.reader(csvfile)
        for row in freader: 
            if row[1]=="NN":
                newword1=pattern.en.pluralize(row[0])
                newword1list.append(newword1)
                newword2list.append(row[2])
                # postags=nltk.pos_tag(newword1)
                # # if len(postags)>1: 
                # #     word1,word2=postags
                # #     word1,tag1=word1
                # #     word2,tag2=word2
                    
                # # else: 
                # word1=postags
                # print(word1)
                # n=0
                # for word1[n] in word1: 
                #     print(word1[n])
                #     (word1,tag1)=(word1[n])
                #     word2="."
                #     tag2="."
                #     n+=1
                
                newtag1list.append("NNS")
                newtag2list.append(row[3])

             
            elif row[1]=="VBG":
                
                #aftert test VBG, we have found that 
                #converting VBG to other verb forms dont make 
                #a lot of sense 

                if testVBG:
                
                    lemma1=lemma(row[0])
                    newword1=lexeme(verb=lemma1)
                    #print(newword1)
                    for word in newword1: 
                        VBG.append(word)
                        VBG1.append(row[2])
                        VBGorVBN.append(row[1])


                else: 
                    pass

            elif row[1]=="VBN": 

                if testVBG: 

                    lemma1=lemma(row[0])
                    newword1=lexeme(verb=lemma1)
                    #print(newword1)
                    for word in newword1: 
                        VBG.append(word)
                        VBG1.append(row[2])
                        print(row[2])
                        VBGorVBN.append(row[1])
                
                else: 
                    pass


        csvfile.close()

    with open("ngramrel2csvout.csv","r",encoding="utf-8", errors="ignore") as csvfile:
        freader = csv.reader(csvfile)
        for row in freader: 
            if row[1]=="NNS":
                newword1=pattern.en.singularize(row[0])
                newword1list.append(newword1)
                newword2list.append(row[2])
                newtag1list.append("NN")
                newtag2list.append(row[3])
        csvfile.close()

    
    with open("ngramrel2csvout.csv","r",encoding="utf-8", errors="ignore") as csvfile:
        freader = csv.reader(csvfile)
        for row in freader: 
            if row[3]=="NNS":
                newword2=pattern.en.singularize(row[2])
                newword2list.append(newword1)
                newword1list.append(row[0])
                newtag2list.append("NNS")
                newtag1list.append(row[1])

            if row[1]=="NN":
                newword1=pattern.en.pluralize(row[0])
                newword1list.append(newword1)
                newword2list.append(row[2])
                # postags=nltk.pos_tag(newword1)
                # # if len(postags)>1: 
                # #     word1,word2=postags
                # #     word1,tag1=word1
                # #     word2,tag2=word2
                    
                # # else: 
                # word1=postags
                # print(word1)
                # n=0
                # for word1[n] in word1: 
                #     print(word1[n])
                #     (word1,tag1)=(word1[n])
                #     word2="."
                #     tag2="."
                #     n+=1
                
                newtag1list.append("NNS")
                newtag2list.append(row[3])

             
            elif row[3]=="VBG" or "VBN":
                
                #aftert test VBG, we have found that 
                #converting VBG to other verb forms dont make 
                #a lot of sense 

                if testVBG:
                
                    lemma1=lemma(row[2])
                    newword1=lexeme(verb=lemma1)
                    #print(newword1)
                    for word in newword1: 
                        VBG.append(row[0])
                        VBG1.append(word)
                        VBGorVBN.append(row[3])


                else: 
                    pass

      
    
    with open("ngramrel2csvout.csv","r",encoding="utf-8", errors="ignore") as csvfile:
        freader = csv.reader(csvfile)
        for row in freader: 
            if row[3]=="NN":
                newword2=pattern.en.pluralize(row[2])
                newword2list.append(newword1)
                newword1list.append(row[0])
                newtag2list.append("NNS")
                newtag1list.append(row[1])
        csvfile.close() 

    
    p=zip(newword1list,newtag1list,newword2list,newtag2list)    
    a=zip(VBG,VBG1,VBGorVBN)


    #print(newword1list)

    with open("trial.csv","w") as csvfile1:
        fwriter1 = csv.writer(csvfile1)
        for word in p: 
            fwriter1.writerow(word)

    with open("verb.csv","w") as csvfile: 
        fwriter=csv.writer(csvfile)
        for word in a: 
            fwriter.writerow(word)


#convertsingular()
                



def posttagamplifiernegator(): 
    list=[]
    word1list=[] 
    word2list=[]
    tag1list=[]
    tag2list=[]
    

    with open("postagampneg.csv", "r",encoding="utf-8", errors="ignore") as csvfile: 
        freader = csv.reader(csvfile)
        for row in freader: 
            words=row[0].split(" ")
            postags=nltk.pos_tag(words)
            if len(postags)>1: 
                word1,word2=postags
                word1,tag1=word1
                word2,tag2=word2
                
            else: 
                word1=postags
                print(word1)
                n=0
                for word1[n] in word1: 
                    print(word1[n])
                    (word1,tag1)=(word1[n])
                    word2="."
                    tag2="."
                    n+=1

                
            word1list.append(word1)
            word2list.append(word2)
            tag1list.append(tag1)
            tag2list.append(tag2)

            result= [(word, tag) for word, tag in postags]

            #print(word1)
            #if word2: 
                #print(word2)

            list.append(result)
         
        p=zip(word1list,tag1list,word2list,tag2list)    

            
        csvfile.close()
        
    with open("postagampnegout.csv","w",encoding="utf-8", errors="ignore") as csvfile:
        fwriter = csv.writer(csvfile)
        for i in p:
            fwriter.writerow(i)
        csvfile.close()

posttagamplifiernegator()

        


def reversedirection(): 
    pass



def nounify(verb_word):
    """ Transform a verb to the closest noun: die -> death """
    verb_synsets = wn.synsets(verb_word, pos="v")

    # Word not found
    if not verb_synsets:
        return []

    # Get all verb lemmas of the word
    verb_lemmas = [l for s in verb_synsets \
                   for l in s.lemmas if s.name.split('.')[1] == 'v']

    # Get related forms
    derivationally_related_forms = [(l, l.derivationally_related_forms()) \
                                    for l in verb_lemmas]

    # filter only the nouns
    related_noun_lemmas = [l for drf in derivationally_related_forms \
                           for l in drf[1] if l.synset.name.split('.')[1] == 'n']

    # Extract the words from the lemmas
    words = [l.name for l in related_noun_lemmas]
    len_words = len(words)

    # Build the result in the form of a list containing tuples (word, probability)
    result = [(w, float(words.count(w))/len_words) for w in set(words)]
    result.sort(key=lambda w: -w[1])

    # return all the possibilities sorted by probability
    return result