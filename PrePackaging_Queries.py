# Pre-Repackaging Queries - to be modified
# to be called in main

def do_pre_repackaging():
    global aid_year
    strm = "no STRM found"
    prompt = "What STRM is this for? (ex. 1154 = Spring 2015:"
    aid_year = "not defined"
    for query_name in os.listdir("."):
        if query_name.startswith("UUFA_PP"):
            while True:
                strm = raw_input(prompt)
                if (len(strm) == 5) and ((0 / int(strm) == 0)):
                    break
                else:
                    print ("\nOnly STRMs in the form of 1(year)4/6/8 are acceptable. Ex: 1168 is Fall of 16.")
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

    if ("22" in query_name.split("-")[0]):
        for query in os.listdir("."):
            # Pre-Pell Repackaging Queries
            if query.startswith("UUFA_PP_RPKG_AGGREGATE_LIMITS"):
                do_query(query, date + " Pell AGG Limits Awards Reduced.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PP_RPKG_AWD_AY_NO_BDGT"):
                do_query(query, date + " Pell Award  AY One STRM Budget.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PP_RPKG_AWD_STRM_INACTIVE"):
                do_query(query, date + " Pell Award STRM Inactive.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PP_RPKG_AWRD_LOCK"):
                do_query(query, date + " Pell Award Lock No FPEL.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PP_RPKG_COA_DOUBLE"):
                do_query(query, date + " Pell COA Double.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PP_RPKG_LTHT_PELL_COA"):
                do_query(query, date + " Pell COA LTHT.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PP_RPKG_RPKG_NO_BUDGET"):
                do_query(query, date + " Pell Repackaging No Budget.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PP_RPKG_RPKG_SNAPSHOT"):
                do_query(query, date + " Pell Repackage Snapshot.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_PP_RPKG_TOTAL_WDRN_DRP"):
                do_query(query, date + " Pell Total Withdrawn Drop.xls", directory,
                         kkmt_mail.attachments)
                
            if query.startswith("UUFA_READY_REPACKAGE"):
                    do_query(query, date + " Ready Repackage.xls", directory,
                             null_mail.attachments)
    else:
        for query in os.listdir("."):
            if("22" not in query_name.split("-")[0]):
                # Pre-Pell Repackaging Queries
                if query.startswith("UUFA_PP_RPKG_AGGREGATE_LIMITS"):
                    do_query(query, date + " Pell AGG Limits Awards Reduced.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PP_RPKG_AWD_AY_NO_BDGT"):
                    do_query(query, date + " Pell Award  AY One STRM Budget.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PP_RPKG_AWD_STRM_INACTIVE"):
                    do_query(query, date + " Pell Award STRM Inactive.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PP_RPKG_AWRD_LOCK"):
                    do_query(query, date + " Pell Award Lock No FPEL.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PP_RPKG_COA_DOUBLE"):
                    do_query(query, date + " Pell COA Double.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PP_RPKG_LTHT_PELL_COA"):
                    do_query(query, date + " Pell COA LTHT.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PP_RPKG_RPKG_NO_BUDGET"):
                    do_query(query, date + " Pell Repackaging No Budget.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PP_RPKG_RPKG_SNAPSHOT"):
                    do_query(query, date + " Pell Repackage Snapshot.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_PP_RPKG_TOTAL_WDRN_DRP"):
                    do_query(query, date + " Pell Total Withdrawn Drop.xls", directory,
                             kkmt_mail.attachments)
                    
                if query.startswith("UUFA_READY_REPACKAGE"):
                    do_query(query, date + " Ready Repackage.xls", directory,
                             null_mail.attachments)
