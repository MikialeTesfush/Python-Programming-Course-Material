import tkinter
from tkinter.ttk import *
window=tkinter.Tk()
window.title('Combobox')
combo=Combobox(window,width=20)
combo['values']=(1,2,3,4,5,"Text")
combo.current(5)
combo.pack()
#combo.grid(column=1,row=0)
window.geometry('400x300')
window.mainloop()