#Created by Iman Essaghir

from tkinter import *
#from tkinter.ttk import *
import tkinter.font as font

rootWindow = Tk()

titleLabel = Label(rootWindow, text="Welcome to the Do Queries Process")

titleLabel.pack()

img=PhotoImage(file='uosfa.png')
Label(rootWindow,image=img).pack()


#Adding widgets


class BobWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Please enter the aid year', fg='red', font=("Times New Roman bold", 13))
        self.lbl2=Label(win, text='Please enter S term', fg='red', font=("Times New Roman bold", 13))
       
        self.t1=Entry(bd=10)
        self.t2=Entry(bd=10)

        self.lbl1.place(x=200, y=300)
        self.t1.place(x=600, y=300)

        self.lbl2.place(x=200, y=400)
        self.t2.place(x=600, y=400)
       
       
        #Next pop up window

        def open_popup():
            top= Toplevel(rootWindow)
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

        #Create a button in the main Window to open the popup
 
        #self.b2=Button(win, text= "Close", command= open_popup2).pack(pady=300)

   
        win.mainloop()


mywin=BobWindow(rootWindow)

rootWindow.mainloop()
