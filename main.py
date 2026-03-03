from logging import root
import tkinter as tk
from tkinter import messagebox,filedialog


class TextEditor:
    def __init__(self, main):
        self.main = main
        self.main.title("Simple Text Editor")
        self.main.geometry("600x400")
        self.file_path = None
        self.text_changed = False

        self.create_widgets()
        self.create_menu()
        self.bind_shortcuts()

        ###Widgets###
        def create_widgets(self):
            self.text_area = tk.Text(self.main,wrap=tk.WORD,font=("Arial 12",undo=True))
            self.text_area.pack(expand=True,fill=tk.BOTH)
            scroll_bar = tk.Scrollbar(self.text_area)
            scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
            self.text_area.config(yscrollcommand=scroll_bar.set)
            scroll_bar.config(command=self.text_area.yview)

            self.status_bar = tk.Label(self.main, text="Ready", anchor="e")
            self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

            self.text_area.bind("<<Modified>>", self.on_text_change)

        ###menu-bar####
        def create_menu(self):
            menu_bar = tk.Menu(self.main)
            self.main.config(menu=menu_bar)
            file_menu = tk.Menu(menu_bar, tearoff=False)
            menu_bar.add_cascade(label="File", menu=file_menu)
            file_menu.add_command(label="New", command=self.new_file)
            file_menu.add_command(label="Open", command=self.open_file)
            file_menu.add_command(label="Save", command=self.save_file) 
            file_menu.add_command(label="Save As", command=self.save_as_file)
            file_menu.add_separator()   
            file_menu.add_command(label="Exit", command=self.exit_editor)

        ###file functions###
        def new_file(self):
             if self.confirm_discard():
                 self.text_area.delete(1.0, tk.END)
                 self.file_path = None
                 self.text_changed = False

        def open_file(self):
            if self.confirm_discard():
                

