from tkinter import *
from tkinter import filedialog
window = Tk()
window.title("GUI")
pic1 = PhotoImage(file = filedialog.askopenfilenames())
l1 = Label(window, image = pic1)
l1.grid(row=0)
pic2=PhotoImage(file=filedialog.askopenfilenames())
l2=Label(window,image=pic2)
l2.grid(column=1,row=0)
window.mainloop()
