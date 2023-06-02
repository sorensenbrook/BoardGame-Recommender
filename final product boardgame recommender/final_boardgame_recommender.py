
import customtkinter as ck
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import pandas as pd
import random
import copy
from keybert import KeyBERT
import nltk
import re
import csv
from nltk import word_tokenize
import gensim.downloader as api


question_lst = [
    'What setting or theme would you like your game to have? A theme refers to the specific context or background in which the game is set. Some examples of themes include the American Civil War, zombies, fantasy worlds, and so on.',
    'What specific genre or type of game would you prefer? Examples of game types include card games, word games, memory-based games, and so on.',
    'What kind of gameplay mechanics would you like your game to feature? In simpler terms, what type of actions or interactions should the game revolve around? Examples of gameplay mechanisms include voting, grid movement, zone controlment, luck-based or dice rolling games.',
    'What is the desired maximum duration for the game? Please provide the answer in minutes.',
    'How many players would you like the game to accommodate?'
    ]



def create_question_dic(lst):
    dic = {}
    for i, q in enumerate(lst):
        dic['Q'+str(i+1)]=q
    return dic    

df_games = pd.read_csv('final_data_f.csv')
data = copy.deepcopy(df_games)
questions = create_question_dic(question_lst)
numofq = len(questions)
answers = {}
question_number = 1
moved_once = 0 #boolean
come_from_last_q = 0 #boolean
completed_q = 0 #boolean

if numofq<3:
    raise ValueError('Question list should contain at leasth 3 questions')

### First program: The questionnaire ##########################################
def continue_with_recommendation():
    global completed_q
    completed_q += 1
    root.destroy()
    

def popup_submit():
    message = 'Are you sure you want to submit your answers? You cannot change your answers afterwards.'

    popup = tk.Tk()
    # Sets the size of the popup and the title in the most upper bar
    popup.geometry('500x250')
    popup.title('SURE TO SUBMIT?')

    # Which message the popups shows. Wraplength makes the message continue on the
    # next line. Without the wraplength parameter the message wont fit on the popup
    label = tk.Label(popup, text=message, font=("Helvetica", 20), wraplength=450)
    label.pack(pady=20)

    # Frames need to be defined otherwise you get errors
    button_frame = tk.Frame(popup)
    button_frame.pack(pady=20)

    # Make the buttons. Lambda: [fuc1, fuc2] is used so both functions are excicuted
    B1 = tk.Button(button_frame, text="Submit", command=lambda: [continue_with_recommendation(), popup.destroy()], width=15, height=20)
    B1.pack(side='right', padx=10)

    B2 = tk.Button(button_frame, text="Cancel", command=popup.destroy, width=15, height=20)
    B2.pack(side='left', padx=10)

    popup.mainloop()



def nextquestioncommand():
    global question_number, textbox
    ans = textbox.get('0.0', 'end-1c')
    answers['A' + str(question_number)] = ans
    textbox.delete('0.0', 'end-1c')
    question_number += 1
    key = 'A' + str(question_number)
    if key in answers:
        textbox.insert('0.0', answers['A' + str(question_number)])
    define_layout()

def previousquestioncommand():
    global question_number, come_from_last_q
    ans = textbox.get('0.0', 'end-1c')
    answers['A' + str(question_number)] = ans
    textbox.delete('0.0', 'end-1c')
    question_number -= 1
    textbox.insert('0.0', answers['A' + str(question_number)])
    define_layout() 

def submitanswerscommand():
    ans = textbox.get('0.0', 'end-1c')
    answers['A' + str(question_number)] = ans
    popup_submit()


def set_question_label():
    global question_label
    question_label.pack_forget()
    question_label = ck.CTkLabel(root, text=questions['Q'+str(question_number)], font=ck.CTkFont(size=20, weight='bold'), wraplength=650)
    question_label.pack()

def set_textbox():
    textbox.pack(padx=(40, 50), pady=30, anchor='center')

