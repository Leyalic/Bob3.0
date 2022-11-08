# TSM Queries - to be modified      
# to be called in main
import os

def do_tsm_queries(test, date, year, query, renamed, aid_year_match):
    #global aid_year
    #year = "19"
    #for query_name in os.listdir("."):
    #    if "_NSLDS" in query_name:
    #        year = str(int(re.search(r'\d+', query_name).group()))
    #        break
    #aid_year = "20" + str(int(year) - 1) + "-20" + year

    if test:
        directory = os.path.realpath(os.path.join('C:/QUERIES/TSM/NSLDS TSM Request'))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/TSM/NSLDS TSM Request'))

    # the list 'my_path' should be populated with the FOLDER variables above.
    if not os.path.isdir(directory):
        os.makedirs(directory)

    year = year[2:]

    move_directory = "Pell Reports"

    toggle = True

    # Change File_Name to be file as it is received and _new_file_name to what
    # the new file should be.  Prefix date
    # will be added.
    if aid_year_match:
    #if ("22" in query_name.split("-")[0]):
        if True:
        #for query in os.listdir("."):
            if ("NSLDS_REQUEST_DN" in query) and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("NSLDS_REQUEST_GR" in query) and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("NSLDS_REQUEST_LW" in query) and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("NSLDS_REQUEST_MD" in query) and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("NSLDS_REQUEST_UG" in query) and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("_NSLDS_VAR_FLAG9_DN" in query) and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("_NSLDS_VAR_FLAG9_GR" in query) and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("_NSLDS_VAR_FLAG9_LW" in query) and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("_NSLDS_VAR_FLAG9_MD" in query) and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("_NSLDS_VAR_FLAG9_UG" in query) and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)
    else:
        if True:
        #for query in os.listdir("."):
            if toggle:
            #if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
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
    return "Empty"
