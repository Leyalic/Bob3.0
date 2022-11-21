# Created by Joshua Hardy and mmason
from asyncio.windows_events import NULL
from genericpath import isfile
import os
import re
import openpyxl
import datetime
import time
import shutil
import tkinter
from tkinter import filedialog
from tkinter import Toplevel
from pathlib import Path

{}
# Query imports
import After_Repack_Queries
import Alt_Loan_Queries
import Atb_Fbill_3C_Queries
import Budget_Queries
import Daily_Queries
import Day_AfterLDR
import Direct_Loan
import Disbursement_Queries
import EndOfTerm_Queries
import Mid_Repack_Queries
import Monday_DailyQueries
import Monthly_Queries
import Packaging_Queries
import PrePackaging_Queries
import Scholarships_Queries
import Second_LDR
import Tsm_Queries


# The date becomes the current date and is then placed in MM-DD-YY format
date = time.strftime("%x").replace("/", "-")
now = datetime.datetime.now()
last_month = now.month - 1 if now.month > 1 else 12
last_months_year = now.year - 1 if now.month == 12 else now.year
month_folder = date[:2] + "-20" + date[-2:]

# Var definitions
odd_aid_years = []
even_aid_years = []
unknown_list = []
current_aid_year = ""
folder_path = Path()
disbursement_date = datetime.datetime.min

rootWindow = ""
select_window = ""

aid_year_regex = ["Aid[\s]?Y(ea)?r"]
date_regex = ["(0*[1-9]|1[012])[-/.](0*[1-9]|[12][0-9]|3[01])[-/.](2\d{3}|\d{2})","(0*[1-9]|[12][0-9]|3[01])[-/.](0*[1-9]|1[012])[-/.](2\d{3}|\d{2})"]

# Directories
#test_UOSFA_directory = Path("O:/Systems/UOSFA Report Archive")
#test_UOSFA_directory = Path("O:/UOSFA Reports")
test_UOSFA_directory = Path("C:/Users/JHARDY/Documents/DoQueries/Destination Folders")
UOSFA_directory = Path("O:/UOSFA Reports")

test = True

# Odd year
def is_odd_year(year):
    year_int = int(year[-1])
    return year_int % 2 == 1

# Search for and return aid year in filename
def has_aid_year(filename):
    filestring = str(filename)
    has = False
    year = "0"
    found_year = re.search("_\d\d-", filestring)
    if found_year:
        has = True
        year = "20" + found_year.group()[1:-1]
    return (has, year)

# Search for and return aid year in excel file
def search_excel_file(filename):
    global folder_path
    has = False
    year = "0"

    fullpath = folder_path / filename
    workbook = openpyxl.load_workbook(fullpath, True)
    sheet = workbook.active
    
    for row in sheet.rows:
        for cell in row:
            if any (re.match(regex_str, str(cell.value), re.IGNORECASE) for regex_str in aid_year_regex):
                has = True
                year = "20" +  str(cell.value)[-2:]
                workbook.close()
                return (has, year)
            if cell.value is not None and cell.is_date:
                has = True
                year = str(cell.value.year)
                if len(str(year)) < 4:
                    year = "20" + year[-2:]
                workbook.close()
                return (has, year)
    workbook.close()
    return (has, year)

def output_sorted_files():
    print("Odds: ")
    for filename in odd_aid_years:
        print("- " + filename)
    print("")
    print("Evens: ")
    for filename in even_aid_years:
        print("- " + filename)
    print("")


# The old rename method from DoQueries without attach lists *modified*
def rename_file(name, new_name, i=2):
    this_name = os.path.realpath(name)
    this_new_name = os.path.realpath(new_name)
    dot_index = this_new_name.find(".")
    num = i
    renamed = this_new_name
    try:
        os.rename(this_name, this_new_name)
    except WindowsError as e:
        try:
            final_name = this_new_name[:dot_index] + " (" + str(num) + ")" + this_new_name[dot_index:]
            os.rename(this_name, final_name)
            renamed = final_name
        except WindowsError:
            rename_file(this_name, this_new_name, num + 1)
    finally:
        return renamed
            

