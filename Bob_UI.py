from tkinter import *
import tkinter.font as font

window=Tk()

#Adding widgets

window.title('UOSFA - Do Queries (Bob)')
window.geometry("700x700+10+20")


class BobWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Aid Year', fg='red', font=("Times New Roman bold", 16))
        self.lbl2=Label(win, text='S Term', fg='red', font=("Times New Roman bold", 16))
       
        self.t1=Entry(bd=10)
        self.t2=Entry(bd=10)
       

       
        self.lbl1.place(x=100, y=100)
        self.t1.place(x=200, y=100)
        self.lbl2.place(x=100, y=200)
        self.t2.place(x=200, y=200)
        self.b1=Button(win, text='Run')
        self.b2=Button(win, text='Close')
   
        f = font.Font(family='Times New Roman', size=12, weight="bold")
        self.b1['font'] = f
        self.b2['font'] = f

        self.b1.place(x=200, y=350)
        self.b2.place(x=400, y=350)
       
 
               
mywin=BobWindow(window)

window.mainloop()