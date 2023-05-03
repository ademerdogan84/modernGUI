from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk()

def popup():
    messagebox.showinfo("This is my popup", "Hello world")
    messagebox.showwarning("This is my popup", "Hello world")
    messagebox.showerror("This is my popup", "Hello world")
    messagebox.askyesno("This is my popup", "Hello world")
    messagebox.askokcancel("This is my popup", "Hello world")
    messagebox.askquestion("This is my popup", "Hello world")

    response = messagebox.askyesno("This is my popup", "Hello world")
    Label(root, text=response).pack()

Button(root, text = "Popup", command=popup).pack()


root.mainloop()