## The old move method from DoQueries *modified*
#def move_to_folder(name, to_directory, num=2):
#    move_name = name
#    move_directory = to_directory
#    try:
#        shutil.move(move_name, move_directory)
#    except FileNotFoundError as e:
#        print(e)
#    except shutil.Error:
#        print ("Already a file with the name:" + name + "at location.")
#        dot_index = move_name.find(".")
#        final_name = move_name[:dot_index] + " (" + str(num) + ")" + move_name[dot_index:]
#        renamed = rename_file(name, final_name, num+1)
#        move_to_folder(renamed, to_directory, num+1)
#    except IOError as e:
#        print(e)
#        pass

## Copies file to folder without removing it
#def copy_to_folder(name, to_directory, num=2):
#    copy_name = name
#    copy_directory = to_directory
#    try:
#        shutil.copy(copy_name, copy_directory)
#    except FileNotFoundError as e:
#        print(e)
#    except shutil.Error:
#        print ("Already a file with the name:" + name + "at location.")
#        renamed = rename_file(name, name, num+1)
#        copy_to_folder(renamed, to_directory, num+1)
#    except IOError as e:
#        print(e)
#        pass

## The old do query method from DoQueries without attach lists *modified*
#def do_query_old(name, new_name, legacy_archive, UOSFA_folder, i=2):
#    global folder_path
#    global UOSFA_directory

#    this_name = str(folder_path / Path(name))
#    this_new_name = str(folder_path / Path(new_name))
#    if test:
#        this_destination = str(test_UOSFA_directory / UOSFA_folder)
#    else:       
#        this_destination = str(UOSFA_directory / UOSFA_folder)

#    num = i
#    if num == 2:
#        renamed = rename_file(this_name, this_new_name, num)
#        this_name = str(folder_path / Path(this_new_name))
#        if UOSFA_folder == "None":
#            move_to_folder(this_name, legacy_archive, i)
#        else:
#            copy_to_folder(this_name, legacy_archive, i)        
#            move_to_folder(this_name, this_destination, i)

# Renames file to ensure no duplicates at desired location
def rename_no_duplicates(folder_path, renamed):
    filepath = str(folder_path / Path(renamed))
    while(isfile(filepath)):
        paren_index = filepath.find("(")
        if paren_index > -1:
            right_paren_index = filepath.find(")")
            dup_num = filepath[paren_index + 1:right_paren_index]
            dup_num = str(int(dup_num) + 1)           
            filepath = filepath[:paren_index+1] + dup_num + filepath[right_paren_index:]
        else:
            dot_index = filepath.find(".")
            filepath = filepath[:dot_index] + " (2)" + filepath[dot_index:]
    return filepath

# A new do query method made from scratch for better handling of duplicate files
def do_query(name, renamed, legacy_archive, UOSFA_folder):

    current_filepath = str(folder_path / Path(name))

    if test:
        UOSFA_destination = str(test_UOSFA_directory / UOSFA_folder)
    else:       
        UOSFA_destination = str(UOSFA_directory / UOSFA_folder)

    if UOSFA_folder == "None":
        legacy_filepath = rename_no_duplicates(legacy_archive, renamed)
        shutil.move(current_filepath, legacy_filepath)
    else:
        legacy_filepath = rename_no_duplicates(legacy_archive, renamed)
        UOSFA_filepath = rename_no_duplicates(UOSFA_destination, renamed)
        shutil.copy(current_filepath, legacy_filepath)
        shutil.move(current_filepath, UOSFA_filepath)    

# The do query method for manually selected folders
def do_query_unknown(name, renamed, destination):
    
    current_filepath = str(folder_path / Path(name))

    if test:
        UOSFA_destination = str(test_UOSFA_directory / destination)
    else:       
        UOSFA_destination = str(UOSFA_directory / destination)

    destination_filepath = rename_no_duplicates(UOSFA_destination, renamed)
    shutil.move(current_filepath, destination_filepath)
        
