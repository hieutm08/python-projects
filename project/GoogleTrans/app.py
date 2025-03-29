from tkinter import *
from PIL import Image,ImageTk
from googletrans import Translator
from google import translate_text
import asyncio

root=Tk()
root.title('Google galaxy')
root.geometry("500x630")
root.iconbitmap("src/logo.ico")
load=Image.open("src/background.png")
render=ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.place(x=0,y=0)

name=Label(root, text="Translator", fg="#FFFFFF", bd=0, bg="#03152D")
name.config(font=("src/Transformers Movie",30))
name.pack(pady=10)

boxInput= Text(root, width=28, height=8, font=("ROBOTO",16))
boxInput.pack(pady=20)

button_frame= Frame(root).pack(side = BOTTOM)

def clear():
    boxInput.delete(1.0,END)
    boxOutput.delete(1.0,END)
def translate():
    boxOutput.delete(1.0,END)
    INPUT = boxInput.get(1.0,END)
    a = asyncio.run(translate_text(INPUT))
    boxOutput.insert(END, a)


clear_button=Button(button_frame, text="Clear", font=(("Arial"),10,"bold"),bg="#303030", fg="#FFFFFF", command=clear)
clear_button.place(x=290,y=310) 
translate_button=Button(button_frame, text="Translate", font=(("Arial"),10,"bold"),bg="#303030", fg="#FFFFFF", command=translate)
translate_button.place(x=150,y=310) 

boxOutput= Text(root, width=28, height=8, font=("ROBOTO",16))
boxOutput.pack(pady=80)
root.mainloop()