'''
IMPORT DATA INTO LIST

Creates two lists, one that will be used to match up with the items in the
data set and one which will be tokenized to use in the similarity function.
'''


import csv

category_list = []  
mechanism_list = []


f = open("./data/categories.csv")
category_list = list(csv.reader(f))

#for some reason bayes_rating shows up twice in this list
category_list.remove(['bayes_rating'])
category_list.remove(['bayes_rating'])

f.close


f = open("./data/mechanisms.csv")
mechanism_list = list(csv.reader(f))

mechanism_list.remove(['bayes_rating'])
mechanism_list.remove(['rating'])

f.close

def lowercase (lst):
  new_lst = []
  for item in lst:
    temp_item = []
    for word in item:
      temp = word.lower()
      temp_item.append(temp)
    new_lst.append(temp_item)
  
  return new_lst

cat_list_lower = lowercase(category_list)
mech_list_lower = lowercase(mechanism_list)


'''
TOKENIZER

Cleans the list of cat and mech so that it can be used in the sim function
'''

import nltk
from nltk import word_tokenize
nltk.download("punkt")
nltk.download("stopwords")
from nltk.stem import WordNetLemmatizer
import re

stops = set(nltk.corpus.stopwords.words('english'))
common_tokens = ['game', 'games', ':', "'s",]


def tokenize (feature_list):
  
  temp_list = []

  for item in feature_list:
    word = item[0].replace('/', ' ')
    word = word.replace('-', ' ')
    word = word.replace('Minimap', 'mini map')
    
    temp_tokens = word_tokenize(word.lower())
    filtered = [w for w in temp_tokens 
                if not w in stops 
                and not w in common_tokens]

    temp_list.append(filtered)

  return temp_list


clean_cat = tokenize(category_list)
clean_mech = tokenize(mechanism_list)

from gensim.models import Word2Vec, KeyedVectors
import pandas as pd
import gensim.downloader as api
wv = api.load('glove-wiki-gigaword-100') 


def user_to_features (feature_list, user_input, dataform_list):
  
  sim_list = []

  for feature in feature_list:
    average = 0
    for word in feature:
      sim_val = wv.similarity(word, user_input)
      average = average + sim_val

    average = average / len(feature)
    temp_tuple = (feature, average)
    sim_list.append(temp_tuple)
        
  sim_df = pd.DataFrame(sim_list, columns = ['word', 'sim']) 
  sim_df = sim_df.sort_values(by=['sim'], ascending=False)

  index = sim_df.index[0]

  return dataform_list[index]



def user_to_pref (input_dict)
  user_list = ["", "", "", 0, 0, 0, 0]

  #Category
  user_list[0] = (user_to_features(category_list, input_dict.get("A1"))[0], cat_list_lower)
  
  #Category2
  user_list[1] = (user_to_features(category_list, input_dict.get("A2"))[0], cat_list_lower)
  
  #Mechanism
  user_list[2] = (user_to_features(mechanism_list, input_dict.get("A3"))[0], mech_list_lower)

  #Minplayers
  user_list[2] = min(input_dict.get("A4"))
  
  #Maxplayers
  user_list[3] = max(input_dict.get("A4"))

  #Min time
  user_list[4] = min(input_dict.get("A5"))

  #Max time
  user_list[5] = max(input_dict.get("A5"))
  
  return user_list

  

