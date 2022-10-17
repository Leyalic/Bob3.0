# After Repackaging Queries - to be modified
# to be called in main

def do_after_repackaging():
    global aid_year
    strm = "no STRM found"
    prompt = "What STRM is this for? (ex. 1154 = Spring 2015:"
    aid_year = "not defined"
    for query_name in os.listdir("."):
        if query_name.startswith("UUFA_AP"):
            while True:
                strm = raw_input(prompt)
                if len(strm) == 5 and (0 / int(strm) == 0):
                    break
                else:
                    print ("\nOnly STRMs in the form of 1(year)4/6/8 are acceptable.")
            if strm[-1] == "8":
                aid_year = "20" + str(strm[1:3]) + "-20" + str(int(strm[1:3]) + 1)
                break
            else:
                aid_year = "20" + str(int(strm[1:3]) - 1) + "-20" + str(strm[1:3])
                break

    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/Pell Repackaging', aid_year))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Pell Repackaging', aid_year))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    year = aid_year[7:]

    for query in os.listdir("."):
        # Pell Repackaging Queries
        if query.startswith("UUFA_AP_RPKG_5TH_YR_2ND_BACH"):
            do_query(query, date + " UG 5th YR 2ND Bachelor.xls", directory,
                     kkmt_mail.attachments)

        if query.startswith("UUFA_AP_RPKG_ACTN"):
            do_query(query, date + " Pell Award Activity.xls", directory,
                     kkmt_mail.attachments)

        if query.startswith("UUFA_AP_RPKG_AWACT_C"):
            do_query(query, date + " Pell Awards Cancelled.xls", directory,
                     kkmt_mail.attachments)

        if query.startswith("UUFA_AP_RPKG_AW_ACT"):
            do_query(query, date + " Pell Repackage Activity.xls", directory,
                     v_mail.attachments)

        if query.startswith("UUFA_AP_RPKG_FPEL_AWARD_LCK"):
            do_query(query, date + " Pell Award Lock FPEL" + year + ".xls", directory,
                     kkmt_mail.attachments)

        if query.startswith("UUFA_AP_RPKG_PLAN_ID_BLANK"):
            do_query(query, date + " Pell Repackaging Plan ID Blank.xls", directory,
                     v_mail.attachments)

        if query.startswith("UUFA_AP_RPKG_RPKG_SNAPSHOT"):
            do_query(query, date + " Pell Repackage Snapshot.xls", directory,
                     null_mail.attachments)

        if query.startswith("UUFA_AP_RPKG_SAP_HOLD_DELETED"):
            do_query(query, date + " Pell SAP Holds.xls", directory,
                     kkmt_mail.attachments)

        if query.startswith("UUFA_AP_RPKG_SKIP"):
            do_query(query, date + " Pell Repackage Skip.xls", directory,
                     ml_mail.attachments)

        if query.startswith("UUFA_AP_RPKG_TERM_FT"):
            do_query(query, date + " Term Pell Awards FT.xls", directory,
                     kkmt_mail.attachments)

        if query.startswith("UUFA_AP_RPKG_TERM_HT"):
            do_query(query, date + " Term Pell Awards HT.xls", directory,
                     kkmt_mail.attachments)

        if query.startswith("UUFA_AP_RPKG_TERM_LH"):
            do_query(query, date + " Term Pell Awards LH.xls", directory,
                     kkmt_mail.attachments)

        if query.startswith("UUFA_AP_RPKG_TERM_NL"):
            do_query(query, date + " Term Pell Awards NL.xls", directory,
                     kkmt_mail.attachments)

        if query.startswith("UUFA_AP_RPKG_TERM_TQ"):
            do_query(query, date + " Term Pell Awards TQ.xls", directory,
                     kkmt_mail.attachments)

