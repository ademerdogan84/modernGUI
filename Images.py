from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Learn To Code")
# root.iconbitmap('D:/Sirubico-Movie-Genre-Comedy-2.256.png')

my_img = ImageTk.PhotoImage(Image.open("D:\codemy.JPG"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()

root.mainloop()