def new_name(name, year):
    hay_result = has_aid_year(name)
    renamed = ""
    if hay_result[0]:
        dot_index = name.find(".")
        dash_index = name.rfind("-")
        if dash_index > -1:
            renamed = date + " " + name[:(dash_index - 3)] + " " + year[2:] + name[dot_index:]
        else:
            renamed = date + " " + name[:(dot_index - 3)] + " " + year[2:] + name[dot_index:]
    else:
        dot_index = name.find(".")
        dash_index = name.rfind("-")
        if dash_index > -1:
            renamed = date + " " + name[:dash_index] + " " + year[2:] + name[dot_index:]
        else:
            renamed = date + " " + name[:dot_index] + " " + year[2:] + name[dot_index:]
    return renamed

def new_name_disb(name, year):
    hay_result = has_aid_year(name)
    renamed = ""
    if hay_result[0]:
        dot_index = name.find(".")
        dash_index = name.rfind("-")
        renamed = disbursement_date + " " + name[:(dash_index - 3)] + " " + year[2:] + name[dot_index:]
    else:
        dot_index = name.find(".")
        dash_index = name.rfind("-")
        renamed = disbursement_date + " " + name[:dash_index] + " " + year[2:] + name[dot_index:]
    return renamed

## Copy the entire file structure to a new folder
#def copy_to_archive():
#    if test:
#        source = test_destination_folder
#        folder_name = "Test" + str(current_aid_year)
#        destination = test_copy_folder / folder_name
#    else:
#        source = destination_folder
#        destination = copy_folder / "new folder name"
#    try:
#        shutil.copytree(source, destination)
#    except shutil.Error:
#        print ("Already a folder at location.")
#    except IOError as e:
#        print(e)
#        pass

# Move files to corresponding directory
def move_files(filename, year, match):
    global current_aid_year
    global unknown_list
    global disbursement_date

    date = time.strftime("%x").replace("/", "-")
    renamed = new_name(filename, year)
    renamed_disb = new_name_disb(filename, year)
    

    info = "Empty" # Stores do_query parameters

# Daily Queries
    if info == "Empty":
        info = Daily_Queries.do_dailies(test, date, year, filename, renamed)
# Monday Weekly Queries
    if info == "Empty": #and filename.startswith("UUFA_WR"):
        info = Monday_DailyQueries.do_monday_weeklies(test, date, year, filename, renamed)
# Budget Queries
    if info == "Empty": #and "UUFA_BR" in filename or "UUFA_BR_COA" in filename:
        info = Budget_Queries.do_budget_queries(test, date, year, filename, renamed)
# Packaging Queries
    if info == "Empty": #and filename.startswith("UUFA_PRT_ACAD_PROG_REVIEW"):
        info = Packaging_Queries.do_packaging_queries(test, date, year, filename, renamed)
# Monthly Queries
    if info == "Empty": #and "MR_PELL_SSN_MISMATCH" in filename:
        info = Monthly_Queries.do_monthlies(test, date, current_aid_year, filename, renamed)
# Disbursement Queries
    if info == "Empty": #and filename.startswith("UUFA_DQ_AUTHORIZED_NOT_DISB"):
        info = Disbursement_Queries.do_disb_queries(test, date, year, filename, renamed_disb)
#2nd LDR Queries
    if info == "Empty": #and filename.startswith("UUFA_PRT_PELL_ELG_NO_PELL"):
        info = Second_LDR.do_2nd_ldr(test, year, filename, renamed)
# End of Term Queries
    if info == "Empty": #and filename.startswith("UUFA_EOT_ACAD_PLAN_RVW"):
        info = EndOfTerm_Queries.do_end_of_term_queries(test, year, filename, renamed)
# Day After LDR Queries
    if info == "Empty": #and filename.startswith("UUFA_LDR_MIN_ENROLLMENT_ATH"):
        info = Day_AfterLDR.do_day_after_ldr(test, year, filename, renamed)
