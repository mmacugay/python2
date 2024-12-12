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

        self.message_menu = Frame(self.window)

        self.message_content = Label(self.message_menu, text="")
        self.message_content.pack(side='bottom', pady=10)
        self.message_menu.pack()

        self.vote_menu = Frame(self.window)        
        
        self.button_start = Button(self.vote_menu, text='START', command=self.begin_vote)
        

        self.button_start.pack(side='left', pady=10)


        self.candidate_menu = Frame(self.window)
        self.radio_result = IntVar()
        self.radio_result.set(3)
        self.voter_label = Label(self.candidate_menu, text="Voter ID")
        self.voter_id = Entry(self.candidate_menu, width=20)
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
        self.voter_label.pack()
        self.voter_id.pack()
        self.candidate_menu.pack()

        # forget message
        self.message_content.forget()

    def submit(self):
        '''
        Begin the voting processing, depending on user selection
        '''
        if self.radio_result.get() > 2 or self.radio_result.get() < 1 or self.voter_id.get() == "":
            self.message_content.config(text = "Please enter required fields")
            self.message_content.pack(side='bottom', pady=10)
        else:
            choice = self.valueParse()
            self.message_content.config(text = choice)
            self.message_content.pack(side='bottom', pady=10)
            
    def valueParse(self) -> str:
        '''
        Voting process relying on the Vote class.
        '''
        # set vote number
        check = self.voter.vote(self.voter_id.get(), self.radio_result.get())
        vote = self.radio_result.get()

        # forget old items
        self.radio_result.set(3)
        self.candidate_menu.forget()
        
        
        # return vote result for display
        if not check:
            return "Voter ID has already voted"
    
        if vote == 1:
            return "You voted for John"
        elif vote == 2:
            return "You voted for Jane"
    