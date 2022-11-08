# Monday Weekly Queries 

# To be modified and called in Main 
import os

def do_monday_weeklies(test, date, year, query, renamed, aid_year_match):
    #global aid_year
    #global year
    #for query_name in os.listdir("."):
    #    if query_name.startswith("UUFA_WR"):
    #        year = str(int(re.search(r'\d+', query_name).group()))
    #        break
    #aid_year = "20" + str(int(year) - 1) + "-20" + year
    aid_year = str(int(year) - 1) + "-" + str(year)
    month_folder = date[:2] + "-20" + date[-2:]

    # Create FOLDER variables to be used in Move() operation and establishes
    # the directory to save the files
    # using the date.
    if test:
        directory               = os.path.realpath(os.path.join('C:/Testing Bob/Monday Weekly', aid_year, month_folder))
        packaging_directory     = os.path.realpath(os.path.join('C:/Testing Bob/Packaging', aid_year, month_folder))
        disb_failure_directory  = os.path.realpath(os.path.join('C:/Testing Bob/Disb Failure ' + aid_year))
        save_directory          = os.path.realpath(os.path.join('C:/Testing Bob/SAVE', aid_year))
    else:
        directory               = os.path.realpath(os.path.join('O:/Systems/QUERIES/Monday Weekly', aid_year, month_folder))
        packaging_directory     = os.path.realpath(os.path.join('O:/Systems/QUERIES/Packaging', aid_year, month_folder))
        disb_failure_directory  = os.path.realpath(os.path.join('O:/Disbursement Failure/Disb Failure ' + aid_year))
        save_directory          = os.path.realpath(os.path.join('O:/Systems/QUERIES/SAVE', aid_year))

    if not os.path.isdir(directory):
        os.makedirs(directory)
    if not os.path.isdir(packaging_directory):
        os.makedirs(packaging_directory)
    if not os.path.isdir(disb_failure_directory):
        os.makedirs(disb_failure_directory)
    if not os.path.isdir(save_directory):
        os.makedirs(save_directory)

    year = year[2:]

    move_directory = "Weekly Reports"
    pack_directory = "Weekly Reports"
    disb_directory = "Weekly Reports"
    other_directory = "Weekly Reports"

    toggle = True

    # Change File_Name to be query ac it is received and _new_file_name to what
    # the new query should be.Prefix date
    # will be added.
    if aid_year_match:
    #if ("22" in query_name.split("-")[0]):
        if True:
        #for query in os.listdir("."):
            if "_WR_ACAD_LVLS_OUT_SYNC" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_ADV_FSOI_INITIATED" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_AGG_CK_MLT_YR_AWDED" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_AID_DISB_NO_ENR_ATH" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_AID_DISB_NO_ENR_FED" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_AID_DISB_NO_ENR_SCH" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_ALL_V4_V5_VER" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_AMERICORP_AWD_POST" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_ATHLETE_NOT_DISB" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_ATH_HRS_AFTR_CENSUS" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_ATH_SF_TERM_BALANCE" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_AUDIT_CLSS_AID_DISB" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_ISA_PER_TERM" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_AWD_UG_NOW_GRAD_ATH" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_AWD_UG_NOW_GRAD_FC" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_AWD_UG_NOW_GRAD_SV" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_CHKLST_STATUS_ERROR" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "WR_CMT_CDE_O_AGR_LMT_2" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "_WR_DISB_ATH_FAILURE" in query and (year in query[:-8]) :
                return (query, renamed, disb_failure_directory, disb_directory)

            if "_WR_DL_DISBURSED_LTHT" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_DL_EC_SUSPENDED" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_DL_ORIG_TRNS_PEND" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_EFT_CONSENT_VERIF" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_FAFSA_CKLST_INCMP" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if  "_WR_FALL_TOTAL_WDRN_DRP" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if  "_WR_SPR_TOTAL_WDRN_DRP" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if  "WR_SNGDO_CAMPUS" in query and year in query[:-8] :
                return (query, renamed, directory, move_directory)

            if  "_WR_SUM_TOTAL_WDRN_DRP" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_FARC_CHECKLIST" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_FARC_CMNT_CODES" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_FED_AID_OVERAWARD" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_FGED_ISIR_DEGREE" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("_WR_FPEL" + year + "_INITIATED_AWDED") in query:
                return (query, renamed, directory, move_directory)

            if "WR_FREV_GR_WS" in query and year in query:
                return (query, renamed, directory, move_directory)

            if "_WR_GENDER" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_HEDU_PARAMEDIC" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "R_HOME_SCHOOLED" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_HRS_DECREASE_ATH" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_HRS_DECREASE_FC" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_HRS_DECREASE_SV" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_FHST_I_HST_COMPLETE" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_ISIR_AS_EFC" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_ISIR_COR_ASSESSMENT" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_ISIR_CORR_REJECT" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_ISIR_DGR_ANSW_CHNG" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_ISIR_DEP_STAT_PRB" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_ISIR_REJECTED_CORR" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if ("UUFA_WR_ISIR_REJECT_CODES" in query and year in query[:-8]) \
                    | (("UUFA_WR_ISIR_REJECT_CODES_20") in query and (year in query[:-8])) :
                return (query, renamed, directory, move_directory)

            if "_WR_ISIR_SS_MCH_NOT_CON" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_ISIR_SUSPENSE" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_LEGAL_ALIEN_WORK" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_LN_ACCPT_STAF_31_32" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_LOAN_CENSUS_DATE" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_LN_FA907_1_REVISED" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_LN_FA907_2_REVISED" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "R_LOAN_ORIG_DEPT_REVIEW" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_LN_SENT_NO_RESPONSE" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_LOAN_TRANSMIT_HOLD" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_LW_MD_DN_AW_NO_DISB" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_MNTGMR_AMCORP_OVRAW" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_MULTIPLE_EMPLIDS" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_NO_COMMENT_CODE" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_NSLDS_LOAN_DATA" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_OVRD_ACAD_LVL" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_PA_EXPECT" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_PA_FDEG_CHECKLIST" in query:
                return (query, renamed, directory, move_directory)

            if "_WR_PELL_AWRD_LOCK" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_PELL_OVERPAYMENT" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_PELL_SUMMER_NO_PELL" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "WR_PELL_SUMMER_AGGS" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_PELL_TERM_FT" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_PELL_TERM_HT" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_PELL_TERM_LH" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_PELL_TERM_NL" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_PELL_TERM_TQ" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_PERK_SPLIT_MISMATCH" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_PRK_LN_ACAD_LVL_CHG" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_QUALITY_ASSURANCE" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "R_RT4_DROPPED_CLASSES" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_SCH_NOT_DISB" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_SCHOLAR_TBP_NO_AWRD" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "_WR_GRAD_FELLOW" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "_WR_SSR_MATCH_NOT_CNFRM" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_SSR_NOT_CNFRMD_VTRN" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_SS_DB_OVERRIDE" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_SUB_ISIR_PACKAGED" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_SUB_ISIR_REAWD_AID" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_SUB_ISIR_SYSG" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_SUB_ISIR_VERIFIED" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_SUMMER_NO_DL" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_SUMMER_PELL_LTHT" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_SSP_DOB_PRB_APPLCNT" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_SSP_NAME_PRB_APLCNT" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_SSP_SSN_PRB_APLCNT" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_TERM_NSLDS_LOAN_YR" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_TITLE_VII_MED_LOANS" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_TRANSFER_ENT_CNS" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_TRANSFER_STU_FA_SP" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_UG_GR_DIR_LN_GR_TRM" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_UG_GR_PLUS_GR_TERM" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "WR_UAC_FASI_STATUS" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_UAC_SNGDO" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_UNDOCUMENTED_STUDENTS" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_VERI_CHKLST_MISSING" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_VERI_INCOME_ADJ" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_VER_NOT_CONSL" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_VETERAN_ACTIVE_DUTY" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_VETERAN_NO_QUALIFY" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_WEEKS_OF_INSTR_FIX" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_DL_AY_SP_CANCELED" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_LOAN_TRANSMIT_HOLD_13" in query:
                return (query, renamed, directory, move_directory)

            if "_WR_REJECT_CODE_ON_ISIR" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_RT4_FA_DROP_CLASSES" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_RT4_SP_DROP_CLASSES" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_RT4_SU_DROP_CLASSES" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "WR_AWARDS_OTHER_INST" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "WR_DEP_PRNT_SSN_RVW" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "WR_DN_LW_MD_AID_ATRB" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "WR_FSEOG_NO_PELL" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "WR_FT_CLASS_OVERRIDES" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "WR_GR_ACAD_LV_OUT_SYNC" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "WR_PELL_COA_DOUBLE" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "WR_PKG_AWD_NO_BDGT" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "WR_SCH_TUITION_FEES" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "WR_SCHOL_GRAD_DATE" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "_WR_STDNT_NOT_PACKAGED" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "WR_SAVE_CTZNSHIP_VER" in query and (year in query[:-8]) :
                return (query, renamed, save_directory, other_directory)

            if "WR_ALL_C_FVRA_I_NO_COR" in query and (year in query[:-8]) :
                return (query, renamed, save_directory, other_directory)

            if "WR_CORRECTION_NOT_SENT" in query and (year in query[:-8]) :
                return (query, renamed, save_directory, other_directory)

            # Manually run Queries
            if "_WR_LOAN_EFT_DETAIL_ERROR" in query:
                return (query, renamed, directory, move_directory)

            if "_WR_NSL_PROMISSORY_NOTE" in query and (year in query[:-8]) :
                return (query, renamed, directory, move_directory)

            if "UUFA_AP_RPKG_FPEL_AWARD_LCK" in query:
                return (query, renamed, directory, move_directory)

            if "WR_FAVR_I_NO_FCOR_ALL_C" in query:
                return (query, renamed, directory, move_directory)

            # Packaging queries that are being manually run.
            if "PRT_ATH_ACCEPT_FED_AID" in query and (year in query[:-8]) :
                return (query, renamed, packaging_directory, pack_directory)

            if "PRT_ATH_AWD_CBA_GRANT" in query and (year in query[:-8]) :
                return (query, renamed, packaging_directory, pack_directory)

            if "PRT_ATHLETE_GRAD_DATE" in query and (year in query[:-8]) :
                return (query, renamed, packaging_directory, pack_directory)

            if "PRT_ATH_OFFERED_FED_AID" in query and (year in query[:-8]) :
                return (query, renamed, packaging_directory, pack_directory)
    
    else:
        if True:
        #for query in os.listdir("."):
            if toggle:
            #if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if "_WR_ACAD_LVLS_OUT_SYNC" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_ADV_FSOI_INITIATED" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_AGG_CK_MLT_YR_AWDED" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_AID_DISB_NO_ENR_ATH" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_AID_DISB_NO_ENR_FED" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_AID_DISB_NO_ENR_SCH" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_ALL_V4_V5_VER" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_AMERICORP_AWD_POST" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_ATHLETE_NOT_DISB" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_ATH_HRS_AFTR_CENSUS" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_ATH_SF_TERM_BALANCE" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_AUDIT_CLSS_AID_DISB" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_ISA_PER_TERM" in query :
                    return (query, renamed, directory, move_directory) 

                if "_WR_AWD_UG_NOW_GRAD_ATH" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_AWD_UG_NOW_GRAD_FC" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_AWD_UG_NOW_GRAD_SV" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_CHKLST_STATUS_ERROR" in query :
                    return (query, renamed, directory, move_directory)

                if "WR_CMT_CDE_O_AGR_LMT_2" in query and year in query[:-8]:
                    return (query, renamed, directory, move_directory)

                if "_WR_DISB_ATH_FAILURE" in query :
                    return (query, renamed, disb_failure_directory, disb_directory)

                if "_WR_DL_DISBURSED_LTHT" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_DL_EC_SUSPENDED" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_DL_ORIG_TRNS_PEND" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_EFT_CONSENT_VERIF" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_FAFSA_CKLST_INCMP" in query :
                    return (query, renamed, directory, move_directory)

                if  "_WR_FALL_TOTAL_WDRN_DRP" in query :
                    return (query, renamed, directory, move_directory)

                if  "_WR_SPR_TOTAL_WDRN_DRP" in query :
                    return (query, renamed, directory, move_directory)

                if  "WR_SNGDO_CAMPUS" in query and year in query[:-8] :
                    return (query, renamed, directory, move_directory)

                if  "_WR_SUM_TOTAL_WDRN_DRP" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_FARC_CHECKLIST" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_FARC_CMNT_CODES" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_FED_AID_OVERAWARD" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_FGED_ISIR_DEGREE" in query :
                    return (query, renamed, directory, move_directory)

                if ("_WR_FPEL" + year + "_INITIATED_AWDED") in query:
                    return (query, renamed, directory, move_directory)

                if "WR_FREV_GR_WS" in query and year in query:
                    return (query, renamed, directory, move_directory)

                if "_WR_GENDER" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_HEDU_PARAMEDIC" in query :
                    return (query, renamed, directory, move_directory)

                if "R_HOME_SCHOOLED" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_HRS_DECREASE_ATH" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_HRS_DECREASE_FC" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_HRS_DECREASE_SV" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_FHST_I_HST_COMPLETE" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_ISIR_AS_EFC" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_ISIR_COR_ASSESSMENT" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_ISIR_CORR_REJECT" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_ISIR_DGR_ANSW_CHNG" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_ISIR_DEP_STAT_PRB" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_ISIR_REJECTED_CORR" in query :
                    return (query, renamed, directory, move_directory)

                if ("UUFA_WR_ISIR_REJECT_CODES" in query and year in query[:-8]) \
                        | (("UUFA_WR_ISIR_REJECT_CODES_20") in query and (year in query[:-8])) :
                    return (query, renamed, directory, move_directory)

                if "_WR_ISIR_SS_MCH_NOT_CON" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_ISIR_SUSPENSE" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_LEGAL_ALIEN_WORK" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_LN_ACCPT_STAF_31_32" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_LOAN_CENSUS_DATE" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_LN_FA907_1_REVISED" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_LN_FA907_2_REVISED" in query :
                    return (query, renamed, directory, move_directory)

                if "R_LOAN_ORIG_DEPT_REVIEW" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_LN_SENT_NO_RESPONSE" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_LOAN_TRANSMIT_HOLD" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_LW_MD_DN_AW_NO_DISB" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_MNTGMR_AMCORP_OVRAW" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_MULTIPLE_EMPLIDS" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_NO_COMMENT_CODE" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_NSLDS_LOAN_DATA" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_OVRD_ACAD_LVL" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_PA_EXPECT" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_PA_FDEG_CHECKLIST" in query:
                    return (query, renamed, directory, move_directory)

                if "_WR_PELL_AWRD_LOCK" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_PELL_OVERPAYMENT" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_PELL_SUMMER_NO_PELL" in query :
                    return (query, renamed, directory, move_directory)

                if "WR_PELL_SUMMER_AGGS" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_PELL_TERM_FT" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_PELL_TERM_HT" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_PELL_TERM_LH" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_PELL_TERM_NL" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_PELL_TERM_TQ" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_PERK_SPLIT_MISMATCH" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_PRK_LN_ACAD_LVL_CHG" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_QUALITY_ASSURANCE" in query :
                    return (query, renamed, directory, move_directory)

                if "R_RT4_DROPPED_CLASSES" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_SCH_NOT_DISB" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_SCHOLAR_TBP_NO_AWRD" in query and year in query[:-8]:
                    return (query, renamed, directory, move_directory)

                if "_WR_GRAD_FELLOW" in query and year in query[:-8]:
                    return (query, renamed, directory, move_directory)

                if "_WR_SSR_MATCH_NOT_CNFRM" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_SSR_NOT_CNFRMD_VTRN" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_SS_DB_OVERRIDE" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_SUB_ISIR_PACKAGED" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_SUB_ISIR_REAWD_AID" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_SUB_ISIR_SYSG" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_SUB_ISIR_VERIFIED" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_SUMMER_NO_DL" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_SUMMER_PELL_LTHT" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_SSP_DOB_PRB_APPLCNT" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_SSP_NAME_PRB_APLCNT" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_SSP_SSN_PRB_APLCNT" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_TERM_NSLDS_LOAN_YR" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_TITLE_VII_MED_LOANS" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_TRANSFER_ENT_CNS" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_TRANSFER_STU_FA_SP" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_UG_GR_DIR_LN_GR_TRM" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_UG_GR_PLUS_GR_TERM" in query :
                    return (query, renamed, directory, move_directory)

                if "WR_UAC_FASI_STATUS" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_UAC_SNGDO" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_UNDOCUMENTED_STUDENTS" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_VERI_CHKLST_MISSING" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_VERI_INCOME_ADJ" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_VER_NOT_CONSL" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_VETERAN_ACTIVE_DUTY" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_VETERAN_NO_QUALIFY" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_WEEKS_OF_INSTR_FIX" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_DL_AY_SP_CANCELED" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_LOAN_TRANSMIT_HOLD_13" in query:
                    return (query, renamed, directory, move_directory)

                if "_WR_REJECT_CODE_ON_ISIR" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_RT4_FA_DROP_CLASSES" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_RT4_SP_DROP_CLASSES" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_RT4_SU_DROP_CLASSES" in query :
                    return (query, renamed, directory, move_directory)

                if "WR_AWARDS_OTHER_INST" in query :
                    return (query, renamed, directory, move_directory)

                if "WR_DEP_PRNT_SSN_RVW" in query :
                    return (query, renamed, directory, move_directory)

                if "WR_DN_LW_MD_AID_ATRB" in query :
                    return (query, renamed, directory, move_directory)

                if "WR_FSEOG_NO_PELL" in query :
                    return (query, renamed, directory, move_directory)

                if "WR_FT_CLASS_OVERRIDES" in query :
                    return (query, renamed, directory, move_directory)

                if "WR_GR_ACAD_LV_OUT_SYNC" in query :
                    return (query, renamed, directory, move_directory)

                if "WR_PELL_COA_DOUBLE" in query :
                    return (query, renamed, directory, move_directory)

                if "WR_PKG_AWD_NO_BDGT" in query :
                    return (query, renamed, directory, move_directory)

                if "WR_SCH_TUITION_FEES" in query :
                    return (query, renamed, directory, move_directory)

                if "WR_SCHOL_GRAD_DATE" in query :
                    return (query, renamed, directory, move_directory)

                if "_WR_STDNT_NOT_PACKAGED" in query :
                    return (query, renamed, directory, move_directory)

                if "WR_SAVE_CTZNSHIP_VER" in query :
                    return (query, renamed, save_directory, other_directory)

                if "WR_ALL_C_FVRA_I_NO_COR" in query :
                    return (query, renamed, save_directory, other_directory)

                if "WR_CORRECTION_NOT_SENT" in query :
                    return (query, renamed, save_directory, other_directory)

                # Manually run Queries
                if "_WR_LOAN_EFT_DETAIL_ERROR" in query:
                    return (query, renamed, directory, move_directory)

                if "_WR_NSL_PROMISSORY_NOTE" in query :
                    return (query, renamed, directory, move_directory)

                if "UUFA_AP_RPKG_FPEL_AWARD_LCK" in query:
                    return (query, renamed, directory, move_directory)

                if "WR_FAVR_I_NO_FCOR_ALL_C" in query:
                    return (query, renamed, directory, move_directory)

                # Packaging queries that are being manually run.
                if "PRT_ATH_ACCEPT_FED_AID" in query :
                    return (query, renamed, packaging_directory, pack_directory)

                if "PRT_ATH_AWD_CBA_GRANT" in query :
                    return (query, renamed, packaging_directory, pack_directory)

                if "PRT_ATHLETE_GRAD_DATE" in query :
                    return (query, renamed, packaging_directory, pack_directory)

                if "PRT_ATH_OFFERED_FED_AID" in query :
                    return (query, renamed, packaging_directory, pack_directory)
    return "Empty"
