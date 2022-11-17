# Disbursement Queries 
import os

def do_disb_queries(test, date, year, query, renamed):

    aid_year = str(int(year) - 1) + "-" + str(year)
    month_folder = date[:2] + "-20" + date[-2:]

    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/Disbursement',
                                                  aid_year, month_folder))
    else:
        directory = os.path.realpath(os.path.join('O:\Systems\QUERIES\Disbursement', aid_year, month_folder))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    move_directory = "Daily Reports"
    
    if query.startswith("UUFA_DQ_AUTHORIZED_NOT_DISB"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DQ_ALL_DISBURSED"):
        return (query, renamed, directory, move_directory)

    if query.startswith("FA_DQ_ATHLETE_RM_BD"):
        return (query, renamed, directory, move_directory)

    if query.startswith("FA_DQ_ATH_OFF_SCHED_RM_BD"):
        return (query, renamed, directory, move_directory)

    if ("_CASH_DISB_TOTALS") in query:
        return (query, renamed, directory, move_directory)

    if ("_DQ_DISB_TOTALS") in query:
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DQ_FALL") :
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DQ_FALL_SPRING"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DQ_DL_SUMMER"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DQ_SPRING"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DQ_UG_PLUS_REFUND_IA"):
        return (query, renamed, directory, move_directory)

    if ("DQ_MISC_CARES_DISB") in query:
        return (query, renamed, directory, move_directory)

    if ("DQ_MISC_CARES_RES_DISB") in query:
        return (query, renamed, directory, move_directory)

    if ("MISC_DISB_TOTALS") in query:
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DQ_MISC_RESOURCE_DISB"):
        return (query, renamed, directory, move_directory)

    if ("NONCASH_DISB_TOTALS") in query:
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DQ_PELL_ACPT_GR8_DISB"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DQ_SF_ITEM_TYPE_ERROR"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DQ_TEACH_GRANT"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DQ_DISB_BREAKDOWN") :
        return (query, renamed, directory, move_directory)

    if ("_DQ_DISB_TOTALS") in query :
        return (query, renamed, directory, move_directory)
    
    if query.startswith("UUFA_DQ_FALL") and "SPRING" not in query:
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_DQ_PELL_ACPT_GR8_DISB") :
        return (query, renamed, directory, move_directory)

    return "Empty" #Leave as last line

