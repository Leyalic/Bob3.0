# 2nd LDR Queries 
# to be called in main

def do_2nd_ldr():
    global aid_year
    year = "18"
    for query_name in os.listdir("."):
        if query_name.startswith("UUFA_PRT_PELL_ELG_NO_PELL"):
            year = str(int(re.search(r'\d+', query_name).group()))
            break
    aid_year = "20" + str(int(year) - 1) + "-20" + str(year)
    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/Term', aid_year))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Term', aid_year))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    if ("22" in query_name.split("-")[0]):
        for query in os.listdir("."):
            if query.startswith("UUFA_CBA_UNDISBURSED"):
                do_query(query, date + " CBA Undisbursed.xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_HRS_DECREASE_ATH"):
                do_query(query, date + " Hours Decrease Athlete.xls", directory,
                         ath_mail.attachments)

            if query.startswith("UUFA_HRS_DECREASE_FC"):
                do_query(query, date + " Hours Decrease FC.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_HRS_DECREASE_SV"):
                do_query(query, date + " Hours Decrease SV.xls", directory,
                         hj_mail.attachments)

            if query.startswith("UUFA_PELL_ELIG_ENROLL_NO_AWARD"):
                do_query(query, date + " Pell Eligible Enrolled NO Award.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PELL_OFFERED_NOT_DISB"):
                do_query(query, date + " Pell Offered Not Disbursed.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PELL_DL_MATH990"):
                do_query(query, date + " Pell-DL Math 990.xls", directory,
                         kkmt_mail.attachments)

            if "PELL_DL_MATH980" in query:
                do_query(query, date + " Pell-DL Math 980.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PELL_DL_ELI575_ELI685"):
                do_query(query, date + " Pell-DL ELI0075 ELI0085.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_SF_DISB_ATH_AWD_NOPOST"):
                do_query(query, date + " Athlete Awd Disb not Posted.xls", directory,
                         ath_mail.attachments)

            if query.startswith("UUFA_SF_DISB_WAIVER_AWD_NOPOST"):
                do_query(query, date + " Waiver Awd Disb not Posted.xls", directory,
                         hj_mail.attachments)

            if query.startswith("UUFA_PRT_PELL_ELG_NO_PELL") and (year in query[:-8]) :
                do_query(query, date + " Pell Eligible No Pell 20" + year + ".xls", directory,
                         kkmt_mail.attachments)
                
    else:
        for query in os.listdir("."):
            if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if query.startswith("UUFA_CBA_UNDISBURSED"):
                    do_query(query, date + " CBA Undisbursed.xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_HRS_DECREASE_ATH"):
                    do_query(query, date + " Hours Decrease Athlete.xls", directory,
                             ath_mail.attachments)

                if query.startswith("UUFA_HRS_DECREASE_FC"):
                    do_query(query, date + " Hours Decrease FC.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_HRS_DECREASE_SV"):
                    do_query(query, date + " Hours Decrease SV.xls", directory,
                             hj_mail.attachments)

                if query.startswith("UUFA_PELL_ELIG_ENROLL_NO_AWARD"):
                    do_query(query, date + " Pell Eligible Enrolled NO Award.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PELL_OFFERED_NOT_DISB"):
                    do_query(query, date + " Pell Offered Not Disbursed.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PELL_DL_MATH990"):
                    do_query(query, date + " Pell-DL Math 990.xls", directory,
                             kkmt_mail.attachments)

                if "PELL_DL_MATH980" in query:
                    do_query(query, date + " Pell-DL Math 980.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PELL_DL_ELI575_ELI685"):
                    do_query(query, date + " Pell-DL ELI0075 ELI0085.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_SF_DISB_ATH_AWD_NOPOST"):
                    do_query(query, date + " Athlete Awd Disb not Posted.xls", directory,
                             ath_mail.attachments)

                if query.startswith("UUFA_SF_DISB_WAIVER_AWD_NOPOST"):
                    do_query(query, date + " Waiver Awd Disb not Posted.xls", directory,
                             hj_mail.attachments)

                if query.startswith("UUFA_PRT_PELL_ELG_NO_PELL") and (year in query[:-8]) :
                    do_query(query, date + " Pell Eligible No Pell 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

