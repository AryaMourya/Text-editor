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
        

        ###Widgets###
    def create_widgets(self):
            self.text_area = tk.Text(self.main, wrap=tk.WORD, font=("Arial", 12), undo=True)
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
                self.file_path= None
                self.main.title("Simple Text Editor")
                self.text_changed = False
    def open_file(self):
            if not self.confirm_discard():
                return
            self.file_path= filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if self.file_path:
                with open(self.file_path, "r") as file:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, file.read())
                self.main.title(f"Simple Text Editor - {self.file_path}")
                self.text_changed = False
    def save_file(self):
            if self.file_path:
                with open(self.file_path, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.text_changed = False
                messagebox.showinfo("Saved","File saved successfully!")
            else:
                self.save_as() 
    def save_as_file(self):
            self.file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if self.file_path:
                with open(self.file_path, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.main.title(f"Simple Text Editor - {self.file_path}")
                self.text_changed = False
                messagebox.showinfo("Saved","File saved successfully!")
            
    def exit_editor(self):
            if self.confirm_discard():
                self.main.destroy()

    def confirm_discard(self):
            if self.text_changed:
                response = messagebox.askyesnocancel("Unsaved Changes", "You have unsaved changes. Do you want to save before exiting?")
                if response:  # Yes
                    self.save_file()
                    return True
                elif response is None:  # Cancel
                    return False
            return True
    def on_text_change(self, event=None):
            self.text_changed = True
            self.text_area.edit_modified(False)
            content = self.text_area.get(1.0, tk.END)
            words = len(content.split())
            lines = content.count("\n")
            self.status_bar.config(text=f"Words: {words}  Lines: {lines}")

