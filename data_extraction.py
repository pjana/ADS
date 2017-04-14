#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 12:45:48 2017

@author: preranajana
run in python 3.6

This code extracts the restaurant and food places reviews and business data from the Yelp dataset 
for the city of Pittsburgh
"""

import pandas as pd
import json


business = pd.read_json('yelp_academic_dataset_business.json', lines=True)
# read reviews dataset
f = open("yelp_academic_dataset_review.json", 'r')
all_lines = f.readlines()
df = pd.DataFrame()
json_obj = [json.loads(item) for item in all_lines]
df = df.append(json_obj)
f.closer()


# subset only pittsburgh
pitt_b = business.loc[business.city == 'Pittsburgh']

# discard restaurants which do not have any categories
pitt_b = pitt_b[pitt_b.categories.notnull()]
pitt_b = pitt_b.reset_index(drop=True)

# select categories only related to food/ restaurants/ bar
list_cat = pitt_b['categories'].values.tolist()
flat_list = [item for sublist in list_cat for item in sublist]
unique_categories = set(flat_list)
# Count of all categories - 712

# manually labelled category extraction
food_category = ['Bagels', 'Italian', 'Venezuelan', 'Do-It-Yourself Food', 'Gelato', 'Kosher', 'Gluten-Free', 'Southern', 'Food', 'Bars', 'Sushi Bars', 'Falafel', 'Noodles', 'Bistros', 'Tex-Mex', 'Tiki Bars', 'Moroccan', 'Donuts', 'Diners', 'Meat Shops', 'Steakhouses', 'Dive Bars', 'Gay Bars', 'Dance Clubs', 'Pasta Shops', 'Sandwiches', 'Imported Food', 'Sports Clubs', 'Smokehouse', 'Mexican', 'Mongolian', 'Nightlife', 'Ethnic Food', 'Halal', 'Bed & Breakfast', 'Barbeque', 'Vape Shops', 'Salad', 'Malaysian', 'Wine Tasting Room', 'Japanese', 'Cheese Shops', 'Cocktail Bars', 'Taiwanese', 'Fast Food', 'Sports Bars', 'Tacos', 'Vegan', 'Bubble Tea', 'Hookah Bars', 'French', 'Whiskey Bars', 'Tobacco Shops', 'Popcorn Shops', 'Social Clubs', 'Teppanyaki', 'Caterers', 'Comfort Food', 'Tea Rooms', 'Wine Bars', 'Fruits & Veggies', 'Filipino', 'Desserts', 'Waffles', 'Buffets', 'American (Traditional)', 'Tapas Bars', 'Burgers', 'Coffee Roasteries', 'Food Court', 'Cafes', 'Soul Food', 'Vegetarian', 'Food Stands', 'Indian', 'Chicken Wings', 'Burmese', 'Arabian', 'Dim Sum', 'Chicken Shop', 'Hawaiian', 'Uzbek', 'Macarons', 'Food Trucks', 'Portuguese', 'Asian Fusion', 'Szechuan', 'Ramen', 'Specialty Food', 'African', 'Hungarian', 'Chinese', 'Cheesesteaks', 'Soup', 'Caribbean', 'German', 'Himalayan/Nepalese', 'Hot Dogs', 'Pretzels', 'Korean', 'Colombian', 'DJs', 'Beer Bar', 'Wraps', 'Creperies', 'Fish & Chips', 'Thai', 'Turkish', 'Restaurants', 'Ice Cream & Frozen Yogurt', 'Cupcakes', 'Gastropubs', 'Food Tours', 'Breakfast & Brunch', 'Persian/Iranian', 'Seafood', 'Beer', 'Middle Eastern', 'Cambodian', 'Pan Asian', 'Beer Tours', 'Pakistani', 'Kombucha', 'Egyptian', 'Live/Raw Food', 'Piano Bars', 'Coffee & Tea', 'Juice Bars & Smoothies', 'Bangladeshi', 'Latin American', 'Ethiopian', 'Brazilian', 'Cafeteria', 'Argentine', 'Herbs & Spices', 'Lounges', 'Pizza', 'Irish Pub', 'Wine & Spirits', 'Chocolatiers & Shops', 'Champagne Bars', 'Beer Gardens', 'Custom Cakes', 'Belgian', 'Mediterranean', 'Lebanese']
# Food related categories - 146

# keep business IDs based on food related categories
food_rest_index = []
index = 0
for item in list_cat:
    print(index)
    for each in item:
        if each in food_category:
            print(item)
            print('--------')
            print(each)
            food_rest_index.append(index)
            break
    index += 1
# count 2795

# keep the business restaurant data only for these indices
pitt_food = pitt_b[pitt_b.index.isin(food_rest_index)]
pitt_food.to_pickle('pitt_food.pkl')

# extract only those user reviews corresponding to these business IDs
pitt_food_business_id = pitt_food['business_id'].values.tolist()

rel_user_reviews = df[df.business_id.isin(pitt_food_business_id)]
# (115841, 10)
rel_user_reviews.to_pickle('rel_user_reviews.pkl')

"""
To get the summarized view of the data
Things to explore -
1. Distribution of Rating
2. Distribution of Number of Reviews
3. NUmber of users vs Number of Reviews
"""