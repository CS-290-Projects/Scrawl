import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from settings import SettingsFrame
from note import NoteFrame

class PanelControlFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Variables
        self.index = tk.IntVar()

        # Widgets
        self.note_button = ttk.Button(self, text='Notes')
        self.settings_button = ttk.Button(self, text='Settings')
          
        # Button Commands
        self.note_button['command'] = lambda: [self.set(0), self.change_frame()]
        self.settings_button['command'] = lambda: [self.set(1), self.change_frame()]
        
        # Widget Placement
        options = {'pady':2, 'ipadx':2, 'ipady':2}

        self.note_button.grid(row=0, column=0, **options)
        self.settings_button.grid(row=1, column=0, pady=20, ipady=2)

        # Frame Placement
        self.grid(column=0, row=0, sticky='NSEW', padx=10)
        
        # Other Frame Init
        self.frames = {}
        self.frames[0] = NoteFrame(parent)
        self.frames[1] = SettingsFrame(parent)
        self.change_frame()
        
        
        # give the parent a reference to this frame
        parent.setPanelControlFrame(self)


    def change_frame(self):
        frame = self.frames[self.index.get()]
        if frame == self.frames[0]:
            #grab the binds the user has created when they switch back to the notes page
            self.frames[0].create_binds()
        frame.tkraise()

    def set(self, index):
        self.index.set(index)