#import tkinter
from tkinter import *
from tkinter import messagebox
#win=tkinter.Tk()
win=Tk()
win.geometry('500x300')
win.title('First GUI')
win.configure(bg='blue')
l1=Label(win,text='User Name',bg='black',fg='white',font=("arial bold",10))
l1.grid(column=0,row=0)
l2=Label(win,text='Password',bg='red',fg='green',font=("arial bold",10))
l2.grid(column=0,row=1)
e1=Entry(win,width=25)
e1.grid(column=1,row=0)
e2=Entry(win,width=25)
e2.grid(column=1,row=1)
def clicked():
    messagebox.showinfo('message','plss click again')
btn=Button(win,text='Login',bg='white',fg='black',command=clicked)
btn.grid(column=1,row=2)
win.mainloop()