import tkinter as tk
from tkinter import ttk
import json


class SettingsFrame(ttk.Notebook):
    def __init__(self, parent):
        super().__init__(parent)

        # Grabbing saved settings or creating the data if not found
        try:
            with open('config.json', 'r') as f:
                self.config = json.loads(f.read())
                self.create_variables()
                f.close()
                
        except:
            print('something went wrong')
            with open('config.json', 'w') as f:
                default_settings = {
                    "theme":"Light Mode",
                    "save note":"Control-s",
                    "create note":"Control-n",
                    "switch note":"Control-",
                    "bold text":"Control-b",
                    "italic text":"Control-i",
                    "underline text":"Control-u",
                    "s1":"...", "w1":"...",
                    "s2":"...", "w2":"...",
                    "s3":"...", "w3":"...",
                    "s4":"...", "w4":"...",
                    "s5":"...", "w5":"...",
                    "s6":"...", "w6":"...",
                    "s7":"...", "w7":"...",
                    "s8":"...", "w8":"...",
                    "s9":"...", "w9":"...",
                    "s10":"...", "w10":"...",
                    "s11":"...", "w11":"...",
                    "s12":"...", "w12":"...",
                    "s13":"...", "w13":"...",
                    "s14":"...", "w14":"...",
                    "s15":"...", "w15":"...",
                    "s16":"...", "w16":"...",
                    "s17":"...", "w17":"...",
                    "s18":"...", "w18":"...",
                    "s19":"...", "w19":"...",
                    "s20":"...", "w20":"...",

                }
                json.dump(default_settings, f, indent=4)
            
            with open('config.json', 'r') as f:
                self.config = json.loads(f.read())
                self.create_variables()
                f.close()
                


        self.configure(height=80, width=70)
        self.grid(column=1, row=0, sticky='NESW')
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=2)
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=2)

        self.init_theme()
        self.create_widgets()
        self.create_layout()
    
    def create_variables(self):
        # Variables
        self.example_var = tk.StringVar()
        self.example_var.set(self.config['save note'])

        ## General
        self.dark_light_mode_var = tk.StringVar()
        self.dark_light_mode_var.set('Dark Mode')

        self.save_note_var = tk.StringVar()
        self.save_note_var.set(self.config['save note'])

        self.create_note_var = tk.StringVar()
        self.create_note_var.set(self.config['create note'])

        self.switch_to_note_var = tk.StringVar()
        self.switch_to_note_var.set(self.config['switch note'])

        self.bold_text_var = tk.StringVar()
        self.bold_text_var.set(self.config['bold text'])

        self.italic_text_var = tk.StringVar()
        self.italic_text_var.set(self.config['italic text'])

        self.underline_text_var = tk.StringVar()
        self.underline_text_var.set(self.config['underline text'])

        
        ## Shorthand
        """
        s# for shorthand, w# for autocompletion
        """
        self.shorthand_s1 = tk.StringVar()
        self.shorthand_s2 = tk.StringVar()
        self.shorthand_s3 = tk.StringVar()
        self.shorthand_s4 = tk.StringVar()
        self.shorthand_s5 = tk.StringVar()
        self.shorthand_s6 = tk.StringVar()
        self.shorthand_s7 = tk.StringVar()
        self.shorthand_s8 = tk.StringVar()
        self.shorthand_s9 = tk.StringVar()
        self.shorthand_s10 = tk.StringVar()
        self.shorthand_s11 = tk.StringVar()
        self.shorthand_s12 = tk.StringVar()
        self.shorthand_s13 = tk.StringVar()
        self.shorthand_s14 = tk.StringVar()
        self.shorthand_s15 = tk.StringVar()
        self.shorthand_s16 = tk.StringVar()
        self.shorthand_s17 = tk.StringVar()
        self.shorthand_s18 = tk.StringVar()
        self.shorthand_s19 = tk.StringVar()
        self.shorthand_s20 = tk.StringVar()

        self.shorthand_s1.set(self.config['s1'])
        self.shorthand_s2.set(self.config['s2'])
        self.shorthand_s3.set(self.config['s3'])
        self.shorthand_s4.set(self.config['s4'])
        self.shorthand_s5.set(self.config['s5'])
        self.shorthand_s6.set(self.config['s6'])
        self.shorthand_s7.set(self.config['s7'])
        self.shorthand_s8.set(self.config['s8'])
        self.shorthand_s9.set(self.config['s9'])
        self.shorthand_s10.set(self.config['s10'])
        self.shorthand_s11.set(self.config['s11'])
        self.shorthand_s12.set(self.config['s12'])
        self.shorthand_s13.set(self.config['s13'])
        self.shorthand_s14.set(self.config['s14'])
        self.shorthand_s15.set(self.config['s15'])
        self.shorthand_s16.set(self.config['s16'])
        self.shorthand_s17.set(self.config['s17'])
        self.shorthand_s18.set(self.config['s18'])
        self.shorthand_s19.set(self.config['s19'])
        self.shorthand_s20.set(self.config['s20'])

        self.shorthand_w1 = tk.StringVar()
        self.shorthand_w2 = tk.StringVar()
        self.shorthand_w3 = tk.StringVar()
        self.shorthand_w4 = tk.StringVar()
        self.shorthand_w5 = tk.StringVar()
        self.shorthand_w6 = tk.StringVar()
        self.shorthand_w7 = tk.StringVar()
        self.shorthand_w8 = tk.StringVar()
        self.shorthand_w9 = tk.StringVar()
        self.shorthand_w10 = tk.StringVar()
        self.shorthand_w11 = tk.StringVar()
        self.shorthand_w12 = tk.StringVar()
        self.shorthand_w13 = tk.StringVar()
        self.shorthand_w14 = tk.StringVar()
        self.shorthand_w15 = tk.StringVar()
        self.shorthand_w16 = tk.StringVar()
        self.shorthand_w17 = tk.StringVar()
        self.shorthand_w18 = tk.StringVar()
        self.shorthand_w19 = tk.StringVar()
        self.shorthand_w20 = tk.StringVar()

        self.shorthand_w1.set(self.config['w1'])
        self.shorthand_w2.set(self.config['w2'])
        self.shorthand_w3.set(self.config['w3'])
        self.shorthand_w4.set(self.config['w4'])
        self.shorthand_w5.set(self.config['w5'])
        self.shorthand_w6.set(self.config['w6'])
        self.shorthand_w7.set(self.config['w7'])
        self.shorthand_w8.set(self.config['w8'])
        self.shorthand_w9.set(self.config['w9'])
        self.shorthand_w10.set(self.config['w10'])
        self.shorthand_w11.set(self.config['w11'])
        self.shorthand_w12.set(self.config['w12'])
        self.shorthand_w13.set(self.config['w13'])
        self.shorthand_w14.set(self.config['w14'])
        self.shorthand_w15.set(self.config['w15'])
        self.shorthand_w16.set(self.config['w16'])
        self.shorthand_w17.set(self.config['w17'])
        self.shorthand_w18.set(self.config['w18'])
        self.shorthand_w19.set(self.config['w19'])
        self.shorthand_w20.set(self.config['w20'])

        self.shorthand_s1_btn = tk.StringVar()
        self.shorthand_s2_btn = tk.StringVar()
        self.shorthand_s3_btn = tk.StringVar()
        self.shorthand_s4_btn = tk.StringVar()
        self.shorthand_s5_btn = tk.StringVar()
        self.shorthand_s6_btn = tk.StringVar()
        self.shorthand_s7_btn = tk.StringVar()
        self.shorthand_s8_btn = tk.StringVar()
        self.shorthand_s9_btn = tk.StringVar()
        self.shorthand_s10_btn = tk.StringVar()
        self.shorthand_s11_btn = tk.StringVar()
        self.shorthand_s12_btn = tk.StringVar()
        self.shorthand_s13_btn = tk.StringVar()
        self.shorthand_s14_btn = tk.StringVar()
        self.shorthand_s15_btn = tk.StringVar()
        self.shorthand_s16_btn = tk.StringVar()
        self.shorthand_s17_btn = tk.StringVar()
        self.shorthand_s18_btn = tk.StringVar()
        self.shorthand_s19_btn = tk.StringVar()
        self.shorthand_s20_btn = tk.StringVar()

        self.shorthand_s1_btn.set('Edit')
        self.shorthand_s2_btn.set('Edit')
        self.shorthand_s3_btn.set('Edit')
        self.shorthand_s4_btn.set('Edit')
        self.shorthand_s5_btn.set('Edit')
        self.shorthand_s6_btn.set('Edit')
        self.shorthand_s7_btn.set('Edit')
        self.shorthand_s8_btn.set('Edit')
        self.shorthand_s9_btn.set('Edit')
        self.shorthand_s10_btn.set('Edit')
        self.shorthand_s11_btn.set('Edit')
        self.shorthand_s12_btn.set('Edit')
        self.shorthand_s13_btn.set('Edit')
        self.shorthand_s14_btn.set('Edit')
        self.shorthand_s15_btn.set('Edit')
        self.shorthand_s16_btn.set('Edit')
        self.shorthand_s17_btn.set('Edit')
        self.shorthand_s18_btn.set('Edit')
        self.shorthand_s19_btn.set('Edit')
        self.shorthand_s20_btn.set('Edit')

        self.shorthand_w1_btn = tk.StringVar()
        self.shorthand_w2_btn = tk.StringVar()
        self.shorthand_w3_btn = tk.StringVar()
        self.shorthand_w4_btn = tk.StringVar()
        self.shorthand_w5_btn = tk.StringVar()
        self.shorthand_w6_btn = tk.StringVar()
        self.shorthand_w7_btn = tk.StringVar()
        self.shorthand_w8_btn = tk.StringVar()
        self.shorthand_w9_btn = tk.StringVar()
        self.shorthand_w10_btn = tk.StringVar()
        self.shorthand_w11_btn = tk.StringVar()
        self.shorthand_w12_btn = tk.StringVar()
        self.shorthand_w13_btn = tk.StringVar()
        self.shorthand_w14_btn = tk.StringVar()
        self.shorthand_w15_btn = tk.StringVar()
        self.shorthand_w16_btn = tk.StringVar()
        self.shorthand_w17_btn = tk.StringVar()
        self.shorthand_w18_btn = tk.StringVar()
        self.shorthand_w19_btn = tk.StringVar()
        self.shorthand_w20_btn = tk.StringVar()

        self.shorthand_w1_btn.set('Edit')
        self.shorthand_w2_btn.set('Edit')
        self.shorthand_w3_btn.set('Edit')
        self.shorthand_w4_btn.set('Edit')
        self.shorthand_w5_btn.set('Edit')
        self.shorthand_w6_btn.set('Edit')
        self.shorthand_w7_btn.set('Edit')
        self.shorthand_w8_btn.set('Edit')
        self.shorthand_w9_btn.set('Edit')
        self.shorthand_w10_btn.set('Edit')
        self.shorthand_w11_btn.set('Edit')
        self.shorthand_w12_btn.set('Edit')
        self.shorthand_w13_btn.set('Edit')
        self.shorthand_w14_btn.set('Edit')
        self.shorthand_w15_btn.set('Edit')
        self.shorthand_w16_btn.set('Edit')
        self.shorthand_w17_btn.set('Edit')
        self.shorthand_w18_btn.set('Edit')
        self.shorthand_w19_btn.set('Edit')
        self.shorthand_w20_btn.set('Edit')
        pass                

    def create_widgets(self):
        # Createing the tabs
        self.general_tab = ttk.Frame(self)
        self.keybinds_tab = ttk.Frame(self)
        self.shorthand_tab = ttk.Frame(self)

        self.add(self.general_tab, text='General')
        self.add(self.keybinds_tab, text='Key Binds')
        self.add(self.shorthand_tab, text='Shorthand')

        # General Tab Widget Creation
        # Any keybinds should be based on the control key


        self.dark_light_mode_label = ttk.Label(self.general_tab, text='Theme')
        self.dark_light_mode_button = ttk.Button(self.general_tab, textvariable=self.dark_light_mode_var)
        self.dark_light_mode_button['command'] = lambda: self.change_theme()

        self.ctrl_bind_header = ttk.Label(self.general_tab, text='Text Editor Hotkeys')
        self.ctrl_bind_header['font'] = '16'
        

        self.keybind_info_gen_tab = ttk.Label(self.general_tab, text='The keybinds offered on this page are configured to use the control key.')

        self.create_note_label = ttk.Label(self.general_tab, text="Create New Note")
        self.create_note_bind = ttk.Entry(self.general_tab, textvariable=self.create_note_var, state='disabled')
        self.create_note_edit = ttk.Button(self.general_tab, text='Edit')
        self.create_note_edit['command'] = lambda: self.change_key_bind(self.create_note_bind, self.create_note_var, self.ctrl_key_detector, 'create note')

        self.save_note_label = ttk.Label(self.general_tab, text='Save Note')
        self.save_note_bind = ttk.Entry(self.general_tab, textvariable=self.save_note_var, state='disabled')
        self.save_note_edit = ttk.Button(self.general_tab, text='Edit')
        self.save_note_edit['command'] = lambda: self.change_key_bind(self.save_note_bind, self.save_note_var, self.ctrl_key_detector, 'save note')

        self.switch_to_note_label = ttk.Label(self.general_tab, text='Switch to Note')
        self.switch_to_note_bind = ttk.Entry(self.general_tab, textvariable=self.switch_to_note_var, state='disabled')
        self.switch_to_note_edit = ttk.Button(self.general_tab, text='Edit')
        self.switch_to_note_edit['command'] = lambda: self.change_key_bind(self.switch_to_note_bind, self.switch_to_note_var, self.ctrl_key_detector, 'switch note')

        self.bold_text_label = ttk.Label(self.general_tab, text='Bold Text')
        self.bold_text_bind = ttk.Entry(self.general_tab, textvariable=self.bold_text_var, state='disabled')
        self.bold_text_edit = ttk.Button(self.general_tab, text='Edit')
        self.bold_text_edit['command'] = lambda: self.change_key_bind(self.bold_text_bind, self.bold_text_var, self.ctrl_key_detector, 'bold text')

        self.italic_text_label = ttk.Label(self.general_tab, text='Italic Text')
        self.italic_text_bind = ttk.Entry(self.general_tab, textvariable=self.italic_text_var, state='disabled')
        self.italic_text_edit = ttk.Button(self.general_tab, text='Edit')
        self.italic_text_edit['command'] = lambda: self.change_key_bind(self.italic_text_bind, self.italic_text_var, self.ctrl_key_detector, 'italic text')

        self.underline_text_label = ttk.Label(self.general_tab, text='Underline Text')
        self.underline_text_bind = ttk.Entry(self.general_tab, textvariable=self.underline_text_var, state='disabled')
        self.underline_text_edit = ttk.Button(self.general_tab, text='Edit')
        self.underline_text_edit['command'] = lambda: self.change_key_bind(self.underline_text_bind, self.underline_text_var, self.ctrl_key_detector, 'underline text')

        # Key Binds Tab Widget Creation
        # Keybinds should be based on the alt key

        self.example_label = ttk.Label(self.keybinds_tab, text="Key Bind:")
        self.example_bind = ttk.Entry(self.keybinds_tab, textvariable=self.example_var, state='disabled')
        self.change_example_bind = ttk.Button(self.keybinds_tab, text='Edit')
        self.change_example_bind['command'] = lambda: self.change_key_bind(self.example_bind, self.example_var, self.alt_key_detector, '')

        # Shorthand Tab Widget Creation
        # label shorthand -> real text
        self.shorthand_label = ttk.Label(self.shorthand_tab, text='Shorthand')
        self.spacer_1 = ttk.Label(self.shorthand_tab, text=' ')
        self.autocomp_label = ttk.Label(self.shorthand_tab, text='Auto-Completion')
        

        self.shorthand_label_frame = ttk.LabelFrame(self.shorthand_tab, text='SHORTHAND')
        self.shorthand_entry_1 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s1, state='disabled')
        self.autocomp_entry_1 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w1, state='disabled')
        self.shorthand_btn_1 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s1_btn)
        self.shorthand_btn_1['command'] = lambda: self.change_shorthand(self.shorthand_entry_1, self.shorthand_s1, self.shorthand_btn_1, self.shorthand_s1_btn, 's1')
        self.autocomp_btn_1 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w1_btn)
        self.autocomp_btn_1['command'] = lambda: self.change_shorthand(self.autocomp_entry_1, self.shorthand_w1, self.autocomp_btn_1, self.shorthand_w1_btn, 'w1')       

        self.shorthand_entry_2 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s2, state='disabled')
        self.autocomp_entry_2 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w2, state='disabled')
        self.shorthand_btn_2 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s2_btn)
        self.shorthand_btn_2['command'] = lambda: self.change_shorthand(self.shorthand_entry_2, self.shorthand_s2, self.shorthand_btn_2, self.shorthand_s2_btn, 's2')
        self.autocomp_btn_2 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w2_btn)
        self.autocomp_btn_2['command'] = lambda: self.change_shorthand(self.autocomp_entry_2, self.shorthand_w2, self.autocomp_btn_2, self.shorthand_w2_btn, 'w2')

        self.shorthand_entry_3 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s3, state='disabled')
        self.autocomp_entry_3 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w3, state='disabled')
        self.shorthand_btn_3 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s3_btn)
        self.shorthand_btn_3['command'] = lambda: self.change_shorthand(self.shorthand_entry_3, self.shorthand_s3, self.shorthand_btn_3, self.shorthand_s3_btn, 's3')
        self.autocomp_btn_3 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w3_btn)
        self.autocomp_btn_3['command'] = lambda: self.change_shorthand(self.autocomp_entry_3, self.shorthand_w3, self.autocomp_btn_3, self.shorthand_w3_btn, 'w3')

        self.shorthand_entry_4 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s4, state='disabled')
        self.autocomp_entry_4 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w4, state='disabled')
        self.shorthand_btn_4 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s4_btn)
        self.shorthand_btn_4['command'] = lambda: self.change_shorthand(self.shorthand_entry_4, self.shorthand_s4, self.shorthand_btn_4, self.shorthand_s4_btn, 's4')
        self.autocomp_btn_4 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w4_btn)
        self.autocomp_btn_4['command'] = lambda: self.change_shorthand(self.autocomp_entry_4, self.shorthand_w4, self.autocomp_btn_4, self.shorthand_w4_btn, 'w4')

        self.shorthand_entry_5 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s5, state='disabled')
        self.autocomp_entry_5 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w5, state='disabled')
        self.shorthand_btn_5 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s5_btn)
        self.shorthand_btn_5['command'] = lambda: self.change_shorthand(self.shorthand_entry_5, self.shorthand_s5, self.shorthand_btn_5, self.shorthand_s5_btn, 's5')
        self.autocomp_btn_5 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w5_btn)
        self.autocomp_btn_5['command'] = lambda: self.change_shorthand(self.autocomp_entry_5, self.shorthand_w5, self.autocomp_btn_5, self.shorthand_w5_btn, 'w5')

        self.shorthand_entry_6 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s6, state='disabled')
        self.autocomp_entry_6 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w6, state='disabled')
        self.shorthand_btn_6 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s6_btn)
        self.shorthand_btn_6['command'] = lambda: self.change_shorthand(self.shorthand_entry_6, self.shorthand_s6, self.shorthand_btn_6, self.shorthand_s6_btn, 's6')
        self.autocomp_btn_6 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w6_btn)
        self.autocomp_btn_6['command'] = lambda: self.change_shorthand(self.autocomp_entry_6, self.shorthand_w6, self.autocomp_btn_6, self.shorthand_w6_btn, 'w6')     
        
        self.shorthand_entry_7 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s7, state='disabled')
        self.autocomp_entry_7 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w7, state='disabled')
        self.shorthand_btn_7 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s7_btn)
        self.shorthand_btn_7['command'] = lambda: self.change_shorthand(self.shorthand_entry_7, self.shorthand_s7, self.shorthand_btn_7, self.shorthand_s7_btn, 's7')
        self.autocomp_btn_7 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w7_btn) 
        self.autocomp_btn_7['command'] = lambda: self.change_shorthand(self.autocomp_entry_7, self.shorthand_w7, self.autocomp_btn_7, self.shorthand_w7_btn, 'w7')

        self.shorthand_entry_8 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s8, state='disabled')
        self.autocomp_entry_8 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w8, state='disabled')
        self.shorthand_btn_8 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s8_btn)
        self.shorthand_btn_8['command'] = lambda: self.change_shorthand(self.shorthand_entry_8, self.shorthand_s8, self.shorthand_btn_8, self.shorthand_s8_btn, 's8')
        self.autocomp_btn_8 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w8_btn) 
        self.autocomp_btn_8['command'] = lambda: self.change_shorthand(self.autocomp_entry_8, self.shorthand_w8, self.autocomp_btn_8, self.shorthand_w8_btn, 'w8')

        self.shorthand_entry_9 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s9, state='disabled')
        self.autocomp_entry_9 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w9, state='disabled')
        self.shorthand_btn_9 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s9_btn)
        self.shorthand_btn_9['command'] = lambda: self.change_shorthand(self.shorthand_entry_9, self.shorthand_s9, self.shorthand_btn_9, self.shorthand_s9_btn, 's9')
        self.autocomp_btn_9 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w9_btn)
        self.autocomp_btn_9['command'] = lambda: self.change_shorthand(self.autocomp_entry_9, self.shorthand_w9, self.autocomp_btn_9, self.shorthand_w9_btn, 'w9')

        self.shorthand_entry_10 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s10, state='disabled')
        self.autocomp_entry_10 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w10, state='disabled')
        self.shorthand_btn_10 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s10_btn)
        self.shorthand_btn_10['command'] = lambda: self.change_shorthand(self.shorthand_entry_10, self.shorthand_s10, self.shorthand_btn_10, self.shorthand_s10_btn, 's10')
        self.autocomp_btn_10 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w10_btn) 
        self.autocomp_btn_10['command'] = lambda: self.change_shorthand(self.autocomp_entry_10, self.shorthand_w10, self.autocomp_btn_10, self.shorthand_w10_btn, 'w10')

        self.shorthand_entry_11 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s11, state='disabled')
        self.autocomp_entry_11 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w11, state='disabled')
        self.shorthand_btn_11 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s11_btn)
        self.shorthand_btn_11['command'] = lambda: self.change_shorthand(self.shorthand_entry_11, self.shorthand_s11, self.shorthand_btn_11, self.shorthand_s11_btn, 's11')
        self.autocomp_btn_11 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w11_btn)
        self.autocomp_btn_11['command'] = lambda: self.change_shorthand(self.autocomp_entry_11, self.shorthand_w11, self.autocomp_btn_11, self.shorthand_w11_btn, 'w11') 

        self.shorthand_entry_12 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s12, state='disabled')
        self.autocomp_entry_12 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w12, state='disabled')
        self.shorthand_btn_12 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s12_btn)
        self.shorthand_btn_12['command'] = lambda: self.change_shorthand(self.shorthand_entry_12, self.shorthand_s12, self.shorthand_btn_12, self.shorthand_s12_btn, 's12')
        self.autocomp_btn_12 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w12_btn)
        self.autocomp_btn_12['command'] = lambda: self.change_shorthand(self.autocomp_entry_12, self.shorthand_w12, self.autocomp_btn_12, self.shorthand_w12_btn, 'w12') 

        self.shorthand_entry_13 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s13, state='disabled')
        self.autocomp_entry_13 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w13, state='disabled')
        self.shorthand_btn_13 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s13_btn)
        self.shorthand_btn_13['command'] = lambda: self.change_shorthand(self.shorthand_entry_13, self.shorthand_s13, self.shorthand_btn_13, self.shorthand_s13_btn, 's13')
        self.autocomp_btn_13 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w13_btn) 
        self.autocomp_btn_13['command'] = lambda: self.change_shorthand(self.autocomp_entry_13, self.shorthand_w13, self.autocomp_btn_13, self.shorthand_w13_btn, 'w13')

        self.shorthand_entry_14 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s14, state='disabled')
        self.autocomp_entry_14 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w14, state='disabled')
        self.shorthand_btn_14 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s14_btn)
        self.shorthand_btn_14['command'] = lambda: self.change_shorthand(self.shorthand_entry_14, self.shorthand_s14, self.shorthand_btn_14, self.shorthand_s14_btn, 's14')
        self.autocomp_btn_14 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w14_btn) 
        self.autocomp_btn_14['command'] = lambda: self.change_shorthand(self.autocomp_entry_14, self.shorthand_w14, self.autocomp_btn_14, self.shorthand_w14_btn, 'w14')

        self.shorthand_entry_15 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s15, state='disabled')
        self.autocomp_entry_15 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w15, state='disabled')
        self.shorthand_btn_15 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s15_btn)
        self.shorthand_btn_15['command'] = lambda: self.change_shorthand(self.shorthand_entry_15, self.shorthand_s15, self.shorthand_btn_15, self.shorthand_s15_btn, 's15')
        self.autocomp_btn_15 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w15_btn) 
        self.autocomp_btn_15['command'] = lambda: self.change_shorthand(self.autocomp_entry_15, self.shorthand_w15, self.autocomp_btn_15, self.shorthand_w15_btn, 'w15')

        self.shorthand_entry_16 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s16, state='disabled')
        self.autocomp_entry_16 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w16, state='disabled')
        self.shorthand_btn_16 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s16_btn)
        self.shorthand_btn_16['command'] = lambda: self.change_shorthand(self.shorthand_entry_16, self.shorthand_s16, self.shorthand_btn_16, self.shorthand_s16_btn, 's16')
        self.autocomp_btn_16 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w16_btn) 
        self.autocomp_btn_16['command'] = lambda: self.change_shorthand(self.autocomp_entry_16, self.shorthand_w16, self.autocomp_btn_16, self.shorthand_w16_btn, 'w16')

        self.shorthand_entry_17 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s17, state='disabled')
        self.autocomp_entry_17 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w17, state='disabled')
        self.shorthand_btn_17 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s17_btn)
        self.shorthand_btn_17['command'] = lambda: self.change_shorthand(self.shorthand_entry_17, self.shorthand_s17, self.shorthand_btn_17, self.shorthand_s17_btn, 's17')
        self.autocomp_btn_17 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w17_btn) 
        self.autocomp_btn_17['command'] = lambda: self.change_shorthand(self.autocomp_entry_17, self.shorthand_w17, self.autocomp_btn_17, self.shorthand_w17_btn, 'w17')

        self.shorthand_entry_18 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s18, state='disabled')
        self.autocomp_entry_18 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w18, state='disabled')
        self.shorthand_btn_18 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s18_btn)
        self.shorthand_btn_18['command'] = lambda: self.change_shorthand(self.shorthand_entry_18, self.shorthand_s18, self.shorthand_btn_18, self.shorthand_s18_btn, 's18')
        self.autocomp_btn_18 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w18_btn) 
        self.autocomp_btn_18['command'] = lambda: self.change_shorthand(self.autocomp_entry_18, self.shorthand_w18, self.autocomp_btn_18, self.shorthand_w18_btn, 'w18')

        self.shorthand_entry_19 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s19, state='disabled')
        self.autocomp_entry_19 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w19, state='disabled')
        self.shorthand_btn_19 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s19_btn)
        self.shorthand_btn_19['command'] = lambda: self.change_shorthand(self.shorthand_entry_19, self.shorthand_s19, self.shorthand_btn_19, self.shorthand_s19_btn, 's19')
        self.autocomp_btn_19 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w19_btn)
        self.autocomp_btn_19['command'] = lambda: self.change_shorthand(self.autocomp_entry_19, self.shorthand_w19, self.autocomp_btn_19, self.shorthand_w19_btn, 'w19')

        self.shorthand_entry_20 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_s20, state='disabled')
        self.autocomp_entry_20 = ttk.Entry(self.shorthand_tab, textvariable=self.shorthand_w20, state='disabled')
        self.shorthand_btn_20 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_s20_btn)
        self.shorthand_btn_20['command'] = lambda: self.change_shorthand(self.shorthand_entry_20, self.shorthand_s20, self.shorthand_btn_20, self.shorthand_s20_btn, 's20')
        self.autocomp_btn_20 = ttk.Button(self.shorthand_tab, textvariable=self.shorthand_w20_btn) 
        self.autocomp_btn_20['command'] = lambda: self.change_shorthand(self.autocomp_entry_20, self.shorthand_w20, self.autocomp_btn_20, self.shorthand_w20_btn, 'w20') 

    def create_layout(self):
        # General Tab Layout

        self.dark_light_mode_label.grid(row=1, column=0, sticky='NW')
        self.dark_light_mode_button.grid(row=1, column=1, sticky='NW')

        self.ctrl_bind_header.grid(row=2, column=0, columnspan=3, sticky='WS')

        self.keybind_info_gen_tab.grid(row=3, column=0, columnspan=3, sticky='NW')
        
        self.create_note_label.grid(row=4, column=0, sticky='NW')
        self.create_note_bind.grid(row=4, column=1, sticky='NW')
        self.create_note_edit.grid(row=4, column=2, sticky='NW')
        
        self.save_note_label.grid(row=5, column=0, sticky='NW')
        self.save_note_bind.grid(row=5, column=1, sticky='NW')
        self.save_note_edit.grid(row=5, column=2, sticky='NW')
        
        self.switch_to_note_label.grid(row=6, column=0, sticky='NW')
        self.switch_to_note_bind.grid(row=6, column=1, sticky='NW')
        self.switch_to_note_edit.grid(row=6, column=2, sticky='NW')
        
        self.bold_text_label.grid(row=7, column=0, sticky='NW')
        self.bold_text_bind.grid(row=7, column=1, sticky='NW')
        self.bold_text_edit.grid(row=7, column=2, sticky='NW')

        self.italic_text_label.grid(row=8, column=0, sticky='NW')
        self.italic_text_bind.grid(row=8, column=1, sticky='NW')
        self.italic_text_edit.grid(row=8, column=2, sticky='NW')

        self.underline_text_label.grid(row=9, column=0, sticky='NW')
        self.underline_text_bind.grid(row=9, column=1, sticky='NW')
        self.underline_text_edit.grid(row=9, column=2, sticky='NW')
        
        # Keybinds Tab Layout

        self.example_label.grid(row=1, column=0)
        self.example_bind.grid(row=1, column=1)
        self.change_example_bind.grid(row=1, column=2)
        
        # Shorthand Tab Layout
        self.shorthand_label_frame.grid(row=0, column=0, sticky='NW')
        
        self.shorthand_label.grid(row=0, column=0, sticky='NW')
        self.spacer_1.grid(row=0, column=1, sticky='NW')
        self.autocomp_label.grid(row=0, column=2, sticky='NW')
        

        self.shorthand_entry_1.grid(row=2, column=0, sticky='NW')
        self.shorthand_btn_1.grid(row=2, column=1, sticky='NW')
        self.autocomp_entry_1.grid(row=2, column=2, sticky='NW')
        self.autocomp_btn_1.grid(row=2, column=3, sticky='NW')

        self.shorthand_entry_2.grid(row=3, column=0, sticky='NW')
        self.shorthand_btn_2.grid(row=3, column=1, sticky='NW')
        self.autocomp_entry_2.grid(row=3, column=2, sticky='NW')
        self.autocomp_btn_2.grid(row=3, column=3, sticky='NW')

        self.shorthand_entry_3.grid(row=4, column=0, sticky='NW')
        self.shorthand_btn_3.grid(row=4, column=1, sticky='NW')
        self.autocomp_entry_3.grid(row=4, column=2, sticky='NW')
        self.autocomp_btn_3.grid(row=4, column=3, sticky='NW')

        self.shorthand_entry_4.grid(row=5, column=0, sticky='NW')
        self.shorthand_btn_4.grid(row=5, column=1, sticky='NW')
        self.autocomp_entry_4.grid(row=5, column=2, sticky='NW')
        self.autocomp_btn_4.grid(row=5, column=3, sticky='NW')

        self.shorthand_entry_5.grid(row=6, column=0, sticky='NW')
        self.shorthand_btn_5.grid(row=6, column=1, sticky='NW')
        self.autocomp_entry_5.grid(row=6, column=2, sticky='NW')
        self.autocomp_btn_5.grid(row=6, column=3, sticky='NW')

        self.shorthand_entry_6.grid(row=7, column=0, sticky='NW')
        self.shorthand_btn_6.grid(row=7, column=1, sticky='NW')
        self.autocomp_entry_6.grid(row=7, column=2, sticky='NW')
        self.autocomp_btn_6.grid(row=7, column=3, sticky='NW')

        self.shorthand_entry_7.grid(row=8, column=0, sticky='NW')
        self.shorthand_btn_7.grid(row=8, column=1, sticky='NW')
        self.autocomp_entry_7.grid(row=8, column=2, sticky='NW')
        self.autocomp_btn_7.grid(row=8, column=3, sticky='NW')

        self.shorthand_entry_8.grid(row=9, column=0, sticky='NW')
        self.shorthand_btn_8.grid(row=9, column=1, sticky='NW')
        self.autocomp_entry_8.grid(row=9, column=2, sticky='NW')
        self.autocomp_btn_8.grid(row=9, column=3, sticky='NW')

        self.shorthand_entry_9.grid(row=10, column=0, sticky='NW')
        self.shorthand_btn_9.grid(row=10, column=1, sticky='NW')
        self.autocomp_entry_9.grid(row=10, column=2, sticky='NW')
        self.autocomp_btn_9.grid(row=10, column=3, sticky='NW')

        self.shorthand_entry_10.grid(row=11, column=0, sticky='NW')
        self.shorthand_btn_10.grid(row=11, column=1, sticky='NW')
        self.autocomp_entry_10.grid(row=11, column=2, sticky='NW')
        self.autocomp_btn_10.grid(row=11, column=3, sticky='NW')

        self.shorthand_entry_11.grid(row=12, column=0, sticky='NW')
        self.shorthand_btn_11.grid(row=12, column=1, sticky='NW')
        self.autocomp_entry_11.grid(row=12, column=2, sticky='NW')
        self.autocomp_btn_11.grid(row=12, column=3, sticky='NW')

        self.shorthand_entry_12.grid(row=13, column=0, sticky='NW')
        self.shorthand_btn_12.grid(row=13, column=1, sticky='NW')
        self.autocomp_entry_12.grid(row=13, column=2, sticky='NW')
        self.autocomp_btn_12.grid(row=13, column=3, sticky='NW')

        self.shorthand_entry_13.grid(row=14, column=0, sticky='NW')
        self.shorthand_btn_13.grid(row=14, column=1, sticky='NW')
        self.autocomp_entry_13.grid(row=14, column=2, sticky='NW')
        self.autocomp_btn_13.grid(row=14, column=3, sticky='NW')

        self.shorthand_entry_14.grid(row=15, column=0, sticky='NW')
        self.shorthand_btn_14.grid(row=15, column=1, sticky='NW')
        self.autocomp_entry_14.grid(row=15, column=2, sticky='NW')
        self.autocomp_btn_14.grid(row=15, column=3, sticky='NW')

        self.shorthand_entry_15.grid(row=16, column=0, sticky='NW')
        self.shorthand_btn_15.grid(row=16, column=1, sticky='NW')
        self.autocomp_entry_15.grid(row=16, column=2, sticky='NW')
        self.autocomp_btn_15.grid(row=16, column=3, sticky='NW')

        self.shorthand_entry_16.grid(row=17, column=0, sticky='NW')
        self.shorthand_btn_16.grid(row=17, column=1, sticky='NW')
        self.autocomp_entry_16.grid(row=17, column=2, sticky='NW')
        self.autocomp_btn_16.grid(row=17, column=3, sticky='NW')

        self.shorthand_entry_17.grid(row=18, column=0, sticky='NW')
        self.shorthand_btn_17.grid(row=18, column=1, sticky='NW')
        self.autocomp_entry_17.grid(row=18, column=2, sticky='NW')
        self.autocomp_btn_17.grid(row=18, column=3, sticky='NW')

        self.shorthand_entry_18.grid(row=19, column=0, sticky='NW')
        self.shorthand_btn_18.grid(row=19, column=1, sticky='NW')
        self.autocomp_entry_18.grid(row=19, column=2, sticky='NW')
        self.autocomp_btn_18.grid(row=19, column=3, sticky='NW')

        self.shorthand_entry_19.grid(row=20, column=0, sticky='NW')
        self.shorthand_btn_19.grid(row=20, column=1, sticky='NW')
        self.autocomp_entry_19.grid(row=20, column=2, sticky='NW')
        self.autocomp_btn_19.grid(row=20, column=3, sticky='NW')

        self.shorthand_entry_20.grid(row=21, column=0, sticky='NW')
        self.shorthand_btn_20.grid(row=21, column=1, sticky='NW')
        self.autocomp_entry_20.grid(row=21, column=2, sticky='NW')
        self.autocomp_btn_20.grid(row=21, column=3, sticky='NW')

        # Wieghts
        ## General 
        self.general_tab.rowconfigure(0, weight=2)
        self.general_tab.rowconfigure(1, weight=2)
        self.general_tab.rowconfigure(2, weight=2)
        self.general_tab.rowconfigure(3, weight=2)
        self.general_tab.rowconfigure(4, weight=2)
        self.general_tab.rowconfigure(5, weight=2)
        self.general_tab.rowconfigure(6, weight=2)
        self.general_tab.rowconfigure(7, weight=2)
        self.general_tab.rowconfigure(8, weight=2)
        self.general_tab.rowconfigure(9, weight=2)
        self.general_tab.columnconfigure(0, weight=2)
        self.general_tab.columnconfigure(1, weight=2)
        self.general_tab.columnconfigure(2, weight=2)

        ## Keybinds

        ## Shorthand
        self.shorthand_tab.rowconfigure(0, weight=2)
        self.shorthand_tab.rowconfigure(1, weight=2)
        self.shorthand_tab.rowconfigure(2, weight=2)
        self.shorthand_tab.rowconfigure(3, weight=2)
        self.shorthand_tab.rowconfigure(4, weight=2)
        self.shorthand_tab.rowconfigure(5, weight=2)
        self.shorthand_tab.rowconfigure(6, weight=2)
        self.shorthand_tab.rowconfigure(7, weight=2)
        self.shorthand_tab.rowconfigure(8, weight=2)
        self.shorthand_tab.rowconfigure(9, weight=2)
        self.shorthand_tab.rowconfigure(10, weight=2)
        self.shorthand_tab.rowconfigure(11, weight=2)
        self.shorthand_tab.rowconfigure(12, weight=2)
        self.shorthand_tab.rowconfigure(13, weight=2)
        self.shorthand_tab.rowconfigure(14, weight=2)
        self.shorthand_tab.rowconfigure(15, weight=2)
        self.shorthand_tab.rowconfigure(16, weight=2)
        self.shorthand_tab.rowconfigure(17, weight=2)
        self.shorthand_tab.rowconfigure(18, weight=2)
        self.shorthand_tab.rowconfigure(19, weight=2)
        self.shorthand_tab.columnconfigure(0, weight=2)
        self.shorthand_tab.columnconfigure(1, weight=2)
        self.shorthand_tab.columnconfigure(2, weight=2)
        self.shorthand_tab.columnconfigure(3, weight=2)
        pass
    
    def alt_key_detector(self, event):
        self.var.set("Alt-" + event.keysym)
        self.obj['state'] = 'disable'
    
    def ctrl_key_detector(self, event):
        self.var.set("Control-" + event.keysym)
        self.obj['state'] = 'disable'
        self.keybind_info_gen_tab.focus_set() # removes the users ablilty to continue editing the bind, even after the entry widget is disabled
        self.config[self.save_grabber] = self.var.get()
        self.auto_save()

    def change_key_bind(self, obj, var, key_detector, save):
        obj['state'] = 'active'
        var.set("")
        obj.focus()
        # Event needs to be a paramater by itself in the key detectors
        # These objects get around that issue
        self.obj = obj
        self.var = var
        self.save_grabber = save
        obj.bind("<KeyPress>", key_detector)
        

    def change_shorthand(self, obj, var, btn, btn_var, save):
        obj['state'] = 'active'
        var.set('')
        btn['command'] = lambda: self.set_shorthand(obj, var, btn, btn_var, save)
        btn_var.set("Set")
        obj.focus()
    
    def set_shorthand(self, obj, var, btn, btn_var, save):
        obj['state'] = 'disabled'
        btn_var.set("Edit")
        
        if var.get() == '':
            var.set('...')
            self.config[save] = var.get()   
        else:
            self.config[save] = var.get()
        
        self.auto_save()
        btn['command'] = lambda: self.change_shorthand(obj, var, btn, btn_var, save)
        
    def auto_save(self):
        with open('config.json', 'w') as f:
            json.dump(self.config, f, indent=4)
            f.close()


    def init_theme(self):
        self.tk.call('source','azure.tcl')
        if self.config['theme'] == 'Light Mode':
            self.tk.call("set_theme", 'light')
        if self.config['theme'] == 'Dark Mode':
            self.tk.call('set_theme', 'dark')
            self.dark_light_mode_var.set('Light Mode')
        
        pass

    def change_theme(self):
        if self.tk.call("ttk::style", "theme", "use") == "azure-dark":
            self.tk.call("set_theme", "light")
            self.dark_light_mode_var.set('Dark Mode')
        else:
            self.tk.call("set_theme", "dark")
            self.dark_light_mode_var.set('Light Mode')
        pass        


                