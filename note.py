import tkinter as tk
from tkinter import ttk
import time

# variables
autosave = True 
autosave_interval = 5 # seconds after the user stops typing to save the note (0 to save on each keyup)

class NoteFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid(column=1, row=0, sticky='NSEW')
        
        # record the time the user started typing (initialize to the current time)
        self.type_timer = 0

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        # create a title for the note
        self.title = tk.Text(self, width=34,height=1)
        # create a text area for the note
        self.notes = tk.Text(self,width=68, height=45) #width and height is measured in characters
        # whenever the user lets their key up, call the on_keyup method
        self.notes.bind('<KeyRelease>', self.on_keyup)
        
    def on_keyup(self, event):
        # set the timer to the current time
        self.type_timer = time.time()
        if autosave:
            # after autosave_interval seconds, save the note unless the user types again
            self.after(autosave_interval * 1000, self.check_timer)
    
    def check_timer(self):
        # if the user hasn't typed for autosave_interval seconds
        if self.type_timer + autosave_interval <= time.time():
            # save the note
            self.master.save_command()

    def create_layout(self):
        self.columnconfigure((0,1), weight=1)
        self.rowconfigure((0,1), weight=1)

        self.title.grid(row=0, column=0, sticky='NSEW')
        self.notes.grid(row=1, column=0, sticky='NSEW')
