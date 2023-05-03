from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Learn To Code")

frame = LabelFrame(root, text="This is my Frame...", padx=50, pady=50)
frame.pack(padx=100, pady=100)

b1 = Button(frame, text="Don't Click")
b2 = Button(frame, text="Click")
b1.grid(row=0, column=0)
b2.grid(row=1, column=0)

root.mainloop()