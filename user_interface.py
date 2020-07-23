# import tkinter from the tkinter library
from tkinter import *
from PIL import ImageTk,Image
import Qr_code_generate

# global declaration of variables
master_screen = ""
user_entry = ""
file_name = ""
user_text = ""
save_as = ""
qr_code_directory = ""

def generate_qr_code():
    user_entry_text_info = user_text.get()
    file_name = save_as.get()
    
    generate = Qr_code_generate.file(user_entry_text_info, file_name)
    generate.generate_code()
    
    Label(master_screen, text="successfully generated your text QR Code!", fg="green", font=("Calibri", 11)).pack()
    

"""
    takes care of creating a new screen(main window)
"""
def main_win():
    global master_screen
    master_screen = Tk()
    master_screen.geometry("550x600")
    
    # master_screen title
    master_screen.title("Qr Code Generator V1.0")
    
    Label(text = "Qr Code Generator", bg="gray", width="400", height="2", font=("Calibri", 13)).pack()
    Label(text = "").pack()
    Label(text = "").pack()
    
    global user_entry
    global file_name
    
    global user_text
    global save_as
    
    # declare some datatypes to variables/declare variables.
    user_text = StringVar()
    save_as = StringVar()
    
    # open file button
    Label(master_screen, text = "Text* ").pack()
    user_entry = Entry(master_screen, textvariable = user_text).pack()
    Label(text="").pack()
    Label(text="").pack()
    
    Label(master_screen, text = "Save as* ").pack()
    file_name = Entry(master_screen, textvariable = save_as).pack() 
    Label(text="").pack()
    Label(text="").pack()
    
    Button(text="Generate text Qr Code", width="30", height="2", command=generate_qr_code).pack()
    Label(text="").pack()
    master_screen.mainloop()

main_win()
