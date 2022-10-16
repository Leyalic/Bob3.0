import os
import re
import openpyxl
import datetime
import time
import shutil
import tkinter
from tkinter import filedialog
from pathlib import Path

odd_aid_years = []
even_aid_years = []
unknown_list = []
current_aid_year = ""
folder_path = ""
disbursement_date = datetime.datetime.min

aid_year_regex = ["Aid[\s]?Y(ea)?r"]
date_regex = ["(0*[1-9]|1[012])[-/.](0*[1-9]|[12][0-9]|3[01])[-/.](2\d{3}|\d{2})","(0*[1-9]|[12][0-9]|3[01])[-/.](0*[1-9]|1[012])[-/.](2\d{3}|\d{2})"]

# Directories
test_destination_folder = Path("C:/Users/JHARDY/Documents/DoQueries/Destination Folders/")
test_copy_folder = Path("C:/Users/JHARDY/Documents/DoQueries/Copied Folders/")
destination_folder = ""
copy_folder = ""

test = True

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
    global current_aid_year
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
            if is_odd_year(current_aid_year):
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
def sort_files():
    global folder_path
    global test

    if test:
        root = tkinter.Tk()    
        root.withdraw()
        directory = filedialog.askdirectory()
        root.destroy()
        folder_path = directory
        for filename in os.listdir(directory):
            find_aid_year(filename)
    else:
        for filename in os.listdir("."):
            find_aid_year(filename)

# The old rename method from DoQueries without attach lists *modified*
def rename_file(name, new_name, i=2):
    this_name = os.path.realpath(name)
    this_new_name = os.path.realpath(new_name)
    dot_index = this_new_name.find(".")
    num = i
    try:
        os.rename(this_name, this_new_name)
    except WindowsError as e:
        try:
            final_name = this_new_name[:dot_index] + " (" + str(num) + ")" + this_new_name[dot_index:]
            os.rename(this_name, final_name)
        except WindowsError:
            rename_file(this_name, this_new_name, num + 1)
            

# The old move method from DoQueries *modified*
def move_to_folder(name, to_directory):
    move_name = name
    move_directory = to_directory
    try:
        shutil.move(move_name, move_directory)
    except FileNotFoundError as e:
        print(e)
    except shutil.Error:
        print ("Already a file with the name:" + name + "at location.")
    except IOError as e:
        print(e)
        pass

# The old do query method from DoQueries without attach lists *modified*
def do_query(name, new_name, destination, i=2):
    this_name = folder_path + "/" + name
    this_new_name = new_name
    this_destination = str(destination)
    num = i
    if num == 2:
        move_to_folder(this_name, destination)
        rename_file(this_destination + "/" + name, this_destination + "/" + this_new_name)

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
    return options[v.get()]

# Prompts user to select folder for unknown files
def handle_unknown_files():
    global unknown_list
    for filename in unknown_list:
        if test:
            folder = test_destination_folder / folder_select_popup(filename)
            new_name = "Manual" + filename;
            do_query(filename, new_name, folder)

        else:
            pass
        # Where does new_name come from?
        # Does the user decide it?
        # Does it not get renamed? 
    pass

# Copies the entire file structure to a new folder
def copy_to_archive():
    if test:
        source = test_destination_folder
        folder_name = "Test" + str(current_aid_year)
        destination = test_copy_folder / folder_name
    else:
        source = destination_folder
        destination = copy_folder / "new folder name"
    try:
        shutil.copytree(source, destination)
    except shutil.Error:
        print ("Already a folder at location.")
    except IOError as e:
        print(e)
        pass

# Moves files to corresponding directory
def move_files():
    global current_aid_year
    global unknown_list

    date = time.strftime("%x").replace("/", "-")

    file_list = []
    if is_odd_year(current_aid_year):
        file_list = odd_aid_years
    else:
        file_list = even_aid_years
    
    if test:
        for filename in file_list:
            if "External" in filename:
                do_query(filename, date + "External" + filename, test_destination_folder / "External Award Reports/")
            
            elif filename.startswith("Daily"):
                do_query(filename, date + "Daily" + disbursement_date.strftime("%m-%d-%y") + filename, test_destination_folder / "Daily Reports/")

            # More elif staements go here
            # copy and paste old versions but remove unused attach_lists parameter

            else:
                unknown_list.append(str(filename))
    else:
        pass

    if len(unknown_list) > 0:
        handle_unknown_files()

    copy_to_archive()

def initialize(user_input):
    global current_aid_year
    global disbursement_date

    current_aid_year = user_input
    today = datetime.date.today()
    if today.weekday() == 0:
        disbursement_date = today - datetime.timedelta(days = 3)
    else:
        disbursement_date = today - datetime.timedelta(days = 1)
    print("Disbursement Date: " + disbursement_date.strftime("%m-%d-%y"))


def main():
    if test:
        initialize("23")
        sort_files()
        output_sorted_files()
        move_files()
    else:
        initialize("user input AidYear")
        sort_files()
        move_files()

    print("Done")

if __name__ == "__main__":
    main()