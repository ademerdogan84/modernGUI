from tkinter import *

root = Tk()

# Creating a label widget
myLabel1 = Label(root, text = "Hello world!")
myLabel2 = Label(root, text = "My name is Adem!")
myLabel3 = Label(root, text = "                ")

# Show it onto the screen
#myLabel1.pack()
#myLabel2.pack()

myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=5)
myLabel3.grid(row=1,column=1)

root.mainloop()