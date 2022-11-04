# Packaging Queries - to be modified 
# to be called in main
import os

def do_packaging_queries(test, date, year, query, aid_year_match):
    #global aid_year
    #year = "23"
    #for query_name in os.listdir("."):
    #    if query_name.startswith("UUFA_PRT_ACAD_PROG_REVIEW"):
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
        directory = os.path.realpath(os.path.join('C:\Testing Bob/Packaging', aid_year, month_folder))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Packaging', aid_year, month_folder))

    # the list 'my_path' should be populated with the FOLDER variables above.
    if not os.path.isdir(directory):
        os.makedirs(directory)

    year = year[2:]
    dot_index = query.find(".")
    dash_index = query.rfind("-")
    renamed = date + " " + query[dash_index:] + " " + year + query[:dot_index]

    move_directory = "Scholarship Reports"

    toggle = True

    # Change File_Name to be query AC it is received and _new_file_name to what
    # the new query should be.  Prefix date
    # will be added.
    if aid_year_match:
    #if (year in query_name.split("-")[0]) or (str(int(year)-1) in query_name.split("-"[0])):
        if True:
        #for query in os.listdir("."):
            if query.startswith("UUFA_PRT_ACAD_LVLS_OUT_SYNC"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_ACAD_PROG_REVIEW") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_ATH_ACCEPT_FED_AID"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_ATH_AWD_CBA_GRANT"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_ATH_GRAD_DATE"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_ATH_OFFRD_FED_AID"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_ATH_OFFR_ACCPT_AID") :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_AWARD_TERM_HAD_SAP"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_AWARDS_OTHER_INST"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_AWD_CMB_OVR_AG_RVW"):
                return (query, renamed, directory, move_directory)

            if query.startswith("FA_PRT_AWD_MASS_P_NO_AWARDS"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_AWD_PLL_ELG_NO_PLL") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_AWD_SUB_OVR_AG_RVW"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_CTZN_IND_AWD_NO_LN"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_DEFR_ENROLLMENT") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_DEP_PRNT_SSN_RVW"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_DIAG_AWD_PELL_TERM") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("FA_PRT_DISB_PLAN_SPLT_CODE") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_DL_DPAY_SCSP") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_DSB_PLN_SPLT_CD_FD") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_DSB_PLN_SPLT_CD_SC") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_EXPECT_GRAD_TERM_11"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_DL_GRAD_TERM_FALL") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_GRAD_TRM_FALL") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_GRAD_TRM_SPRING") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_HEAL"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_LEU_C_PELL_FSEOG") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_LEU_C_PELL_AWARD") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_LEU_E_PELL_FSEOG") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_LN_CBA_AWD_NO_ELIG"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_NO_FALL_11" + str(int(year) - 1) + "8"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_NSL_LOAN_RPT_VERI") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_NURSING_LOAN_RPT") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_ON_LINE_PACKAGING"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_PELL_COMMENT_037") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_PELL_ELG_NO_PELL") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_PLL_EL_CTZN_NOT_INDCT"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_PELL_FPEL" + year + "_INITIATED"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_PELL_UG_5TH_YR_2ND_BA"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_PHARM_NO_HEAL"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_PKG_AWD_NO_BDGT"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_PKG_SCH_AWD_NO_BGT") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_PRIOR_TERM_STFFRD_OFR"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_READY_PKG_20" + year):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_SCHOL_GRAD_DATE"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_SUB_UNSUB_SP_SP"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_SET_HEAL_FLAG") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_STATE_OF_RES_FM_MH_PW"):
                return (query, renamed, directory, move_directory)

            if query.startswith("FA_PRT_STILL_UNPRCD_AFTER_PKG"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_STDNT_NOT_PACKAGED") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_PRT_TEACH_CREDENTIAL") and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("PRT_SUB_UNSUB_FA_FA") in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("PRT_PELL_PKG_LOAD_CHCK") in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("PRT_COUNT_ITEM_TYPE") in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("PKG_NOT_PKGD_NO_UNITS") in query :
                return (query, renamed, directory, move_directory)
                
    else:
        if True:
        #for query in os.listdir("."):
            if toggle:
            #if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if query.startswith("UUFA_PRT_ACAD_LVLS_OUT_SYNC"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_ACAD_PROG_REVIEW")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_ATH_ACCEPT_FED_AID"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_ATH_AWD_CBA_GRANT"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_ATH_GRAD_DATE"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_ATH_OFFRD_FED_AID"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_ATH_OFFR_ACCPT_AID")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_AWARD_TERM_HAD_SAP"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_AWARDS_OTHER_INST"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_AWD_CMB_OVR_AG_RVW"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("FA_PRT_AWD_MASS_P_NO_AWARDS"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_AWD_PLL_ELG_NO_PLL")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_AWD_SUB_OVR_AG_RVW"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_CTZN_IND_AWD_NO_LN"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_DEFR_ENROLLMENT")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_DEP_PRNT_SSN_RVW"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_DIAG_AWD_PELL_TERM")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("FA_PRT_DISB_PLAN_SPLT_CODE")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_DL_DPAY_SCSP")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_DSB_PLN_SPLT_CD_FD")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_DSB_PLN_SPLT_CD_SC")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_EXPECT_GRAD_TERM_11"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_DL_GRAD_TERM_FALL")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_GRAD_TRM_FALL")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_GRAD_TRM_SPRING")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_HEAL"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_LEU_C_PELL_FSEOG")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_LEU_C_PELL_AWARD")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_LEU_E_PELL_FSEOG")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_LN_CBA_AWD_NO_ELIG"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_NSL_LOAN_RPT_VERI")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_NURSING_LOAN_RPT")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_ON_LINE_PACKAGING"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_PELL_COMMENT_037")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_PELL_ELG_NO_PELL")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_PLL_EL_CTZN_NOT_INDCT"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_PELL_UG_5TH_YR_2ND_BA"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_PHARM_NO_HEAL"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_PKG_AWD_NO_BDGT"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_PKG_SCH_AWD_NO_BGT")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_PRIOR_TERM_STFFRD_OFR"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_SCHOL_GRAD_DATE"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_SUB_UNSUB_SP_SP"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_SET_HEAL_FLAG")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_STATE_OF_RES_FM_MH_PW"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("FA_PRT_STILL_UNPRCD_AFTER_PKG"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_STDNT_NOT_PACKAGED")  :
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_PRT_TEACH_CREDENTIAL")  :
                    return (query, renamed, directory, move_directory)

                if ("PRT_SUB_UNSUB_FA_FA") in query  :
                    return (query, renamed, directory, move_directory)

                if ("PRT_PELL_PKG_LOAD_CHCK") in query  :
                    return (query, renamed, directory, move_directory)

                if ("PRT_COUNT_ITEM_TYPE") in query  :
                    return (query, renamed, directory, move_directory)

                if ("PKG_NOT_PKGD_NO_UNITS") in query  :
                    return (query, renamed, directory, move_directory)
                    
                if query.startswith("UUFA_READY_PACKAGE" + year):
                    return (query, renamed, directory, move_directory)

