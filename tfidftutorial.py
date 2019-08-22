import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

import nltk

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score

from subprocess import check_output
print(check_output(["ls", "../input"]).decode("utf8"))

train_df = pd.read_csv("../input/train.csv")
test_df = pd.read_csv("../input/test.csv")

train_comments = train_df['comment_text']
test_comments = test_df['comment_text']

all_comments = pd.concat([train_comments, test_comments])

train_df.head(3)

labels = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(
    analyzer='word', 
    sublinear_tf=True,
    strip_accents='unicode',
    token_pattern=r'\w{1,}',
    ngram_range=(1, 1),
    max_features=10000)
print('Start Fit vectorizer')

tfidf = vectorizer.fit(train_comments)

print('Fit vectorizer')

print('Start transform test comments')

test_comment_features = vectorizer.transform(test_comments)

print('Transformed test comments')

print('Start transform train comments')

train_comment_features = vectorizer.transform(train_comments)

print('Transformed train comments')

import pickle

pickle.dump(tfidf, open("tfidf.pickle", "wb"))
pickle.dump(train_comment_features, open("train_comment_features.pickle", "wb"))
pickle.dump(test_comment_features, open("test_comment_features.pickle", "wb"))




###########################################



characters = ['Adam', 'Eve', 'God', 'Satan']
files = ['sp/' + character for character in characters]
contents = [open(file, encoding='utf-8', errors='ignore').read() 
            for file in files]


vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(contents)
feature_names = vectorizer.get_feature_names()
dense = tfidf_matrix.todense() #Return a dense matrix representation of this matrix.
denselist = dense.tolist()


df = pd.DataFrame(denselist, columns=feature_names, index=characters)
df