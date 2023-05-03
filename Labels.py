from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Look, I click a button!")
    myLabel.pack()


myButton1 = Button(root, text = "Click1!")
myButton2 = Button(root, text = "Click2!", state=DISABLED)
myButton3 = Button(root, text = "Click3!", padx=100, pady=50)
myButton4 = Button(root, text = "Click4!", command=myClick, fg="blue", bg="red")

myButton1.pack()
myButton2.pack()
myButton3.pack()
myButton4.pack()

root.mainloop()