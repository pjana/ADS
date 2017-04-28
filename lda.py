#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Created on Thu Apr 27 21:31:56 2017

@author: AkshayPatil
"""

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import string

from stemming.porter2 import stem

stop = set(stopwords.words('english'))
exclude = set(string.punctuation)
lemma = WordNetLemmatizer()
print('h')

reviews = pd.read_pickle('/Users/AkshayPatil/Desktop/ADS/rel_user_reviews.pkl')
reviews_text = reviews['text'].tolist()
reviews_clean = []
stem_p = []
stem_n = []

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    stemmed = " ".join(stem(word) for word in normalized.split())
    print(stemmed)
    return stemmed

for j in range(len(reviews_text)):
    print(j)
    reviews_clean.append(clean((reviews_text[j])))

p_w = open('/Users/AkshayPatil/Desktop/ADS/positive-words.txt','r')
pos_words = p_w.readlines()
positive_word = pd.DataFrame(pos_words)
positive_words = positive_word.iloc[:,0]
positive_words = positive_words.str.split('\n').str.get(0)
positive_words.tolist()
p = positive_words.tolist()



n_w = open('/Users/AkshayPatil/Desktop/ADS/negative-words.txt','r', encoding = 'latin-1')
neg_words = n_w.readlines()
negative_word = pd.DataFrame(neg_words)
negative_words = negative_word.iloc[:,0]
negative_words = negative_words.str.split('\n').str.get(0)
negative_words.tolist()
n = negative_words.tolist()

for i in range(len(p)):
    stem_p.append(stem(p[i]))

stem_p = list(set(stem_p))

for j in range(len(n)):
    stem_n.append(stem(n[j]))
stem_n = list(set(stem_n))

for m in range(len(reviews_clean)):
    for n in range(len(reviews_clean[m])):
        a = reviews_clean[m].split()
        for k in range(len(stem_p)):
            try:
                print(a.index(stem_p[k]))
                print(stem_p[k])
                inject_positive(
            except ValueError:
                b = 1


for m in range(len(reviews_clean)):
    for n in range(len(reviews_clean[m])):
        a = reviews_clean[m].split()
        for k in range(len(stem_n)):
            try:
                print(a.index(stem_n[k]))
                print(stem_n[k])
            except ValueError:
                b = 1

def inject_positive(a,b):

    reviews_clean[b].insert(a, 'goodreview')

def inject_negative(a):

    reviews_clean[b].insert(a, 'badreview')


for i in range(len(b)):
    if (b[i].find('bad') == 0):
        print(i)
        b.insert(i,'goodreview')

b = a
b.insert(a.index('bad')+1,'goodreview')


line = 'this food is really good , it is simply good'
indices = [i for i, x in enumerate(line.split()) if x == "good"]

inserted_line = line.split()
for i in range(len(indices)):
    index = indices[i] + i
    inserted_line.insert(index,'yay')
