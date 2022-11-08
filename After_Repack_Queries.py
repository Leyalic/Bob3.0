# After Repackaging Queries - to be modified
# to be called in main
import os

def do_after_repackaging(test, date, year, query, renamed):
    #global aid_year
    #strm = "no STRM found"
    #prompt = "What STRM is this for? (ex. 1154 = Spring 2015:"
    aid_year = str(int(year) - 1) + "-" + str(year)
    #for query_name in os.listdir("."):
    #    if query_name.startswith("UUFA_AP"):
    #        while True:
    #            strm = term
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

    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/Pell Repackaging', aid_year))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Pell Repackaging', aid_year))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    year = year[2:]

    move_directory = "Pell Reports"

    if True:
    #for query in os.listdir("."):
        # Pell Repackaging Queries
        if query.startswith("UUFA_AP_RPKG_5TH_YR_2ND_BACH"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_AP_RPKG_ACTN"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_AP_RPKG_AWACT_C"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_AP_RPKG_AW_ACT"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_AP_RPKG_FPEL_AWARD_LCK"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_AP_RPKG_PLAN_ID_BLANK"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_AP_RPKG_RPKG_SNAPSHOT"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_AP_RPKG_SAP_HOLD_DELETED"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_AP_RPKG_SKIP"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_AP_RPKG_TERM_FT"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_AP_RPKG_TERM_HT"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_AP_RPKG_TERM_LH"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_AP_RPKG_TERM_NL"):
            return (query, renamed, directory, move_directory)

        if query.startswith("UUFA_AP_RPKG_TERM_TQ"):
            return (query, renamed, directory, move_directory)
    return "Empty"