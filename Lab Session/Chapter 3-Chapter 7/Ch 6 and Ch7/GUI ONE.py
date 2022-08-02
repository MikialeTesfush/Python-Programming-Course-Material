#import tkinter
from tkinter import*
from tkinter import messagebox
win=Tk()
win.title("First GUI")
win.configure(bg='gray')
win.geometry('600x400')
l1=Label(win,text="First Name",bg="red",fg="black",font=("arial bold",10))
l1.grid(column=0,row=0)
e1=Entry(win,width="30").grid(column=1,row=0)
l2=Label(win,text="Department",font=("arial bold",10))
l2.grid(column=0,row=1)
e2=Entry(win,width="30").grid(column=1,row=1)
l3=Label(win,text='Age',font=("arial bold",10))
l3.grid(column=0,row=2)
def register():
    messagebox.showinfo("Done","Good work")
btn1=Button(win,text="Register",bg="green",fg='red',font=("arial bold",15),command=register)
btn1.grid(column=2,row=5)
win.mainloop()