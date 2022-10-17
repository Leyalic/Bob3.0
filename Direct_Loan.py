# Direct Loan Pre-Outbound Queries - to be modified
# to be called in main

def dl_pre_outbound():
    global aid_year
    year = '17'
    for query_name in os.listdir("."):
        if "DLR_LOAN_ORIG_EDIT_ERR" in query_name:
            year = str(int(re.search(r'\d+', query_name).group()))
            break
    aid_year = "20" + str(int(year) - 1) + "-20" + year
    orig_file_doc = date + " DL ORIG 20" + year + ".doc"
    orig_file_doc_2 = date + " DL ORIG 20" + year + " (2).doc"
    orig_file_docx = date + " DL ORIG 20" + year + ".docx"
    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/Direct Loans', 'DL Pre-Outbound'))
        orig_doc = os.path.realpath(os.path.join('C:\Testing Bob\Direct Loans', 'Origination', orig_file_doc))
        orig_docx = os.path.realpath(os.path.join('C:\Testing Bob\Direct Loans', 'Origination', orig_file_docx))

    else:
        directory = os.path.realpath(os.path.join('O:/Systems/Direct Loans', 'DL Pre-Outbound'))
        orig_doc = os.path.realpath(os.path.join('O:/Systems/Direct Loans', 'Origination', orig_file_doc))
        orig_doc_2 = os.path.realpath(os.path.join('O:/Systems/Direct Loans', 'Origination', orig_file_doc_2))
        orig_docx = os.path.realpath(os.path.join('O:/Systems/Direct Loans', 'Origination', orig_file_docx))

    # the list 'my_path' should be populated with the FOLDER variables above.
    if not os.path.isdir(directory):
        os.makedirs(directory)

    # Change File_Name to be file as it is received and _new_file_name to what
    # the new file should be.  Prefix date
    # will be added.
    if ("22" in query_name.split("-")[0]):
        for query in os.listdir("."):
            if query.startswith("UUFA_DLR_ORIG_TRNS_PEND") and (year in query[:-8]) :
                do_query(query, date + " DL Orig-Trans Pending " + year + ".xls", directory,
                         dl_mail.attachments)

            if query.startswith("UUFA_DLR_ENTRANCE_COUNSEL") and (year in query[:-8]) :
                do_query(query, date + " DL Entrance Counseling I  " + year + ".xls", directory,
                         dl_mail.attachments)

            if query.startswith("UUFA_DLR_LOAN_EFT_DT_LNDR_ERR"):
                do_query(query, date + " Loan EFT Date Lender Error.xls", directory,
                         dl_mail.attachments)

            if query.startswith("UUFA_DLR_LOAN_ORIG_FA_LOAD"):
                do_query(query, date + " DL ORIG FA Load " + year + ".xls", directory,
                         dl_mail.attachments)

            if query.startswith("UUFA_DLR_LOAN_NO_NSLDS") and (year in query[:-8]) :
                do_query(query, date + " Loan No NSLDS " + year + ".xls", directory,
                         dl_mail.attachments)

            if query.startswith("UUFA_DLR_LOAN_ORIG_ACAD_LVL") and (year in query[:-8]) :
                do_query(query, date + " Loans Academic Level " + year + ".xls", directory,
                         dl_mail.attachments)

            if query.startswith("UUFA_DLR_LOAN_ORIG_EDIT_ERR"):
                do_query(query, date + " Loan Originate Edit Errors.xls", directory,
                         dl_mail.attachments)

            if query.startswith("UUFA_DLR_LOAN_ORIG_SPLT_CDS") and (year in query[:-8]) :
                do_query(query, date + " Loan Split Codes " + year + ".xls", directory,
                         dl_mail.attachments)

            if "LN_ORIG_VLOAN_RSN" in query and (year in query[:-8]) :
                do_query(query, date + " Loan ORIG VLOAN Reasons.xls", directory,
                         dl_mail.attachments)

            if query.startswith("UUFA_DLR_LOAN_SPC_NEED_OVWD") and (year in query[:-8]) :
                do_query(query, date + " Loan Overaward Special Need " + year + ".xls", directory,
                         dl_mail.attachments)

            if "DLR_LN_ACPT_STAF_31_32" in query and year in query[:-8] :
                do_query(query, date + " Stafford Accept Offer " + year + ".xls", directory,
                         dl_mail.attachments)

            if query.startswith("UUFA_DLR_NOT_DISB") and (year in query[:-8]) :
                do_query(query, date + " DL Disb Errors " + year + ".xls", directory,
                         dl_mail.attachments)

            if query.startswith("UUFA_DLR_NOT_DISBURSED") and (year in query[:-8]) :
                do_query(query, date + " DL Disbursement Errors " + year + "(Old).xls", directory,
                         dl_mail.attachments)

            if query.startswith("UUFA_DLR_NOT_DISBURSED_20") and (year in query[:-8]) :
                do_query(query, date + " DL Disbursement Errors " + year + ".xls", directory,
                         dl_mail.attachments)

            if query.startswith("UUFA_DLR_UG_PLUS_REFND_IND"):
                do_query(query, date + " DL UG PLUS Refund Indicator.xls", directory,
                         dl_mail.attachments)
                
    else:
        for query in os.listdir("."):
            if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if query.startswith("UUFA_DLR_ORIG_TRNS_PEND") :
                    do_query(query, date + " DL Orig-Trans Pending " + year + ".xls", directory,
                             dl_mail.attachments)

                if query.startswith("UUFA_DLR_ENTRANCE_COUNSEL") :
                    do_query(query, date + " DL Entrance Counseling I  " + year + ".xls", directory,
                             dl_mail.attachments)

                if query.startswith("UUFA_DLR_LOAN_EFT_DT_LNDR_ERR"):
                    do_query(query, date + " Loan EFT Date Lender Error.xls", directory,
                             dl_mail.attachments)

                if query.startswith("UUFA_DLR_LOAN_ORIG_FA_LOAD"):
                    do_query(query, date + " DL ORIG FA Load " + year + ".xls", directory,
                             dl_mail.attachments)

                if query.startswith("UUFA_DLR_LOAN_NO_NSLDS") :
                    do_query(query, date + " Loan No NSLDS " + year + ".xls", directory,
                             dl_mail.attachments)

                if query.startswith("UUFA_DLR_LOAN_ORIG_ACAD_LVL") :
                    do_query(query, date + " Loans Academic Level " + year + ".xls", directory,
                             dl_mail.attachments)

                if query.startswith("UUFA_DLR_LOAN_ORIG_EDIT_ERR"):
                    do_query(query, date + " Loan Originate Edit Errors.xls", directory,
                             dl_mail.attachments)

                if query.startswith("UUFA_DLR_LOAN_ORIG_SPLT_CDS") :
                    do_query(query, date + " Loan Split Codes " + year + ".xls", directory,
                             dl_mail.attachments)

                if "LN_ORIG_VLOAN_RSN" in query :
                    do_query(query, date + " Loan ORIG VLOAN Reasons.xls", directory,
                             dl_mail.attachments)

                if query.startswith("UUFA_DLR_LOAN_SPC_NEED_OVWD") :
                    do_query(query, date + " Loan Overaward Special Need " + year + ".xls", directory,
                             dl_mail.attachments)

                if "DLR_LN_ACPT_STAF_31_32" in query and year in query[:-8] :
                    do_query(query, date + " Stafford Accept Offer " + year + ".xls", directory,
                             dl_mail.attachments)

                if query.startswith("UUFA_DLR_NOT_DISB") :
                    do_query(query, date + " DL Disb Errors " + year + ".xls", directory,
                             dl_mail.attachments)

                if query.startswith("UUFA_DLR_NOT_DISBURSED") :
                    do_query(query, date + " DL Disbursement Errors " + year + "(Old).xls", directory,
                             dl_mail.attachments)

                if query.startswith("UUFA_DLR_NOT_DISBURSED_20") :
                    do_query(query, date + " DL Disbursement Errors " + year + ".xls", directory,
                             dl_mail.attachments)

                if query.startswith("UUFA_DLR_UG_PLUS_REFND_IND"):
                    do_query(query, date + " DL UG PLUS Refund Indicator.xls", directory,
                             dl_mail.attachments)

    if not test:
        while True:
            if os.path.isfile(orig_doc):
                dl_mail.attachments.append(orig_doc)
                if os.path.isfile(orig_doc_2):
                    dl_mail.attachments.append(orig_doc_2)
                break
            if os.path.isfile(orig_docx):
                dl_mail.attachments.append(orig_docx)
                if os.path.isfile(orig_doc_2):
                    dl_mail.attachments.append(orig_doc_2)
                break
            else:
                raw_input("\nCould not locate DL ORIG 20" + year + ".doc\nMake sure it is located in O:/Systems/Direct Loans/Origination\n\nPress Enter when ready.")