# Direct Loans Pre-Outbound Queries
    if info == "Empty": #and "DLR_LOAN_ORIG_EDIT_ERR" in filename:
        info = Direct_Loan.dl_pre_outbound(test, date, year, filename, renamed)
## Alternative Loan Pre-Outbound Queries
    if info == "Empty": #and filename.startswith("UUFA_ALR_LOAN_ORG_LND_NT_CK"):
        info = Alt_Loan_Queries.al_pre_outbound(test, date, year, filename, renamed)
# Pre-Repackaging Queries
    if info == "Empty": #and filename.startswith("UUFA_PP"):
        info = PrePackaging_Queries.do_pre_repackaging(test, year, filename, renamed)
# Mid-Repackaging Queries
    if info == "Empty": #and filename.startswith("UUFA_MP"):
        info = Mid_Repack_Queries.do_mid_repack_queries(test, year, filename, renamed)
# After Repackaging Queries
    if info == "Empty": #and filename.startswith("UUFA_AP"):
        info = After_Repack_Queries.do_after_repackaging(test, year, filename, renamed)
# Daily Scholarships Queries
    if info == "Empty": #and filename.startswith("UUFA_SCHOLAR_DISB_ZERO"):
        info = Scholarships_Queries.do_daily_scholarships(test, year, filename, renamed)
# Weekly Scholarships Queries
    if info == "Empty": #and ("UUFA_WS" in filename):
        info = Scholarships_Queries.do_weekly_scholarships(test, year, filename, renamed)
# Budget Testing Queries
    if info == "Empty": #and filename.startswith("UUFA_BUDGET_20"):
        info = Budget_Queries.do_budget_test_queries(test, date, year, filename, renamed)
# ATB and 3C Queries
    if info == "Empty": #and "UUFA_ATB" in filename:
        info = Atb_Fbill_3C_Queries.do_atb_fb_3c_queries(test, filename, renamed)
# Remove extra files 
    if "FASTDVER" in filename or "FINAID_Checklist" in filename  or "ussfa09" in filename or "USSFA090 Reset" in filename or "O-A" in filename:
        os.remove(folder_path / Path(filename))
        print("Removed " + filename)
        info = "Removed"
# Transfer Student Monitoring
    if info == "Empty": #and "_NSLDS" in filename:
        info = Tsm_Queries.do_tsm_queries(test, filename, renamed)

# Unknown File
    if info == "Empty":
        unknown_list.append(str(filename))
    elif info == "Removed":
        pass
    else:
        do_query(info[0], info[1], info[2], info[3])

## Asks user to select a folder
#def folder_select_popup(filename):
#    global select_window
#    select_window = Toplevel(rootWindow)
#    prompt = "The following file could not be sorted. Please select a destination folder."
#    options = [
#                "Alternative Loan Reports",
#                "Budget Reports",
#                "Daily Reports",
#                "Direct Loan Reports",
#                "External Award Reports",
#                "Financial Aid Reports",
#                "Monthly Reports",
#                "Packaging Reports",
#                "Pell Reports",
#                "SAP Reports",
#                "Scholarship Reports",
#                "Unknown Reports",
#                "Weekly Reports"              
#              ]
#    tkinter.Label(select_window, text=prompt, padx=10, pady=5).pack()
#    tkinter.Label(select_window, text=filename, fg='#00f', padx=10).pack()
#    v = tkinter.IntVar()
#    for i, option in enumerate(options):
#        tkinter.Radiobutton(select_window, text=option, variable=v, value=i).pack(anchor="w")
#    tkinter.Button(select_window, text="Submit", command=lambda: handle_selection(options[v.get()], filename)).pack()
#    select_window.mainloop()

#def handle_selection(UOSFA_folder, filename):
#    global select_window
#    select_window.destroy()
#    if test:
#        folder = test_UOSFA_directory / Path(UOSFA_folder)
#        renamed = new_name(filename, current_aid_year)
#        do_query_unknown(filename, renamed, folder)
#    else:
#        folder = UOSFA_directory / Path(UOSFA_folder)
#        renamed = new_name(filename, current_aid_year)
#        do_query_unknown(filename, renamed, folder)
#    done = handle_unknown_files()
#    if(done):
#        pass


