# Alt Loan Pre-Outbound Queries - to be modified
# to be called in main

def al_pre_outbound():
    global aid_year
    for query_name in os.listdir("."):
        if query_name.startswith("UUFA_ALR_LOAN_ORG_LND_NT_CK"):
            year = str(int(re.search(r'\d+', query_name).group()))
            break
    aid_year = "20" + str(int(year) - 1) + "-20" + year
    skip = "n"
    orig_file_doc = date + " ALT Loan ORIG " + year + ".doc"
    orig_file_docx = date + " ALT Loan ORIG " + year + ".docx"

    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/ALT Loans/'))
        orig_doc = os.path.realpath(os.path.join('C:\Testing Bob/ALT Loans/', orig_file_doc))
        orig_docx = os.path.realpath(os.path.join('C:\Testing Bob/ALT Loans/', orig_file_docx))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/ALT Loans/'))
        orig_doc = os.path.realpath(os.path.join('O:/Systems/QUERIES/ALT Loans/', orig_file_doc))
        orig_docx = os.path.realpath(os.path.join('O:/Systems/QUERIES/ALT Loans/', orig_file_docx))

    # the list 'my_path' should be populated with the FOLDER variables above.
    if not os.path.isdir(directory):
        os.makedirs(directory)

    # Change File_Name to be file as it is received and _new_file_name to what
    # the new file should be.  Prefix date
    # will be added.
    if ("22" in query_name.split("-")[0]):
        for query in os.listdir("."):
            if query.startswith("UUFA_ALR_110_CHNG_PDG_TRANS"):
                do_query(query, date + " Loan Pending Change Transactions.xls", directory,
                         alt_mail.attachments)

            if query.startswith("UUFA_ALR_CL_APP_RSPNS_ERR"):
                do_query(query, date + " CL Response Load Errors.xls", directory,
                         alt_mail.attachments)

            if query.startswith("UUFA_ALR_LN_FA907_1_REVISE"):
                do_query(query, date + " Loan Disbursed Report " + year + ".xls", directory,
                         alt_mail.attachments)

            if query.startswith("UUFA_ALR_LN_FA907_2_REVISE"):
                do_query(query, date + " CLoan Not Disbursed Report " + year + ".xls", directory,
                         alt_mail.attachments)

            if query.startswith("UUFA_ALR_LN_SENT_NO_RESP"):
                do_query(query, date + " CLoan Sent No Response " + year + ".xls", directory,
                         alt_mail.attachments)

            if query.startswith("UUFA_ALR_LN_EFT_DETAIL_ERR"):
                do_query(query, date + " Loans EFT Detail Error.xls", directory,
                         alt_mail.attachments)

            if query.startswith("UUFA_ALR_LN_EFT_DT_LNDR_ERR"):
                do_query(query, date + " Loan EFT Date Lender Errors.xls", directory,
                         alt_mail.attachments)

            if query.startswith("UUFA_ALR_LOAN_ORIG_ACAD_LVL") and (year in query[:-8]) :
                do_query(query, date + " Loans Academic Level " + year + ".xls", directory,
                         alt_mail.attachments)

            if query.startswith("UUFA_ALR_LN_ORIG_EDIT_ERR"):
                do_query(query, date + " Loan Originate Edit Errors.xls", directory,
                         alt_mail.attachments)

            if query.startswith("UUFA_ALR_LOAN_ORIG_FA_LOAD") and (year in query[:-8]) :
                do_query(query, date + " Loan ORIG FA Load " + year + ".xls", directory,
                         alt_mail.attachments)

            if query.startswith("UUFA_ALR_LOAN_ORG_LND_NT_CK") and (year in query[:-8]) :
                do_query(query, date + " Loan ORIG Lender Note " + year + ".xls", directory,
                         alt_mail.attachments)

            if query.startswith("UUFA_ALR_LOAN_ORIG_SPLT_CDS") and (year in query[:-8]) :
                do_query(query, date + " Loan ORIG Split Codes " + year + ".xls", directory,
                         alt_mail.attachments)

            if query.startswith("UUFA_ALR_LN_ORIG_VLOAN_RSN"):
                do_query(query, date + " Loan ORIG VLOAN Reasons.xls", directory,
                         alt_mail.attachments)

            if query.startswith("UUFA_ALR_LOAN_SPC_NEED_OVWD") and (year in query[:-8]) :
                do_query(query, date + " Loan Overaward Special Need " + year + ".xls", directory,
                         alt_mail.attachments)
    else:
        for query in os.listdir("."):
            if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if query.startswith("UUFA_ALR_110_CHNG_PDG_TRANS"):
                    do_query(query, date + " Loan Pending Change Transactions.xls", directory,
                             alt_mail.attachments)

                if query.startswith("UUFA_ALR_CL_APP_RSPNS_ERR"):
                    do_query(query, date + " CL Response Load Errors.xls", directory,
                             alt_mail.attachments)

                if query.startswith("UUFA_ALR_LN_FA907_1_REVISE"):
                    do_query(query, date + " Loan Disbursed Report " + year + ".xls", directory,
                             alt_mail.attachments)

                if query.startswith("UUFA_ALR_LN_FA907_2_REVISE"):
                    do_query(query, date + " CLoan Not Disbursed Report " + year + ".xls", directory,
                             alt_mail.attachments)

                if query.startswith("UUFA_ALR_LN_SENT_NO_RESP"):
                    do_query(query, date + " CLoan Sent No Response " + year + ".xls", directory,
                             alt_mail.attachments)

                if query.startswith("UUFA_ALR_LN_EFT_DETAIL_ERR"):
                    do_query(query, date + " Loans EFT Detail Error.xls", directory,
                             alt_mail.attachments)

                if query.startswith("UUFA_ALR_LN_EFT_DT_LNDR_ERR"):
                    do_query(query, date + " Loan EFT Date Lender Errors.xls", directory,
                             alt_mail.attachments)

                if query.startswith("UUFA_ALR_LOAN_ORIG_ACAD_LVL") :
                    do_query(query, date + " Loans Academic Level " + year + ".xls", directory,
                             alt_mail.attachments)

                if query.startswith("UUFA_ALR_LN_ORIG_EDIT_ERR"):
                    do_query(query, date + " Loan Originate Edit Errors.xls", directory,
                             alt_mail.attachments)

                if query.startswith("UUFA_ALR_LOAN_ORIG_FA_LOAD") :
                    do_query(query, date + " Loan ORIG FA Load " + year + ".xls", directory,
                             alt_mail.attachments)

                if query.startswith("UUFA_ALR_LOAN_ORG_LND_NT_CK") :
                    do_query(query, date + " Loan ORIG Lender Note " + year + ".xls", directory,
                             alt_mail.attachments)

                if query.startswith("UUFA_ALR_LOAN_ORIG_SPLT_CDS") :
                    do_query(query, date + " Loan ORIG Split Codes " + year + ".xls", directory,
                             alt_mail.attachments)

                if query.startswith("UUFA_ALR_LN_ORIG_VLOAN_RSN"):
                    do_query(query, date + " Loan ORIG VLOAN Reasons.xls", directory,
                             alt_mail.attachments)

                if query.startswith("UUFA_ALR_LOAN_SPC_NEED_OVWD") :
                    do_query(query, date + " Loan Overaward Special Need " + year + ".xls", directory,
                             alt_mail.attachments)

    if not test:
        while True:
            if os.path.isfile(orig_doc):
                alt_mail.attachments.append(orig_doc)
                break
            if os.path.isfile(orig_docx):
                alt_mail.attachments.append(orig_docx)
                break
            if str.capitalize(skip) == "Y":
                break
            else:
                skip = raw_input("\nCould not locate ALT Loan ORIG 20" + year + ".doc\nMake sure it is located in O:/Systems/Queries/ALT Loans/" + aid_year + "\n\nPress Enter when ready.")
