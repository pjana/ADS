#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 12:45:48 2017

@author: preranajana
run in python 2.7
"""
import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
from scipy.stats.stats import pearsonr
import enchant
from nltk.metrics import edit_distance


# read the data
business = pd.read_pickle('pitt_food.pkl')
reviews = pd.read_pickle('rel_user_reviews.pkl')

# spell checker
class SpellingReplacer():
    def __init__(self, dict_name, max_dist):
        self.spell_dict = enchant.Dict(dict_name)
        self.max_dist = max_dist
    def replace(self, word):
        if self.spell_dict.check(word):
            return word
        suggestions = self.spell_dict.suggest(word)
        if suggestions and (edit_distance(word, suggestions[0]) <= self.max_dist):
            return suggestions[0]
        else:
            return word


def spell_check(sentence):
    word_list = nltk.word_tokenize(sentence)
    checked_list = []
    for item in word_list:
        replacer = SpellingReplacer(dict_name='en_US', max_dist=len(item))
        r = replacer.replace(item)
        r = r.lower()
        checked_list.append(r)
    return ' '.join(item for item in checked_list)


# sentiment analysis
text = reviews['text'].values.tolist()
name = []
review = []

sid = SentimentIntensityAnalyzer()


sentiments = pd.DataFrame(columns=['review', 'compound', 'positive', 'neutral', 'negative'])

count = 0
for review in text:
    count += 1
    lines_list = tokenize.sent_tokenize(review)
    pos_rate = []
    neu_rate = []
    neg_rate = []
    compound_rate = []
        
    for sentence in lines_list:
        corrected_sentence = spell_check(sentence)
        ss = sid.polarity_scores(corrected_sentence)
        compound_rate = ss['compound']
        pos_rate = ss['pos']
        neu_rate = ss['neu']
        neg_rate = ss['neg']
        
    compound = np.mean(compound_rate)
    pos = np.mean(pos_rate)
    neg = np.mean(neg_rate)
    neu = np.mean(neu_rate)
    sentiments = sentiments.append({"review": review, "compound": compound_rate, "positive": pos, "neutral": neu,
                                    "negative": neg}, ignore_index=True)

    if count % 1000 == 0:
        print(count)

for review in text:
    count += 1
    corrected_review = spell_check(review)
    ss = sid.polarity_scores(corrected_review)
    compound_rate = ss['compound']
    pos = ss['pos']
    neu = ss['neu']
    neg = ss['neg']
    sentiments = sentiments.append({"review": corrected_review, "compound": compound_rate, "positive": pos, "neutral": neu,
                                    "negative": neg}, ignore_index=True)
    if count % 1000 == 0:
        print(count)

sentiments = sentiments.set_index(reviews.index)
result = pd.concat([reviews, sentiments], axis=1, join_axes=[reviews.index], join='outer')
result.to_csv('sentiments_passage_corrected5000.csv', sep=',')

result.to_pickle('sentiments_ratings_corrected_passage.pkl')

# evaluation

comp = result['compound']
stars = result['stars']

# sentences - 0.28
# comma separated - 0.428
# passage - 0.55

# statistical significance
pearsonr(comp, stars)






