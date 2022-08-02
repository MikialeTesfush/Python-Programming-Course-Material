from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("400x300")
def clicked():
    #msg = messagebox.showinfo("error", "please try again")
    msg=messagebox.showinfo('pls send again!','message content')
btn=Button(window,text='enter',command=clicked).pack()
#mybutton=Button(window,text="click me",command=clicked,bg="yellow",fg="red").pack()
window.mainloop()
