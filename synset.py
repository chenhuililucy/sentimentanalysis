


from nltk.corpus import wordnet as wn

for 

list=["strategic","acquisitions","banking","business"]

for word in list: 
    synsets=wn.synsets(word)
    print(synsets)
