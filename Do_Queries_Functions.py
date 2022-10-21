import os
import re
import openpyxl
import datetime
import time
import shutil
import tkinter
from tkinter import filedialog
from pathlib import Path


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
folder_path = ""
disbursement_date = datetime.datetime.min

aid_year_regex = ["Aid[\s]?Y(ea)?r"]
date_regex = ["(0*[1-9]|1[012])[-/.](0*[1-9]|[12][0-9]|3[01])[-/.](2\d{3}|\d{2})","(0*[1-9]|[12][0-9]|3[01])[-/.](0*[1-9]|1[012])[-/.](2\d{3}|\d{2})"]

# Directories
test_destination_folder = Path("O:/Systems/QUERIES/_DoQueries")
test_copy_folder = Path("O:/Systems/DoQueries_Archive")
destination_folder = ""
copy_folder = ""

test = True

# Odd year
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

# Search for and return aid year in excel file
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

# Sort file into list depending on aid year
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
        if test:
            print("Couldn't find year of " + filename)
        else:
            pass
        # Possibly prompt user here with popup?
        # Possibly set default aid year to current year?

def output_sorted_files():
    print("Odds: ")
    for filename in odd_aid_years:
        print("- " + filename)
    print("")
    print("Evens: ")
    for filename in even_aid_years:
        print("- " + filename)
    print("")

# Sort all files in directory into odd or even aid years
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

# Copies file to folder without removing it
def copy_to_folder(name, to_directory):
    copy_name = name
    copy_directory = to_directory
    try:
        shutil.copy(copy_name, copy_directory)
    except FileNotFoundError as e:
        print(e)
    except shutil.Error:
        print ("Already a file with the name:" + name + "at location.")
    except IOError as e:
        print(e)
        pass

# The old do query method from DoQueries without attach lists *modified*
def do_query(name, new_name, archive, destination, i=2):
    this_name = folder_path + "/" + name
    this_new_name = new_name
    this_destination = str(destination)
    num = i
    if num == 2:
        rename_file(this_name, this_destination + "/" + this_new_name)
        this_name = this_destination + "/" + this_new_name
        copy_to_folder(this_name, archive)
        move_to_folder(this_name, destination)
        

# Asks user to select a folder
def folder_select_popup(filename):
    root = tkinter.Tk()
    prompt = "The following file could not be sorted. Please select a destination folder."
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

# Prompt user to select folder for unknown files
def handle_unknown_files():
    global unknown_list
    for filename in unknown_list:
        if test:
            folder = test_destination_folder / folder_select_popup(filename)
            archive_folder = ""
            new_name = date + filename + current_aid_year;
            do_query(filename, new_name, archive_folder, folder)

        else:
            pass

# Copy the entire file structure to a new folder
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

# Move files to corresponding directory
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
                archive_folder = test_copy_folder
                do_query(filename, date + filename + current_aid_year, archive_folder, test_destination_folder / "External Award Reports/")
            
            elif filename.startswith("Daily"):
                archive_folder = test_copy_folder
                do_query(filename, date + "Daily" + disbursement_date.strftime("%m-%d-%y") + filename, archive_folder, test_destination_folder / "Daily Reports/")

            # More elif staements go here
            # copy and paste old versions but remove unused attach_lists parameter



            else:
                unknown_list.append(str(filename))
    else:
        pass

    if len(unknown_list) > 0:
        handle_unknown_files()

    #copy_to_archive()


# User Input - Initialize Aid year and disbursement date
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

def run(user_input):
    if test:
        initialize(user_input)
        sort_files()
        output_sorted_files()
        #move_files()
    else:
        initialize(user_input)
        sort_files()
        #move_files()

# Main method
def main():
    #run("23")
    pass
    #print("Done")

    # add imports after fixinf=x the files then uncomment

    # for filename in os.listdir("."):
    ## Daily Queries
    #    if filename.startswith("UUFA_IL_ALL_ITEMS_OVERAWARD"):
    #        do_dailies()
    ## Monday Weekly Queries
    #    if filename.startswith("UUFA_WR"):
    #        do_monday_weeklies()
    ## Budget Queries
    #    if "UUFA_BR" in filename:
    #        do_budget_queries()
    ## Packaging Queries
    #    if filename.startswith("UUFA_PRT_ACAD_PROG_REVIEW"):
    #        do_packaging_queries()
    ## Monthly Queries
    #    if "MR_PELL_SSN_MISMATCH" in filename:
    #        do_monthlies()
    ## Disbursement Queries
    #    if filename.startswith("UUFA_DQ_AUTHORIZED_NOT_DISB"):
    #        do_disb_queries()
    ##2nd LDR Queries
    #    if filename.startswith("UUFA_PRT_PELL_ELG_NO_PELL"):
    #        do_2nd_ldr()
    ## End of Term Queries
    #    if filename.startswith("UUFA_EOT_ACAD_PLAN_RVW"):
    #        do_end_of_term_queries()
    ## Day After LDR Queries
    #    if filename.startswith("UUFA_LDR_MIN_ENROLLMENT_ATH"):
    #        do_day_after_ldr()
    ## Direct Loans Pre-Outbound Queries
    #    if "DLR_LOAN_ORIG_EDIT_ERR" in filename:
    #        dl_pre_outbound()
    ## Alternative Loan Pre-Outbound Queries
    #    if filename.startswith("UUFA_ALR_LOAN_ORG_LND_NT_CK"):
    #        al_pre_outbound()
    ## Pre-Repackaging Queries
    #    if filename.startswith("UUFA_PP"):
    #        do_pre_repackaging()
    ## Mid-Repackaging Queries
    #    if filename.startswith("UUFA_MP"):
    #        do_mid_repack_queries()
    ## After Repackaging Queries
    #    if filename.startswith("UUFA_AP"):
    #        do_after_repackaging()
    ## Daily Scholarships Queries
    #    if filename.startswith("UUFA_SCHOLAR_DISB_ZERO"):
    #        do_daily_scholarships()
    ## Weekly Scholarships Queries
    #    if ("UUFA_WS" in filename):
    #        do_weekly_scholarships()
    ## Budget Testing Queries
    #    if filename.startswith("UUFA_BUDGET_20"):
    #        do_budget_test_queries()
    ## ATB and 3C Queries
    #    if "UUFA_ATB" in filename:
    #        do_atb_fb_3c_queries()
    ## Remove extra files 
    #    if "FASTDVER" in filename or "FINAID_Checklist" in filename  or "ussfa09" in filename or "USSFA090 Reset" in filename or "O-A" in filename:
    #        os.remove(filename)
    #        print("Removed " + filename)
    ## Transfer Student Monitoring
    #    if "_NSLDS" in filename:
    #        do_tsm_queries()

      # TEMPLATE
        # Change File_Name to be file as it is received and _new_file_name to what the new file should be.  Prefix date
        # will be added.
        # for query in os.listdir("."):
        # if query.startswith("___________________"):
        #        do_query(query, date + " _______________" + year + ".xls", directory,
        #                 lkj_mail.attachments)

        #for mail_group in mail_groups:
        #if(mail_group.attachments):
        #    mailer("", aid_year + " Queries", mail_group.recipients,"", mail_group.attachments)
        #    del mail_group.attachments[:]


if __name__ == "__main__":
    main()

#raw_input("So Long, and Thanks for All the Fish.\nPRESS ENTER TO CLOSE.")

