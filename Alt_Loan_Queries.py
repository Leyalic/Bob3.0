# Alt Loan Pre-Outbound Queries - to be modified
# to be called in main
import os
import shutil
from pathlib import Path

def move_orig(orig_doc, orig_docx, name, aid_year):
    copy_name = orig_doc
    copy_docx_name = orig_docx
    copy_directory = Path("O:/Systems/UOSFA Reports/Alternative Loan Reports")
    try:
        shutil.copy(copy_name, copy_directory)
    except FileNotFoundError as e:
        try:
            shutil.copy(copy_docx_name, copy_directory)
        except FileNotFoundError as f:
            input("\nCould not locate "+ name + "\nMake sure it is located in O:/Systems/Queries/ALT Loans/" + aid_year + "\n\nPress Enter when ready.")
    except shutil.Error:
        pass

def al_pre_outbound(test, date, year, query, aid_year_match):
    #global aid_year
    #for query_name in os.listdir("."):
    #    if query_name.startswith("UUFA_ALR_LOAN_ORG_LND_NT_CK"):
    #        year = str(int(re.search(r'\d+', query_name).group()))
    #        break
    #aid_year = "20" + str(int(year) - 1) + "-20" + year
    #skip = "n"
    aid_year = str(int(year - 1)) + "-" + str(year)
    orig_file_doc = date + " ALT Loan ORIG " + year + ".doc"
    orig_file_docx = date + " ALT Loan ORIG " + year + ".docx"

    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/ALT Loans/', aid_year))
        orig_doc = os.path.realpath(os.path.join('C:\Testing Bob/ALT Loans/', orig_file_doc))
        orig_docx = os.path.realpath(os.path.join('C:\Testing Bob/ALT Loans/', orig_file_docx))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/ALT Loans/', aid_year))
        orig_doc = os.path.realpath(os.path.join('O:/Systems/QUERIES/ALT Loans/', orig_file_doc))
        orig_docx = os.path.realpath(os.path.join('O:/Systems/QUERIES/ALT Loans/', orig_file_docx))

    # the list 'my_path' should be populated with the FOLDER variables above.
    if not os.path.isdir(directory):
        os.makedirs(directory)

    move_orig(orig_doc, orig_docx, "ALT Loan ORIG 20" + year, aid_year)

    year = year[2:]
    dot_index = query.find(".")
    dash_index = query.rfind("-")
    renamed = date + " " + query[dash_index:] + " " + year + query[:dot_index]

    move_directory = "Alternative Loan Reports"

    toggle = True

    # Change File_Name to be file as it is received and _new_file_name to what
    # the new file should be.  Prefix date
    # will be added.
    if aid_year_match:
    #if ("22" in query_name.split("-")[0]):
        if True:
        #for query in os.listdir("."):
            if query.startswith("UUFA_ALR_110_CHNG_PDG_TRANS"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_ALR_CL_APP_RSPNS_ERR"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_ALR_LN_FA907_1_REVISE"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_ALR_LN_FA907_2_REVISE"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_ALR_LN_SENT_NO_RESP"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_ALR_LN_EFT_DETAIL_ERR"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_ALR_LN_EFT_DT_LNDR_ERR"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_ALR_LOAN_ORIG_ACAD_LVL") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_ALR_LN_ORIG_EDIT_ERR"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_ALR_LOAN_ORIG_FA_LOAD") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_ALR_LOAN_ORG_LND_NT_CK") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_ALR_LOAN_ORIG_SPLT_CDS") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_ALR_LN_ORIG_VLOAN_RSN"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_ALR_LOAN_SPC_NEED_OVWD") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)
    else:
        if True:
        #for query in os.listdir("."):
            if toggle:
            #if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if query.startswith("UUFA_ALR_110_CHNG_PDG_TRANS"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_ALR_CL_APP_RSPNS_ERR"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_ALR_LN_FA907_1_REVISE"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_ALR_LN_FA907_2_REVISE"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_ALR_LN_SENT_NO_RESP"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_ALR_LN_EFT_DETAIL_ERR"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_ALR_LN_EFT_DT_LNDR_ERR"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_ALR_LOAN_ORIG_ACAD_LVL") :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_ALR_LN_ORIG_EDIT_ERR"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_ALR_LOAN_ORIG_FA_LOAD") :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_ALR_LOAN_ORG_LND_NT_CK") :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_ALR_LOAN_ORIG_SPLT_CDS") :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_ALR_LN_ORIG_VLOAN_RSN"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_ALR_LOAN_SPC_NEED_OVWD") :
                    return (query, renamed, directory, move_directory)

    #if not test:
    #    while True:
    #        if os.path.isfile(orig_doc):
    #            alt_mail.attachments.append(orig_doc)
    #            break
    #        if os.path.isfile(orig_docx):
    #            alt_mail.attachments.append(orig_docx)
    #            break
    #        if str.capitalize(skip) == "Y":
    #            break
    #        else:
    #            skip = raw_input("\nCould not locate ALT Loan ORIG 20" + year + ".doc\nMake sure it is located in O:/Systems/Queries/ALT Loans/" + aid_year + "\n\nPress Enter when ready.")
