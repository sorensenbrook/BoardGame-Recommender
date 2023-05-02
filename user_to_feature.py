from gensim.models import Word2Vec, KeyedVectors
import pandas as pd
import gensim.downloader as api
wv = api.load('glove-wiki-gigaword-100') 

#need to import the list of different keywords from data still
category_list = {}  
mechanism_list = {}

#finds the most similar word from the feature list to what the user input was
#TODO: have a check to see that there is something that meets a certain similarity
def user_to_features (feature_list, user_input):
  
  sim_list = {}

  for word in feature_list:
    sim_val = wv.similarity(word, user_input)
    sim_list.append = (word, sim_val)

  sim_df = pd.DataFrame(sim_list, columns=["word", "sim"])
  sim_df.sort_values("sim", ascending = True)

  #should return the from the feature list that is the most similiar
  return sim_df["word"].head(n=1)
