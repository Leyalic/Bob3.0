# Daily Scholarships Queries
import os

def do_daily_scholarships(test, year, query, renamed):

    aid_year = str(int(year) - 1) + "-" + str(year)

    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob', aid_year + ' Scholar\Queries'))
    else:
        directory = os.path.realpath(os.path.join('O:\Systems', aid_year + ' Scholar\Queries'))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    move_directory = "Scholarship Reports"

    # FORMAT: return (query, renamed, archive_directory, UOSFA_folder)
    # query: The original file name
    # renamed: The name the file should have after being moved
    # archive_directory: The folder the file will be copied to
    # UOSFA_folder: The name of the folder the renamed file should be moved to
    # - (eg. "Budget Reports", "SAP Reports", "Unknown Reports") 
    # - put "None" if it shouldn't be moved to a folder in 'O:/UOSFA Reports/'

    if query.startswith("UUFA_SCHOLAR_DISB_ZERO") :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_SCHOLAR_TWO_CAREERS") :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_SCHOLAR_AUTH_NOT_DISB") :
        return (query, renamed, directory, move_directory)

    return "Empty" #Leave as last line
 

# Weekly Scholarships Queries
def do_weekly_scholarships(test, year, query, renamed):

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

    move_directory = "Scholarship Reports"
    external_directory = "External Award Reports"

    # FORMAT: return (query, renamed, archive_directory, UOSFA_folder)
    # query: The original file name
    # renamed: The name the file should have after being moved
    # archive_directory: The folder the file will be copied to
    # UOSFA_folder: The name of the folder the renamed file should be moved to
    # - (eg. "Budget Reports", "SAP Reports", "Unknown Reports") 
    # - put "None" if it shouldn't be moved to a folder in 'O:/UOSFA Reports/'

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

    return "Empty" #Leave as last line