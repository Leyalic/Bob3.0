#Created by Iman Essaghir

from tkinter import *
import tkinter.font as font

rootWindow = Tk()

titleLabel = Label(rootWindow, text="Welcome to the Do Queries Process")

titleLabel.pack()

img=PhotoImage(file='uosfa.png')
Label(rootWindow,image=img).pack()

rootWindow.geometry("850x750")

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
 
        self.b1=Button(win, text= "Run", command= open_popup).pack(side=BOTTOM, anchor="center",padx=18, pady=18)
    
        exit_Button = Button(rootWindow, text="Exit Program", command=rootWindow.quit)
        exit_Button.pack(side=BOTTOM, anchor="e", padx=8, pady=8)

   
        win.mainloop()


mywin=BobWindow(rootWindow)

rootWindow.mainloop()
