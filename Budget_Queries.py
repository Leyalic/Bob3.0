# Budget Queries - to be modified 
# to be called in main
import os

def do_budget_queries(test, date, year, query, aid_year_match):
    #global aid_year
    #year = "23"
    #for query_name in os.listdir("."):
    #    if "BR_BDGT" in query_name:
    #        if str(int(re.search(r'\d+', query_name).group())) == "22":
    #            year = "22"
    #        break
    #aid_year = "20" + str(int(year) - 1) + "-20" + year
    aid_year = str(int(year - 1)) + "-" + str(year)
    month_folder = date[:2] + "-20" + date[-2:]
    
    # Create FOLDER variables to be used in Move() operation and establishes
    # the directory to save the files
    # using the date.
    # Create variables to be used in Move() operation.
    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/Budgets', aid_year, month_folder))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Budgets', aid_year, month_folder))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    # Change File_Name to be query AC it is received and _new_file_name to what
    # the new query should be.  Prefix date
    # will be added.

    year = year[2:]
    dot_index = query.find(".")
    dash_index = query.rfind("-")
    renamed = date + " " + query[dash_index:] + " " + year + query[:dot_index]

    move_directory = "Budget Reports"

    toggle1 = True;
    
    if aid_year_match:
    #if ("22" in query_name.split("-")[0]):
        if True:
        #for query in os.listdir("."):
            if query.startswith("UUFA_BR_ACAD_LVLS_OUT_SYNC") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BR_ATH_TUIT_INCR_NR") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BR_ATH_TUITION_INCRS") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_BR_BDGT_DOUBLE_BUDGETS" in query :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BR_COA_LESS_HT") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BR_COA_TUIT_ZERO") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BR_DN_LW_MD_AID_ATRB") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BR_FT_CLASS_OVERRIDES") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BR_COA_ISIR_BDGT_DIFF") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BR_NO_BUDGET_ATTEND") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BR_PELL_COA_BLANK") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if (("BR_PELL_COA_CHECK" in query) and (year in query[:-8])) :
                return (query, renamed, directory, move_directory)


            if query.startswith("UUFA_BR_PELL_COA_DOUBLE") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "BR_PELL_COA_DBLD_WRNG" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("FA_BR_PELL_COA_LESS_HT_20") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BR_PROC_STAT_RVW_STAT") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BR_RES_NON_RES_BDGT") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BR_SCH_TUITION_FEES_NR") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BR_SCH_TUITION_ONLY_NR") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BR_SCHOLAR_TUIT_FEES") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BR_SCHOLAR_TUIT_ONLY") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("FA_BR_UFORM_CHANGE_BUD_DUR") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "BR_ACAD_LVLS_NOT_SYNC" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "BR_ACAD_LVLS_NOT_SYNC" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)
                
    else:
        if True:
        #for query in os.listdir("."):
            if toggle1:
            #if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if query.startswith("UUFA_BR_ACAD_LVLS_OUT_SYNC")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BR_ATH_TUIT_INCR_NR")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BR_ATH_TUITION_INCRS")  :
                    return (query, renamed, directory, move_directory)

                if "_BR_BDGT_DOUBLE_BUDGETS" in query :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BR_COA_LESS_HT")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BR_COA_TUIT_ZERO")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BR_DN_LW_MD_AID_ATRB")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BR_FT_CLASS_OVERRIDES")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BR_COA_ISIR_BDGT_DIFF")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BR_NO_BUDGET_ATTEND")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BR_PELL_COA_BLANK")  :
                    return (query, renamed, directory, move_directory)

                if (("BR_PELL_COA_CHECK" in query) ) :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BR_PELL_COA_DOUBLE")  :
                    return (query, renamed, directory, move_directory)

                if "BR_PELL_COA_DBLD_WRNG" in query  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("FA_BR_PELL_COA_LESS_HT_20")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BR_PROC_STAT_RVW_STAT")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BR_RES_NON_RES_BDGT")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BR_SCH_TUITION_FEES_NR")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BR_SCH_TUITION_ONLY_NR")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BR_SCHOLAR_TUIT_FEES")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BR_SCHOLAR_TUIT_ONLY")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("FA_BR_UFORM_CHANGE_BUD_DUR")  :
                    return (query, renamed, directory, move_directory)

                if "BR_ACAD_LVLS_NOT_SYNC" in query  :
                    return (query, renamed, directory, move_directory)

                if "BR_ACAD_LVLS_NOT_SYNC" in query  :
                    return (query, renamed, directory, move_directory)
    
