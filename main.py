from tkinter import *

root = Tk()
root.geometry("500x400")
Label(root,text="Welcome",font=("",20,"bold")).pack()
Button(root,text="Exit",command=exit).pack()
root.mainloop()