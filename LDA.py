
import os 

os.chdir("/Users/lilucy/Desktop/Data-structure-and-Algo-Notes/newdic")

import gensim
from gensim.utils import simple_preprocess

file=[]
corpus=[]

for files in glob.glob("/Users/lilucy/Desktop/Data-structure-and-Algo-Notes/newdic/*.txt"):
#alternative: glob.glob(".txt/*"):
    with open(files) as f: 

      print(files)
        #files.encode('utf-8').strip()
      lineList = f.readlines()
      if debug1:
        print(lineList)
      lines1="".join(lineList) 
      lines = re.sub(r'\d', '', lines1)
      if debug1:
        print(lines)
      corpus.append(lines)
      if debug2:
        print(corpus)


def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations
data = corpus
data_words = list(sent_to_words(data))
print(data_words[:1])

#sent_to_words(corpus)

#The 2 important arguments to phrases are mincount and threshold

# Build the bigram and trigram models
bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100) # higher threshold fewer phrases.
#trigram = gensim.models.Phrases(bigram[data_words], threshold=100)
# Faster way to get a sentence clubbed as a trigram/bigram
bigram_mod = gensim.models.phrases.Phraser(bigram)
#trigram_mod = gensim.models.phrases.Phraser(trigram)

# NLTK Stop words
# import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
#stop_words.extend(['from', 'subject', 're', 'edu', 'use'])
# Define functions for stopwords, bigrams, trigrams and lemmatization


import spacy
# Remove Stop Words
data_words_nostops = remove_stopwords(data_words)
# Form Bigrams
data_words_bigrams = make_bigrams(data_words_nostops)
# Initialize spacy 'en' model, keeping only tagger component (for efficiency)
nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])
# Do lemmatization keeping only noun, adj, vb, adv
data_lemmatized = lemmatization(data_words_bigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])
print(data_lemmatized[:1])
#latent dirichlet allocation 

import gensim.corpora as corpora
# Create Dictionary
id2word = corpora.Dictionary(data_lemmatized)
# Create Corpus
texts = data_lemmatized
# Term Document Frequency
corpus = [id2word.doc2bow(text) for text in texts]
# View
print(corpus[:1])


lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                       id2word=id2word,
                                       num_topics=10, 
                                       random_state=100,
                                       chunksize=100,
                                       passes=10,
                                       per_word_topics=True)