# Daily Scholarships Queries - to be modified
# to be called in main

def do_daily_scholarships():
    year = "23"
    for query_name in os.listdir("."):
        if query_name.startswith("UUFA_SCHOLAR_DISB_ZERO"):
            year = str(int(re.search(r'\d+', query_name).group()))
            break
    aid_year = "20" + str(int(year) - 1) + "-20" + year

    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob', aid_year + ' Scholar\Queries'))
    else:
        directory = os.path.realpath(os.path.join('O:\Systems', aid_year + ' Scholar\Queries'))

    # the list 'my_path' should be populated with the FOLDER variables above.
    if not os.path.isdir(directory):
        os.makedirs(directory)

    # Change File_Name to be file as it is received and _new_file_name to what
    # the new file should be.  Prefix date
    # will be added.
    for query in os.listdir("."):
        if query.startswith("UUFA_SCHOLAR_DISB_ZERO") :
            do_query(query, date + " Scholarships awarded not disbursed " + year + ".xls", directory,
                     ss_mail.attachments)

        if query.startswith("UUFA_SCHOLAR_TWO_CAREERS") :
            do_query(query, date + " Scholarship Award with Two Careers " + year + ".xls", directory,
                     maisa_mail.attachments)

        if query.startswith("UUFA_SCHOLAR_AUTH_NOT_DISB") :
            do_query(query, date + " Scholar Authorized Not Disbursed " + year + ".xls", directory,
                     maisa_mail.attachments)

 

