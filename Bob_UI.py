#Created by Iman Essaghir

from asyncio.windows_events import NULL
import tkinter as tk
from tkinter import *
import tkinter.font as font
import Do_Queries_Functions

year_valid = False
term_valid = False

rootWindow = Tk()

titleLabel = Label(rootWindow, text="Welcome to the Do Queries Process")

titleLabel.pack()

img=PhotoImage(file='uosfa.png')
Label(rootWindow,image=img).pack()

rootWindow.geometry("850x750")

#Adding widgets

class BobWindow(tk.Frame):
    

    def validate_aid_year(self, d, i, P, s, S, v, V, W):     
        global year_valid
        global term_valid
        if V == "key":
            if P.isnumeric():
                if len(P) == 4:
                    year_valid = True
                else:
                    year_valid = False
            else:
                year_valid = False
            return True
        elif V == "focusout":
            if P.isnumeric():
                if len(P) == 4:
                    self.aid_warn_label.config(text = "")
                    year_valid = True
                    return True
                else:
                    self.aid_warn_label.config(text = "Aid Year must have 4 digits")
                    year_valid = False
                    return False
            else:
                self.aid_warn_label.config(text = "Aid Year must be a number")
                year_valid = False
                return False
        elif V == "focusin":
            return True
        
    def validate_STerm(self, d, i, P, s, S, v, V, W): 
        global year_valid
        global term_valid
        if V == "key":
            if P.isnumeric():
                if len(P) == 4:
                    term_valid = True
                else:
                    term_valid = False
            else:
                term_valid = False
            return True
        elif V == "focusout":
            if P.isnumeric():
                if len(P) == 4:
                    self.term_warn_label.config(text = "")
                    term_valid = True
                    return True
                else:
                    self.term_warn_label.config(text = "STerm must have 4 digits")                  
                    term_valid = False
                    return False
            else:
                self.term_warn_label.config(text = "STerm must be a number")
                term_valid = False
                return False
        elif V == "focusin":
            return True


    def __init__(self, win):
        tk.Frame.__init__(self, win)
        self.lbl1=Label(win, text='Please enter the aid year', fg='red', font=("Times New Roman bold", 13))
        self.lbl2=Label(win, text='Please select S term', fg='red', font=("Times New Roman bold", 13))
       
        aid_valid = (self.register(self.validate_aid_year),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        term_valid = (self.register(self.validate_STerm),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.t1=Entry(bd=10, validate="all", validatecommand=aid_valid)
        
        #sTerm = tk.IntVar()
        #options = ["S", "U", "F"]
        #self.springTerm=Radiobutton(win, text="Spring", font=("Times New Roman bold", 13), variable=sTerm, value=0)
        #self.summerTerm=Radiobutton(win, text="Summer", font=("Times New Roman bold", 13), variable=sTerm, value=1)
        #self.fallTerm=Radiobutton(win, text="Fall", font=("Times New Roman bold", 13), variable=sTerm, value=2)

        #self.t2=Entry(bd=10, validate="all", validatecommand=term_valid)

        self.aid_warn_label = Label(win, text="", fg='blue', font=("Times New Roman bold", 13))
        self.aid_warn_label.place(x=570, y=340)

        #self.term_warn_label = Label(win, text="", fg='blue', font=("Times New Roman bold", 13))
        #self.term_warn_label.place(x=580, y=440)

        self.lbl1.place(x=200, y=300)
        self.t1.place(x=600, y=300)

        #self.lbl2.place(x=200, y=400)
        #self.springTerm.place(x=600, y=400)
        #self.summerTerm.place(x=600, y=430)
        #self.fallTerm.place(x=600, y=460)

        #self.t2.place(x=600, y=400)
       
       
        #Next pop up window

        def open_popup():
            global year_valid
            #global term_valid
            if year_valid:
                #top= Toplevel(rootWindow)
                #top.geometry("750x250")
                #top.title("Run Window")
                #Label(top, text= "Program running, please do not close the window", font=('Helvetica 18 bold')).place(x=100,y= 80)
                Do_Queries_Functions.run(self.t1.get(), rootWindow)
            else:
                self.bell()
                prev = self.focus_get()
                self.b1.focus()
                prev.focus()
                

        #Create a button in the main Window to open the popup
 
        self.b1=Button(win, text="Run", command=open_popup)
        self.b1.pack(side=BOTTOM, anchor="center",padx=18, pady=18)
    
        exit_Button = Button(rootWindow, text="Exit Program", command=rootWindow.quit)
        exit_Button.pack(side=BOTTOM, anchor="e", padx=8, pady=8)

   
        win.mainloop()


mywin=BobWindow(rootWindow)

rootWindow.mainloop()
