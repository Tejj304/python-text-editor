import tkinter as tk
from tkinter.filedialog import askopenfilename , asksaveasfilename


def open_file() :
    filepath = askopenfilename(
        filetypes= [("Text Files" , "*.txt") , ("All Files" , "*.*")]
    )
    if not filepath :
        return
    text_edit.delete(1.0 , tk.END)
    with open(filepath , "r") as input_file :
        text = input_file.read()
        text_edit.insert(tk.END , text)
    window.title(f"Text Editor Application by Tej - {filepath}")

def save_file() :
    filepath = asksaveasfilename(
        defaultextension = "text",
        filetypes = [("Text Files" , "*.txt") , ("All Files" , "*.*")] ,
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_edit.get(1.0 , tk.END)
        output_file.write(text)
    window.title(f"Text Editor Application by Tej - {filepath}")

window = tk.Tk()
window.title("Text Editor By Tej")

window.rowconfigure(0, minsize=800 , weight=1) #here there is only one row in our text editor and we know in python we start indexing by 0 so that we write here 0 means 1 row.
window.columnconfigure(1, minsize=800 , weight=1) #here there are two columns in our text editor and we know in python we start indexing by 0 so that we write here 1 means 2 column

#Here we are choosing Text and frame from Tkinter Library

text_edit = tk.Text(window)
fr_button = tk.Frame(window , relief = tk.RAISED , bd=2) # relief 3d parameter properties

btn_open = tk.Button(fr_button , text="Open" , command=open_file)
btn_save = tk.Button(fr_button , text="Save As..", command=save_file)

btn_open.grid(row = 0 , column = 0 , sticky="ew" , padx=5 , pady = 5) #ew means East-West direction
btn_save.grid(row = 1 , column = 0 , sticky="ew" , padx=5)

fr_button.grid(row=0 , column=0 , sticky="ns")
text_edit.grid(row=0, column=1 , sticky = "nsew")











window.mainloop()