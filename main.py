from tkinter import *

root = Tk()
root.geometry("500x400")
root.config(bg="skyblue")
Label(root,text="Welcome",font=("",20,"bold"),background="skyblue").pack()
Button(root,text="Exit",command=exit).pack(side=BOTTOM,anchor="se",padx=20,pady=20)
root.mainloop()
#This is comment line
