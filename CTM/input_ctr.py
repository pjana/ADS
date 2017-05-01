"""
Input format for Collaborative Topic Modeling

@author: preranajana
run in python 3.6

"""

import pandas as pd
import json
import pickle

"""
Read the json files
"""
# read the business dataset
bfile = '/Volumes/Sandbox/yelp_dataset_challenge_round9/yelp_academic_dataset_business.json' 
business = pd.read_json(bfile, lines=True)
# read reviews dataset
rfile = "/Volumes/Sandbox/yelp_dataset_challenge_round9/yelp_academic_dataset_review.json"
f = open(rfile, 'r')
all_lines = f.readlines()
df = pd.DataFrame()
json_obj = [json.loads(item) for item in all_lines]
df = df.append(json_obj)
f.close()

"""
Extract Pittsburgh Restaurant business and reviews
"""
# subset only pittsburgh
pitt_b = business.loc[business.city == 'Pittsburgh']

# discard restaurants which do not have any categories
pitt_b = pitt_b[pitt_b.categories.notnull()]
pitt_b = pitt_b.reset_index(drop=True)

# select categories only related to Restaurants
pitt_food = pd.DataFrame(columns=pitt_b.columns)
for i in range(pitt_b.shape[0]):
	if 'Restaurants' in pitt_b['categories'].iloc[i]:
		print(pitt_b['name'].iloc[i])
		pitt_food = pitt_food.append(pitt_b.iloc[i], ignore_index = True)
# 1990		


# extract only those user reviews corresponding to these business IDs
pitt_food_business_id = pitt_food['business_id'].values.tolist()
rel_user_reviews = df[df.business_id.isin(pitt_food_business_id)]
# (100765, 10)


review_count = rel_user_reviews.groupby(by=['business_id']).count()
review_count = review_count.sort_values(by='review_id', ascending = False)

# keep businesses with more than 30 reviews 
reviews_more30 = review_count.loc[review_count.review_id > 30]
reviews_more30 = reviews_more30.index.values.tolist()
# 800 restaurants


# get reviews for these restaurants
pitt_food_final = business[business.business_id.isin(reviews_more30)] # 800
rel_user_reviews = df[df.business_id.isin(reviews_more30)] # 86,395

rel_user_reviews.to_pickle('rel_user_reviews.pkl')
pitt_food_final.to_pickle('pitt_food_final.pkl')

"""
Get the input format ready for CTM
"""
