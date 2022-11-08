# Daily Scholarships Queries - to be modified
# to be called in main
import os

def do_daily_scholarships(test, date, year, query, renamed):
    #year = "23"
    #for query_name in os.listdir("."):
    #    if query_name.startswith("UUFA_SCHOLAR_DISB_ZERO"):
    #        year = str(int(re.search(r'\d+', query_name).group()))
    #        break
    #aid_year = "20" + str(int(year) - 1) + "-20" + year
    aid_year = str(int(year) - 1) + "-" + str(year)

    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob', aid_year + ' Scholar\Queries'))
    else:
        directory = os.path.realpath(os.path.join('O:\Systems', aid_year + ' Scholar\Queries'))

    # the list 'my_path' should be populated with the FOLDER variables above.
    if not os.path.isdir(directory):
        os.makedirs(directory)

    year = year[2:]

    move_directory = "Scholarship Reports"

    # Change File_Name to be file as it is received and _new_file_name to what
    # the new file should be.  Prefix date
    # will be added.
    if True:
    #for query in os.listdir("."):
        if query.startswith("UUFA_SCHOLAR_DISB_ZERO") :
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_SCHOLAR_TWO_CAREERS") :
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_SCHOLAR_AUTH_NOT_DISB") :
            return (query, renamed, directory, move_directory)
    return "Empty"
 

# Weekly Scholarships Queries
def do_weekly_scholarships(test, date, year, query, renamed, aid_year_match):
    #year = "23"
    #aid_year = "2023"
    #for query_name in os.listdir("."):
    #    if ("UUFA_WS_" in query_name) and ("22" in query_name.split("-")[0]):
    #        year = "22"
    #        break
    #aid_year = "20" + str(int(year) - 1) + "-20" + year
    aid_year = str(int(year) - 1) + "-" + str(year)

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

    year = year[2:]

    move_directory = "Scholarship Reports"
    external_directory = "External Award Reports"

    toggle = True;

    # Change File_Name to be file as it is received and _new_file_name to what
    # the new file should be.  Prefix date
    # will be added.
    if aid_year_match:
    #if ("22" in query_name.split("-")[0]):
        if True:
        #for query in os.listdir("."):
            if ("DEPT_POST_WRNG_ITEM" in query) and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("MISC_TOTAL" in query) and (year in query[:-8]) :
                return (query, renamed, directory_save, move_directory)

            if ("CARES_HEERF" in query):
                return (query, renamed, directory, move_directory)

            if ("MISC_NOPOST" in query) and (year in query[:-8]) :
                return (query, renamed, directory_save, move_directory)

            if ("BOOKS_TOTAL" in query) and (year in query[:-8]) :
                return (query, renamed, directory_save, move_directory)

            if ("BOOKS_NOPOST" in query) and (year in query[:-8]) :
                return (query, renamed, directory_save, move_directory)

            if ("ROOMBOARD_TOTAL" in query) and (year in query[:-8]) :
                return (query, renamed, directory_save, move_directory)

            if ("ROOMBOARD_NOPOST" in query) and (year in query[:-8]) :
                return (query, renamed, directory_save, move_directory)

            if ("TRAVEL_TOTAL" in query) and (year in query[:-8]) :
                return (query, renamed, directory_save, move_directory)

            if ("TRAVEL_NOPOST" in query) and (year in query[:-8]) :
                return (query, renamed, directory_save, move_directory)

            if (("TRAINEESHIP" in query) and ("TOTAL" in query)) and (year in query[:-8]) :
                return (query, renamed, directory_save, move_directory)

            if ("TRAINEESHIP_NOPOST" in query) and (year in query[:-8]) :
                return (query, renamed, directory_save, move_directory)

            #if( year == int(date[-2:])+1):
            if ("SCH_ALL_NEED" in query) and (year in query[:-8]):
                return (query, renamed, directory, move_directory)

            if ("SCH_ALL_NRFRESH" in query) and (year in query[:-8]):
                return (query, renamed, directory, move_directory)

            if ("SCH_ALL_NRTRAN" in query) and (year in query[:-8]):
                return (query, renamed, directory, move_directory)

            if ("SCH_ALL_RESFRESH" in query) and (year in query[:-8]):
                return (query, renamed, directory, move_directory)

            if ("SCH_ALL_RESTRAN" in query) and (year in query[:-8]):
                return (query, renamed, directory, move_directory)

            if ("WS_UT_PROMISE_CHKLST" in query) and (year in query[:-8]):
                    return (query, renamed, directory, move_directory)

            if ("WS_SCH_ALL_EA_ERRORS" in query):
                    return (query, renamed, directory_errors, external_directory)

            if ("WS_SCHOLAR_ADM_REVIEW" in query) and (year in query[:-8]):
                    return (query, renamed, directory, move_directory)

            if ("WS_FAC_STAFF" in query) and (year in query[:-8]):
                    return (query, renamed, directory, move_directory)

            if ("WS_SCHOLAR_STATUS" in query):
                    return (query, renamed, directory, move_directory)
    else:
        if True:
        #for query in os.listdir("."):
            if toggle:
            #if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if ("DEPT_POST_WRNG_ITEM" in query) :
                    return (query, renamed, directory, move_directory)

                if ("MISC_TOTAL" in query) :
                    return (query, renamed, directory_save, move_directory)

                if ("CARES_HEERF" in query):
                    return (query, renamed, directory, move_directory)

                if ("MISC_NOPOST" in query) :
                    return (query, renamed, directory_save, move_directory)

                if ("BOOKS_TOTAL" in query) :
                    return (query, renamed, directory_save, move_directory)

                if ("BOOKS_NOPOST" in query) :
                    return (query, renamed, directory_save, move_directory)

                if ("ROOMBOARD_TOTAL" in query) :
                    return (query, renamed, directory_save, move_directory)

                if ("ROOMBOARD_NOPOST" in query) :
                    return (query, renamed, directory_save, move_directory)

                if ("TRAVEL_TOTAL" in query) :
                    return (query, renamed, directory_save, move_directory)

                if ("TRAVEL_NOPOST" in query) :
                    return (query, renamed, directory_save, move_directory)

                if (("TRAINEESHIP" in query) and ("TOTAL" in query)) :
                    return (query, renamed, directory_save, move_directory)

                if ("TRAINEESHIP_NOPOST" in query) :
                    return (query, renamed, directory_save, move_directory)

                #if( year == int(date[-2:])+1):
                if ("SCH_ALL_NEED" in query):
                    return (query, renamed, directory, move_directory)

                if ("SCH_ALL_NRFRESH" in query):
                    return (query, renamed, directory, move_directory)

                if ("SCH_ALL_NRTRAN" in query):
                    return (query, renamed, directory, move_directory)

                if ("SCH_ALL_RESFRESH" in query):
                    return (query, renamed, directory, move_directory)

                if ("SCH_ALL_RESTRAN" in query):
                    return (query, renamed, directory, move_directory)

                if ("WS_UT_PROMISE_CHKLST" in query):
                        return (query, renamed, directory, move_directory)

                if ("WS_SCH_ALL_EA_ERRORS" in query):
                        return (query, renamed, directory_errors, external_directory)

                if ("WS_SCHOLAR_ADM_REVIEW" in query):
                        return (query, renamed, directory, move_directory)

                if ("WS_FAC_STAFF" in query):
                        return (query, renamed, directory, move_directory)

                if ("WS_SCHOLAR_STATUS" in query):
                        return (query, renamed, directory, move_directory)
    return "Empty"