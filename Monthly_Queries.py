# Monthly Queries - to be modified
# to be called in main 
import calendar
import datetime
import os

def do_monthlies(test, date, year, query, renamed, aid_year_match):
    #aid_year = "2023"
    #year = "23"
    #for query_name in os.listdir("."):
    #    if "MR_PELL_SSN_MISMATCH" in query_name:
    #        if str(int(re.search(r'\d+', query_name).group())) == "22":
    #            year = "22"
    #        break
    #aid_year = "20" + str(int(year) - 1) + "-20" + year
    now = datetime.datetime.now()
    last_month = now.month - 1 if now.month > 1 else 12
    last_months_year = now.year - 1 if now.month == 12 else now.year
    month_folder = date[:2] + "-20" + date[-2:]
    t_path = "Award Summary " + year + "/Award Summary " + calendar.month_name[last_month] + " " + str(last_months_year)

    # Create FOLDER variables to be used in Move() operation and establishes
    # the directory to save the files
    # using the date.
    # Create variables to be used in Move() operation.
    if test:
        directory = os.path.realpath(os.path.join('C:/Testing Bob/Monthly', month_folder))
        dl_directory = os.path.realpath(os.path.join('C:/Testing Bob/Direct Loans', 'Monthly'))
        acct_directory = os.path.realpath(os.path.join('C:/Testing Bob/ACCT/Chartfields'))
        t_directory = os.path.realpath(os.path.join('C:/Testing Bob/ACCT/Award Summary', t_path))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Monthly', month_folder))
        dl_directory = os.path.realpath(os.path.join('O:/Systems/Direct Loans','Monthly'))
        acct_directory = os.path.realpath(os.path.join('O:/ACCT/Chartfields'))
        t_directory = os.path.realpath(os.path.join('O:/ACCT/Award Summary', t_path))

    # the list 'my_path' should be populated with the FOLDER variables above.
    if not os.path.isdir(directory):
        os.makedirs(directory)
    if not os.path.isdir(dl_directory):
        os.makedirs(dl_directory)
    if not os.path.isdir(acct_directory):
        os.makedirs(acct_directory)
    if not os.path.isdir(t_directory):
        os.makedirs(t_directory)

    year = year[2:]

    move_directory = "Monthly Reports"
    direct_directory = "Monthly Reports"
    chart_directory = "Monthly Reports"
    award_directory = "Monthly Reports"

    toggle = True

    # Change File_Name to be file ac it is received and _new_file_name to what
    # the new file should be.  Prefix date
    # will be added.
    if aid_year_match:
    #if ("22" in query_name.split("-")[0]):
        if True:
        #for query in os.listdir("."):
            if "MR_COMMENT_CODE_298" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_3RD_PARTY_CROSSWALK" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_3RD_PRT_MNTR_IA_ALL" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_ACAD_LVLS_NOT_SYNC" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_ADM_DEFERRAL" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_ALT_LN_TRNSMIT_HOLD" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_ATHLETE_T53_AWARDS" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_COD_DL" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_COD_PELL_TEACH_IASG" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_DIR_LN_TRNSMIT_HOLD" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_DISB_ATH_AWD_NOPOST" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_DL_DISB_FAILED" in query and year in query[:-8]:
                return (query, renamed, dl_directory, direct_directory)

            if "MR_DL_ORIG_AWARD" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_DSB_CASH_AWD_NOPOST" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_DSB_WAVR_AWD_NOPOST" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "DSB_AWD_NOPOST" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_DN_INC_CHECKLISTS" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_M_L_D_INI_CHECKLIST" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_FWS_WITH_NSI_HOLD" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_GRAD_TERM_PRB" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_ITEM_CHARTFLD_SETUP" in query and year in query[:-8]:
                return (query, renamed, acct_directory, chart_directory)

            if "MR_ITEM_TYPE_DISB_RULE" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_LAW_INC_CHECKLISTS" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_LOAN_AWD_PARTL_DISB" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_MED_INC_CHECKLISTS" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_MED_LAW_LVL_REVIEW" in query or "_MR_DN_LW_MD_LVL_RVW" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_PART_TW_OTHER_SCH" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_PELL_AWD_ADJUSTMENT" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_PELL_ONLY" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_PELL_SSN_MISMATCH" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_PERKINS_CLASS_LIMIT" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_PERK_MISC_LN_CNCLD" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_PERK_MISC_LOAN_DISB" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "_MR_SCH_IT_RECON" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_SCH" in query and "LOA" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "SCHOLAR_REINSTATE" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_SF_DIS_AWD_PT_ER_FC" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_SF_DIS_AWD_PT_ER_SV" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_STATE_FM_MH_PW" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_SUSPEND_RC2" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_UFORM_GRAD_TERM_PRB" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_UNDS_OFFER_SCHOLAR" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_UNDS_OFRD_AMT_FDRL" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_UNDS_OFRD_AMT_ATH" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_VERIFY_DEP_OVERRIDE" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "MR_GRBEN_EA_POST" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "SEFA_DL_TOTAL_AWARDS" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "SEFA_TOTAL_STUDENT" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "STP_DISB_RULE_MISMATCH" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "ussfa037" in query and year in query:
                return (query, renamed, t_directory, award_directory)

            if "ussfa035-" in query and year in query:
                return (query, renamed, t_directory, award_directory)

            if "MR_EXPIRED_MPN_CURR_LN" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)

            if "_MR_RNDM_GRAD_ENR_CHANG" in query and year in query[:-8]:
                return (query, renamed, directory, move_directory)            
    else:
        if True:
        #for query in os.listdir("."):
            if toggle:
            #if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if "MR_COMMENT_CODE_298" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_3RD_PARTY_CROSSWALK" in query :
                    return (query, renamed, directory, move_directory)
                    
                if "MR_FDEGRX_FABCX_FBLKD_FDG" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_3RD_PRT_MNTR_IA_ALL" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_ACAD_LVLS_NOT_SYNC" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_ADM_DEFERRAL" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_ALT_LN_TRNSMIT_HOLD" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_ATHLETE_T53_AWARDS" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_COD_DL" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_COD_PELL_TEACH_IASG" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_DIR_LN_TRNSMIT_HOLD" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_DISB_ATH_AWD_NOPOST" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_DL_DISB_FAILED" in query :
                    return (query, renamed, dl_directory, direct_directory)

                if "MR_DL_ORIG_AWARD" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_DSB_CASH_AWD_NOPOST" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_DSB_WAVR_AWD_NOPOST" in query :
                    return (query, renamed, directory, move_directory)

                if "DSB_AWD_NOPOST" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_DN_INC_CHECKLISTS" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_M_L_D_INI_CHECKLIST" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_FWS_WITH_NSI_HOLD" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_GRAD_TERM_PRB" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_ITEM_CHARTFLD_SETUP" in query :
                    return (query, renamed, acct_directory, chart_directory)

                if "MR_ITEM_TYPE_DISB_RULE" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_LAW_INC_CHECKLISTS" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_LOAN_AWD_PARTL_DISB" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_MED_INC_CHECKLISTS" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_MED_LAW_LVL_REVIEW" in query or "_MR_DN_LW_MD_LVL_RVW" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_PART_TW_OTHER_SCH" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_PELL_AWD_ADJUSTMENT" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_PELL_ONLY" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_PELL_SSN_MISMATCH" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_PERKINS_CLASS_LIMIT" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_PERK_MISC_LN_CNCLD" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_PERK_MISC_LOAN_DISB" in query :
                    return (query, renamed, directory, move_directory)

                if "_MR_SCH_IT_RECON" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_SCH" in query and "LOA" in query :
                    return (query, renamed, directory, move_directory)

                if "SCHOLAR_REINSTATE" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_SF_DIS_AWD_PT_ER_FC" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_SF_DIS_AWD_PT_ER_SV" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_STATE_FM_MH_PW" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_SUSPEND_RC2" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_UFORM_GRAD_TERM_PRB" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_UNDS_OFFER_SCHOLAR" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_UNDS_OFRD_AMT_FDRL" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_UNDS_OFRD_AMT_ATH" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_VERIFY_DEP_OVERRIDE" in query :
                    return (query, renamed, directory, move_directory)

                if "MR_GRBEN_EA_POST" in query :
                    return (query, renamed, directory, move_directory)

                if "SEFA_DL_TOTAL_AWARDS" in query :
                    return (query, renamed, directory, move_directory)

                if "SEFA_TOTAL_STUDENT" in query :
                    return (query, renamed, directory, move_directory)

                if "STP_DISB_RULE_MISMATCH" in query :
                    return (query, renamed, directory, move_directory)

                if "ussfa037" in query and year in query:
                    return (query, renamed, t_directory, award_directory)

                if "ussfa035-" in query and year in query:
                    return (query, renamed, t_directory, award_directory)

                if "MR_EXPIRED_MPN_CURR_LN" in query :
                    return (query, renamed, directory, move_directory)

                if "_MR_RNDM_GRAD_ENR_CHANG" in query :
                    return (query, renamed, directory, move_directory)
    return "Empty"

