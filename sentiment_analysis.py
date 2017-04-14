#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 12:45:48 2017

@author: preranajana
run in python 3.6
"""
import pandas as pd
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize


business = pd.read_pickle('pitt_food.pkl')
reviews = pd.read_pickle('rel_user_reviews.pkl')

text = reviews['text'].values.tolist()
name = []
review = []

sid = SentimentIntensityAnalyzer()

reviews = reviews[0:1000]
text = text[0:1000]

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
        ss = sid.polarity_scores(sentence)
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
sentiments = sentiments.set_index(reviews.index)
result = pd.concat([reviews, sentiments], axis=1, join_axes=[reviews.index], join='outer')
result.to_csv('sentiments_base5000.csv', sep=',')


