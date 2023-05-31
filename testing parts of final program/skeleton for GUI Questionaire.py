def set_question_label():
    question_label = ck.CTkLabel(root, text=questions['Q'+str(question_number)], font=ck.CTkFont(size=20, weight='bold'))
    question_label.pack() 

def set_textbox():
    textbox=ck.CTkTextbox(root, width=680, height=200, fg_color='#383838')
    textbox.insert('0.0','Answer here')
    textbox.pack(pady=10)

def set_next_button():
    next_button = ck.CTkButton(root, text='Next Question', width=250, command=nextquestion)
    next_button.pack(side='right', padx=50)
    
def set_previous_button():
    previous_button = ck.CTkButton(root, text='Previous Question', width=250, command=previousquestion)
    previous_button.pack(side='left', padx=50)

def set_sumbit_button():
    submit_button = ck.CTkButton(root, text='Submit', width=250, command=submitanswers)
    submit_button.pack(side='right', padx=50)


def set_quit_button():
    quit_button = ck.CTkButton(root, text='quit', width=45, height=10, command=root.destroy, fg_color='red', text_color='black')
    quit_button.pack(side="left", anchor="sw", padx=10, pady=10)

# Main body of coding:
    # Runs all functions which sets all visuals in ordor 
    # Runs the title before any function

# First run: question_number==1 and moved_once==0:
    # We dont want to pack_forget anything
    # We want to set all visuals in the right ordor:
        # Run Question_label
        # Run TextBox
        # Run next button (the big one)
        # Run !NO! previous button
        # Run Quit button

# Go from Q1 to Q2: 1<question_number<number_of_questions and moved_once==0:
    # Update moved_once variable
    # Forget question_label
    # Forget TextBox
    # Forget next_button
    # Run Question_label
    # Run TextBox
    # Run next button
    # Run previous button

# When you go back to Q1: question_number==1 and moven_once !=0:
    # Forget question_label
    # Forget TextBox
    # Forget next_button
    # Forget previous_button
    # Run Question_label
    # Run TextBox
    # Run next button

# When you move from to any Q except the last or first: 
                            #1<question_number<number_of_1 and moved_once !=0:
    # Forget question_label
    # Forget TextBox
    # Forget next_button
    # Forget previous_button
    # Check if come_from_last_q is true:
        # If so, forget submit button and update come_from_last_q to False
    # Run Question_label
    # Run TextBox
    # Run next button
    # Run previous button

# When you move to last Q: question_number==number_of_q  and moved_once !=0:
    # Update come_from_last_q to True
    # Forget question_label
    # Forget TextBox
    # Forget next_button
    # Forget previous_button
    # Run Question_label
    # Run TextBox
    # Run submut button
    # Run previous button
        
    
    