def set_next_button():
    next_button.pack(side='right', padx=50)
    
def set_previous_button():
    previous_button.pack(side='left', padx=50)

def set_sumbit_button():
    submit_button.pack(side='right', padx=50)

def set_quit_button():
    quit_button.pack(side="left", anchor="sw", padx=10, pady=10)

def define_layout():
    global next_button, previous_button, submit_button, moved_once, come_from_last_q
    
    # When first runned. How the GUI pops up
    if question_number == 1 and moved_once == 0:
        set_question_label()
        set_textbox()
        set_next_button()
        set_quit_button()
        
    
    # When you first go from question 1 to 2
    elif 1<question_number<numofq  and moved_once == 0:
        moved_once += 1
        question_label.pack_forget()
        textbox.pack_forget()
        next_button.pack_forget()
        set_question_label()
        set_textbox()
        set_next_button()
        set_previous_button()        
    
    # If you go back to question 1
    elif question_number == 1 and moved_once != 0:
        textbox.pack_forget()
        next_button.pack_forget()
        previous_button.pack_forget()
        set_question_label()
        set_textbox()
        set_next_button()        
    
    # When you go to any next question if not the last question 
    elif 1<question_number<numofq and moved_once !=0: 
        textbox.pack_forget()
        next_button.pack_forget()
        previous_button.pack_forget()
        # To make sure that if you were at the last question the submit gets 
        # thrown away
        if come_from_last_q != 0:
            submit_button.pack_forget()
            come_from_last_q -= 1
                
        set_question_label()
        set_textbox()
        set_next_button() 
        set_previous_button()
    
    # When you go to the last question (cause only then will question_number 
    # not be below numofq and moved_once wont be equal to 0. It is the only 
    # possibilty left)
    else:
        textbox.pack_forget()
        next_button.pack_forget()
        previous_button.pack_forget()
        come_from_last_q += 1
        set_question_label()
        set_textbox()
        set_sumbit_button() 
        set_previous_button()
        


root = ck.CTk()

root.geometry('750x450')
root.title('Boardgame Recommender')
ck.set_appearance_mode("Dark")

title_label = ck.CTkLabel(root, text='Boardgame Questionnaire', font=ck.CTkFont(size=30, weight='bold')) 
title_label.pack(padx=5, pady=5)

question_label = ck.CTkLabel(root, text=questions['Q'+str(question_number)], font=ck.CTkFont(size=20, weight='bold'), wraplength=650)

textbox=ck.CTkTextbox(root, width=680, height=200, fg_color='#383838')
textbox.insert('0.0','Answer here')

next_button = ck.CTkButton(root, text='Next Question', width=250, command=nextquestioncommand)

previous_button = ck.CTkButton(root, text='Previous Question', width=250, command=previousquestioncommand)

submit_button = ck.CTkButton(root, text='Submit', width=250, command=submitanswerscommand)

quit_button = ck.CTkButton(root, text='quit', width=45, height=10, command=root.destroy, fg_color='red', text_color='black')



define_layout()

root.mainloop()

  
              
while completed_q!=1:
    pass


### Second program: Loading screen ############################################

root = ck.CTk()

root.geometry('750x450')
root.title('Boardgame Recommender')
ck.set_appearance_mode("Dark")

title_label = ck.CTkLabel(root, text='Loading...', font=ck.CTkFont(size=30, weight='bold')) 
title_label.pack(padx=5, pady=5)

def show_gif():
    image1 = Image.open(r"loading3.1.gif")
    framesTotal = image1.n_frames

    play_back_delay = 150
    animation = []

    def loadGif():
        for x in range(framesTotal):
            frame = ImageTk.PhotoImage(image1.copy())
            animation.append(frame)
            image1.seek(x)


    def update(ind):
        frame = animation[ind]
        label.configure(image=frame)
        
        ind += 1
        if ind == framesTotal:
            ind = 0

        root.after(play_back_delay, update, ind)
        
    label = ck.CTkLabel(root)
    label.configure(text='')  # Set the text to an empty string
    label.pack()
    loadGif()
    update(0)

