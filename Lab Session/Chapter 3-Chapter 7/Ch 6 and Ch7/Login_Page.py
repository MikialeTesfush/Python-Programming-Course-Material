from tkinter import *
from tkinter import messagebox
gui=Tk()
gui.geometry("1080x1080")
gui.title("GUI2")
gui['bg']="green"
gui_frame=Frame(gui,width=700,height=450)
gui_frame.place(x=200,y=200)
label=Label(gui_frame,text="Student Login Page",font=("arial","20","bold"),bg="blue").place(x=250,y=10)
label_user_id=Label(gui_frame,text="User Id:",font=("arial","12","bold")).place(x=100,y=200)
label_password=Label(gui_frame,text="Password:",font=("arial","12","bold")).place(x=100,y=300)

entry_user_id=Entry(gui_frame,font=("arial","12","bold")).place(x=200,y=200)
entry_password=Entry(gui_frame,show="*",font=("arial","12","bold")).place(x=200,y=300)

def verify():
        messagebox.showinfo(title="Welcome",message="Welcome User")

btn_login=Button(gui_frame,text='Login',font=("arial","12","bold"),command=verify)
btn_login.place(x=400,y=400)

gui.mainloop()
