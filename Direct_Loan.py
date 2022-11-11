# Direct Loan Pre-Outbound Queries - to be modified
# to be called in main
import os
import shutil
from pathlib import Path

def move_orig(orig_doc, orig_doc_2, orig_docx, name):
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
    

def dl_pre_outbound(test, date, year, query, renamed, aid_year_match):
    #global aid_year
    #year = '17'
    #for query_name in os.listdir("."):
    #    if "DLR_LOAN_ORIG_EDIT_ERR" in query_name:
    #        year = str(int(re.search(r'\d+', query_name).group()))
    #        break
    #aid_year = "20" + str(int(year) - 1) + "-20" + year

    orig_file_doc = date + " DL ORIG " + year + ".doc"
    orig_file_doc_2 = date + " DL ORIG " + year + " (2).doc"
    orig_file_docx = date + " DL ORIG " + year + ".docx"
    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/Direct Loans', 'DL Pre-Outbound'))
        orig_doc = os.path.realpath(os.path.join('C:\Testing Bob\Direct Loans', 'Origination', orig_file_doc))
        orig_doc_2 = os.path.realpath(os.path.join('C:\Testing Bob\Direct Loans', 'Origination', orig_file_doc_2))
        orig_docx = os.path.realpath(os.path.join('C:\Testing Bob\Direct Loans', 'Origination', orig_file_docx))

    else:
        directory = os.path.realpath(os.path.join('O:/Systems/Direct Loans', 'DL Pre-Outbound'))
        orig_doc = os.path.realpath(os.path.join('O:/Systems/Direct Loans', 'Origination', orig_file_doc))
        orig_doc_2 = os.path.realpath(os.path.join('O:/Systems/Direct Loans', 'Origination', orig_file_doc_2))
        orig_docx = os.path.realpath(os.path.join('O:/Systems/Direct Loans', 'Origination', orig_file_docx))

    # the list 'my_path' should be populated with the FOLDER variables above.
    if not os.path.isdir(directory):
        os.makedirs(directory)


    year = year[2:]

    move_directory = "Direct Loan Reports"

    toggle = True

    # Change File_Name to be file as it is received and _new_file_name to what
    # the new file should be.  Prefix date
    # will be added.
    if aid_year_match:
    #if ("22" in query_name.split("-")[0]):
        if True:
        #for query in os.listdir("."):
            if query.startswith("UUFA_DLR_ORIG_TRNS_PEND") and (year in query[:-8]) :
                move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DLR_ENTRANCE_COUNSEL") and (year in query[:-8]) :
                move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DLR_LOAN_EFT_DT_LNDR_ERR"):
                move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DLR_LOAN_ORIG_FA_LOAD"):
                move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DLR_LOAN_NO_NSLDS") and (year in query[:-8]) :
                move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DLR_LOAN_ORIG_ACAD_LVL") and (year in query[:-8]) :
                move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DLR_LOAN_ORIG_EDIT_ERR"):
                move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DLR_LOAN_ORIG_SPLT_CDS") and (year in query[:-8]) :
                move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                return (query, renamed, directory, move_directory)

            if "LN_ORIG_VLOAN_RSN" in query and (year in query[:-8]) :
                move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DLR_LOAN_SPC_NEED_OVWD") and (year in query[:-8]) :
                move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                return (query, renamed, directory, move_directory)

            if "DLR_LN_ACPT_STAF_31_32" in query and year in query[:-8] :
                move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DLR_NOT_DISB") and (year in query[:-8]) :
                move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DLR_NOT_DISBURSED") and (year in query[:-8]) :
                move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DLR_NOT_DISBURSED_20") and (year in query[:-8]) :
                move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DLR_UG_PLUS_REFND_IND"):
                move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                return (query, renamed, directory, move_directory)
                
    else:
        if True:
        #for query in os.listdir("."):
            if toggle:
            #if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if query.startswith("UUFA_DLR_ORIG_TRNS_PEND") :
                    move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DLR_ENTRANCE_COUNSEL") :
                    move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DLR_LOAN_EFT_DT_LNDR_ERR"):
                    move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DLR_LOAN_ORIG_FA_LOAD"):
                    move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DLR_LOAN_NO_NSLDS") :
                    move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DLR_LOAN_ORIG_ACAD_LVL") :
                    move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DLR_LOAN_ORIG_EDIT_ERR"):
                    move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DLR_LOAN_ORIG_SPLT_CDS") :
                    move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                    return (query, renamed, directory, move_directory)

                if "LN_ORIG_VLOAN_RSN" in query :
                    move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DLR_LOAN_SPC_NEED_OVWD") :
                    move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                    return (query, renamed, directory, move_directory)

                if "DLR_LN_ACPT_STAF_31_32" in query and year in query[:-8] :
                    move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DLR_NOT_DISB") :
                    move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DLR_NOT_DISBURSED") :
                    move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DLR_NOT_DISBURSED_20") :
                    move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DLR_UG_PLUS_REFND_IND"):
                    move_orig(orig_doc, orig_doc_2, orig_docx, "DL ORIG 20" + year)
                    return (query, renamed, directory, move_directory)
    return "Empty"

    #if not test:
    #    while True:
    #        if os.path.isfile(orig_doc):
    #            dl_mail.attachments.append(orig_doc)
    #            if os.path.isfile(orig_doc_2):
    #                dl_mail.attachments.append(orig_doc_2)
    #            break
    #        if os.path.isfile(orig_docx):
    #            dl_mail.attachments.append(orig_docx)
    #            if os.path.isfile(orig_doc_2):
    #                dl_mail.attachments.append(orig_doc_2)
    #            break
    #        else:
    #            raw_input("\nCould not locate DL ORIG 20" + year + ".doc\nMake sure it is located in O:/Systems/Direct Loans/Origination\n\nPress Enter when ready.")

