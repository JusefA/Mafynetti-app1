from tkinter import *

root = Tk()

MyLabel1 =Label(root, text="hello world")
MyLabel2 =Label(root, text="idk this sum weird shit")

MyLabel1.grid(row=0, column=0)
MyLabel2.grid(row=1, column=0)

root.mainloop()