## Prompt user to select folder for unknown files
#def handle_unknown_files():
#    global unknown_list
#    done = True
#    for filename in unknown_list:
#        done = False
#        unknown_list.remove(filename)
#        folder_select_popup(filename)
#    return done
        


def aid_year_match(year):
    global current_aid_year
    if is_odd_year(current_aid_year):
        return is_odd_year(year)
    else:
        return not is_odd_year(year)

# Sort file into list depending on aid year
def find_aid_year(filename):
    global current_aid_year
    global odd_aid_years
    global even_aid_years

    filestring = str(filename)

    file_year = has_aid_year(filestring)
    if file_year[0]:
        if is_odd_year(file_year[1]):
            odd_aid_years.append(str(filestring))
            move_files(filestring, file_year[1], aid_year_match(file_year[1]))
        else:
            even_aid_years.append(str(filestring))
            move_files(filestring, file_year[1], aid_year_match(file_year[1]))

    elif filestring.lower().endswith(('xlsx', 'xlsm', 'xltx', 'xltm')):
        file_year = search_excel_file(filename) # file_year: (bool has_year, str year)
        if file_year[0]:
            if is_odd_year(file_year[1]):
                odd_aid_years.append(str(filestring))
                move_files(filestring, file_year[1], aid_year_match(file_year[1]))
            else:
                even_aid_years.append(str(filestring))
                move_files(filestring, file_year[1], aid_year_match(file_year[1]))
        else: # Default for spreadsheets is current year
            if is_odd_year(current_aid_year):
                odd_aid_years.append(str(filestring))
                move_files(filestring, current_aid_year, True)
            else:
                even_aid_years.append(str(filestring))
                move_files(filestring, current_aid_year, True)
    else:
        if test:
            # Default is current year
            if is_odd_year(current_aid_year):
                odd_aid_years.append(str(filestring))
                move_files(filestring, current_aid_year, True)
            else:
                even_aid_years.append(str(filestring))
                move_files(filestring, current_aid_year, True)
            #print("Couldn't find year of " + filestring)
        else:
            if is_odd_year(current_aid_year):
                odd_aid_years.append(str(filestring))
                move_files(filestring, current_aid_year, True)
            else:
                even_aid_years.append(str(filestring))
                move_files(filestring, current_aid_year, True)
    
# Sort all files in directory into odd or even aid years
def sort_files():
    global folder_path
    global test
    global unknown_list

    if test:
        root = tkinter.Tk()    
        root.withdraw()
        directory = filedialog.askdirectory()
        root.destroy()
        if directory is "":
            return
        folder_path = directory
        for filename in os.listdir(directory):
            pFilename = Path(filename)
            find_aid_year(pFilename)
        if len(unknown_list) > 0:
            #handle_unknown_files()
            pass
    else:
        folder_path = Path(os.getcwd())
        for filename in os.listdir("."):
            pFilename = Path(filename)
            find_aid_year(pFilename)

        if len(unknown_list) > 0:
            #handle_unknown_files()
            pass


# User Input - Initialize Aid year and disbursement date
def initialize(year, root):
    global current_aid_year
    global STerm
    global disbursement_date
    global rootWindow

    rootWindow = root

    current_aid_year = year
    today = datetime.date.today()
    if today.weekday() == 0:
        disbursement_date = today - datetime.timedelta(days = 3)
        disbursement_date = disbursement_date.strftime("%m-%d-%y")
    else:
        disbursement_date = today - datetime.timedelta(days = 1)
        disbursement_date = disbursement_date.strftime("%m-%d-%y")
    if test:
        print("Disbursement Date: " + disbursement_date)

def run(year, root):
    if test:
        initialize(year, root)
        sort_files()
        output_sorted_files()
        print("Done")
        
    else:
        initialize(year, root)
        sort_files()

    return unknown_list
        



