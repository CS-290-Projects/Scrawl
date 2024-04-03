import tkinter as tk
from tkinter import ttk
from tkinter import font
import time
import json



# variables
autosave = True 
autosave_interval = 5 # seconds after the user stops typing to save the note (0 to save on each keyup)
avaliable_fonts = {}




class NoteFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid(column=1, row=0, sticky='NSEW')
        
        
        # record the time the user started typing (initialize to the current time)
        self.type_timer = 0
        self.bold_on_off = False
        
    




        self.create_widgets()
        self.create_layout()
        self.create_binds()


        self.notes.tag_configure("predictive", foreground='grey')
        self.notes.tag_configure('normal', foreground='black')
        self.notes.tag_configure("shorthand", foreground='blue', background='light blue')
        self.predicted_list = ["hello", "banana", "apple", "blame", "beautiful"]
        self.shorthand = {'asd':'asdfghjkl'}

    def create_widgets(self):
        # create a title for the note
        self.title = tk.Text(self, width=34,height=1)
        # create a text area for the note
        self.notes = tk.Text(self,width=68, height=35) #width and height is measured in characters
        # whenever the user lets their key up, call the on_keyup method
        self.notes.bind('<KeyRelease>', self.on_keyup)
        
        self.notes.bind('<KeyRelease>', self.on_input)
        self.notes.bind('<Right>', self.auto_complete)
        self.notes.bind('<Up>', self.insert_shorthand)
        self.notes.bind('<Left>', self.move_left)
        self.notes.bind('<space>', self.space_pressed)
    

        text_font = ("Helvetica", 12)
        self.notes.configure(font=text_font)
        self.title.configure(font=text_font)

    def create_binds(self):
        with open('config.json', 'r') as f:
            config = json.loads(f.read())
            f.close()

        # user defined
        self.notes.bind('<'+config['bold text']+'>', self.change_bold)
        self.notes.bind('<'+config['italic text']+'>', self.change_italics)
        self.notes.bind('<'+config['underline text']+'>', self.change_underline)
        pass

    def change_bold(self, *args):
        bold_font = font.Font(self.notes, self.notes.cget("font"))
        bold_font.configure(weight="bold")
        self.notes.tag_configure("bold", font=bold_font)
        
        try: # change selection to bold
            current_tags = self.notes.tag_names("sel.first")
            if "bold" in current_tags:
                self.notes.tag_remove("bold", "sel.first", "sel.last")
            elif "bold" not in current_tags:
                self.notes.tag_add("bold", "sel.first", "sel.last")
        except: # change word to bold
            text_cursor_position = self.notes.index(tk.INSERT + ' wordstart')
            text_end = self.notes.index(tk.INSERT + ' wordend')
            current_tags = self.notes.tag_names(text_cursor_position)
            if 'bold' in current_tags:
                self.notes.tag_remove("bold", text_cursor_position, text_end)
            else:
                self.notes.tag_add("bold", text_cursor_position, text_end)

    def change_italics(self, *args):
        italic_font = font.Font(self.notes, self.notes.cget("font"))
        italic_font.configure(slant="italic")
        self.notes.tag_configure("italic", font=italic_font)
        
        try: # change selection to italic
            current_tags = self.notes.tag_names("sel.first")
            if "italic" in current_tags:
                self.notes.tag_remove("italic", "sel.first", "sel.last")
            elif "italic" not in current_tags:
                self.notes.tag_add("italic", "sel.first", "sel.last")
        except: # change word to italic
            text_cursor_position = self.notes.index(tk.INSERT + ' wordstart')
            text_end = self.notes.index(tk.INSERT + ' wordend')
            current_tags = self.notes.tag_names(text_cursor_position)
            if 'italic' in current_tags:
                self.notes.tag_remove("italic", text_cursor_position, text_end)
            else:
                self.notes.tag_add("italic", text_cursor_position, text_end)

    def change_underline(self, *args):
        underline_font = font.Font(self.notes, self.notes.cget("font"))
        underline_font.configure(underline=True)
        self.notes.tag_configure("underline", font=underline_font)

        try:
            current_tags = self.notes.tag_names("sel.first")
            if "underline" in current_tags:
                self.notes.tag_remove("underline", "sel.first", "sel.last")
            elif "underline" not in current_tags:
                self.notes.tag_add("underline", "sel.first", "sel.last")
        except:
            text_cursor_position = self.notes.index(tk.INSERT + ' wordstart')
            text_end = self.notes.index(tk.INSERT + ' wordend')
            current_tags = self.notes.tag_names(text_cursor_position)
            if 'underline' in current_tags:
                self.notes.tag_remove("underline", text_cursor_position, text_end)
            else:
                self.notes.tag_add("underline", text_cursor_position, text_end)


    def on_keyup(self, event):
        # set the timer to the current time
        self.type_timer = time.time()
        if autosave:
            # after autosave_interval seconds, save the note unless the user types again
            self.after(autosave_interval * 1000, self.check_timer)

           
    def on_input(self, event):
        user_text = self.get_user_text()
        if user_text == ' ':
            print('no user input')
            return
        check = self.check_if_in_word()
        if check is True:
            # remove pred text
            self.remove_pred_text()
            return
        self.check_if_shorthand(user_txt=user_text)
        pred_text = self.compare_to_pred_list(user_text=user_text)
        if pred_text is None:
            self.remove_pred_text()
            return
        # remove pred text
        self.remove_pred_text()
        self.insert_pred_text(pred_text=pred_text)
         
    def get_user_text(self):
        self.start_txt = self.notes.index(tk.INSERT + " -1c wordstart")
        if self.notes.tag_ranges('predictive'):
            self.end_user_txt = "{}".format(self.notes.tag_ranges('predictive')[0].string)
        else:
            self.end_user_txt = self.notes.index(tk.INSERT + ' -1c wordend')
        return self.notes.get(self.start_txt, self.end_user_txt)

    def check_if_shorthand(self, user_txt):
        start_text = self.start_txt
        end_user_text = self.end_user_txt
        if user_txt in self.shorthand.keys():
            self.notes.tag_add('shorthand', start_text, end_user_text)
            self.complete = self.shorthand[user_txt]
        else:
            self.notes.tag_remove('shorthand', start_text, end_user_text)
            self.complete = ''
        return None
    

    def check_if_in_word(self):
        cursor_pos = self.notes.index(tk.INSERT)
        start_txt = float(self.start_txt)
        end_user_txt = float(self.end_user_txt)
        char_count = end_user_txt - start_txt
        check = float(cursor_pos) - start_txt
        if check == char_count:
            return False
        else:
            return True
    
    def compare_to_pred_list(self, user_text):
        print('user text: {}'.format(user_text))
        for word in self.predicted_list:
            limiter = int(len(word)/2) + 1
            if word.lower().startswith(user_text.lower()):
                if int(len(word[len(user_text):])) < limiter:
                    print(limiter)
                    print('Pred: {}'.format(word[len(user_text):]))
                    return(word[len(user_text):])
                return None
        return None
    
    def insert_pred_text(self, pred_text):
        end_user_txt = self.end_user_txt

        self.notes.insert(end_user_txt, pred_text)
        new_end = self.notes.index(tk.INSERT + ' wordend')
        self.notes.mark_set('insert',  end_user_txt)
        self.notes.tag_add('predictive', 'insert', new_end)
        pass

    def remove_pred_text(self):
        end_user_text = self.end_user_txt
        end_pred_text = self.notes.index(tk.INSERT + '-1c wordend')
        if self.notes.tag_nextrange('predictive', end_user_text, end_pred_text) != '':
            print(self.notes.tag_ranges('predictive'))
            self.notes.delete(end_user_text, end_pred_text)
        pass
    
    def insert_shorthand(self, event):
        start_txt = self.start_txt
        end_user_txt = self.end_user_txt

        if self.notes.tag_nextrange('shorthand', start_txt, end_user_txt) != '':
            self.notes.delete(start_txt, end_user_txt)
            self.notes.insert(start_txt, self.complete)
        else:
            return None
        pass

    def auto_complete(self, event):
        end_pred_text = self.notes.index(tk.INSERT + ' wordend')
        start_txt = self.start_txt
        check = self.check_if_in_word()
        if check is True:
            return None
        if self.notes.tag_ranges('predictive') != '':
            self.notes.tag_remove('predictive', start_txt, end_pred_text)
            self.notes.mark_set('insert', end_pred_text)
        else:
            return None

    def move_left(self, event):
        self.notes.mark_set('insert', 'insert')

    def space_pressed(self, event):
        self.remove_pred_text()
    
    
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
