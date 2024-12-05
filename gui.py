from tkinter import *

import os.path
from vote import Vote

class Gui:
    def __init__(self, root):
        self.window = root
        self.voter = Vote()

        self.vote_menu = Frame(self.window)        
        
        self.button_start = Button(self.vote_menu, text='START', command=self.begin_vote)
        self.message = ""
        self.message_content = Label(self.vote_menu, text=self.message)

        self.message_content.pack()
        self.button_start.pack(side='bottom')
        self.vote_menu.pack(pady=10)


        self.candidate_menu = Frame(self.window)
        self.radio_result = IntVar()
        self.radio_result.set(3)
        self.radio_one = Radiobutton(self.candidate_menu, text="John", variable=self.radio_result, value = 1)
        self.radio_two = Radiobutton(self.candidate_menu, text="Jane", variable=self.radio_result, value = 2)

        self.button_save = Button(self.candidate_menu, text='VOTE', command=self.submit)

        self.button_save.pack(side='bottom')

        self.vote_menu.pack()
        
    def begin_vote(self):
        # pack needed items
        self.radio_one.pack(side="left", anchor="w")
        self.radio_two.pack(side="left", anchor="w")
        self.candidate_menu.pack()

        

    def submit(self):
        if self.radio_result.get() > 3 and self.radio_result.get() < 1:
            self.message_content.config(text = "Please select candidate")
        else:
            choice = self.valueParse()
            self.message_content.config(text = f"You voted for {choice}")
            
    def valueParse(self):
        # set vote number
        self.voter.vote(self.radio_result.get())

        # forget old items
        self.radio_result.set(3)
        self.candidate_menu.forget()
        self.message_content.forget()
        
        # return vote result for display
        if self.radio_result.get() == 1:
            return "John"
        else:
            return "Jane"
