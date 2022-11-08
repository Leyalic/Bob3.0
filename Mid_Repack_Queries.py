# Mid-Repackaging Queries
# to be called in main
import os

def do_mid_repack_queries(test, date, year, query, renamed):
    #global aid_year
    #strm = "no STRM found"
    #prompt = "What STRM is this for? (EX. 1154 = Spring 2015:)"
    #aid_year = "not defined"
    #for query_name in os.listdir("."):
    #    if query_name.startswith("UUFA_MP"):
    #        while True:
    #            strm = raw_input(prompt)
    #            if len(strm) == 5 and (0 / int(strm) == 0):
    #                break
    #            else:
    #                print ("\nOnly STRMs in the form of 1(year)4/6/8 are acceptable.")
    #        if strm[-1] == "8":
    #            aid_year = "20" + str(strm[1:3]) + "-20" + str(int(strm[1:3]) + 1)
    #            break
    #        else:
    #            aid_year = "20" + str(int(strm[1:3]) - 1) + "-20" + str(strm[1:3])
    #            break
    aid_year = str(int(year) - 1) + "-" + str(year)

    if test:
        directory = os.path.realpath(os.path.join('C:/QueryRunnerProj/Testing/Test/Pell Repackaging', aid_year))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Pell Repackaging', aid_year))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    #year = aid_year[7:]

    year = year[2:]

    move_directory = "Pell Reports"

    if True:
    #for query in os.listdir("."):
        if query.startswith("UUFA_MP_RPKG_AID_PROC_STATUS_4"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_MP_RPKG_AWD_STRM_INACTIVE"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_MP_RPKG_FCIT"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_MP_RPKG_FDR"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_MP_RPKG_FOVP_FARC_I"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_MP_RPKG_ISIR_CMT_346_347"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_MP_RPKG_LEAVE"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_MP_RPKG_TOTAL_WDRN_DRP"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_MP_RPKG_TOTAL_WTHDRN_DRP"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_MP_RPKG_VAR_1_2"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_MP_RPKG_VER_UNFLAG"):
            return (query, renamed, directory, move_directory)
    return "Empty"