show_gif()

quit_button = ck.CTkButton(root, text='quit', width=45, height=10, command=root.destroy, fg_color='red', text_color='black')
quit_button.pack()





### Third program: Extracting data from answers ###############################

sw = ['boardgames', 'boardgame', 'theme', 'game', 'games', 'themes', 'set', 'atmosphere', 'topic', 'topics', 'mechanisms', 'mechanism']
kw_model = KeyBERT()

def extract_keyword(input_user):
    all_keywords = kw_model.extract_keywords(input_user, stop_words=sw)
    return all_keywords[0][0]

def find_spelled_integers(sentence):
    # Define a dictionary to map spelled-out numbers to their corresponding integer values
    number_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
        'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12,
        'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
        'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40,
        'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
        'hundred': 100, 'thousand': 1000
    }

    # Define a pattern to match spelled-out numbers
    pattern = r"\b(?:{})\b".format("|".join(number_dict.keys()))

    # Find all matches of spelled-out numbers in the sentence
    matches = re.findall(pattern, sentence, re.IGNORECASE)

    # Convert the spelled-out numbers to integers
    integers = [number_dict[match.lower()] for match in matches]

    # Remove duplicate integers
    integers = list(set(integers))

    return integers

def find_intergers(sentence):
    tok_input = nltk.tokenize.word_tokenize(sentence)
    nums = [int(word) for word in tok_input if word.isdigit()]
    return nums


###############################################################################
# This function only finds highest number. We want to find min and max.
###############################################################################

def find_all_numbers(user_input):
    '''
    Returns a list with smallest number and biggest number the users' answer  
    '''
    lst1 = find_intergers(user_input)
    lst2 = find_spelled_integers(user_input)
    lst_nums = lst1+lst2
    if len(lst_nums) == 1:
        return [0, lst_nums[0]]
    else:
        return [min(lst_nums), max(lst_nums)]

keyword_catagory_theme = extract_keyword(answers['A1']) 
keyword_catagory_type = extract_keyword(answers['A2'])
keyword_mechanism = extract_keyword(answers['A3'])


### Fourth program: Getting preferences #######################################

lst_playtime = find_all_numbers(answers['A4'])
ans_min_playtime = lst_playtime[0]
ans_max_playtime = lst_playtime[1]

lst_num_players = find_all_numbers(answers['A5'])
ans_min_players = lst_num_players[0]
ans_max_players = lst_num_players[1]



category_list = []  
mechanism_list = []


f = open("categories.csv")
category_list = list(csv.reader(f))

#for some reason bayes_rating shows up twice in this list
category_list.remove(['bayes_rating'])
category_list.remove(['bayes_rating'])

f.close


f = open("mechanisms.csv")
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



nltk.download("punkt")
nltk.download("stopwords")


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



def user_to_pref():
  user_list = ["", "", "", 0, 0, 0, 0]

  #Category
  user_list[0] = user_to_features(clean_cat, keyword_catagory_theme, cat_list_lower)[0]
  
  #Category2
  user_list[1] = user_to_features(clean_cat, keyword_catagory_type, cat_list_lower)[0]
  
  #Mechanism
  user_list[2] = user_to_features(clean_mech, keyword_mechanism, mech_list_lower)[0]

  #Minplayers
  user_list[3] = ans_min_players
  
  #Maxplayers
  user_list[4] = ans_max_players

  #Min time
  user_list[5] = ans_min_playtime

  #Max time
  user_list[6] = ans_max_playtime
  
  return user_list

preferences_list = user_to_pref()





### Fifth program: Getting top games ##########################################

