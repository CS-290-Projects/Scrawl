import tkinter as tk
import os

from panelControlFrame import PanelControlFrame
from databaseHandler import DatabaseHandler

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Scrawl')
        self.geometry('1000x800')
        self.option_add('*tearOff', False)

        # Menu bar
        self.menu_bar = tk.Menu(self)
        self['menu'] = self.menu_bar
        self.menu_file = tk.Menu(self.menu_bar)
        self.menu_help = tk.Menu(self.menu_bar)

        self.menu_bar.add_cascade(menu=self.menu_file, label='File')
        self.menu_file.add_command(label='New')
        self.menu_file.add_command(label='Save', command=self.save_command)
        self.menu_file.add_command(label='Open', command=self.open_command)
        
        self.menu_bar.add_cascade(menu=self.menu_help, label='Help')
        self.menu_help.add_command(label='Settings')

        # add a text area for the name of the note

        # a reference to the panelControlFrame so we can access it
        self.panelControlFrame = None 
        # a reference to the filepath of the current note
        self.filepath = None
        # create a database handler
        self.db = DatabaseHandler()

        # save when the window is closed, then close the window
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.save_command()
        self.destroy()
    def setPanelControlFrame(self, panelControlFrame):
        self.panelControlFrame = panelControlFrame

    def save_command(self): # save the current note
        title = self.panelControlFrame.frames[0].title.get('1.0', 'end-1c')
        # access the note from the NoteFrame
        text = self.panelControlFrame.frames[0].notes.get('1.0', 'end-1c')
        # save the note to the database
        self.db.save_note_to_db(title, text)
    
    def open_command(self): # open the selected note from the database
        # get the title of the note from the title text area
        title = self.panelControlFrame.frames[0].title.get('1.0', 'end-1c')
        # get the note from the database
        text = self.db.open_note_from_db(title)
        # display the note in the frame
        self.panelControlFrame.frames[0].notes.delete('1.0', 'end')
        self.panelControlFrame.frames[0].notes.insert('1.0', text)


if __name__ == "__main__":
    app = App()
    control = PanelControlFrame(app)
    app.mainloop()