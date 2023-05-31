import nltk 
import gensim.downloader as api


# Still need software to ask the questions in a user friendly way
input_user1 = 'I prefer boardgames which have a midieval atmosphere. Themes like knights and dragons maybe'
input_user2 = 'I prefer a game which takes place in a dangerous city. A distopian future where technology took over and robots rule the world.'
input_user3 = 'I have always been a big fan of Jack Sparrow. I wonder if there is any boardgame which allows me to sail the seven seas and hunt treasures'

# Function which extracts the keywords from the user's input and filters it
# The function takes all the nouns from the input and filters words like: 
# boardgames and themes out of it. It also filters every word contained within 
# these words such as theme (not plural) and game
# The keywords found are put into a list
def get_key_words(inpt):
    tok_tag_input = nltk.pos_tag(nltk.word_tokenize(inpt), tagset='universal')
    filter_words = 'boardgames' + 'themes' + 'mechanics' + 'mechanisms' 
    filtered_input = []
    for word in tok_tag_input:
        if word[1] == 'NOUN' and str.lower(word[0]) not in filter_words:
            filtered_input.append(word)
    keywords = [keyword[0] for keyword in filtered_input]
    return keywords


# A function to load to model which is used in overall_key_word() function
# This is done in a seperate function so the model does not has to be reloaded
# everytime since it is not really fast
def load_model(model_name):
    return api.load(model_name)


# A function which takes in the list of all keywords from the input and the 
# loaded model and returns the word which is most similar to all keywords
# It does this by getting the average vector of all key word vectors
# and then finding which word is most similar to the average vector
def overall_key_word(lst, model):
    vectors = [model[word] for word in lst if word in model.key_to_index]
    avg_vector = sum(vectors) / len(vectors)
    theme = model.similar_by_vector(avg_vector, topn=1)[0][0]
    return theme



model = load_model('word2vec-google-news-300')

key_words1 = get_key_words(input_user1)
key_words2 = get_key_words(input_user2)
key_words3 = get_key_words(input_user3)

 
theme1 = overall_key_word(key_words1, model)
theme2 = overall_key_word(key_words2, model)
theme3 = overall_key_word(key_words3, model)


print(f'Overall theme of input sentence user 1 is: {theme1}')
print(f'Overall theme of input sentence user 2 is: {theme2}')
print(f'Overall theme of input sentence user 3 is: {theme3}')

