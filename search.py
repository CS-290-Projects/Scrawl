import tkinter as tk
from tkinter import ttk
import time

# variables
autocomplete = True 
autosave_interval = 0.5 # seconds after the user stops typing to attempt an autocomplete (0 to save on each keyup)
tabtoautocomplete = True # if the user presses tab, attempt to autocomplete the title of the note

class SearchFrame(ttk.Frame):
    def __init__(self, parent, controlframe):
        super().__init__(parent)
        self.use_synonyms = False

        self.grid(column=1, row=0, sticky='NSEW')
        
        # record the time the user started typing (initialize to the current time)
        self.type_timer = 0

        self.create_widgets()
        self.create_layout()
        self.master = parent
        self.controlframe = controlframe
        

    def create_widgets(self):
        
        # create a search bar
        self.search = ttk.Entry(self)
        # create a listbox to display the search results
        self.results = tk.Listbox(self)
        # create a box to preview the note
        self.preview = tk.Text(self, width=40, height=45)
        self.preview.config(state='disabled')
        # a button to toggle the use of synonyms
        self.synonyms = ttk.Checkbutton(self, text='Use Synonyms', command=self.toggle_synonyms)
        # display everything
        self.search_command()
        # when the user types in the search bar, call the search method
        self.search.bind('<KeyRelease>', self.search_command)
    def toggle_synonyms(self):
        # toggle the use of synonyms
        self.use_synonyms = not self.use_synonyms
        # search again
        self.search_command()
    def preview_command(self, title):
        # get the note from the database
        text = self.master.db.open_note_from_db(title)
        # display the note in the preview box
        self.preview.config(state='normal')
        self.preview.delete('1.0', 'end')
        self.preview.insert('1.0', text)
        self.preview.config(state='disabled')
    def on_button_click(self, event):
        # Get the index of the clicked item
        index = self.results.curselection()
        # If an item was clicked, open it and preview it
        if index:
            self.master.open_command(self.results.get(index))
            self.preview_command(self.results.get(index))
        
    def open_note(self, event):
         # simply switch to the note view
        self.controlframe.set(0)
        self.controlframe.change_frame()

    def search_command(self, event=None):
        # record the time the user started typing
        self.type_timer = time.time()
        # get the text from the search bar
        text = self.search.get()
        # search the database for notes that match the text
        titles = self.master.db.search_titles(text, self.use_synonyms)
        # clear the listbox
        self.results.delete(0, 'end')
        # remove unnamed notes
        titles = [title for title in titles if title != '']
        # add the titles to the listbox
        for title in titles:
            self.results.insert('end', title)
        # on click, open the note
        self.results.bind('<ButtonRelease-1>', self.on_button_click)
        # on double click, switch to the note view
        self.results.bind('<Double-ButtonRelease-1>', self.open_note)
    
    def check_timer(self):
        # if the user hasn't typed for autosave_interval seconds
        if self.type_timer + autosave_interval <= time.time():
            # save the note
            self.master.save_command()

    def create_layout(self):
        self.columnconfigure((0,1), weight=1)
        self.rowconfigure((0,1), weight=10)
        self.rowconfigure(2, weight=30)
        
        # add another row to the search frame

        self.search.grid(row=0, column=0, sticky='NSEW')
        self.synonyms.grid(row=0, column=1, sticky='NSEW')
        self.results.grid(row=1, column=0, sticky='NSEW')
        self.preview.grid(row=1, column=1, sticky='NSEW')
        
        
