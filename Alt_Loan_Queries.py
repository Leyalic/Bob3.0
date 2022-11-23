# Alt Loan Pre-Outbound Queries
from genericpath import isfile
import os
import shutil
from pathlib import Path

def move_orig(filename, source_folder, date, year):
    renamed = date + "ALT Loan ORIG " + year + ".doc"
    dest_folder = Path("O:/UOSFA Reports/Alternative Loan Reports")

    source_file = source_folder / Path(filename)
    source_filex = Path(str(source_file) + "x")
    dest_file = dest_folder / Path(renamed)
    dest_filex = Path(str(dest_file) + "x")
    
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
    

def al_pre_outbound(test, date, year, query, renamed):

    #orig_filename = date + " ALT Loan ORIG " + year + ".doc"

    if test:
        directory = os.path.realpath('C:\Testing Bob/ALT Loans/')
        #orig_folder = Path('C:/Testing Bob/ALT Loans/')
        #orig_doc = os.path.realpath(os.path.join('C:\Testing Bob/ALT Loans/', orig_filename))
    else:
        directory = os.path.realpath('O:/Systems/QUERIES/ALT Loans/')
        #orig_folder = Path('O:/Systems/QUERIES/ALT Loans/')
        #orig_doc = os.path.realpath(os.path.join('O:/Systems/QUERIES/ALT Loans/', orig_filename))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    move_directory = "Alternative Loan Reports"

    # FORMAT: return (query, renamed, archive_directory, UOSFA_folder)
    # query: The original file name
    # renamed: The name the file should have after being moved
    # archive_directory: The folder the file will be copied to
    # UOSFA_folder: The name of the folder the renamed file should be moved to
    # - (eg. "Budget Reports", "SAP Reports", "Unknown Reports") 
    # - put "None" if it shouldn't be moved to a folder in 'O:/UOSFA Reports/'

    if query.startswith("UUFA_ALR_110_CHNG_PDG_TRANS"):
        #move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_CL_APP_RSPNS_ERR"):
        #move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LN_FA907_1_REVISE"):
        #move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LN_FA907_2_REVISE"):
        #move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LN_SENT_NO_RESP"):
        #move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LN_EFT_DETAIL_ERR"):
        #move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LN_EFT_DT_LNDR_ERR"):
        #move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LOAN_ORIG_ACAD_LVL"):
        #move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LN_ORIG_EDIT_ERR"):
        #move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LOAN_ORIG_FA_LOAD"):
        #move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LOAN_ORG_LND_NT_CK"):
        #move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LOAN_ORIG_SPLT_CDS"):
        #move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LN_ORIG_VLOAN_RSN"):
        #move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_ALR_LOAN_SPC_NEED_OVWD"):
        #move_orig(orig_filename, orig_folder, date, year)
        return (query, renamed, directory, move_directory)

    return "Empty" #Leave as final line
    