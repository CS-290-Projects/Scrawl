import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
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
        self.menu_file.add_command(label='Open', command=self.open_command)
        
        self.menu_bar.add_cascade(menu=self.menu_help, label='Help')
        self.menu_help.add_command(label='Settings')

        # add a text area for the name of the note

        # a reference to the panelControlFrame so we can access it
        self.panelControlFrame = None 
        # a reference to the filepath of the current note
        self.filepath = None

    def setPanelControlFrame(self, panelControlFrame):
        self.panelControlFrame = panelControlFrame
    
    def save_command(self): # save the current note
        title = self.panelControlFrame.frames[0].title.get('1.0', 'end-1c')
        # access the note from the NoteFrame
        text = self.panelControlFrame.frames[0].notes.get('1.0', 'end-1c')
        # if filepath exists, use it
        if hasattr(self, 'filepath') and self.filepath:
            filename = self.filepath
        else:

            # replace spaces with underscores so we can use it as a filename
            title = title.replace(' ', '_')
            # if the title is empty, use 'untitled'
            if title == '':
                title = 'untitled'
            # if the notes directory doesn't exist, create it
            if not os.path.exists('notes'):
                os.makedirs('notes')
            # generate the filename
            filename = 'notes/' + title + '.txt'
        # save the note to a file
        with open(filename, 'w') as file:
            file.write(text)
    
    def open_command(self): # open the selected note
        # open a dialog box for the user to select a file
        filepath = filedialog.askopenfilename(initialdir="notes", title="Select file",
                                              filetypes=(("text files", "*.txt"), ("all files", "*.*")))# if a file was selected
        if filepath:
            # try to open the note file
            try:
                with open(filepath, 'r') as file:
                    text = file.read()
            except FileNotFoundError:
                text = 'File not found.'
            # get the title of the note from the filename
            title = os.path.basename(filepath)
            # remove the .txt extension
            title = title[:-4]
            # display the title in the frame
            self.panelControlFrame.frames[0].title.delete('1.0', 'end')
            self.panelControlFrame.frames[0].title.insert('1.0', title)
            # display the note in the frame
            self.panelControlFrame.frames[0].notes.delete('1.0', 'end')
            self.panelControlFrame.frames[0].notes.insert('1.0', text)
            # save the filepath so we can save the note back to the same file
            self.filepath = filepath

        

class NoteFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid(column=1, row=0, sticky='NSEW')
        
        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        # create a title for the note
        self.title = tk.Text(self, width=34,height=1)
        # create a text area for the note
        self.notes = tk.Text(self,width=68, height=45) #width and height is measured in characters

    def create_layout(self):
        self.columnconfigure((0,1), weight=1)
        self.rowconfigure((0,1), weight=1)

        self.title.grid(row=0, column=0, sticky='NSEW')
        self.notes.grid(row=1, column=0, sticky='NSEW')

        
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