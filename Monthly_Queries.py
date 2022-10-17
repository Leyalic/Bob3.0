# Monthly Queries - to be modified
# to be called in main 

def do_monthlies():
    aid_year = "2023"
    year = "23"
    for query_name in os.listdir("."):
        if "MR_PELL_SSN_MISMATCH" in query_name:
            if str(int(re.search(r'\d+', query_name).group())) == "22":
                year = "22"
            break
    aid_year = "20" + str(int(year) - 1) + "-20" + year
    t_path = "Award Summary 20" + year + "/Award Summary " + calendar.month_name[last_month] + " " + str(last_months_year)

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

    # Change File_Name to be file ac it is received and _new_file_name to what
    # the new file should be.  Prefix date
    # will be added.
    if ("22" in query_name.split("-")[0]):
        for query in os.listdir("."):
            if "MR_COMMENT_CODE_298" in query and year in query[:-8]:
                do_query(query, date + " IASG - Pell Eligible " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "MR_3RD_PARTY_CROSSWALK" in query and year in query[:-8]:
                do_query(query, date + " Third Party Crosswalk " + year + ".xls", directory,
                         hjr_mail.attachments)

            if "MR_3RD_PRT_MNTR_IA_ALL" in query and year in query[:-8]:
                do_query(query, date + " Third Party Monitor " + year + ".xls", directory,
                         hjr_mail.attachments)

            if "MR_ACAD_LVLS_NOT_SYNC" in query and year in query[:-8]:
                do_query(query, date + " Academic Levels out of SYNC " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "MR_ADM_DEFERRAL" in query and year in query[:-8]:
                do_query(query, date + " FA Admission Deferral " + year + ".xls", directory,
                         hjj_mail.attachments)

            if "MR_ALT_LN_TRNSMIT_HOLD" in query and year in query[:-8]:
                do_query(query, date + " Alt Loan Transmit Hold " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "MR_ATHLETE_T53_AWARDS" in query and year in query[:-8]:
                do_query(query, date + " Athlete T53 Awards Accepted " + year + ".xls", directory,
                         ath_mail.attachments)

            if "MR_COD_DL" in query and year in query[:-8]:
                do_query(query, date + " COD DL FATB" + year + " FCRD" + year + " FHMS" + year + ".xls", directory,
                         acnt_kkt_mail.attachments)

            if "MR_COD_PELL_TEACH_IASG" in query and year in query[:-8]:
                do_query(query, date + " COD Grant FCRD" + year + "-FHMS" + year + " Report.xls", directory,
                         acnt_kkt_mail.attachments)

            if "MR_DIR_LN_TRNSMIT_HOLD" in query and year in query[:-8]:
                do_query(query, date + " COD Direct Loan Transmit Hold " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "MR_DISB_ATH_AWD_NOPOST" in query and year in query[:-8]:
                do_query(query, date + " Athlete Waiver Disbursed Not Posted " + year + ".xls", directory,
                         ath_mail.attachments)

            if "MR_DL_DISB_FAILED" in query and year in query[:-8]:
                do_query(query, date + " DL Disbursement Failed " + year + ".xls", dl_directory,
                         krms_mail.attachments)

            if "MR_DL_ORIG_AWARD" in query and year in query[:-8]:
                do_query(query, date + " DL ORIG Award " + year + ".xls", directory,
                         loans_c_mail.attachments)

            if "MR_DSB_CASH_AWD_NOPOST" in query and year in query[:-8]:
                do_query(query, date + " Cash Disbursed Not Posted " + year + ".xls", directory,
                         hjj_mail.attachments)

            if "MR_DSB_WAVR_AWD_NOPOST" in query and year in query[:-8]:
                do_query(query, date + " Waiver-Scholarship Disbursed Not Posted " + year + ".xls", directory,
                         hj_mail.attachments)

            if "DSB_AWD_NOPOST" in query and year in query[:-8]:
                do_query(query, date + " Award Disbursed Not Posted " + year + ".xls", directory,
                         hjjk_mail.attachments)

            if "MR_DN_INC_CHECKLISTS" in query and year in query[:-8]:
                do_query(query, date + " Dental Students with I Checklists " + year + ".xls", directory,
                         prof_mail.attachments)

            if "MR_M_L_D_INI_CHECKLIST" in query and year in query[:-8]:
                do_query(query, date + " L-M-D Students with I Checklists " + year + ".xls", directory,
                         prof_mail.attachments)

            if "MR_FWS_WITH_NSI_HOLD" in query and year in query[:-8]:
                do_query(query, date + " FWS with NSI Holds.xls", directory,
                         acnt_mail.attachments)

            if "MR_GRAD_TERM_PRB" in query and year in query[:-8]:
                do_query(query, date + " Grad Term Wrong " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "MR_ITEM_CHARTFLD_SETUP" in query and year in query[:-8]:
                do_query(query, date + " Item Chartfield Setup.xls", acct_directory,
                         bhjkn_mail.attachments)

            if "MR_ITEM_TYPE_DISB_RULE" in query and year in query[:-8]:
                do_query(query, date + " Item Type Career - Match Disb Rule Career " + year + ".xls", directory,
                         ahjmv_mail.attachments)

            if "MR_LAW_INC_CHECKLISTS" in query and year in query[:-8]:
                do_query(query, date + " Law Students with I Checklists " + year + ".xls", directory,
                         prof_mail.attachments)

            if "MR_LOAN_AWD_PARTL_DISB" in query and year in query[:-8]:
                do_query(query, date + " Loan Awards Partial Disbursed " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "MR_MED_INC_CHECKLISTS" in query and year in query[:-8]:
                do_query(query, date + " Med Students with I Checklists " + year + ".xls", directory,
                         prof_mail.attachments)

            if "MR_MED_LAW_LVL_REVIEW" in query or "_MR_DN_LW_MD_LVL_RVW" in query and year in query[:-8]:
                do_query(query, date + " MED-LAW Academic Level Review " + year + ".xls", directory,
                         prof_mail.attachments)

            if "MR_PART_TW_OTHER_SCH" in query and year in query[:-8]:
                do_query(query, date + " Partial TW Other Scholarship " + year + ".xls", directory,
                         hj_mail.attachments)

            if "MR_PELL_AWD_ADJUSTMENT" in query and year in query[:-8]:
                do_query(query, date + " Pell Award Adjust " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "MR_PELL_ONLY" in query and year in query[:-8]:
                do_query(query, date + " Pell Awd  Zero Grants Loans " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "MR_PELL_SSN_MISMATCH" in query and year in query[:-8]:
                do_query(query, date + " SSN Mismatch " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "MR_PERKINS_CLASS_LIMIT" in query and year in query[:-8]:
                do_query(query, date + " Perkins Class Limits " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "MR_PERK_MISC_LN_CNCLD" in query and year in query[:-8]:
                do_query(query, date + " Perkins - Misc Loans Cancelled " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "MR_PERK_MISC_LOAN_DISB" in query and year in query[:-8]:
                do_query(query, date + " Perkins - Misc Loans Disbursed " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "_MR_SCH_IT_RECON" in query and year in query[:-8]:
                do_query(query, date + " Scholarship IT Recon " + year + ".xls", directory,
                         schol_mail.attachments)

            if "MR_SCH" in query and "LOA" in query and year in query[:-8]:
                do_query(query, date + " Scholarship LOA " + year + ".xls", directory,
                         hjj_mail.attachments)

            if "SCHOLAR_REINSTATE" in query and year in query[:-8]:
                do_query(query, date + " Scholarship Reinstate " + year + ".xls", directory,
                         hjj_mail.attachments)

            if "MR_SF_DIS_AWD_PT_ER_FC" in query and year in query[:-8]:
                do_query(query, date + " Federal Award Disb Post Error " + year + ".xls", directory,
                         loans_kkt_mail.attachments)

            if "MR_SF_DIS_AWD_PT_ER_SV" in query and year in query[:-8]:
                do_query(query, date + " SCHOL-ATH Award Disb Post Error " + year + ".xls", directory,
                         hj_mail.attachments)

            if "MR_STATE_FM_MH_PW" in query and year in query[:-8]:
                do_query(query, date + " Palau - Micronesia - Marshall Islands Students " + year + ".xls", directory,
                         acnt_kkmt_mail.attachments)

            if "MR_SUSPEND_RC2" in query and year in query[:-8]:
                do_query(query, date + " ISIR Suspended Reason Code 2 " + year + ".xls", directory,
                         kkmtv_mail.attachments)

            if "MR_UFORM_GRAD_TERM_PRB" in query and year in query[:-8]:
                do_query(query, date + " Grad Term Wrong " + year + ".xls", directory,
                         hjr_mail.attachments)

            if "MR_UNDS_OFFER_SCHOLAR" in query and year in query[:-8]:
                do_query(query, date + " Scholarship Awards UNDS Career " + year + ".xls", directory,
                         hj_mail.attachments)

            if "MR_UNDS_OFRD_AMT_FDRL" in query and year in query[:-8]:
                do_query(query, date + " Federal Awards UNDS Career " + year + ".xls", directory,
                         ath_mail.attachments)

            if "MR_UNDS_OFRD_AMT_ATH" in query and year in query[:-8]:
                do_query(query, date + " Athlete Awards UNDS Career " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "MR_VERIFY_DEP_OVERRIDE" in query and year in query[:-8]:
                do_query(query, date + " Verification Dependency Override " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "MR_GRBEN_EA_POST" in query and year in query[:-8]:
                do_query(query, date + " Grad Benefit EA Post " + year + ".xls", directory,
                         hjr_mail.attachments)

            if "SEFA_DL_TOTAL_AWARDS" in query and year in query[:-8]:
                do_query(query, date + " SEFA DL Amounts " + year + ".xls", directory,
                         monthly_dl_mail.attachments)

            if "SEFA_TOTAL_STUDENT" in query and year in query[:-8]:
                do_query(query, date + " SEFA DL Total Students " + year + ".xls", directory,
                         monthly_dl_mail.attachments)

            if "STP_DISB_RULE_MISMATCH" in query and year in query[:-8]:
                do_query(query, date + " Item Type Setup Mismatch " + year + ".xls", directory,
                         sys_mail.attachments)

            if "ussfa037" in query and year in query:
                do_query(query, query, t_directory,
                         null_mail.attachments)

            if "ussfa035-" in query and year in query:
                do_query(query, query, t_directory,
                         null_mail.attachments)

            if "MR_EXPIRED_MPN_CURR_LN" in query and year in query[:-8]:
                do_query(query, date + " Expired MPN Current LN " + year + ".xls", directory,
                        loans_mail.attachments)

            if "_MR_RNDM_GRAD_ENR_CHANG" in query and year in query[:-8]:
                do_query(query, date + " Audit Graduation & Enrollment Change " + year + ".xls", directory,
                         loans_mail.attachments)             
    else:
        for query in os.listdir("."):
            if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if "MR_COMMENT_CODE_298" in query :
                    do_query(query, date + " IASG - Pell Eligible " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "MR_3RD_PARTY_CROSSWALK" in query :
                    do_query(query, date + " Third Party Crosswalk " + year + ".xls", directory,
                             hjr_mail.attachments)
                    
                if "MR_FDEGRX_FABCX_FBLKD_FDG" in query :
                    do_query(query, date + " Complete FDEGRX FABCX FBLKD FDG " + year + ".xls", directory,
                             prof_kmt_mail.attachments)

                if "MR_3RD_PRT_MNTR_IA_ALL" in query :
                    do_query(query, date + " Third Party Monitor " + year + ".xls", directory,
                             hjr_mail.attachments)

                if "MR_ACAD_LVLS_NOT_SYNC" in query :
                    do_query(query, date + " Academic Levels out of SYNC " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "MR_ADM_DEFERRAL" in query :
                    do_query(query, date + " FA Admission Deferral " + year + ".xls", directory,
                             hjj_mail.attachments)

                if "MR_ALT_LN_TRNSMIT_HOLD" in query :
                    do_query(query, date + " Alt Loan Transmit Hold " + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "MR_ATHLETE_T53_AWARDS" in query :
                    do_query(query, date + " Athlete T53 Awards Accepted " + year + ".xls", directory,
                             ath_mail.attachments)

                if "MR_COD_DL" in query :
                    do_query(query, date + " COD DL FATB" + year + " FCRD" + year + " FHMS" + year + ".xls", directory,
                             acnt_kkt_mail.attachments)

                if "MR_COD_PELL_TEACH_IASG" in query :
                    do_query(query, date + " COD Grant FCRD" + year + "-FHMS" + year + " Report.xls", directory,
                             acnt_kkt_mail.attachments)

                if "MR_DIR_LN_TRNSMIT_HOLD" in query :
                    do_query(query, date + " COD Direct Loan Transmit Hold " + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "MR_DISB_ATH_AWD_NOPOST" in query :
                    do_query(query, date + " Athlete Waiver Disbursed Not Posted " + year + ".xls", directory,
                             ath_mail.attachments)

                if "MR_DL_DISB_FAILED" in query :
                    do_query(query, date + " DL Disbursement Failed " + year + ".xls", dl_directory,
                             krms_mail.attachments)

                if "MR_DL_ORIG_AWARD" in query :
                    do_query(query, date + " DL ORIG Award " + year + ".xls", directory,
                             loans_c_mail.attachments)

                if "MR_DSB_CASH_AWD_NOPOST" in query :
                    do_query(query, date + " Cash Disbursed Not Posted " + year + ".xls", directory,
                             hjj_mail.attachments)

                if "MR_DSB_WAVR_AWD_NOPOST" in query :
                    do_query(query, date + " Waiver-Scholarship Disbursed Not Posted " + year + ".xls", directory,
                             hj_mail.attachments)

                if "DSB_AWD_NOPOST" in query :
                    do_query(query, date + " Award Disbursed Not Posted " + year + ".xls", directory,
                             hjjk_mail.attachments)

                if "MR_DN_INC_CHECKLISTS" in query :
                    do_query(query, date + " Dental Students with I Checklists " + year + ".xls", directory,
                             prof_mail.attachments)

                if "MR_M_L_D_INI_CHECKLIST" in query :
                    do_query(query, date + " L-M-D Students with I Checklists " + year + ".xls", directory,
                             prof_mail.attachments)

                if "MR_FWS_WITH_NSI_HOLD" in query :
                    do_query(query, date + " FWS with NSI Holds.xls", directory,
                             acnt_mail.attachments)

                if "MR_GRAD_TERM_PRB" in query :
                    do_query(query, date + " Grad Term Wrong " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "MR_ITEM_CHARTFLD_SETUP" in query :
                    do_query(query, date + " Item Chartfield Setup.xls", acct_directory,
                             bhjkn_mail.attachments)

                if "MR_ITEM_TYPE_DISB_RULE" in query :
                    do_query(query, date + " Item Type Career - Match Disb Rule Career " + year + ".xls", directory,
                             ahjmv_mail.attachments)

                if "MR_LAW_INC_CHECKLISTS" in query :
                    do_query(query, date + " Law Students with I Checklists " + year + ".xls", directory,
                             prof_mail.attachments)

                if "MR_LOAN_AWD_PARTL_DISB" in query :
                    do_query(query, date + " Loan Awards Partial Disbursed " + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "MR_MED_INC_CHECKLISTS" in query :
                    do_query(query, date + " Med Students with I Checklists " + year + ".xls", directory,
                             prof_mail.attachments)

                if "MR_MED_LAW_LVL_REVIEW" in query or "_MR_DN_LW_MD_LVL_RVW" in query :
                    do_query(query, date + " MED-LAW Academic Level Review " + year + ".xls", directory,
                             prof_mail.attachments)

                if "MR_PART_TW_OTHER_SCH" in query :
                    do_query(query, date + " Partial TW Other Scholarship " + year + ".xls", directory,
                             hj_mail.attachments)

                if "MR_PELL_AWD_ADJUSTMENT" in query :
                    do_query(query, date + " Pell Award Adjust " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "MR_PELL_ONLY" in query :
                    do_query(query, date + " Pell Awd  Zero Grants Loans " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "MR_PELL_SSN_MISMATCH" in query :
                    do_query(query, date + " SSN Mismatch " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "MR_PERKINS_CLASS_LIMIT" in query :
                    do_query(query, date + " Perkins Class Limits " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "MR_PERK_MISC_LN_CNCLD" in query :
                    do_query(query, date + " Perkins - Misc Loans Cancelled " + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "MR_PERK_MISC_LOAN_DISB" in query :
                    do_query(query, date + " Perkins - Misc Loans Disbursed " + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "_MR_SCH_IT_RECON" in query :
                    do_query(query, date + " Scholarship IT Recon " + year + ".xls", directory,
                             schol_mail.attachments)

                if "MR_SCH" in query and "LOA" in query :
                    do_query(query, date + " Scholarship LOA " + year + ".xls", directory,
                             hjj_mail.attachments)

                if "SCHOLAR_REINSTATE" in query :
                    do_query(query, date + " Scholarship Reinstate " + year + ".xls", directory,
                             hjj_mail.attachments)

                if "MR_SF_DIS_AWD_PT_ER_FC" in query :
                    do_query(query, date + " Federal Award Disb Post Error " + year + ".xls", directory,
                             loans_kkt_mail.attachments)

                if "MR_SF_DIS_AWD_PT_ER_SV" in query :
                    do_query(query, date + " SCHOL-ATH Award Disb Post Error " + year + ".xls", directory,
                             hj_mail.attachments)

                if "MR_STATE_FM_MH_PW" in query :
                    do_query(query, date + " Palau - Micronesia - Marshall Islands Students " + year + ".xls", directory,
                             acnt_kkmt_mail.attachments)

                if "MR_SUSPEND_RC2" in query :
                    do_query(query, date + " ISIR Suspended Reason Code 2 " + year + ".xls", directory,
                             kkmtv_mail.attachments)

                if "MR_UFORM_GRAD_TERM_PRB" in query :
                    do_query(query, date + " Grad Term Wrong " + year + ".xls", directory,
                             hjr_mail.attachments)

                if "MR_UNDS_OFFER_SCHOLAR" in query :
                    do_query(query, date + " Scholarship Awards UNDS Career " + year + ".xls", directory,
                             hj_mail.attachments)

                if "MR_UNDS_OFRD_AMT_FDRL" in query :
                    do_query(query, date + " Federal Awards UNDS Career " + year + ".xls", directory,
                             ath_mail.attachments)

                if "MR_UNDS_OFRD_AMT_ATH" in query :
                    do_query(query, date + " Athlete Awards UNDS Career " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "MR_VERIFY_DEP_OVERRIDE" in query :
                    do_query(query, date + " Verification Dependency Override " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "MR_GRBEN_EA_POST" in query :
                    do_query(query, date + " Grad Benefit EA Post " + year + ".xls", directory,
                             hjr_mail.attachments)

                if "SEFA_DL_TOTAL_AWARDS" in query :
                    do_query(query, date + " SEFA DL Amounts " + year + ".xls", directory,
                             monthly_dl_mail.attachments)

                if "SEFA_TOTAL_STUDENT" in query :
                    do_query(query, date + " SEFA DL Total Students " + year + ".xls", directory,
                             monthly_dl_mail.attachments)

                if "STP_DISB_RULE_MISMATCH" in query :
                    do_query(query, date + " Item Type Setup Mismatch " + year + ".xls", directory,
                             sys_mail.attachments)

                if "ussfa037" in query and year in query:
                    do_query(query, query, t_directory,
                             null_mail.attachments)

                if "ussfa035-" in query and year in query:
                    do_query(query, query, t_directory,
                             null_mail.attachments)

                if "MR_EXPIRED_MPN_CURR_LN" in query :
                    do_query(query, date + " Expired MPN Current LN " + year + ".xls", directory,
                            loans_mail.attachments)

                if "_MR_RNDM_GRAD_ENR_CHANG" in query :
                    do_query(query, date + " Audit Graduation & Enrollment Change " + year + ".xls", directory,
                             loans_mail.attachments)


