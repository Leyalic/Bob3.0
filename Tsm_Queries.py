# TSM Queries 
import os

def do_tsm_queries(test, query, renamed):

    if test:
        directory = os.path.realpath(os.path.join('C:/QUERIES/TSM/NSLDS TSM Request'))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/TSM/NSLDS TSM Request'))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    move_directory = "Financial Aid Reports"

    # FORMAT: return (query, renamed, archive_directory, UOSFA_folder)
    # query: The original file name
    # renamed: The name the file should have after being moved
    # archive_directory: The folder the file will be copied to
    # UOSFA_folder: The name of the folder the renamed file should be moved to
    # - (eg. "Budget Reports", "SAP Reports", "Unknown Reports") 
    # - put "None" if it shouldn't be moved to a folder in 'O:/UOSFA Reports/'

    if ("NSLDS_REQUEST_DN" in query) :
        return (query, renamed, directory, move_directory)

    if ("NSLDS_REQUEST_GR" in query) :
        return (query, renamed, directory, move_directory)

    if ("NSLDS_REQUEST_LW" in query) :
        return (query, renamed, directory, move_directory)

    if ("NSLDS_REQUEST_MD" in query) :
        return (query, renamed, directory, move_directory)

    if ("NSLDS_REQUEST_UG" in query) :
        return (query, renamed, directory, move_directory)

    if ("_NSLDS_VAR_FLAG9_DN" in query) :
        return (query, renamed, directory, move_directory)

    if ("_NSLDS_VAR_FLAG9_GR" in query) :
        return (query, renamed, directory, move_directory)

    if ("_NSLDS_VAR_FLAG9_LW" in query) :
        return (query, renamed, directory, move_directory)

    if ("_NSLDS_VAR_FLAG9_MD" in query) :
        return (query, renamed, directory, move_directory)

    if ("_NSLDS_VAR_FLAG9_UG" in query) :
        return (query, renamed, directory, move_directory)

    return "Empty" #Leave as last line
