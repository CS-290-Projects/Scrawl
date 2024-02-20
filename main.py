import tkinter as tk
from tkinter import ttk
import os

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
        self.menu_file.add_command(label='Open')
        
        self.menu_bar.add_cascade(menu=self.menu_help, label='Help')
        self.menu_help.add_command(label='Settings')
        # a reference to the panelControlFrame so we can access it
        self.panelControlFrame = None 

    def setPanelControlFrame(self, panelControlFrame):
        self.panelControlFrame = panelControlFrame
    
    def save_command(self): # save the current note
        # access the note from the NoteFrame
        text = self.panelControlFrame.frames[0].notes.get('1.0', 'end-1c')
        # like in other note programs, the first line is the title
        title = text.split('\n')[0]
        # replace spaces with underscores so we can use it as a filename
        title = title.replace(' ', '_')
        # if the title is empty, use 'untitled'
        if title == '':
            title = 'untitled'
        # if the notes directory doesn't exist, create it
        if not os.path.exists('notes'):
            os.makedirs('notes')
        # save the note to a file
        with open('notes/' + title + '.txt', 'w') as file:
            file.write(text)

class NoteFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid(column=1, row=0, sticky='NSEW')
        
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.notes = tk.Text(self,width=68, height=45) #width and height is measured in characters

    def create_layout(self):
        self.columnconfigure((0,1,2), weight=1, uniform='a')
        self.rowconfigure((0,1,2), weight=1, uniform='a')

        self.notes.grid(row=0, column=0, sticky='NSEW')

        
class SettingsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.button = ttk.Button(self, text='YAAAAY IM WORKING')
        self.button.grid(column=0, row=0)

        self.grid(column=1, row=0, sticky='NSEW')

        def create_widgets(self):
            pass

        def create_layout(self):
            
            pass



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
        frame.tkraise()

    def set(self, index):
        self.index.set(index)


    


if __name__ == "__main__":
    app = App()
    control = PanelControlFrame(app)
    app.mainloop()