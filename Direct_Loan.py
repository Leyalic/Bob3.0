# Direct Loan Pre-Outbound Queries
from genericpath import isfile
import os
import shutil
from pathlib import Path

# Deprecated
def move_orig_old(orig_doc, orig_doc_2, orig_docx, name):
    copy_name = orig_doc
    copy_2_name = orig_doc_2
    copy_docx_name = orig_docx
    copy_directory = Path("O:/Systems/UOSFA Reports/Direct Loan Reports")
    try:
        shutil.copy(copy_name, copy_directory)
    except FileNotFoundError as e:
        try:
            shutil.copy(copy_docx_name, copy_directory)
        except FileNotFoundError as f:
            input("\nCould not locate "+ name + "\nMake sure it is located in O:/Systems/Direct Loans/Origination\n\nPress Enter when ready.")
    except shutil.Error:
        pass

    try:
        shutil.copy(copy_2_name, copy_directory)
    except FileNotFoundError as e:
        pass
    except shutil.Error:
        pass

def move_orig(filename, source_folder, date, year):
    renamed = date + " DL ORIG " + year + ".doc"
    dest_folder = Path("O:/UOSFA Reports/Direct Loan Reports")

    source_file = source_folder / Path(filename)
    source_filex = Path(str(source_file) + "x")
    dest_file = dest_folder / Path(renamed)
    dest_filex = Path(str(dest_file) + "x")

    source_file2 = source_folder / Path(str(filename) + " (2)")
    source_file2x = Path(str(source_file2) + "x")
    dest_file2 = dest_folder / Path(str(renamed) + " (2)")
    dest_file2x = Path(str(dest_file2) + "x")
    
    # Copy orig file
    if not isfile(dest_file) and not isfile(dest_filex):
        try:
            shutil.copy(source_file, dest_file)
        except FileNotFoundError as e:
            try:
                shutil.copy(source_filex, dest_filex)
            except FileNotFoundError as e:
                pass
                #input("\nCould not locate " + filename + "\nMake sure it is located in " + str(source_folder) + "\n\nPress Enter when ready.")
                #move_orig(filename, source_folder, date, year)
    
    # Copy orig file (2)
    if not isfile(dest_file2) and not isfile(dest_file2x):
        try:
            shutil.copy(source_file2, dest_file2)
        except FileNotFoundError as e:
            try:
                shutil.copy(source_file2x, dest_file2x)
            except FileNotFoundError as e:
                pass
                #input("\nCould not locate " + filename + " (2)\nIf it exists, make sure it is located in " + str(source_folder) + "\n\nPress Enter when ready.")
                #move_orig(filename, source_folder, date, year)
    

def dl_pre_outbound(test, date, year, query, renamed):

    orig_filename = date + " DL ORIG " + year + ".doc"

    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/Direct Loans', 'DL Pre-Outbound'))
        orig_folder = Path('C:/Testing Bob/Direct Loans/Origination')
        #orig_doc = os.path.realpath(os.path.join('C:\Testing Bob\Direct Loans', 'Origination', orig_file_doc))
        #orig_doc_2 = os.path.realpath(os.path.join('C:\Testing Bob\Direct Loans', 'Origination', orig_file_doc_2))
        #orig_docx = os.path.realpath(os.path.join('C:\Testing Bob\Direct Loans', 'Origination', orig_file_docx))

    else:
        directory = os.path.realpath(os.path.join('O:/Systems/Direct Loans', 'DL Pre-Outbound'))
        orig_folder = Path('O:/Systems/Direct Loans/Origination')
        #orig_doc = os.path.realpath(os.path.join('O:/Systems/Direct Loans', 'Origination', orig_file_doc))
        #orig_doc_2 = os.path.realpath(os.path.join('O:/Systems/Direct Loans', 'Origination', orig_file_doc_2))
        #orig_docx = os.path.realpath(os.path.join('O:/Systems/Direct Loans', 'Origination', orig_file_docx))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    move_directory = "Direct Loan Reports"

    # FORMAT: return (query, renamed, archive_directory, UOSFA_folder)
    # query: The original file name
    # renamed: The name the file should have after being moved
    # archive_directory: The folder the file will be copied to
    # UOSFA_folder: The name of the folder the renamed file should be moved to
    # - (eg. "Budget Reports", "SAP Reports", "Unknown Reports") 
    # - put "None" if it shouldn't be moved to a folder in 'O:/UOSFA Reports/'

    if query.startswith("UUFA_DLR_ORIG_TRNS_PEND"):
        move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_ENTRANCE_COUNSEL"):
        move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_LOAN_EFT_DT_LNDR_ERR"):
        move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_LOAN_ORIG_FA_LOAD"):
        move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_LOAN_NO_NSLDS"):
        move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_LOAN_ORIG_ACAD_LVL"):
        move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_LOAN_ORIG_EDIT_ERR"):
        move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_LOAN_ORIG_SPLT_CDS"):
        move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    # Possibly remove
    if "DLR_LN_ORIG_VLOAN_RSN" in query:
        move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_LOAN_SPC_NEED_OVWD"):
        move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if "DLR_LN_ACPT_STAF_31_32" in query:
        move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_NOT_DISB"):
        move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_NOT_DISBURSED"):
        move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_NOT_DISBURSED_20"):
        move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DLR_UG_PLUS_REFND_IND"):
        move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)
                
    return "Empty" #Leave as final line
