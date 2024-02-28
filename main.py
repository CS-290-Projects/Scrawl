import tkinter as tk
from tkinter import ttk

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
        self.menu_file.add_command(label='Save')
        self.menu_file.add_command(label='Open')
        
        self.menu_bar.add_cascade(menu=self.menu_help, label='Help')
        self.menu_help.add_command(label='Settings')


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

        
class SettingsFrame(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)

        
        # Variables
        self.example_var = tk.StringVar()
        self.example_var.set("Alt + a")

        ## General
        self.dark_light_mode_var = tk.StringVar()
        self.dark_light_mode_var.set('Light mode')

        self.conflict_notifier_var = tk.StringVar()
        self.conflict_notifier_var.set("")

        self.save_note_var = tk.StringVar()
        self.save_note_var.set("Ctrl + s")

        self.create_note_var = tk.StringVar()
        self.create_note_var.set('Ctrl + n')

        self.switch_to_note_var = tk.StringVar()
        self.switch_to_note_var.set('Ctrl + m')

        self.bold_text_var = tk.StringVar()
        self.bold_text_var.set('Ctrl + b')

        self.italic_text_var = tk.StringVar()
        self.italic_text_var.set('Ctrl + i')

        self.underline_text_var = tk.StringVar()
        self.underline_text_var.set('Ctrl + u')

        ## Keybinds 
        self.kb_conflict_notifier_var = tk.StringVar()
        self.kb_conflict_notifier_var.set('')

        self.configure(height=70, width=70)
        self.grid(column=1, row=0, sticky='NESW')

        

        self.create_widgets()
        self.create_layout()
        
                

    def create_widgets(self):
        # Createing the tabs
        self.general_tab = ttk.Frame(self)
        self.keybinds_tab = ttk.Frame(self)

        self.add(self.general_tab, text='General')
        self.add(self.keybinds_tab, text='Key Binds')

        # General Tab Widget Creation
        # Any keybinds should be based on the control key
        # top frame for warnings
        self.warning_section = ttk.Frame(self.general_tab)
        self.gen_conflict_notifier = ttk.Label(self.warning_section, textvariable=self.conflict_notifier_var)
        self.gen_conflict_notifier['font'] = '14'

        self.save_to_label = ttk.Label(self.general_tab, text="Save Folder")

        self.dark_light_mode_label = ttk.Label(self.general_tab, text='Theme')
        self.dark_light_mode_button = ttk.Button(self.general_tab, textvariable=self.dark_light_mode_var)
        

        self.keybind_info_gen_tab = ttk.Label(self.general_tab, text='The keybinds offered on this page are configured to use the control key.')

        self.create_note_label = ttk.Label(self.general_tab, text="Create New Note")
        self.create_note_bind = ttk.Entry(self.general_tab, textvariable=self.create_note_var, state='disabled')
        self.create_note_edit = ttk.Button(self.general_tab, text='Edit')
        self.create_note_edit['command'] = lambda: self.change_key_bind(self.create_note_bind, self.create_note_var, self.ctrl_key_detector)

        self.save_note_label = ttk.Label(self.general_tab, text='Save Note')
        self.save_note_bind = ttk.Entry(self.general_tab, textvariable=self.save_note_var, state='disabled')
        self.save_note_edit = ttk.Button(self.general_tab, text='Edit')
        self.save_note_edit['command'] = lambda: self.change_key_bind(self.save_note_bind, self.save_note_var, self.ctrl_key_detector)

        self.switch_to_note_label = ttk.Label(self.general_tab, text='Switch to Note')
        self.switch_to_note_bind = ttk.Entry(self.general_tab, textvariable=self.switch_to_note_var, state='disabled')
        self.switch_to_note_edit = ttk.Button(self.general_tab, text='Edit')
        self.switch_to_note_edit['command'] = lambda: self.change_key_bind(self.switch_to_note_bind, self.switch_to_note_var, self.ctrl_key_detector)

        self.bold_text_label = ttk.Label(self.general_tab, text='Bold Text')
        self.bold_text_bind = ttk.Entry(self.general_tab, textvariable=self.bold_text_var, state='disabled')
        self.bold_text_edit = ttk.Button(self.general_tab, text='Edit')
        self.bold_text_edit['command'] = lambda: self.change_key_bind(self.bold_text_bind, self.bold_text_var, self.ctrl_key_detector)

        self.italic_text_label = ttk.Label(self.general_tab, text='Italic Text')
        self.italic_text_bind = ttk.Entry(self.general_tab, textvariable=self.italic_text_var, state='disabled')
        self.italic_text_edit = ttk.Button(self.general_tab, text='Edit')
        self.italic_text_edit['command'] = lambda: self.change_key_bind(self.italic_text_bind, self.italic_text_var, self.ctrl_key_detector)

        self.underline_text_label = ttk.Label(self.general_tab, text='Underline Text')
        self.underline_text_bind = ttk.Entry(self.general_tab, textvariable=self.underline_text_var, state='disabled')
        self.underline_text_edit = ttk.Button(self.general_tab, text='Edit')
        self.underline_text_edit['command'] = lambda: self.change_key_bind(self.underline_text_bind, self.underline_text_var, self.ctrl_key_detector)

        # Key Binds Tab Widget Creation
        # Keybinds should be based on the alt key
        self.kb_conflict_notifier = ttk.Label(self.keybinds_tab, textvariable=self.kb_conflict_notifier_var)

        self.example_label = ttk.Label(self.keybinds_tab, text="Key Bind:")
        self.example_bind = ttk.Entry(self.keybinds_tab, textvariable=self.example_var, state='disabled')
        self.change_example_bind = ttk.Button(self.keybinds_tab, text='Edit')
        self.change_example_bind['command'] = lambda: self.change_key_bind(self.example_bind, self.example_var, self.alt_key_detector)    
        
    def create_layout(self):
        # General Tab Layout
        self.warning_section.grid(row=0, column=0, columnspan=4)
        self.gen_conflict_notifier.grid(row=0, column=0, columnspan=4)

        self.save_to_label.grid(row=1, column=0)

        self.dark_light_mode_label.grid(row=2, column=0)
        self.dark_light_mode_button.grid(row=2, column=1)

        self.keybind_info_gen_tab.grid(row=3, column=0, columnspan=3)
        
        self.create_note_label.grid(row=4, column=0)
        self.create_note_bind.grid(row=4, column=1)
        self.create_note_edit.grid(row=4, column=2)
        
        self.save_note_label.grid(row=5, column=0)
        self.save_note_bind.grid(row=5, column=1)
        self.save_note_edit.grid(row=5, column=2)
        
        self.switch_to_note_label.grid(row=6, column=0)
        self.switch_to_note_bind.grid(row=6, column=1)
        self.switch_to_note_edit.grid(row=6, column=2)
        
        self.bold_text_label.grid(row=7, column=0)
        self.bold_text_bind.grid(row=7, column=1)
        self.bold_text_edit.grid(row=7, column=2)

        self.italic_text_label.grid(row=8, column=0)
        self.italic_text_bind.grid(row=8, column=1)
        self.italic_text_edit.grid(row=8, column=2)

        self.underline_text_label.grid(row=9, column=0)
        self.underline_text_bind.grid(row=9, column=1)
        self.underline_text_edit.grid(row=9, column=2)
        
        # Keybinds Tab Layout
        self.kb_conflict_notifier.grid(row=0, column=0, columnspan=4)

        self.example_label.grid(row=1, column=0)
        self.example_bind.grid(row=1, column=1)
        self.change_example_bind.grid(row=1, column=2)
        pass
    
    def alt_key_detector(self, event):
        self.var.set("Alt_L + " + event.keysym)
        self.obj['state'] = 'disable'
        # add a focus to a label
        self.kb_tab_bind_list = []
        self.conflict_checker(self.kb_tab_bind_list)
    
    def ctrl_key_detector(self, event):
        self.var.set("Ctrl + " + event.keysym)
        self.obj['state'] = 'disable'
        self.keybind_info_gen_tab.focus_set() # removes the users ablilty to continue editing the bind, even after the entry widget is disabled
        # list of ctrl key binds
        self.gen_tab_bind_list = [self.save_note_var.get(), self.create_note_var.get(), self.switch_to_note_var.get(), self.bold_text_var.get(), self.underline_text_var.get()]
        self.conflict_checker(self.gen_tab_bind_list)
    
    def conflict_checker(self, bind_list):
        number_of_conflicts = 0
        for i in range(len(bind_list)):
            for j in range(i + 1, len(bind_list)):
                if bind_list[i] == bind_list[j]:
                    number_of_conflicts += 1
        if number_of_conflicts != 0:
            text = "WARNING: There are keybinds that share the same command. Please fix this issue to avoid command problems."
            self.conflict_notifier_var.set(text)
        else:
            text = ''
            self.conflict_notifier_var.set(text)

    def change_key_bind(self, obj, var, key_detector):
        obj['state'] = 'active'
        var.set("")
        obj.focus()
        # Event needs to be a paramater by itself in the key detectors
        # These objects get around that issue
        self.obj = obj
        self.var = var
        obj.bind("<KeyPress>", key_detector)
        
        
    
        


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

    def change_frame(self):
        frame = self.frames[self.index.get()]
        frame.tkraise()

    def set(self, index):
        self.index.set(index)


    


if __name__ == "__main__":
    app = App()
    control = PanelControlFrame(app)
    app.mainloop()