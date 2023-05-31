import tkinter as tk

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

# Make the buttons
B1 = tk.Button(button_frame, text="Submit", command=popup.destroy, width=15, height=20)
B1.pack(side='right', padx=10)

B2 = tk.Button(button_frame, text="Cancel", command=popup.destroy, width=15, height=20)
B2.pack(side='left', padx=10)


popup.mainloop()