# Disbursement Queries - to be modified
# to be called in main

def do_disb_queries():
    global aid_year
    year = "23"
    for query_name in os.listdir("."):
        if query_name.startswith("UUFA_DQ_AUTHORIZED_NOT_DISB"):
            if str(int(re.search(r'\d+', query_name).group())) == "22":
                year = "22"
            break
        
    aid_year = "20" + str(int(year) - 1) + "-20" + year
    disb_date = str(raw_input("Enter Date the most recent Disbursement ran in 'MM-DD-YY' format:"))
    disb_date = disb_date[:-1]
    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/Disbursement',
                                                  aid_year, month_folder))
    else:
        directory = os.path.realpath(os.path.join('O:\Systems\QUERIES\Disbursement', aid_year, month_folder))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    if ("22" in query_name.split("-")[0]):
        for query in os.listdir("."):
            if query.startswith("UUFA_DQ_AUTHORIZED_NOT_DISB") and (year in query[:-8]) :
                do_query(query, disb_date + " Item Types Authorized Not Disbursed " + year + ".xls", directory,
                         disb_mail.attachments)

            if query.startswith("UUFA_DQ_ALL_DISBURSED") and (year in query[:-8]) :
                do_query(query, disb_date + " All Item Types Disbursed " + year + ".xls", directory,
                         disb_mail.attachments)

            if query.startswith("FA_DQ_ATHLETE_RM_BD") and (year in query[:-8]) :
                do_query(query, disb_date + " Athlete Room and Board " + year + ".xls", directory,
                         disb_mail.attachments)

            if query.startswith("FA_DQ_ATH_OFF_SCHED_RM_BD") and (year in query[:-8]) :
                do_query(query, disb_date + " Athlete Off Schedule R&B " + year + ".xls", directory,
                         disb_mail.attachments)

            if ("_CASH_DISB_TOTALS") in query and (year in query[:-8]) :
                do_query(query, disb_date + " Cash Disbursement Totals " + year + ".xls", directory,
                         disb_tot_mail.attachments)

            if ("_DQ_DISB_TOTALS") in query and (year in query[:-8]) :
                do_query(query, disb_date + " Disbursement Totals " + year + ".xls", directory,
                         disb_tot_mail.attachments)

            if query.startswith("UUFA_DQ_FALL" + year) :
                do_query(query, disb_date + " DL Fall Awards 20" + year + ".xls", directory,
                         disb_mail.attachments)

            if query.startswith("UUFA_DQ_FALL_SPRING") and (year in query[:-8]) :
                do_query(query, disb_date + " DL Fall Spring Awards 20" + year + ".xls", directory,
                         disb_mail.attachments)

            if query.startswith("UUFA_DQ_DL_SUMMER") and (year in query[:-8]) :
                do_query(query, disb_date + " DL Summer Awards 20" + year + ".xls", directory,
                         disb_mail.attachments)

            if query.startswith("UUFA_DQ_SPRING") and (year in query[:-8]) :
                do_query(query, disb_date + " DL Spring Awards 20" + year + ".xls", directory,
                         disb_mail.attachments)

            if query.startswith("UUFA_DQ_UG_PLUS_REFUND_IA") and (year in query[:-8]) :
                do_query(query, disb_date + " DL UG PLUS Refund Borrower " + year + ".xls", directory,
                         sl_mail.attachments)

            if ("DQ_MISC_CARES_DISB") in query and (year in query[:-8]) :
                do_query(query, disb_date + " Misc CARES Disbursement Total " + year + ".xls", directory,
                         sl_mail.attachments)

            if ("DQ_MISC_CARES_RES_DISB") in query and (year in query[:-8]) :
                do_query(query, disb_date + " Misc CARES Resources Disb " + year + ".xls", directory,
                         sl_mail.attachments)

            if ("MISC_DISB_TOTALS") in query and (year in query[:-8]) :
                do_query(query, disb_date + " Misc Disbursement Totals " + year + ".xls", directory,
                         disb_tot_mail.attachments)

            if query.startswith("UUFA_DQ_MISC_RESOURCE_DISB") and (year in query[:-8]) :
                do_query(query, disb_date + " Misc Resources Disbursement " + year + ".xls", directory,
                         disb_mail.attachments)

            if ("NONCASH_DISB_TOTALS") in query and (year in query[:-8]) :
                do_query(query, disb_date + " Non-cash Disbursement Totals " + year + ".xls", directory,
                         disb_tot_mail.attachments)

            if query.startswith("UUFA_DQ_PELL_ACPT_GR8_DISB") and (year in query[:-8]) :
                do_query(query, disb_date + " Pell Accepted Awards Greater Disb " + year + ".xls", directory,
                         disb_mail.attachments)

            if query.startswith("UUFA_DQ_SF_ITEM_TYPE_ERROR"):
                do_query(query, disb_date + " FA SF Item Type Error " + year + ".xls", directory,
                         disb_mail.attachments)

            if query.startswith("UUFA_DQ_TEACH_GRANT" + str(int(year) - 1)):
                do_query(query, disb_date + " Teach Grant Recipients 20" + str(int(year) - 1) + ".xls", directory,
                         disb_mail.attachments)

            if query.startswith("UUFA_DQ_TEACH_GRANT") and (year in query[:-8]) :
                do_query(query, disb_date + " Teach Grant Recipients 20" + year + ".xls", directory,
                         disb_mail.attachments)
    else:
        for query in os.listdir("."):
            if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if query.startswith("UUFA_DQ_AUTHORIZED_NOT_DISB") :
                    do_query(query, disb_date + " Item Types Authorized Not Disbursed " + year + ".xls", directory,
                             disb_mail.attachments)

                if query.startswith("UUFA_DQ_ALL_DISBURSED") :
                    do_query(query, disb_date + " All Item Types Disbursed " + year + ".xls", directory,
                             disb_mail.attachments)

                if query.startswith("FA_DQ_ATHLETE_RM_BD") :
                    do_query(query, disb_date + " Athlete Room and Board " + year + ".xls", directory,
                             disb_mail.attachments)

                if query.startswith("FA_DQ_ATH_OFF_SCHED_RM_BD") :
                    do_query(query, disb_date + " Athlete Off Schedule R&B " + year + ".xls", directory,
                             disb_mail.attachments)

                if ("_CASH_DISB_TOTALS") in query :
                    do_query(query, disb_date + " Cash Disbursement Totals " + year + ".xls", directory,
                             disb_tot_mail.attachments)

                if ("_DQ_DISB_TOTALS") in query :
                    do_query(query, disb_date + " Disbursement Totals " + year + ".xls", directory,
                             disb_tot_mail.attachments)

                if query.startswith("UUFA_DQ_FALL") and "SPRING" not in query:
                    do_query(query, disb_date + " DL Fall Awards 20" + year + ".xls", directory,
                             disb_mail.attachments)

                if query.startswith("UUFA_DQ_FALL_SPRING") :
                    do_query(query, disb_date + " DL Fall Spring Awards 20" + year + ".xls", directory,
                             disb_mail.attachments)

                if query.startswith("UUFA_DQ_DL_SUMMER") :
                    do_query(query, disb_date + " DL Summer Awards 20" + year + ".xls", directory,
                             disb_mail.attachments)

                if query.startswith("UUFA_DQ_SPRING") :
                    do_query(query, disb_date + " DL Spring Awards 20" + year + ".xls", directory,
                             disb_mail.attachments)

                if query.startswith("UUFA_DQ_UG_PLUS_REFUND_IA") :
                    do_query(query, disb_date + " DL UG PLUS Refund Borrower " + year + ".xls", directory,
                             sl_mail.attachments)

                if ("DQ_MISC_CARES_DISB") in query :
                    do_query(query, disb_date + " Misc CARES Disbursement Total " + year + ".xls", directory,
                             sl_mail.attachments)

                if ("DQ_MISC_CARES_RES_DISB") in query :
                    do_query(query, disb_date + " Misc CARES Resources Disb " + year + ".xls", directory,
                             sl_mail.attachments)

                if ("MISC_DISB_TOTALS") in query :
                    do_query(query, disb_date + " Misc Disbursement Totals " + year + ".xls", directory,
                             disb_tot_mail.attachments)

                if query.startswith("UUFA_DQ_MISC_RESOURCE_DISB") :
                    do_query(query, disb_date + " Misc Resources Disbursement " + year + ".xls", directory,
                             disb_mail.attachments)

                if ("NONCASH_DISB_TOTALS") in query :
                    do_query(query, disb_date + " Non-cash Disbursement Totals " + year + ".xls", directory,
                             disb_tot_mail.attachments)

                if query.startswith("UUFA_DQ_PELL_ACPT_GR8_DISB") :
                    do_query(query, disb_date + " Pell Accepted Awards Greater Disb " + year + ".xls", directory,
                             disb_mail.attachments)

                if query.startswith("UUFA_DQ_SF_ITEM_TYPE_ERROR"):
                    do_query(query, disb_date + " FA SF Item Type Error " + year + ".xls", directory,
                             disb_mail.attachments)

                if query.startswith("UUFA_DQ_TEACH_GRANT" + str(int(year) - 1)):
                    do_query(query, disb_date + " Teach Grant Recipients 20" + str(int(year) - 1) + ".xls", directory,
                             disb_mail.attachments)

                if query.startswith("UUFA_DQ_TEACH_GRANT") :
                    do_query(query, disb_date + " Teach Grant Recipients 20" + year + ".xls", directory,
                             disb_mail.attachments)

                if query.startswith("UUFA_DQ_DISB_BREAKDOWN") :
                    do_query(query, disb_date + " Disbursement Breakdown 20" + year + ".xls", directory,
                             disb_mail.attachments)


