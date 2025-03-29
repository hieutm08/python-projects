from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title = "Digital Clock"
label = Label(root, font=("digital-7",100), background="black", foreground="green")
label.pack(anchor= CENTER)
def clock():
    string = strftime("%I:%M:%S:%p")
    label.config(text=string)
    label.after(1000, clock)
clock()
root.mainloop()