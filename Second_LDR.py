# 2nd LDR Queries 
# to be called in main
import os

def do_2nd_ldr(test, date, year, query, aid_year_match):
    #global aid_year
    #year = "18"
    #for query_name in os.listdir("."):
    #    if query_name.startswith("UUFA_PRT_PELL_ELG_NO_PELL"):
    #        year = str(int(re.search(r'\d+', query_name).group()))
    #        break
    #aid_year = "20" + str(int(year) - 1) + "-20" + str(year)
    aid_year = str(int(year - 1)) + "-" + str(year)

    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/Term', aid_year))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Term', aid_year))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    year = year[2:]
    dot_index = query.find(".")
    dash_index = query.rfind("-")
    renamed = date + " " + query[dash_index:] + " " + year + query[:dot_index]

    move_directory = "Pell Reports"

    toggle = True

    if aid_year_match:
    #if ("22" in query_name.split("-")[0]):
        if True:
        #for query in os.listdir("."):
            if query.startswith("UUFA_CBA_UNDISBURSED"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_HRS_DECREASE_ATH"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_HRS_DECREASE_FC"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_HRS_DECREASE_SV"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PELL_ELIG_ENROLL_NO_AWARD"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PELL_OFFERED_NOT_DISB"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PELL_DL_MATH990"):
                return (query, renamed, directory, move_directory)

            if "PELL_DL_MATH980" in query:
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PELL_DL_ELI575_ELI685"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_SF_DISB_ATH_AWD_NOPOST"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_SF_DISB_WAIVER_AWD_NOPOST"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_PELL_ELG_NO_PELL") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)
                
    else:
        if True:
        #for query in os.listdir("."):
            if toggle:
            #if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if query.startswith("UUFA_CBA_UNDISBURSED"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_HRS_DECREASE_ATH"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_HRS_DECREASE_FC"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_HRS_DECREASE_SV"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PELL_ELIG_ENROLL_NO_AWARD"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PELL_OFFERED_NOT_DISB"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PELL_DL_MATH990"):
                    return (query, renamed, directory, move_directory)

                if "PELL_DL_MATH980" in query:
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PELL_DL_ELI575_ELI685"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_SF_DISB_ATH_AWD_NOPOST"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_SF_DISB_WAIVER_AWD_NOPOST"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_PELL_ELG_NO_PELL") and (year in query[:-8]) :
                    return (query, renamed, directory, move_directory)

