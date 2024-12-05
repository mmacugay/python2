from tkinter import *

import os.path
from vote import Vote

class Gui:
    def __init__(self, root):
        '''
        Creates the user interface to be manipulated by buttons.

        Args:
            root - provided tkinter window
        '''
        self.window = root
        self.voter = Vote()

        self.vote_menu = Frame(self.window)        
        
        self.button_start = Button(self.vote_menu, text='START', command=self.begin_vote)
        self.button_stop = Button(self.vote_menu, text="CALCULATE", command=self.finish_vote)
        self.message_content = Label(self.vote_menu, text="")

        self.button_start.pack(side='left', pady=10)
        self.button_stop.pack(side="right", pady=10)
        self.message_content.pack(side='bottom', pady=10)


        self.candidate_menu = Frame(self.window)
        self.radio_result = IntVar()
        self.radio_result.set(3)
        self.radio_one = Radiobutton(self.candidate_menu, text="John", variable=self.radio_result, value = 1)
        self.radio_two = Radiobutton(self.candidate_menu, text="Jane", variable=self.radio_result, value = 2)
        self.button_save = Button(self.candidate_menu, text='VOTE', command=self.submit)

        self.button_save.pack(side='bottom')

        self.vote_menu.pack()
        
    def begin_vote(self):
        '''
        Render the Candidate window
        '''
        # pack needed items
        self.radio_one.pack(side="left", anchor="w")
        self.radio_two.pack(side="left", anchor="w")
        self.candidate_menu.pack()

        # forget message
        self.message_content.forget()

    def submit(self):
        '''
        Begin the voting processing, depending on user selection
        '''
        if self.radio_result.get() > 3 and self.radio_result.get() < 1:
            self.message_content.config(text = "Please select candidate")
            self.message_content.pack(side='bottom', pady=10)
        else:
            choice = self.valueParse()
            self.message_content.config(text = f"You voted for {choice}")
            self.message_content.pack(side='bottom', pady=10)
            
    def valueParse(self):
        '''
        Voting process relying on the Vote class.
        '''
        # set vote number
        self.voter.vote(self.radio_result.get())

        # forget old items
        self.radio_result.set(3)
        self.candidate_menu.forget()
        
        
        # return vote result for display
        if self.radio_result.get() == 1:
            return "John"
        else:
            return "Jane"

    def finish_vote(self):
        self.message_content.config(text = str(self.voter))
        self.message_content.pack(side='bottom', pady=10)