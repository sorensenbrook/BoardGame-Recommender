from keybert import KeyBERT

input_user1 = 'I prefer boardgames which have a midieval atmosphere. Themes like knights and dragons maybe'
input_user2 = 'I prefer a game which takes place in a dangerous city. A distopian future where technology took over and robots rule the world.'
input_user3 = 'I have always been a big fan of Jack-Sparrow. I wonder if there is any boardgame which allows me to sail the seven seas and hunt treasures'
sw = ['boardgames', 'boardgame', 'theme', 'game', 'games', 'themes', 'set', 'atmosphere', 'topic', 'topics']

kw_model = KeyBERT()
keywords1 = kw_model.extract_keywords(input_user1, stop_words=sw)
keywords2 = kw_model.extract_keywords(input_user2, stop_words=sw)
keywords3 = kw_model.extract_keywords(input_user3, stop_words=sw)

print(keywords1)
print(keywords2)
print(keywords3)

def keysentece(lst):
    sentence = ''
    for tup in lst:
        sentence += tup[0]
        sentence += ' '
    return sentence

keysent = keysentece(keywords2)

finalkey = kw_model.extract_keywords(keysent)


