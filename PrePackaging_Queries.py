# Pre-Repackaging Queries - to be modified
# to be called in main
import os

def do_pre_repackaging(test, date, year, query, renamed, aid_year_match):
    #global aid_year
    #strm = "no STRM found"
    #prompt = "What STRM is this for? (ex. 1154 = Spring 2015:"
    #aid_year = "not defined"
    #for query_name in os.listdir("."):
    #    if query_name.startswith("UUFA_PP"):
    #        while True:
    #            strm = raw_input(prompt)
    #            if (len(strm) == 5) and ((0 / int(strm) == 0)):
    #                break
    #            else:
    #                print ("\nOnly STRMs in the form of 1(year)4/6/8 are acceptable. Ex: 1168 is Fall of 16.")
    #        if strm[-1] == "8":
    #            aid_year = "20" + str(strm[1:3]) + "-20" + str(int(strm[1:3]) + 1)
    #            break
    #        else:
    #            aid_year = "20" + str(int(strm[1:3]) - 1) + "-20" + str(strm[1:3])
    #            break
    aid_year = str(int(year) - 1) + "-" + str(year)

    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/Pell Repackaging', aid_year))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Pell Repackaging', aid_year))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    year = year[2:]

    move_directory = "Pell Reports"

    toggle = True

    if aid_year_match:
    #if ("22" in query_name.split("-")[0]):
        if True:
        #for query in os.listdir("."):
            # Pre-Pell Repackaging Queries
            if query.startswith("UUFA_PP_RPKG_AGGREGATE_LIMITS"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PP_RPKG_AWD_AY_NO_BDGT"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PP_RPKG_AWD_STRM_INACTIVE"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PP_RPKG_AWRD_LOCK"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PP_RPKG_COA_DOUBLE"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PP_RPKG_LTHT_PELL_COA"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PP_RPKG_RPKG_NO_BUDGET"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PP_RPKG_RPKG_SNAPSHOT"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PP_RPKG_TOTAL_WDRN_DRP"):
                return (query, renamed, directory, move_directory)
                
            if query.startswith("UUFA_READY_REPACKAGE"):
                    return (query, renamed, directory, move_directory)
    else:
        if True:
        #for query in os.listdir("."):
            if toggle:
            #if("22" not in query_name.split("-")[0]):
                # Pre-Pell Repackaging Queries
                if query.startswith("UUFA_PP_RPKG_AGGREGATE_LIMITS"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PP_RPKG_AWD_AY_NO_BDGT"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PP_RPKG_AWD_STRM_INACTIVE"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PP_RPKG_AWRD_LOCK"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PP_RPKG_COA_DOUBLE"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PP_RPKG_LTHT_PELL_COA"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PP_RPKG_RPKG_NO_BUDGET"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PP_RPKG_RPKG_SNAPSHOT"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PP_RPKG_TOTAL_WDRN_DRP"):
                    return (query, renamed, directory, move_directory)
                    
                if query.startswith("UUFA_READY_REPACKAGE"):
                    return (query, renamed, directory, move_directory)
    return "Empty"