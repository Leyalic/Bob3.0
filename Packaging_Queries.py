# Packaging Queries - to be modified 
# to be called in main


def do_packaging_queries():
    global aid_year
    year = "23"
    for query_name in os.listdir("."):
        if query_name.startswith("UUFA_PRT_ACAD_PROG_REVIEW"):
            if str(int(re.search(r'\d+', query_name).group())) == "22":
                year = "22"
            break
    aid_year = "20" + str(int(year) - 1) + "-20" + year
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

    # Change File_Name to be query AC it is received and _new_file_name to what
    # the new query should be.  Prefix date
    # will be added.
    if (year in query_name.split("-")[0]) or (str(int(year)-1) in query_name.split("-"[0])):
        for query in os.listdir("."):
            if query.startswith("UUFA_PRT_ACAD_LVLS_OUT_SYNC"):
                do_query(query, date + " UG Acad Levels Out of Sync.xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_ACAD_PROG_REVIEW") and (year in query[:-8]) :
                do_query(query, date + " Academic Progress Review.xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_ATH_ACCEPT_FED_AID"):
                do_query(query, date + " Athlete Accepted Federal Aid.xls", directory,
                         ath_mail.attachments)

            if query.startswith("UUFA_PRT_ATH_AWD_CBA_GRANT"):
                do_query(query, date + " Athlete Awarded CBA Grant.xls", directory,
                         ath_mail.attachments)

            if query.startswith("UUFA_PRT_ATH_GRAD_DATE"):
                do_query(query, date + " Athlete Expected Grad Date.xls", directory,
                         ath_mail.attachments)

            if query.startswith("UUFA_PRT_ATH_OFFRD_FED_AID"):
                do_query(query, date + " Athlete Offered Federal Aid.xls", directory,
                         ath_mail.attachments)

            if query.startswith("UUFA_PRT_ATH_OFFR_ACCPT_AID") :
                do_query(query, date + " ATH Fed State Inst O-A.xls", directory,
                         ath_mail.attachments)

            if query.startswith("UUFA_PRT_AWARD_TERM_HAD_SAP"):
                do_query(query, date + " SAP Hold Term Award Review.xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_AWARDS_OTHER_INST"):
                do_query(query, date + " Checklist FAOI" + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_AWD_CMB_OVR_AG_RVW"):
                do_query(query, date + " Award Combined Over Aggregate.xls", directory,
                         loans_kt_mail.attachments)

            if query.startswith("FA_PRT_AWD_MASS_P_NO_AWARDS"):
                do_query(query, date + " Award Mass Packaging No Awards.xls", directory,
                         ml_mail.attachments)

            if query.startswith("UUFA_PRT_AWD_PLL_ELG_NO_PLL") and (year in query[:-8]) :
                do_query(query, date + " PELL ELIGIBLE NO PELL 20" + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_AWD_SUB_OVR_AG_RVW"):
                do_query(query, date + " SUB Over Aggregate.xls", directory,
                         loans_kkt_mail.attachments)

            if query.startswith("UUFA_PRT_CTZN_IND_AWD_NO_LN"):
                do_query(query, date + " LA-wk eligible - Award No Loans.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PRT_DEFR_ENROLLMENT") and (year in query[:-8]) :
                do_query(query, date + " DEFER Enrollment " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PRT_DEP_PRNT_SSN_RVW"):
                do_query(query, date + " Parent SSN Review.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PRT_DIAG_AWD_PELL_TERM") and (year in query[:-8]) :
                do_query(query, date + " Term Pell Awards 20" + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("FA_PRT_DISB_PLAN_SPLT_CODE") and (year in query[:-8]) :
                do_query(query, date + " Disb Plan FY Split Code XX.xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_DL_DPAY_SCSP") and (year in query[:-8]) :
                do_query(query, date + " Disb Plan AY-Split Code SP.xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_DSB_PLN_SPLT_CD_FD") and (year in query[:-8]) :
                do_query(query, date + " Federal Disb Plan FY Split Code XX " + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_DSB_PLN_SPLT_CD_SC") and (year in query[:-8]) :
                do_query(query, date + " Scholarship Disb Plan FY Split Code XX " + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_EXPECT_GRAD_TERM_11"):
                do_query(query, date + " Expected Grad Term 1" + str(int(year) - 1) + "8.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PRT_DL_GRAD_TERM_FALL") and (year in query[:-8]) :
                do_query(query, date + " DL Expected Grad Term Fall " + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_GRAD_TRM_FALL") and (year in query[:-8]) :
                do_query(query, date + " Loan Proration Grad Term Fall " + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_GRAD_TRM_SPRING") and (year in query[:-8]) :
                do_query(query, date + " Loan Proration Grad Term Spring " + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_HEAL"):
                do_query(query, date + " Heal 20 " + year + ".xls", directory,
                         loans_kkt_mail.attachments)

            if query.startswith("UUFA_PRT_LEU_C_PELL_FSEOG") and (year in query[:-8]) :
                do_query(query, date + " LEU C Flag Awarded FSEOG " + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_LEU_C_PELL_AWARD") and (year in query[:-8]) :
                do_query(query, date + " LEU C Flag Awarded Pell " + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_LEU_E_PELL_FSEOG") and (year in query[:-8]) :
                do_query(query, date + " LEU E Flag Awarded FSEOG " + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_LN_CBA_AWD_NO_ELIG"):
                do_query(query, date + " Loan CBA Review Eligible.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PRT_NO_FALL_11" + str(int(year) - 1) + "8"):
                do_query(query, date + " Packaging No Fall 1" + str(int(year) - 1) + "8 (2).xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PRT_NSL_LOAN_RPT_VERI") and (year in query[:-8]) :
                do_query(query, date + " NSL Loan Need Verification.xls", directory,
                         loans_c_mail.attachments)

            if query.startswith("UUFA_PRT_NURSING_LOAN_RPT") and (year in query[:-8]) :
                do_query(query, date + " NSL Needs NSL P-N Checklist " + year + ".xls", directory,
                         prof_mail.attachments)

            if query.startswith("UUFA_PRT_ON_LINE_PACKAGING"):
                do_query(query, date + " Manual Packaging Counselors.xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_PELL_COMMENT_037") and (year in query[:-8]) :
                do_query(query, date + " Pell Comment Code 037 20" + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_PELL_ELG_NO_PELL") and (year in query[:-8]) :
                do_query(query, date + " PELL ELIGIBLE NO PELL " + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_PLL_EL_CTZN_NOT_INDCT"):
                do_query(query, date + " Pell Eligible Citizenship Not Indicated.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PRT_PELL_FPEL" + year + "_INITIATED"):
                do_query(query, date + " Pell FPEL" + year + " Initiated.xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_PELL_UG_5TH_YR_2ND_BA"):
                do_query(query, date + " Pell UG 5th YR.xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_PHARM_NO_HEAL"):
                do_query(query, date + " Pharmacy students with NO HEAL.xls", directory,
                         loans_kkt_mail.attachments)

            if query.startswith("UUFA_PRT_PKG_AWD_NO_BDGT"):
                do_query(query, date + " Award NO Budget for Term.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PRT_PKG_SCH_AWD_NO_BGT") and (year in query[:-8]) :
                do_query(query, date + " Scholarship Award NO Budget for Term.xls", directory,
                         hj_mail.attachments)

            if query.startswith("UUFA_PRT_PRIOR_TERM_STFFRD_OFR"):
                do_query(query, date + " Cancel Prior Term Stafford Offer " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_READY_PKG_20" + year):
                do_query(query, date + " Students Ready to Package " + year + ".xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_PRT_SCHOL_GRAD_DATE"):
                do_query(query, date + " Scholarship-Expected Grad Date.xls", directory,
                         jj_mail.attachments)

            if query.startswith("UUFA_PRT_SUB_UNSUB_SP_SP"):
                do_query(query, date + " Loan Offrd Disb Plan SP Split Code SP.xls", directory,
                         loans_kt_mail.attachments)

            if query.startswith("UUFA_PRT_SET_HEAL_FLAG") and (year in query[:-8]) :
                do_query(query, date + " MD - Pharmacy Heal Eligible Flag.xls", directory,
                         loans_kkt_mail.attachments)

            if query.startswith("UUFA_PRT_STATE_OF_RES_FM_MH_PW"):
                do_query(query, date + " State of Residence FM MH PW.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("FA_PRT_STILL_UNPRCD_AFTER_PKG"):
                do_query(query, date + " Students Not Packaged (old).xls", directory,
                         ml_mail.attachments)

            if query.startswith("UUFA_PRT_STDNT_NOT_PACKAGED") and (year in query[:-8]) :
                do_query(query, date + " Students Not Packaged " + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_PRT_TEACH_CREDENTIAL") and (year in query[:-8]) :
                do_query(query, date + " Teach Credential 20" + year + ".xls", directory,
                         kkt_mail.attachments)

            if ("PRT_SUB_UNSUB_FA_FA") in query and (year in query[:-8]) :
                do_query(query, date + " Loan Offrd Disb Plan FA Split Code FA " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if ("PRT_PELL_PKG_LOAD_CHCK") in query and (year in query[:-8]) :
                do_query(query, date + " Pell Package Load Check " + year + ".xls", directory,
                         kkt_mail.attachments)

            if ("PRT_COUNT_ITEM_TYPE") in query and (year in query[:-8]) :
                do_query(query, date + " Aid Awarded No Funds " + year + ".xls", directory,
                         bekkt_mail.attachments)

            if ("PKG_NOT_PKGD_NO_UNITS") in query :
                do_query(query, date + " Not Packaged No Units " + year + ".xls", directory,
                         kkt_mail.attachments)
                
    else:
        for query in os.listdir("."):
            if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if query.startswith("UUFA_PRT_ACAD_LVLS_OUT_SYNC"):
                    do_query(query, date + " UG Acad Levels Out of Sync.xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_ACAD_PROG_REVIEW")  :
                    do_query(query, date + " Academic Progress Review.xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_ATH_ACCEPT_FED_AID"):
                    do_query(query, date + " Athlete Accepted Federal Aid.xls", directory,
                             ath_mail.attachments)

                if query.startswith("UUFA_PRT_ATH_AWD_CBA_GRANT"):
                    do_query(query, date + " Athlete Awarded CBA Grant.xls", directory,
                             ath_mail.attachments)

                if query.startswith("UUFA_PRT_ATH_GRAD_DATE"):
                    do_query(query, date + " Athlete Expected Grad Date.xls", directory,
                             ath_mail.attachments)

                if query.startswith("UUFA_PRT_ATH_OFFRD_FED_AID"):
                    do_query(query, date + " Athlete Offered Federal Aid.xls", directory,
                             ath_mail.attachments)

                if query.startswith("UUFA_PRT_ATH_OFFR_ACCPT_AID")  :
                    do_query(query, date + " ATH Fed State Inst O-A.xls", directory,
                             ath_mail.attachments)

                if query.startswith("UUFA_PRT_AWARD_TERM_HAD_SAP"):
                    do_query(query, date + " SAP Hold Term Award Review.xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_AWARDS_OTHER_INST"):
                    do_query(query, date + " Checklist FAOI" + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_AWD_CMB_OVR_AG_RVW"):
                    do_query(query, date + " Award Combined Over Aggregate.xls", directory,
                             loans_kt_mail.attachments)

                if query.startswith("FA_PRT_AWD_MASS_P_NO_AWARDS"):
                    do_query(query, date + " Award Mass Packaging No Awards.xls", directory,
                             ml_mail.attachments)

                if query.startswith("UUFA_PRT_AWD_PLL_ELG_NO_PLL")  :
                    do_query(query, date + " PELL ELIGIBLE NO PELL 20" + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_AWD_SUB_OVR_AG_RVW"):
                    do_query(query, date + " SUB Over Aggregate.xls", directory,
                             loans_kkt_mail.attachments)

                if query.startswith("UUFA_PRT_CTZN_IND_AWD_NO_LN"):
                    do_query(query, date + " LA-wk eligible - Award No Loans.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PRT_DEFR_ENROLLMENT")  :
                    do_query(query, date + " DEFER Enrollment " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PRT_DEP_PRNT_SSN_RVW"):
                    do_query(query, date + " Parent SSN Review.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PRT_DIAG_AWD_PELL_TERM")  :
                    do_query(query, date + " Term Pell Awards 20" + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("FA_PRT_DISB_PLAN_SPLT_CODE")  :
                    do_query(query, date + " Disb Plan FY Split Code XX.xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_DL_DPAY_SCSP")  :
                    do_query(query, date + " Disb Plan AY-Split Code SP.xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_DSB_PLN_SPLT_CD_FD")  :
                    do_query(query, date + " Federal Disb Plan FY Split Code XX " + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_DSB_PLN_SPLT_CD_SC")  :
                    do_query(query, date + " Scholarship Disb Plan FY Split Code XX " + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_EXPECT_GRAD_TERM_11"):
                    do_query(query, date + " Expected Grad Term 1" + str(int(year) - 1) + "8.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PRT_DL_GRAD_TERM_FALL")  :
                    do_query(query, date + " DL Expected Grad Term Fall " + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_GRAD_TRM_FALL")  :
                    do_query(query, date + " Loan Proration Grad Term Fall " + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_GRAD_TRM_SPRING")  :
                    do_query(query, date + " Loan Proration Grad Term Spring " + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_HEAL"):
                    do_query(query, date + " Heal 20 " + year + ".xls", directory,
                             loans_kkt_mail.attachments)

                if query.startswith("UUFA_PRT_LEU_C_PELL_FSEOG")  :
                    do_query(query, date + " LEU C Flag Awarded FSEOG " + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_LEU_C_PELL_AWARD")  :
                    do_query(query, date + " LEU C Flag Awarded Pell " + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_LEU_E_PELL_FSEOG")  :
                    do_query(query, date + " LEU E Flag Awarded FSEOG " + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_LN_CBA_AWD_NO_ELIG"):
                    do_query(query, date + " Loan CBA Review Eligible.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PRT_NSL_LOAN_RPT_VERI")  :
                    do_query(query, date + " NSL Loan Need Verification.xls", directory,
                             loans_c_mail.attachments)

                if query.startswith("UUFA_PRT_NURSING_LOAN_RPT")  :
                    do_query(query, date + " NSL Needs NSL P-N Checklist " + year + ".xls", directory,
                             prof_mail.attachments)

                if query.startswith("UUFA_PRT_ON_LINE_PACKAGING"):
                    do_query(query, date + " Manual Packaging Counselors.xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_PELL_COMMENT_037")  :
                    do_query(query, date + " Pell Comment Code 037 20" + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_PELL_ELG_NO_PELL")  :
                    do_query(query, date + " PELL ELIGIBLE NO PELL " + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_PLL_EL_CTZN_NOT_INDCT"):
                    do_query(query, date + " Pell Eligible Citizenship Not Indicated.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PRT_PELL_UG_5TH_YR_2ND_BA"):
                    do_query(query, date + " Pell UG 5th YR.xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_PHARM_NO_HEAL"):
                    do_query(query, date + " Pharmacy students with NO HEAL.xls", directory,
                             loans_kkt_mail.attachments)

                if query.startswith("UUFA_PRT_PKG_AWD_NO_BDGT"):
                    do_query(query, date + " Award NO Budget for Term.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PRT_PKG_SCH_AWD_NO_BGT")  :
                    do_query(query, date + " Scholarship Award NO Budget for Term.xls", directory,
                             hj_mail.attachments)

                if query.startswith("UUFA_PRT_PRIOR_TERM_STFFRD_OFR"):
                    do_query(query, date + " Cancel Prior Term Stafford Offer " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PRT_SCHOL_GRAD_DATE"):
                    do_query(query, date + " Scholarship-Expected Grad Date.xls", directory,
                             jj_mail.attachments)

                if query.startswith("UUFA_PRT_SUB_UNSUB_SP_SP"):
                    do_query(query, date + " Loan Offrd Disb Plan SP Split Code SP.xls", directory,
                             loans_kt_mail.attachments)

                if query.startswith("UUFA_PRT_SET_HEAL_FLAG")  :
                    do_query(query, date + " MD - Pharmacy Heal Eligible Flag.xls", directory,
                             loans_kkt_mail.attachments)

                if query.startswith("UUFA_PRT_STATE_OF_RES_FM_MH_PW"):
                    do_query(query, date + " State of Residence FM MH PW.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("FA_PRT_STILL_UNPRCD_AFTER_PKG"):
                    do_query(query, date + " Students Not Packaged (old).xls", directory,
                             ml_mail.attachments)

                if query.startswith("UUFA_PRT_STDNT_NOT_PACKAGED")  :
                    do_query(query, date + " Students Not Packaged " + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_PRT_TEACH_CREDENTIAL")  :
                    do_query(query, date + " Teach Credential 20" + year + ".xls", directory,
                             kkt_mail.attachments)

                if ("PRT_SUB_UNSUB_FA_FA") in query  :
                    do_query(query, date + " Loan Offrd Disb Plan FA Split Code FA.xls" + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if ("PRT_PELL_PKG_LOAD_CHCK") in query  :
                    do_query(query, date + " Pell Package Load Check " + year + ".xls", directory,
                             kkt_mail.attachments)

                if ("PRT_COUNT_ITEM_TYPE") in query  :
                    do_query(query, date + " Aid Awarded No Funds " + year + ".xls", directory,
                             bekkt_mail.attachments)

                if ("PKG_NOT_PKGD_NO_UNITS") in query  :
                    do_query(query, date + " Not Packaged No Units " + year + ".xls", directory,
                             kkt_mail.attachments)
                    
                if query.startswith("UUFA_READY_PACKAGE" + year):
                    do_query(query, date + " Students Ready to Package " + year + ".xls", directory,
                         null_mail.attachments)