# Weekly Scholarships Queries
def do_weekly_scholarships():
    year = "23"
    aid_year = "2023"
    for query_name in os.listdir("."):
        if ("UUFA_WS_" in query_name) and ("22" in query_name.split("-")[0]):
            year = "22"
            break
    aid_year = "20" + str(int(year) - 1) + "-20" + year

    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/Scholarships', aid_year + ' Scholar\Queries'))
        directory_save = os.path.realpath(os.path.join('C:\Testing Bob/Save', aid_year))
        directory_errors = os.path.realpath('C:\Systems\External Awards\Errors')
    else:
        directory = os.path.realpath(os.path.join('O:\Systems\Scholarships', aid_year + ' Scholar\Queries'))
        directory_save = os.path.realpath(os.path.join('O:\Systems\Queries\Save', aid_year))
        directory_errors = os.path.realpath('O:\Systems\External Awards\Errors')

    # the list 'my_path' should be populated with the FOLDER variables above.
    if not os.path.isdir(directory):
        os.makedirs(directory)
    if not os.path.isdir(directory_save):
        os.makedirs(directory_save)
    if not os.path.isdir(directory_errors):
        os.makedirs(directory_errors)

    # Change File_Name to be file as it is received and _new_file_name to what
    # the new file should be.  Prefix date
    # will be added.
    if ("22" in query_name.split("-")[0]):
        for query in os.listdir("."):
            if ("DEPT_POST_WRNG_ITEM" in query) and (year in query[:-8]) :
                do_query(query, date + " Depts posting to the wrong item type  " + year + ".xls", directory,
                         bjns_mail.attachments)

            if ("MISC_TOTAL" in query) and (year in query[:-8]) :
                do_query(query, date + " IT Dept Misc Awards Total (10001) " + year + ".xls", directory_save,
                         null_mail.attachments)

            if ("CARES_HEERF" in query):
                do_query(query, date + " Cares & HEERF Awards by Term.xls", directory,
                         schol_mail.attachments)

            if ("MISC_NOPOST" in query) and (year in query[:-8]) :
                do_query(query, date + " 7880013 Dept Misc Awards No Post " + year + ".xls", directory_save,
                         hjr_mail.attachments)

            if ("BOOKS_TOTAL" in query) and (year in query[:-8]) :
                do_query(query, date + " 788 IT Dept Books Awards Total (10002) " + year + ".xls", directory_save,
                         null_mail.attachments)

            if ("BOOKS_NOPOST" in query) and (year in query[:-8]) :
                do_query(query, date + " 7880015 Dept Books No Post " + year + ".xls", directory_save,
                         hjr_mail.attachments)

            if ("ROOMBOARD_TOTAL" in query) and (year in query[:-8]) :
                do_query(query, date + " 788 IT Dept Room & Board Awards Total (10003) " + year + ".xls", directory_save,
                         null_mail.attachments)

            if ("ROOMBOARD_NOPOST" in query) and (year in query[:-8]) :
                do_query(query, date + " 7880029 Dept Room & Board No Post " + year + ".xls", directory_save,
                         hjr_mail.attachments)

            if ("TRAVEL_TOTAL" in query) and (year in query[:-8]) :
                do_query(query, date + " 788 IT Dept Travel Awards Total (10004) " + year + ".xls", directory_save,
                         null_mail.attachments)

            if ("TRAVEL_NOPOST" in query) and (year in query[:-8]) :
                do_query(query, date + " 7880033 Dept Travel No Post " + year + ".xls", directory_save,
                         hjr_mail.attachments)

            if (("TRAINEESHIP" in query) and ("TOTAL" in query)) and (year in query[:-8]) :
                do_query(query, date + " 788 IT Dept Traineeship Awards Total (10005) " + year + ".xls", directory_save,
                         null_mail.attachments)

            if ("TRAINEESHIP_NOPOST" in query) and (year in query[:-8]) :
                do_query(query, date + " 7880034 Dept Traineeship No Post " + year + ".xls", directory_save,
                         hjr_mail.attachments)

            #if( year == int(date[-2:])+1):
            if ("SCH_ALL_NEED" in query) and (year in query[:-8]):
                do_query(query, date + " All Scholarships Need Based " + year + ".xls", directory,
                         bhjjns_mail.attachments)

            if ("SCH_ALL_NRFRESH" in query) and (year in query[:-8]):
                do_query(query, date + " All Scholarships Non Res Freshman " + year + ".xls", directory,
                         bhjjns_mail.attachments)

            if ("SCH_ALL_NRTRAN" in query) and (year in query[:-8]):
                do_query(query, date + " All Scholarships Non Res Transfer " + year + ".xls", directory,
                         bhjjns_mail.attachments)

            if ("SCH_ALL_RESFRESH" in query) and (year in query[:-8]):
                do_query(query, date + " All Scholarships Res Freshman " + year + ".xls", directory,
                         bhjjns_mail.attachments)

            if ("SCH_ALL_RESTRAN" in query) and (year in query[:-8]):
                do_query(query, date + " All Scholarships Res Transfer " + year + ".xls", directory,
                         bhjjns_mail.attachments)

            if ("WS_UT_PROMISE_CHKLST" in query) and (year in query[:-8]):
                    do_query(query, date + " Utah Promise Checklist " + year + ".xls", directory,
                         jj_mail.attachments)

            if ("WS_SCH_ALL_EA_ERRORS" in query):
                    do_query(query, date + " Weekly Error Query " + year + ".xls", directory_errors,
                         schol_mail.attachments)

            if ("WS_SCHOLAR_ADM_REVIEW" in query) and (year in query[:-8]):
                    do_query(query, date + " Scholarship Admin Review " + year + ".xls", directory,
                         schol_mail.attachments)

            if ("WS_FAC_STAFF" in query) and (year in query[:-8]):
                    do_query(query, date + " Faculty-Staff Not Posted " + year + ".xls", directory,
                         schol_mail.attachments)

            if ("WS_SCHOLAR_STATUS" in query):
                    do_query(query, date + " Scholarship Offer Status DEIN " + year + ".xls", directory,
                         schol2_mail.attachments)
    else:
        for query in os.listdir("."):
            if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if ("DEPT_POST_WRNG_ITEM" in query) :
                    do_query(query, date + " Depts posting to the wrong item type  " + year + ".xls", directory,
                             bjns_mail.attachments)

                if ("MISC_TOTAL" in query) :
                    do_query(query, date + " IT Dept Misc Awards Total (10001) " + year + ".xls", directory_save,
                             null_mail.attachments)

                if ("CARES_HEERF" in query):
                    do_query(query, date + " Cares & HEERF Awards by Term.xls", directory,
                             schol_mail.attachments)

                if ("MISC_NOPOST" in query) :
                    do_query(query, date + " 7880013 Dept Misc Awards No Post " + year + ".xls", directory_save,
                             hjr_mail.attachments)

                if ("BOOKS_TOTAL" in query) :
                    do_query(query, date + " 788 IT Dept Books Awards Total (10002) " + year + ".xls", directory_save,
                             null_mail.attachments)

                if ("BOOKS_NOPOST" in query) :
                    do_query(query, date + " 7880015 Dept Books No Post " + year + ".xls", directory_save,
                             hjr_mail.attachments)

                if ("ROOMBOARD_TOTAL" in query) :
                    do_query(query, date + " 788 IT Dept Room & Board Awards Total (10003) " + year + ".xls", directory_save,
                             null_mail.attachments)

                if ("ROOMBOARD_NOPOST" in query) :
                    do_query(query, date + " 7880029 Dept Room & Board No Post " + year + ".xls", directory_save,
                             hjr_mail.attachments)

                if ("TRAVEL_TOTAL" in query) :
                    do_query(query, date + " 788 IT Dept Travel Awards Total (10004) " + year + ".xls", directory_save,
                             null_mail.attachments)

                if ("TRAVEL_NOPOST" in query) :
                    do_query(query, date + " 7880033 Dept Travel No Post " + year + ".xls", directory_save,
                             hjr_mail.attachments)

                if (("TRAINEESHIP" in query) and ("TOTAL" in query)) :
                    do_query(query, date + " 788 IT Dept Traineeship Awards Total (10005) " + year + ".xls", directory_save,
                             null_mail.attachments)

                if ("TRAINEESHIP_NOPOST" in query) :
                    do_query(query, date + " 7880034 Dept Traineeship No Post " + year + ".xls", directory_save,
                             hjr_mail.attachments)

                #if( year == int(date[-2:])+1):
                if ("SCH_ALL_NEED" in query):
                    do_query(query, date + " All Scholarships Need Based " + year + ".xls", directory,
                             bhjjns_mail.attachments)

                if ("SCH_ALL_NRFRESH" in query):
                    do_query(query, date + " All Scholarships Non Res Freshman " + year + ".xls", directory,
                             bhjjns_mail.attachments)

                if ("SCH_ALL_NRTRAN" in query):
                    do_query(query, date + " All Scholarships Non Res Transfer " + year + ".xls", directory,
                             bhjjns_mail.attachments)

                if ("SCH_ALL_RESFRESH" in query):
                    do_query(query, date + " All Scholarships Res Freshman " + year + ".xls", directory,
                             bhjjns_mail.attachments)

                if ("SCH_ALL_RESTRAN" in query):
                    do_query(query, date + " All Scholarships Res Transfer " + year + ".xls", directory,
                             bhjjns_mail.attachments)

                if ("WS_UT_PROMISE_CHKLST" in query):
                        do_query(query, date + " Utah Promise Checklist " + year + ".xls", directory,
                             jj_mail.attachments)

                if ("WS_SCH_ALL_EA_ERRORS" in query):
                        do_query(query, date + " Weekly Error Query " + year + ".xls", directory_errors,
                             schol_mail.attachments)

                if ("WS_SCHOLAR_ADM_REVIEW" in query):
                        do_query(query, date + " Scholarship Admin Review " + year + ".xls", directory,
                             schol_mail.attachments)

                if ("WS_FAC_STAFF" in query):
                        do_query(query, date + " Faculty-Staff Not Posted " + year + ".xls", directory,
                             schol_mail.attachments)

                if ("WS_SCHOLAR_STATUS" in query):
                        do_query(query, date + " Scholarship Offer Status DEIN " + year + ".xls", directory,
                             schol2_mail.attachments)