def get_top_games(lst):
    # 1: Category
    def category(user, df):
        user_cat = user[0] # extract relevant string
        sub_df = df[df[user_cat]==True] # take subsection of df
        return sub_df


    # 1.2: Category2

    def category2(user, df):
        user_cat = user[1]
        sub_df = df[df[user_cat]==True]
        return sub_df

    
    # 2: Mechanisms
    
    def mechanisms(user, df):
        user_mec = user[2]
        sub_df = df[df[user_mec]==True]
        return sub_df

    # 3: Number of players

    def numplayers(user, df):
        
        # extract user's interval
        min_num = user[3]
        max_num = user[4]
        
        # take subsection of df
        sub_df = df.query("@min_num <= minplayers <= @max_num" or 
                          "@min_num <= maxplayers <= @max_num")
        return sub_df
    
    
    # 4: Playtime
    
    def playtime(user, df):
        
        min_time = user[5]
        max_time = user[6] 
        
        sub_df = df.query("@min_time <= playingtime <= @max_time")
        return sub_df

    def user_to_data(user, df):
        '''
        Takes in a list of user preferences over boardgame specifications and a dataframe of 
        boardgames. Returns a subsection of the initial dataframe, containing only the boardgames
        in line with the user\'s preferences.
        '''
        
        subdf_1 = category(user, df)
        subdf_2 = category2(user, subdf_1)
        subdf_3 = mechanisms(user, subdf_2)
        subdf_4 = numplayers(user, subdf_3)
        final_subdf = playtime(user, subdf_4)
        
        return final_subdf

    p = preferences_list

    suitable_games = user_to_data(p, data)
    suitable_games.reset_index(drop=True, inplace=True)

    # Raise error if df with possible games is empty
    def check_empty(df):
        if df.empty:
            popup_empty()
            raise ValueError('No matching game found')



    def popup_empty():
        message = 'Sorry, we could not find any games which fit your preferences. Please close the program and try again.'

        popup = tk.Tk()
        # Sets the size of the popup and the title in the most upper bar
        popup.geometry('500x250')
        popup.title('No matches')

        # Which message the popups shows. Wraplength makes the message continue on the
        # next line. Without the wraplength parameter the message wont fit on the popup
        label = tk.Label(popup, text=message, font=("Helvetica", 20), wraplength=450)
        label.pack(pady=20)

        # Frames need to be defined otherwise you get errors
        button_frame = tk.Frame(popup)
        button_frame.pack(pady=20)

        B = tk.Button(button_frame, text="Close", command=popup.destroy, width=15, height=20)
        B.pack(padx=10)

        popup.mainloop()
        
    
    
    # 1: Highest rated

    def rated(df):
        return df.loc[0, 'name']


    # 2: Most played

    def played(df):
        sorted_df = df.sort_values('usersrated', ascending=False)
        sorted_df.reset_index(drop=True, inplace=True)
        return sorted_df.loc[0, 'name']

    def names(df):
        check_empty(df)
        r = rated(df)
        p = played(df)
        
        return r, p
    
    high_rated, most_played = names(suitable_games)
    return high_rated, most_played, suitable_games

highest_ranked, most_ranked, df_filtered = get_top_games(preferences_list)



### Sixth program: presenting boardgame #######################################

def get_image_link(game_name):
    row = df_filtered.loc[df_filtered['name'] == game_name]
    return row['image'].values[0]

def get_description(game_name):
    row = df_filtered.loc[df_filtered['name'] == game_name]
    return row['description'].values[0]

used_numbers = []
def random_nonrepeat(x):
    # Create a list of possible numbers to choose from
    nums = list(range(x+1))
    # Remove any previously used numbers
    for num in used_numbers:
        nums.remove(num)
    # Choose a random number from the remaining pool
    y = random.choice(nums)
    # Add the new number to the list of used numbers
    used_numbers.append(y)
    # If all numbers have been used, reset the list of used numbers
    if len(used_numbers) == x+1:
        used_numbers.clear()
    return y

