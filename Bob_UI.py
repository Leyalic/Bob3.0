#Created by Iman Essaghir

import tkinter as tk
from tkinter import *
from tkinter import filedialog
import tkinter.font as font
import Do_Queries_Functions
from pathlib import Path

year_valid = False
term_valid = False

rootWindow = Tk()

titleLabel = Label(rootWindow, text="Welcome to the Do Queries Process")

titleLabel.pack()

img=PhotoImage(file='uosfa.png')
Label(rootWindow,image=img).pack()

rootWindow.geometry("850x550")

# Return values of Do_Queries_FUnctions
direct_loan_flag = False
alt_loan_flag = False
unknown_list = []

select_window = None

folder_option = ""

aid_year = ""

#Adding widgets

class BobWindow(tk.Frame):
    
    def create_dir_orig_window():
        pass

    def create_alt_orig_window():
        pass

    def handle_direct_orig():
        success = Do_Queries_Functions.move_direct_orig()
        if not success:
            # Prompt user for orig file
            # TODO: Call create_dir_orig_window()
            orig_file = Path(filedialog.askopenfilename()).name
            Do_Queries_Functions.move_direct_orig_fn(orig_file)

    def handle_alt_orig():
        success = Do_Queries_Functions.move_alt_orig()
        if not success:
            # Prompt user for orig file
            # TODO: Call create_alt_orig_window
            orig_file = Path(filedialog.askopenfilename()).name
            Do_Queries_Functions.move_alt_orig_fn(orig_file)

    def handle_selection(option):
        global folder_option
        global select_window

        folder_option = option
        select_window.destroy()

    # Prompt user to select folder for unknown file
    def folder_select_popup(filename):
        global select_window
        select_window = Toplevel(rootWindow)
        prompt = "The following file could not be sorted. Please select a destination folder."
        options = [
                    "Alternative Loan Reports",
                    "Budget Reports",
                    "Daily Reports",
                    "Direct Loan Reports",
                    "External Award Reports",
                    "Financial Aid Reports",
                    "Monthly Reports",
                    "Packaging Reports",
                    "Pell Reports",
                    "SAP Reports",
                    "Scholarship Reports",
                    "Unknown Reports",
                    "Weekly Reports"              
                  ]
        tk.Label(select_window, text=prompt, padx=10, pady=5).pack()
        tk.Label(select_window, text=filename, fg='#00f', padx=10).pack()
        v = tk.IntVar()
        for i, option in enumerate(options):
            tk.Radiobutton(select_window, text=option, variable=v, value=i).pack(anchor="w")
        tk.Button(select_window, text="Submit", command=lambda: BobWindow.handle_selection(options[v.get()])).pack()
        #select_window.mainloop()
        select_window.title("Select Folder")
        return select_window


    # Prompt user to select folder for unknown files
    def handle_unknown_files():
        global unknown_list
        global folder_option

        done = True
        while len(unknown_list) > 0:
            done = False
            folder_option = ""

            # Ask user to select folder
            filename = unknown_list[0]                     
            wind = BobWindow.folder_select_popup(filename)
            rootWindow.wait_window(wind)

            if folder_option == "":
                unknown_list.remove(filename)
                continue

            print("Moved to " + folder_option)

            # Move file to selected folder
            renamed = Do_Queries_Functions.new_name(filename, aid_year)           
            Do_Queries_Functions.do_query_unknown(filename, renamed, folder_option)
            unknown_list.remove(filename)

        print("All Unknown Files Handled")

        return done

    # Runs Do_Queries on all files
    def open_popup(self):       
        global aid_year
        global direct_loan_flag
        global alt_loan_flag
        global unknown_list

        if year_valid:
            self.exit_Button["state"] = "disabled"
            self.t1["state"] = "disabled"

            aid_year = self.t1.get()           
            direct_loan_flag, alt_loan_flag, unknown_list = Do_Queries_Functions.run(self.t1.get(), rootWindow)

            if len(unknown_list) > 0:
                # Disable all window input here
                
                BobWindow.handle_unknown_files()
                # Re-enable all window input here
                
                print("Process Completed")

            if direct_loan_flag:
                BobWindow.handle_direct_orig()

            if alt_loan_flag:
                BobWindow.handle_alt_orig()

            self.t1["state"] = "normal"
            self.exit_Button["state"] = "normal"

        else:
            rootWindow.bell()
            prev = self.focus_get()
            self.b1.focus()
            prev.focus()
            self.aid_warn_label.config(text = "Aid Year must be provided")

    # Checks if aid year is a 4-digit number
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
        

    def __init__(self, win):
        tk.Frame.__init__(self, win)
        self.lbl1=Label(win, text='Please enter the aid year', fg='red', font=("Times New Roman bold", 13))
        self.lbl2=Label(win, text='Please select S term', fg='red', font=("Times New Roman bold", 13))
       
        aid_valid = (self.register(self.validate_aid_year),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

        self.t1=Entry(bd=10, validate="all", validatecommand=aid_valid)
        
        self.aid_warn_label = Label(win, text="", fg='blue', font=("Times New Roman bold", 13))
        self.aid_warn_label.place(x=570, y=340)


        self.lbl1.place(x=200, y=300)
        self.t1.place(x=600, y=300)
        
                

        #Create a button in the main Window to open the popup
 
        self.b1=Button(win, text="Run", bd="4", command=self.open_popup, height="5", width="30")
        self.b1.pack(side=BOTTOM, anchor="center",padx=18, pady=18)
    
        self.exit_Button = Button(rootWindow, text="Exit Program", command=rootWindow.destroy)
        self.exit_Button.pack(side=BOTTOM, anchor="e", padx=8, pady=8)

        self.winfo_toplevel().title("Bob Window")
   
        #win.mainloop()

mywin=BobWindow(rootWindow)

rootWindow.mainloop()
