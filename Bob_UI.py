#Created by Iman Essaghir

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
        self.lbl2.place(x=100, y=200)
        self.t2.place(x=200, y=200)

       
        self.lbl1.place(x=100, y=100)
        self.t1.place(x=200, y=100)
       
       
       
        #Next pop up window

        def open_popup():
         top= Toplevel(window)
         top.geometry("750x250")
         top.title("Run Window")
         Label(top, text= "Program running, please do not close the window", font=('Helvetica 18 bold')).place(x=100,y= 80)

        #Create a button in the main Window to open the popup
 
        self.b1=Button(win, text= "Run", command= open_popup).pack(pady=300)

 
       #After the program in done and run successfully
       
        #def open_popup2():
        # top_2= Toplevel(window)
        # top_2.geometry("750x250")
        # top_2.title("Result Window")
        # Label(top, text= "Program run was successful", font=('Helvetica 18 bold')).place(x=100,y= 80)

        ##Create a button in the main Window to open the popup
 
        #self.b2=Button(win, text= "Close", command= open_popup2).pack(pady=300)

   
     
        win.mainloop()

     
               
mywin=BobWindow(window)

window.mainloop()
