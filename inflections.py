



import csv
import nltk
import pattern
from pattern.text.en import singularize
from pattern.text.en import pluralize
from pattern.en import pluralize, singularize, conjugate
from pattern.en import conjugate, lemma, lexeme,PRESENT,SG
import os
import re

#Please import pattern .en from the nodebox lib 
os.chdir("/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7")
# please modify the source directory to where the main csv with all the words are stored
src= "/Users/lucy/Desktop/assortedcodes/negativeperf.csv" 
#os.chdir("/Users/lucy/Desktop/assortedcodes/builddic/")




""" 
Find all possible inflections of a phrase 
""" 


# utility function: converting noun to adjective and vice versa. 
from nltk.corpus import wordnet as wn
import re 
 
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
        return True
        

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

def out(classifyingphraselist): 
    global word1list
    global word2list
    global amended
    finalphrase=[]
    cha=[] #store matching for first word 
    cha1=[] #store matching for second word 
    amended=[]
    x=0 
    y=len(classifyingphraselist)
    for item in classifyingphraselist: 
        words=item.split(" ")
        postags=nltk.pos_tag([i for i in words if i]) # rid empty strings

        x+=1 
        
        # dump items 

        """
        for item in cha1: 
            for item1 in cha: 
                full=item+" "+item1
                amended.append(full)


        """
        cha=[]
        cha1=[]

        if len(postags)>1:
        #[('And', 'CC'), ('now', 'RB')]
            word1,word2=postags
            word1,postags1=word1
            word2,postags2=word2
            # if both word1 and word2 are nouns, then 4 matches
            # if either one is noun, then 2 matches 
            # else pass
            if postags1=="NN": 
                f1=pattern.en.pluralize(word1)
                f2=convert(word1, "n", "JJ")
                cha.extend([f1,f2])
                cha.append(word1)
            
            elif postags1=="NNS": 
                f1=pattern.en.singularize(word1)
                f2=convert(word1, "n", "JJ")
                cha.extend([f1,f2])
                cha.append(word1)

            elif postags1=="VBG" or postags1=="VBN" or postags1=="VBZ" or postags1=="VB" or  postags1=="VBD": 
                #finalword1=lemmatize(word1)
                f1=conjugate(word1,tense="past")
                f4=conjugate(word1,tense="past",person=2)
                f2=conjugate(word1,tense="infinitive")
                f3=conjugate(word1,tense="present",person=3)
                f5=conjugate(word1,tense="present",person=2)
                #f4=en.verb.present_participle(word1)
                #f5=en.verb.past(word1)
                cha.extend([f1,f2,f3,f4,f5])

            elif postags1=="JJ": 
                f2=convert(word1, "a", "NN")
                f3=convert(word1, "a", "NNS")
                f1=close_adv(word1) 
                cha.append(word1)
                cha.extend([f1,f2])

            elif postags1=="RB": 
                f1=close_adv(word1) 
                cha.append(word1)
                cha.append(f1)

            else: 
                cha.append(word1)

            

            # =============================================== #
            if postags2=="NN": 
                
                finalword2=pattern.en.pluralize(word2)
                cha1.append(finalword2)
                cha1.append(word2)

            elif postags2=="NNS": 
                finalword2=pattern.en.singularize(word2)
                cha1.append(finalword2)
                cha1.append(word2)
                #finalphrase.extend([finalword1+" "+finalword2,finalword1+" "+word2,word1+" "+finalword2,word1+" "+word2])

            #else: 
                #finalphrase.extend([finalword1+" "+word2,word1+" "+word2])


            elif postags2=="VBG" or postags2=="VBN" or postags2=="VBZ" or postags2=="VB" or  postags2=="VBZ": 
                #finalword1=lemmatize(word1)
                #finalword1=en.verb.present(word2)
                f1=conjugate(word2,tense="past")
                f4=conjugate(word2,tense="past",person=2)
                f2=conjugate(word2,tense="infinitive")
                f3=conjugate(word2,tense="present",person=3)
                f5=conjugate(word2,tense="present",person=2)
                cha1.extend([f1,f2,f3,f4,f5])

            elif postags2=="JJ": 
                
                finalword2=close_adv(word2) 
                cha1.append(word2)
                cha1.append(finalword2)

            elif postags2=="RB":
                finalword2=close_adv(word2) 
                cha1.append(word2)
                cha1.append(finalword2)


            else: 
                cha1.append(word2)

            #if x==y: 
            #print("cha1")
            #print(cha1)
            #print("cha")
            #print(cha)
            for item1 in cha1: 
                for item2 in cha: 
                    if item1!=item2:
                        if item1 is not None and item2 is not None: 
                            if item1!=[] and item2!=[]: # not sure why theres is an empty list
                                full=item2+" "+item1
                                amended.append(full)
                                full=item1+" "+item2
                                amended.append(full)

        
        else: 
            if len(postags)==1: 
                word1=postags 
                #print(postags)

                
                for word1[0] in word1: 
                    #print(word1[0])
                    (word1,tag1)=(word1[0])
            
                #(word1,tag1)=(word)
                if tag1=="NN": 
                    f1=pattern.en.pluralize(word1)
                    amended.append(f1)
                    amended.append(word1)
            
                elif tag1=="NNS": 
                    f1=pattern.en.singularize(word1)
                    amended.append(f1)
                    amended.append(word1)

                elif tag1=="VBG" or tag1=="VBN" or tag1=="VBZ" or tag1=="VB" or  tag1=="VBZ": 
                    #finalword1=lemmatize(word1)
                    f1=conjugate(word1,tense="past")
                    f4=conjugate(word1,tense="past",person=2)
                    f2=conjugate(word1,tense="infinitive")
                    f3=conjugate(word1,tense="present",person=3)
                    f5=conjugate(word1,tense="present",person=2)
                    amended.extend([f1,f2,f3,f4,f5])

                elif tag1=="JJ": 
                    f1=close_adv(word1) 
                    amended.append(word1)
                    amended.append(f1)

                elif tag1=="RB":
                    f1=close_adv(word1) 
                    amended.append(word1)
                    amended.append(f1)


    #posttagperformance(amended)



out(classifyingphraselist)


with open("negativelemma.csv","w",encoding="utf-8", errors="ignore") as csvfile:
    fwriter = csv.writer(csvfile)
    for i in amended:
        if i is not None:
            fwriter.writerow([i])
    csvfile.close()