import customtkinter as ck
import tkinter as tk
import sys

questions = {'Q1': 'What is?', 'Q2': 'Why is?', 'Q3': 'How is?'}
numofq = len(questions)
answers = {}
question_number = 1
moved_once = 0
come_from_last_q = 0
completed_q = 0

if numofq<3:
    print('ERROR: There needs to be at leasth 3 questions')
    sys.exit()


###############################################################################   
    # Here we need to figure out how this function will cause the rest of the 
    # recommendation code to run. See below the block which indicates where 
    # this code should be placed.
###############################################################################

def continue_with_recommendation():
    global completed_q
    print('Recommend:....')
    print(f'saved answers: {answers}')
    completed_q += 1
    
    
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
    question_label = ck.CTkLabel(root, text=questions['Q'+str(question_number)], font=ck.CTkFont(size=20, weight='bold'))
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
root.title('Boardgame Recommender Questionnaire')
ck.set_appearance_mode("Dark")

title_label = ck.CTkLabel(root, text='Boardgame Questionnaire', font=ck.CTkFont(size=30, weight='bold')) 
title_label.pack(padx=5, pady=5)

question_label = ck.CTkLabel(root, text=questions['Q'+str(question_number)], font=ck.CTkFont(size=20, weight='bold'))

textbox=ck.CTkTextbox(root, width=680, height=200, fg_color='#383838')
textbox.insert('0.0','Answer here')

next_button = ck.CTkButton(root, text='Next Question', width=250, command=nextquestioncommand)

previous_button = ck.CTkButton(root, text='Previous Question', width=250, command=previousquestioncommand)

submit_button = ck.CTkButton(root, text='Submit', width=250, command=submitanswerscommand)

quit_button = ck.CTkButton(root, text='quit', width=45, height=10, command=root.destroy, fg_color='red', text_color='black')



define_layout()

###############################################################################
# The code will continue here after questionaire. Thus here needs to be all the 
# code that will recommend the boardgame
##############################################################################
#print('test')   # As can be seen with this print, this code excicutes immediatly 
                # We need to find a way that a call of continue_with_recommendation
                # causes this code to run and not earlier
                
                # Maybe make a bigass function which the continue_woth_recommendation
                # will call??
                

root.mainloop()

                
while completed_q!=1:
    pass

print('TEST!')

root = ck.CTk()

root.geometry('750x450')
root.title('Boardgame Recommender Questionnaire')
ck.set_appearance_mode("Dark")

title_label = ck.CTkLabel(root, text='Boardgame Questionnaire', font=ck.CTkFont(size=30, weight='bold')) 
title_label.pack(padx=5, pady=5)

question_label = ck.CTkLabel(root, text=questions['Q'+str(question_number)], font=ck.CTkFont(size=20, weight='bold'))

textbox=ck.CTkTextbox(root, width=680, height=200, fg_color='#383838')
textbox.insert('0.0','Answer here')


quit_button = ck.CTkButton(root, text='quit', width=45, height=10, command=root.destroy, fg_color='red', text_color='black')
quit_button.pack()
                

root.mainloop()

