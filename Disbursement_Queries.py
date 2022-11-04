# Disbursement Queries - to be modified
# to be called in main
import os

def do_disb_queries(test, date, year, query, aid_year_match, disb_date):
    #global aid_year
    #year = "23"
    #for query_name in os.listdir("."):
    #    if query_name.startswith("UUFA_DQ_AUTHORIZED_NOT_DISB"):
    #        if str(int(re.search(r'\d+', query_name).group())) == "22":
    #            year = "22"
    #        break
        
    #aid_year = "20" + str(int(year) - 1) + "-20" + year
    #disb_date = str(raw_input("Enter Date the most recent Disbursement ran in 'MM-DD-YY' format:"))
    #disb_date = disb_date[:-1]
    aid_year = str(int(year - 1)) + "-" + str(year)
    month_folder = date[:2] + "-20" + date[-2:]

    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/Disbursement',
                                                  aid_year, month_folder))
    else:
        directory = os.path.realpath(os.path.join('O:\Systems\QUERIES\Disbursement', aid_year, month_folder))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    year = year[2:]
    dot_index = query.find(".")
    dash_index = query.rfind("-")
    renamed = disb_date + " " + query[dash_index:] + " " + year + query[:dot_index]

    move_directory = "Daily Reports"

    toggle = True
    
    if aid_year_match:
    #if ("22" in query_name.split("-")[0]):
        if True:
        #for query in os.listdir("."):
            if query.startswith("UUFA_DQ_AUTHORIZED_NOT_DISB") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DQ_ALL_DISBURSED") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("FA_DQ_ATHLETE_RM_BD") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("FA_DQ_ATH_OFF_SCHED_RM_BD") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("_CASH_DISB_TOTALS") in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("_DQ_DISB_TOTALS") in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DQ_FALL" + year) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DQ_FALL_SPRING") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DQ_DL_SUMMER") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DQ_SPRING") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DQ_UG_PLUS_REFUND_IA") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("DQ_MISC_CARES_DISB") in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("DQ_MISC_CARES_RES_DISB") in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("MISC_DISB_TOTALS") in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DQ_MISC_RESOURCE_DISB") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("NONCASH_DISB_TOTALS") in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DQ_PELL_ACPT_GR8_DISB") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DQ_SF_ITEM_TYPE_ERROR"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DQ_TEACH_GRANT" + str(int(year) - 1)):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_DQ_TEACH_GRANT") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)
    else:
        if True:
        #for query in os.listdir("."):
            if toggle:
            #if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if query.startswith("UUFA_DQ_AUTHORIZED_NOT_DISB") :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DQ_ALL_DISBURSED") :
                    return (query, renamed, directory, move_directory)

                if query.startswith("FA_DQ_ATHLETE_RM_BD") :
                    return (query, renamed, directory, move_directory)

                if query.startswith("FA_DQ_ATH_OFF_SCHED_RM_BD") :
                    return (query, renamed, directory, move_directory)

                if ("_CASH_DISB_TOTALS") in query :
                    return (query, renamed, directory, move_directory)

                if ("_DQ_DISB_TOTALS") in query :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DQ_FALL") and "SPRING" not in query:
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DQ_FALL_SPRING") :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DQ_DL_SUMMER") :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DQ_SPRING") :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DQ_UG_PLUS_REFUND_IA") :
                    return (query, renamed, directory, move_directory)

                if ("DQ_MISC_CARES_DISB") in query :
                    return (query, renamed, directory, move_directory)

                if ("DQ_MISC_CARES_RES_DISB") in query :
                    return (query, renamed, directory, move_directory)

                if ("MISC_DISB_TOTALS") in query :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DQ_MISC_RESOURCE_DISB") :
                    return (query, renamed, directory, move_directory)

                if ("NONCASH_DISB_TOTALS") in query :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DQ_PELL_ACPT_GR8_DISB") :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DQ_SF_ITEM_TYPE_ERROR"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DQ_TEACH_GRANT" + str(int(year) - 1)):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DQ_TEACH_GRANT") :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_DQ_DISB_BREAKDOWN") :
                    return (query, renamed, directory, move_directory)


