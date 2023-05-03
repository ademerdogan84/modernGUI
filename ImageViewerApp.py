from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Learn To Code")
# root.iconbitmap('D:/Sirubico-Movie-Genre-Comedy-2.256.png')

my_img1 = ImageTk.PhotoImage(Image.open("D:\Python_Images\codemy1.JPG"))
my_img2 = ImageTk.PhotoImage(Image.open("D:\Python_Images\codemy2.JPG"))
my_img3 = ImageTk.PhotoImage(Image.open("D:\Python_Images\codemy3.JPG"))

image_list = [my_img1, my_img2, my_img3]

status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=3)


def forw(image_number):
    global my_label
    global button_forw
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forw = Button(root, text=">>", command=lambda: forw(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 3:
        button_forw = Button(root, text=">>", state=DISABLED)


    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forw.grid(row=1, column=2)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

def back(image_number):
    global my_label
    global button_forw
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forw = Button(root, text=">>", command=lambda: forw(image_number+1))
    button_back = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=1)
    button_forw.grid(row=1, column=2)
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text="<<",   command=back, state=DISABLED)
button_exit = Button(root, text="EXIT", command=root.quit)
button_forw = Button(root, text=">>",   command=lambda: forw(2))
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forw.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()