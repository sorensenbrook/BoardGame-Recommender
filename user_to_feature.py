'''
Import Data Names 
'''
import csv

category_list = []  
mechanism_list = []

f = open("/content/drive/MyDrive/Colab_Notebooks/data/categories.csv")
category_list = list(csv.reader(f))

#for some reason bayes_rating shows up twice in this list
category_list.remove(['bayes_rating'])
category_list.remove(['bayes_rating'])

f.close


f = open("/content/drive/MyDrive/Colab_Notebooks/data/mechanisms.csv")
mechanism_list = list(csv.reader(f))

mechanism_list.remove(['bayes_rating'])
mechanism_list.remove(['rating'])

f.close


'''
Tokenizer
'''
import nltk
from nltk import word_tokenize
nltk.download("punkt")
nltk.download("stopwords")
from nltk.stem import WordNetLemmatizer

#TODO: still need to clean up different repeat words such as "game" and deal with
#any other symbols.

def tokenize (feature_list):
  
  temp_list = []

  for item in feature_list:
    word = item[0].replace('/', ' ')
    word = word.replace('-', ' ')
    temp_list.append(word_tokenize(word.lower()))

  return temp_list


'''
Similarity Function


finds the most similar word from the feature list to what the user input was
TODO: have a check to see that there is something that meets a certain similarity


This takes in a list of different features, these features should be tokenized
so that they can be found in the word vec. It then takes the list of each feature, since 
some features are more than one token, finds the average (might want to change to
the highest?) and that is the sim value for that category.
It then returns the most similiar category.
'''
def user_to_features (feature_list, user_input):
  
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

  print(sim_df)

  #should return the from the feature list that is the most similiar
  return sim_df["word"].head(n=1)

