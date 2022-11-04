# Day After LDR Queries - to be modified
# to be called in main
import os

def do_day_after_ldr(test, date, year, query, aid_year_match):
    #global aid_year
    #for query_name in os.listdir("."):
    #    if query_name.startswith("UUFA_PRT_PELL_ELG_NO_PELL"):
    #        year = str(int(re.search(r'\d+', query_name).group()))
    #        break
    #aid_year = "20" + str(int(year) - 1) + "-20" + year
    aid_year = str(int(year - 1)) + "-" + str(year)

    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/LDR', aid_year))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/LDR', aid_year))

    # the list 'my_path' should be populated with the FOLDER variables above.
    if not os.path.isdir(directory):
        os.makedirs(directory)

    year = year[2:]
    dot_index = query.find(".")
    dash_index = query.rfind("-")
    renamed = date + " " + query[dash_index:] + " " + year + query[:dot_index]

    move_directory = "Daily Reports"

    toggle = True

    # Change File_Name to be file as it is received and _new_file_name to what
    # the new file should be.  Prefix date
    # will be added.
    if aid_year_match:
    #if ("22" in query_name.split("-")[0]):
        if True:
        #for query in os.listdir("."):
            if query.startswith("UUFA_LDR_MIN_ENROLLMENT_ATH"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_LDR_MINIMUM_ENROLLMENT_FC"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_LDR_MINIMUM_ENROLLMENT_SV"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_LDR_PELL_AWARDS"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_ATHLETE_AWARD_DISBURSED"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_CBA_UNDISBURSED"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PELL_DL_MATH990"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PELL_DL_ELI575_ELI685"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PELL_ELIG_ENROLL_NO_AWARD"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PELL_OFFERED_NOT_DISB"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PELL_SUMMER_ENROLLMENT"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_THESIS_STUDENTS_NONRES"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_REGISTERED_CENSUS_DATE"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_SF_DISB_ATH_AWD_NOPOST"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_SF_DISB_WAIVER_AWD_NOPOST"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_AWD_PLL_ELG_NO_PLL") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_NO_MTRC_STU_ATH_BAL_OWING"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_FATERM_SOURCE_N_AWD_ATH"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_FATERM_SOURCE_N_AWD_SV"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_PELL_ELG_NO_PELL"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_ATH_NO_MTRC_STU_BAL_OWING"):
                return (query, renamed, directory, move_directory)
    else:
        if True:
        #for query in os.listdir("."):
            if toggle:
            #if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if query.startswith("UUFA_LDR_MIN_ENROLLMENT_ATH"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_LDR_MINIMUM_ENROLLMENT_FC"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_LDR_MINIMUM_ENROLLMENT_SV"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_LDR_PELL_AWARDS"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_ATHLETE_AWARD_DISBURSED"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_CBA_UNDISBURSED"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PELL_DL_MATH990"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PELL_DL_ELI575_ELI685"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PELL_ELIG_ENROLL_NO_AWARD"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PELL_OFFERED_NOT_DISB"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PELL_SUMMER_ENROLLMENT"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_THESIS_STUDENTS_NONRES"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_REGISTERED_CENSUS_DATE"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_SF_DISB_ATH_AWD_NOPOST"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_SF_DISB_WAIVER_AWD_NOPOST"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_AWD_PLL_ELG_NO_PLL") and (year in query[:-8]) :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_NO_MTRC_STU_ATH_BAL_OWING"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_FATERM_SOURCE_N_AWD_ATH"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_FATERM_SOURCE_N_AWD_SV"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_PELL_ELG_NO_PELL"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_ATH_NO_MTRC_STU_BAL_OWING"):
                    return (query, renamed, directory, move_directory)

