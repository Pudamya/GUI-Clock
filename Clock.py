from tkinter import *
from tkinter.ttk import *
from time import strftime

window=Tk()
window.title("My Clock")

    
def dis_time():
    str_time=strftime("%H : %M : %S %p")
    label.config(text=str_time)
    label.after(1000,dis_time)

label=Label(window,font=("Arial",50),background="black",foreground="yellow")
label.grid(column=0,row=0)

dis_time()

window.mainloop()
