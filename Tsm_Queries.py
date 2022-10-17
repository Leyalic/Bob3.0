# TSM Queries - to be modified      
# to be called in main

def do_tsm_queries():
    global aid_year
    year = "19"
    for query_name in os.listdir("."):
        if "_NSLDS" in query_name:
            year = str(int(re.search(r'\d+', query_name).group()))
            break
    aid_year = "20" + str(int(year) - 1) + "-20" + year

    if test:
        directory = os.path.realpath(os.path.join('C:/QUERIES/TSM/NSLDS TSM Request'))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/TSM/NSLDS TSM Request'))

    # the list 'my_path' should be populated with the FOLDER variables above.
    if not os.path.isdir(directory):
        os.makedirs(directory)

    # Change File_Name to be file as it is received and _new_file_name to what
    # the new file should be.  Prefix date
    # will be added.
    if ("22" in query_name.split("-")[0]):
        for query in os.listdir("."):
            if ("NSLDS_REQUEST_DN" in query) and (year in query[:-8]) :
                do_query(query, date + " NSLDS Request DN " + year + ".xls", directory,
                         null_mail.attachments)

            if ("NSLDS_REQUEST_GR" in query) and (year in query[:-8]) :
                do_query(query, date + " NSLDS Request DN " + year + ".xls", directory,
                         null_mail.attachments)

            if ("NSLDS_REQUEST_LW" in query) and (year in query[:-8]) :
                do_query(query, date + " NSLDS Request DN " + year + ".xls", directory,
                         null_mail.attachments)

            if ("NSLDS_REQUEST_MD" in query) and (year in query[:-8]) :
                do_query(query, date + " NSLDS Request DN " + year + ".xls", directory,
                         null_mail.attachments)

            if ("NSLDS_REQUEST_UG" in query) and (year in query[:-8]) :
                do_query(query, date + " NSLDS Request DN " + year + ".xls", directory,
                         null_mail.attachments)

            if ("_NSLDS_VAR_FLAG9_DN" in query) and (year in query[:-8]) :
                do_query(query, date + " NSLDS Var Flag9 DN " + year + ".xls", directory,
                         null_mail.attachments)

            if ("_NSLDS_VAR_FLAG9_GR" in query) and (year in query[:-8]) :
                do_query(query, date + " NSLDS Var Flag9 GR " + year + ".xls", directory,
                         null_mail.attachments)

            if ("_NSLDS_VAR_FLAG9_LW" in query) and (year in query[:-8]) :
                do_query(query, date + " NSLDS Var Flag9 LW " + year + ".xls", directory,
                         null_mail.attachments)

            if ("_NSLDS_VAR_FLAG9_MD" in query) and (year in query[:-8]) :
                do_query(query, date + " NSLDS Var Flag9 MD " + year + ".xls", directory,
                         null_mail.attachments)

            if ("_NSLDS_VAR_FLAG9_UG" in query) and (year in query[:-8]) :
                do_query(query, date + " NSLDS Var Flag9 UG " + year + ".xls", directory,
                         null_mail.attachments)
    else:
        for query in os.listdir("."):
            if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if ("NSLDS_REQUEST_DN" in query) :
                    do_query(query, date + " NSLDS Request DN " + year + ".xls", directory,
                             null_mail.attachments)

                if ("NSLDS_REQUEST_GR" in query) :
                    do_query(query, date + " NSLDS Request GR " + year + ".xls", directory,
                             null_mail.attachments)

                if ("NSLDS_REQUEST_LW" in query) :
                    do_query(query, date + " NSLDS Request LW " + year + ".xls", directory,
                             null_mail.attachments)

                if ("NSLDS_REQUEST_MD" in query) :
                    do_query(query, date + " NSLDS Request MD " + year + ".xls", directory,
                             null_mail.attachments)

                if ("NSLDS_REQUEST_UG" in query) :
                    do_query(query, date + " NSLDS Request UG " + year + ".xls", directory,
                             null_mail.attachments)

                if ("_NSLDS_VAR_FLAG9_DN" in query) :
                    do_query(query, date + " NSLDS Var Flag9 DN " + year + ".xls", directory,
                             null_mail.attachments)

                if ("_NSLDS_VAR_FLAG9_GR" in query) :
                    do_query(query, date + " NSLDS Var Flag9 GR " + year + ".xls", directory,
                             null_mail.attachments)

                if ("_NSLDS_VAR_FLAG9_LW" in query) :
                    do_query(query, date + " NSLDS Var Flag9 LW " + year + ".xls", directory,
                             null_mail.attachments)

                if ("_NSLDS_VAR_FLAG9_MD" in query) :
                    do_query(query, date + " NSLDS Var Flag9 MD " + year + ".xls", directory,
                             null_mail.attachments)

                if ("_NSLDS_VAR_FLAG9_UG" in query) :
                    do_query(query, date + " NSLDS Var Flag9 UG " + year + ".xls", directory,
                             null_mail.attachments)

