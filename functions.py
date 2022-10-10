# Created by Josh Hardy
# SOme functions are new, others are taken from the currenr DoQueries

import os
import re
import openpyxl
import datetime
import shutil
import tkinter
from tkinter import filedialog

odd_aid_years = []
even_aid_years = []
unknown_list = []
current_aid_year = 23
is_current_aid_year_odd = current_aid_year % 2 == 1
folder_path = ""
disbursement_date = datetime.datetime.min

aid_year_regex = ["Aid[\s]?Y(ea)?r"]
date_regex = ["(0*[1-9]|1[012])[-/.](0*[1-9]|[12][0-9]|3[01])[-/.](2\d{3}|\d{2})","(0*[1-9]|[12][0-9]|3[01])[-/.](0*[1-9]|1[012])[-/.](2\d{3}|\d{2})"]

def is_odd_year(year):
    year_int = int(year[-1])
    return year_int % 2 == 1

def has_aid_year(filename):
    has = False
    year = 0
    found_year = re.search("_\d\d_", filename)
    if found_year:
        has = True
        year = found_year.group()[1:-1]
    return (has, year)

# Searches for and returns aid year in excel file
def search_excel_file(filename):
    global folder_path
    has = False
    year = 0

    fullpath = ""
    if ("\\" in folder_path):
        fullpath = folder_path + "\\" + filename
    elif ("/" in folder_path):
        fullpath = folder_path + "/" + filename
    workbook = openpyxl.load_workbook(fullpath, True)
    sheet = workbook.active
    
    for row in sheet.rows:
        for cell in row:
            if any (re.match(regex_str, str(cell.value), re.IGNORECASE) for regex_str in aid_year_regex):
                has = True
                year = str(cell.value)[-2:]
                workbook.close()
                return (has, year)
            if cell.value is not None and cell.is_date:
                has = True
                year = str(cell.value.year)
                workbook.close()
                return (has, year)
    workbook.close()
    return (has, year)

# Sorts file into list depending on aid year
def find_aid_year(filename):
    global odd_aid_years
    global even_aid_years

    file_year = has_aid_year(filename)
    if file_year[0]:
        if is_odd_year(file_year[1]):
            odd_aid_years.append(str(filename))
        else:
            even_aid_years.append(str(filename))

    elif filename.lower().endswith(('xlsx', 'xlsm', 'xltx', 'xltm')):
        file_year = search_excel_file(filename) # file_year: (bool has_year, str year)
        if file_year[0]:
            if is_odd_year(file_year[1]):
                odd_aid_years.append(str(filename))
            else:
                even_aid_years.append(str(filename))
        else: # Default for spreadsheets is current year
            if is_current_aid_year_odd:
                odd_aid_years.append(str(filename))
            else:
                even_aid_years.append(str(filename))
    else:
        print("Couldn't find year of " + filename)
        # Possibly prompt user here with popup?

def output_sorted_files():
    print("Odds: ")
    for filename in odd_aid_years:
        print("- " + filename)
    print("")
    print("Evens: ")
    for filename in even_aid_years:
        print("- " + filename)
    print("")

# Sorts all files in directory into odd or even aid years
def sort_files(test):
    global folder_path

    if (test == 0):
        for filename in os.listdir("."):
            find_aid_year(filename)

    if (test == 1):
        root = tkinter.Tk()    
        root.withdraw()
        directory = filedialog.askdirectory()
        root.destroy()
        folder_path = directory
        for filename in os.listdir(directory):
            find_aid_year(filename)

# The old rename method from DoQueries without attach lists
def rename_file(name, new_name, i=2):
    this_name = os.path.realpath(name)
    this_new_name = os.path.realpath(new_name)
    num = i
    try:
        os.rename(this_name, this_new_name)
    except WindowsError as e:
        try:
            final_name = this_new_name[:-4] + " (" + str(num) + ")" + this_new_name[-4:]
            os.rename(this_name, final_name)
        except WindowsError:
            rename_file(this_name, this_new_name, num + 1)

# The old move method from DoQueries
def move_to_folder(name, to_directory):
    move_name = name
    move_directory = to_directory
    try:
        shutil.move(move_name, move_directory)
    except shutil.Error:
        print ("Already a file with the name:" + name + "at location.")
    except IOError as e:
        print(e)
        pass

# The old do query method from DoQueries without attach lists
def do_query(name, new_name, destination, i=2):
    this_name = name
    this_new_name = new_name
    this_destination = destination
    num = i
    if num == 2:
        move_to_folder(this_name, this_destination)
        rename_file(destination + "/" + this_name, destination + "/" + this_new_name)

# Asks user to select a folder
def folder_select_popup(filename):
    root = tkinter.Tk()
    prompt = "The following file could not be sorted. Please select a folder."
    options = [
                "Alternative Loan Reports",
                "Budget Reports",
                "Daily Reports",
                "Direct Loan Reports",
                "External Award Reports",
                "Monthly Reports",
                "Pell Reports",
                "Scholarship Reports",
                "Weekly Reports"
              ]
    tkinter.Label(root, text=prompt, padx=10, pady=5).pack()
    tkinter.Label(root, text=filename, fg='#00f', padx=10).pack()
    v = tkinter.IntVar()
    for i, option in enumerate(options):
        tkinter.Radiobutton(root, text=option, variable=v, value=i).pack(anchor="w")
    tkinter.Button(text="Submit", command=root.destroy).pack()
    root.mainloop()
    if v.get() == 0: return None
    return options[v.get()]

def handle_unknown_files():
    global unknown_list
    for filename in unknown_list:
        folder = folder_select_popup(filename)
        do_query(filename, new_name, folder)
        # Where does new_name come from?
        # Does the user decide it?
        # Does it not get renamed? 
    pass

def copy_to_archive():
    source_folder = "location of moved files"
    destination_folder = "file path to Archive Folder" + "new folder name"
    try:
        shutil.copytree(source_folder, destination_folder)
    except shutil.Error:
        print ("Already a folder at location.")
    except IOError as e:
        print(e)
        pass

# Moves files to corresponding directory
def move_files():
    global unknown_list

    file_list = []
    if is_current_aid_year_odd:
        file_list = odd_aid_years
    else:
        file_list = even_aid_years
  
    for filename in file_list:
        if "String" in filename:
            do_query(filename, new_name, folder) 
            # copy and paste old versions but remove unused attach_lists parameter
        # More elif staements go here
        else:
            unknown_list.append(str(filename))

    if len(unknown_list > 0):
        handle_unknown_files()

    copy_to_archive()

def initialize(user_input):
    global current_aid_year
    global is_current_aid_year_odd
    global disbursement_date

    current_aid_year = user_input
    is_current_aid_year_odd = current_aid_year % 2 == 1
    today = datetime.date.today()
    if today.weekday == 0:
        disbursement_date = today - datetime.timedelta(days = 3)
    else:
        disbursement_date = today - datetime.timedelta(days = 1)
    print("Disbursement Date: " + disbursement_date.strftime("%m-%d-%y"))


def main():
    initialize(23)
    sort_files(1)
    output_sorted_files()
    #move_files() #<-unfinished
    
    # Just a test
    folder = folder_select_popup("unknown_file.txt")
    print(folder)

    print("Done")

if __name__ == "__main__":
    main()