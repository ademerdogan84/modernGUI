from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.geometry("400x400")

def show_int():
    myLabel1 = Label(root, text=var_int.get()).pack()

var_int = IntVar()
var_int_c = Checkbutton(root, text="Check this box!", variable=var_int)
var_int_c.pack()
myButton1 = Button(root, text = "Show!", command=show_int).pack()


def show_str():
    myLabel2 = Label(root, text=var_str.get()).pack()

var_str = StringVar()
var_str_c = Checkbutton(root, text="Check this box!", variable=var_str, onvalue="On", offvalue="Off")
var_str_c.deselect()
var_str_c.pack()
myButton2 = Button(root, text = "Show!", command=show_str).pack()

root.mainloop()