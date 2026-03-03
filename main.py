import tkinter as tk
from tkinter import messagebox,filedialog


main = tk.Tk()
main.title("Simple Text Editor")
main.geometry("600x400")

text_area = tk.Text(
    main,
    wrap=tk.WORD,
    font=("Arial", 12))

text_area.pack(expand=True, fill=tk.BOTH)

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    #open file dialogue
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text files","*.txt")]
    )
    if file_path:
        #open file
        with open(file_path,"r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())

def save_file():
    #save file 
    file_path =filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files","*.txt")]
    )
    if file_path:
        with open(file_path,"w") as file:
            file.write(text_area.get(1.0, tk.END))

    messagebox.showinfo("info","File saved successfully!")

##MENU##
menu_bar =tk.Menu(main)
main.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar)
#new file,open file,save file,exit

menu_bar.add_cascade(label="File",menu=file_menu)

file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=main.quit)

main.mainloop()