displayed_random_game = []
df = data
def random_game():
    global displayed_random_game, df
    df = df.drop(df[df['name'] == highest_ranked].index)
    df = df.drop(df[df['name'] == most_ranked].index)
    if len(displayed_random_game) != 0:
        df = df.drop(df[df['name'] == displayed_random_game[-1]].index)    
    size_df = len(df)
    i = random_nonrepeat(size_df)
    game_title = df.loc[i, 'name']
    game_description = df.loc[i, 'description']
    game_image_link = df.loc[i, 'image']
    displayed_random_game.append(game_title)
    return game_title, game_description, game_image_link

def create_tkImage(link):
    img_url = link
    response = requests.get(img_url)
    img_data = response.content
    img = Image.open(BytesIO(img_data))
    img = img.resize((300, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img

def random_button():
    global frame3, discrip_label_3, frame3_3, frame3_2, frame3_1, title_random, title_game_label_3
    title_game_3, discription_3, image_link_3 = random_game()
    
    discrip_label_3.pack_forget()
    frame3_3.pack_forget()
    title_game_label_3.pack_forget()
    frame3_2.pack_forget()
    frame3_1.pack_forget()
    title_random.pack_forget()
    frame3.pack_forget()
    
    
    frame3 = ck.CTkFrame(root, fg_color='#383838')
    frame3.pack(side='left', fill='both', expand=True, padx=5, pady=5)
    
    title_random = ck.CTkLabel(frame3, text='3. Random game which fits your preferences', font=ck.CTkFont(size=20, weight='bold'), wraplength=340) 
    title_random.pack(pady=10)
    
    frame3_1 = ck.CTkFrame(frame3, fg_color='black', width=300, height=200)
    frame3_1.pack()
    
    image_3 = create_tkImage(image_link_3)
    image_label_3 = ck.CTkLabel(frame3_1, image=image_3)
    image_label_3.configure(text='')  # Set the text to an empty string
    image_label_3.pack()
    image_label_3.image = image_3
    
    frame3_2 = ck.CTkFrame(frame3, fg_color='#383838', width=300, height=50)
    frame3_2.pack(pady=10)
    
    title_game_label_3 = ck.CTkLabel(frame3_2, text=title_game_3, font=ck.CTkFont(size=17, weight='normal'), wraplength=350) 
    title_game_label_3.pack()
    
    frame3_3 = ck.CTkScrollableFrame(frame3, fg_color='#2b2b2b', width=300, height=250)
    frame3_3.pack(pady=10)
    
    discrip_label_3 = ck.CTkLabel(frame3_3, text=discription_3, font=ck.CTkFont(size=12, weight='normal'), wraplength=300) 
    discrip_label_3.pack() 


# This root.mainloop is from the loading popup. This way all above code is 
# excicuded 
root.after(2000, root.destroy)
root.mainloop()


root = ck.CTk()


title_game_3, discription_3, image_link_3 = random_game()  

image_link_1 = get_image_link(highest_ranked) 
image_link_2 = get_image_link(most_ranked)

title_game_1 = highest_ranked
title_game_2 = most_ranked

discription_1 =  get_description(highest_ranked)
discription_2 =  get_description(most_ranked)


root.geometry('1020x600')
root.title('Boardgame Recommender')
ck.set_appearance_mode("Dark")

title_label = ck.CTkLabel(root, text='Boardgame Recommendation', font=ck.CTkFont(size=30, weight='bold')) 
title_label.pack(padx=5, pady=5)

quit_button = ck.CTkButton(root, text='quit', width=45, height=10, command=root.destroy, fg_color='red', text_color='black')
quit_button.pack(side="bottom", anchor="se", padx=10, pady=10)

refresh_button = ck.CTkButton(root, text='load different random game', width=45, height=10, command=random_button)
refresh_button.pack(side="bottom", anchor="se", padx=10, pady=10)

frame1 = ck.CTkFrame(root, fg_color='#383838')
frame1.pack(side='left', fill='both', expand=True, padx=5, pady=5)

frame2 = ck.CTkFrame(root, fg_color='#383838')
frame2.pack(side='left', fill='both', expand=True, padx=5, pady=5)

frame3 = ck.CTkFrame(root, fg_color='#383838')
frame3.pack(side='left', fill='both', expand=True, padx=5, pady=5)

title_high_r = ck.CTkLabel(frame1, text='1. Highest rated game which fits your preferences', font=ck.CTkFont(size=20, weight='bold'), wraplength=340) 
title_high_r.pack(pady=10) 

title_most_p = ck.CTkLabel(frame2, text='2. Most rated game which fits your preferences', font=ck.CTkFont(size=20, weight='bold'), wraplength=340) 
title_most_p.pack(pady=10) 

title_random = ck.CTkLabel(frame3, text='3. Random game which fits your preferences', font=ck.CTkFont(size=20, weight='bold'), wraplength=340) 
title_random.pack(pady=10) 

frame1_1 = ck.CTkFrame(frame1, fg_color='black', width=300, height=200)
frame1_1.pack()

frame2_1 = ck.CTkFrame(frame2, fg_color='black', width=300, height=200)
frame2_1.pack()

frame3_1 = ck.CTkFrame(frame3, fg_color='black', width=300, height=200)
frame3_1.pack()

image_1 = create_tkImage(image_link_1)
image_label_1 = ck.CTkLabel(frame1_1, image=image_1)
image_label_1.configure(text='')  # Set the text to an empty string
image_label_1.pack()
image_label_1.image = image_1

image_2 = create_tkImage(image_link_2)
image_label_2 = ck.CTkLabel(frame2_1, image=image_2)
image_label_2.configure(text='')  # Set the text to an empty string
image_label_2.pack()
image_label_2.image = image_2

image_3 = create_tkImage(image_link_3)
image_label_3 = ck.CTkLabel(frame3_1, image=image_3)
image_label_3.configure(text='')  # Set the text to an empty string
image_label_3.pack()
image_label_3.image = image_3

frame1_2 = ck.CTkFrame(frame1, fg_color='#383838', width=300, height=50)
frame1_2.pack(pady=10)

frame2_2 = ck.CTkFrame(frame2, fg_color='#383838', width=300, height=50)
frame2_2.pack(pady=10)

frame3_2 = ck.CTkFrame(frame3, fg_color='#383838', width=300, height=50)
frame3_2.pack(pady=10)

title_game_label_1 = ck.CTkLabel(frame1_2, text=title_game_1, font=ck.CTkFont(size=17, weight='normal'), wraplength=350) 
title_game_label_1.pack() 

title_game_label_2 = ck.CTkLabel(frame2_2, text=title_game_2, font=ck.CTkFont(size=17, weight='normal'), wraplength=350) 
title_game_label_2.pack() 

title_game_label_3 = ck.CTkLabel(frame3_2, text=title_game_3, font=ck.CTkFont(size=17, weight='normal'), wraplength=350) 
title_game_label_3.pack() 

frame1_3 = ck.CTkScrollableFrame(frame1, fg_color='#2b2b2b', width=300, height=250)
frame1_3.pack(pady=10)

frame2_3 = ck.CTkScrollableFrame(frame2, fg_color='#2b2b2b', width=300, height=250)
frame2_3.pack(pady=10)

frame3_3 = ck.CTkScrollableFrame(frame3, fg_color='#2b2b2b', width=300, height=250)
frame3_3.pack(pady=10)

discrip_label_1 = ck.CTkLabel(frame1_3, text=discription_1, font=ck.CTkFont(size=12, weight='normal'), wraplength=300) 
discrip_label_1.pack() 

discrip_label_2 = ck.CTkLabel(frame2_3, text=discription_2, font=ck.CTkFont(size=12, weight='normal'), wraplength=300) 
discrip_label_2.pack(anchor='w') 

discrip_label_3 = ck.CTkLabel(frame3_3, text=discription_3, font=ck.CTkFont(size=12, weight='normal'), wraplength=300) 
discrip_label_3.pack() 


root.mainloop()
