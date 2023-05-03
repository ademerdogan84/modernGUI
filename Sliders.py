from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.geometry("400x400")


def slide(var):
    root.geometry(str(horizont.get()) + "x" + str(vertical.get()))

vertical = Scale(root, from_=0, to=400, command=slide)
vertical.pack()
horizont = Scale(root, from_=0, to=400, command=slide, orient=HORIZONTAL)
horizont.pack()


my_btn = Button(root, text = "Click!", command=slide).pack()

root.mainloop()