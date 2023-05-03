from tkinter import *
from PIL import ImageTk,Image

root = Tk()

def open():
    global my_img
    top = Toplevel()
    my_img = ImageTk.PhotoImage(Image.open("D:\Python_Images\codemy1.JPG"))
    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window!", command=top.destroy).pack()

btn = Button(root, text = "Open second window!", command=open, fg="blue", bg="red").pack()

root.mainloop()