#Budget Testing Queries
def do_budget_test_queries(test, date, year, query, aid_year_match):
    #global aid_year
    #for query_name in os.listdir("."):
    #    if query_name.startswith("UUFA_BUDGET"):
    #        year = str(int(re.search(r'\d+', query_name).group()))
    #        break
    #aid_year = "20" + str(int(year) - 1) + "-20" + year
    aid_year = str(int(year - 1)) + "-" + str(year)
    month_folder = date[:2] + "-20" + date[-2:]

    # Create FOLDER variables to be used in Move() operation and establishes
    # the directory to save the files
    # using the date.
    # Create variables to be used in Move() operation.
    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/Budgets', aid_year, month_folder,"Wrong Budget Queries"))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Budgets', aid_year, month_folder, "Wrong Budget Queries"))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    year = year[2:]
    dot_index = query.find(".")
    dash_index = query.rfind("-")
    renamed = date + " " + query[dash_index:] + " " + year + query[:dot_index]

    move_directory = "Budget Reports"

    toggle2 = True;

    # Change File_Name to be query AC it is received and _new_file_name to what
    # the new query should be.  Prefix date
    # will be added.
    if aid_year_match:
    #if ("22" in query_name.split("-")[0]):
        if True:
        #for query in os.listdir("."):
            if query.startswith("UUFA_BUDGET_20" + year + "_DN1"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_DN2"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_DN3"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_DN4"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_ACCTMAC"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_ARCHMAR"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_BUSINESS"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_COMDIS"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_EAEMS"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_EDUCATION"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_ED_PSYCH"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_ENGINERING"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_FINE_ARTS"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_GENERAL_GR"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_GENETICS"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_HEALTH"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_PRO_HEALTH"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_HUMANITIES"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_MBA_BUADMB"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_MD_SCIENCE"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_MEDICAL"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_NURSING"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_PA"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_PHARMACY"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_PLANNING"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_PMBAMBA"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_PUBLICPOLI"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_PUBLIC_ADM"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_SCIENCE"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_SOC_BEHAV"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_SW"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_XMBAMBA"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_LW1"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_LW2"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_LW3"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_MD1"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_MD2"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_MD3"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_MD4"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_UNDERGRAD"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_UG_BUSINESS"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_UG_BUS_LTHT"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_UG_ENGINERING"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_UG_ENG_LTHT"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_UG_LTHT"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_UG_NURSE_LTHT"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_BUDGET_20" + year + "_UG_NURSING"):
                return (query, renamed, directory, move_directory)
                
    else:
        if True:
        #for query in os.listdir("."):
            if toggle2:
            #if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if query.startswith("UUFA_BUDGET_20" + year + "_DN1"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_DN2"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_DN3"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_DN4"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_ACCTMAC"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_ARCHMAR"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_BUSINESS"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_COMDIS"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_EAEMS"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_EDUCATION"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_ED_PSYCH"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_ENGINERING"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_FINE_ARTS"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_GENERAL_GR"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_GENETICS"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_HEALTH"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_PRO_HEALTH"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_HUMANITIES"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_MBA_BUADMB"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_MD_SCIENCE"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_MEDICAL"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_NURSING"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_PA"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_PHARMACY"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_PLANNING"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_PMBAMBA"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_PUBLICPOLI"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_PUBLIC_ADM"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_SCIENCE"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_SOC_BEHAV"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_SW"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_XMBAMBA"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_LW1"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_LW2"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_LW3"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_MD1"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_MD2"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_MD3"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_MD4"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_UNDERGRAD"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_UG_BUSINESS"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_UG_BUS_LTHT"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_UG_ENGINERING"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_UG_ENG_LTHT"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_UG_LTHT"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_UG_NURSE_LTHT"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_BUDGET_20" + year + "_UG_NURSING"):
                    return (query, renamed, directory, move_directory)
