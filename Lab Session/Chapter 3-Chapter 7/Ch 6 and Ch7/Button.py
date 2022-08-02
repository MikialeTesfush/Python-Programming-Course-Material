import tkinter
from tkinter import *
window=tkinter.Tk()
button=tkinter.Button(window,text="Enter",bg='red',fg='black').pack(side="bottom")
#button.grid(column=1,row=0)
window.geometry('400x350')
window.mainloop()