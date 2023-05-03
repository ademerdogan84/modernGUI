from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.geometry("400x400")

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked = StringVar()
clicked.set(options[1])
drop = OptionMenu(root, clicked, *options)
drop.pack()

def show():
    myLabel = Label(root, text=clicked.get()).pack()

myButton = Button(root, text = "Show!", command=show).pack()

root.mainloop()