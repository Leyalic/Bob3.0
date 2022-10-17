# Monday Weekly Queries 

# To be modified and called in Main 

def do_monday_weeklies():
    global aid_year
    global year
    for query_name in os.listdir("."):
        if query_name.startswith("UUFA_WR"):
            year = str(int(re.search(r'\d+', query_name).group()))
            break
    aid_year = "20" + str(int(year) - 1) + "-20" + year
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

    # Change File_Name to be query ac it is received and _new_file_name to what
    # the new query should be.Prefix date
    # will be added.
    if ("22" in query_name.split("-")[0]):
        for query in os.listdir("."):
            if "_WR_ACAD_LVLS_OUT_SYNC" in query and (year in query[:-8]) :
                do_query(query, date + " UG Academic Levels Out of Sync " + year + ".xls", directory,
                         kkt_mail.attachments)

            if "_WR_ADV_FSOI_INITIATED" in query and (year in query[:-8]) :
                do_query(query, date + " FSOI Initiated  " + year + ".xls", directory,
                         kmt_mail.attachments)

            if "_WR_AGG_CK_MLT_YR_AWDED" in query and (year in query[:-8]) :
                do_query(query, date + " Student Pkgd for " + str(int(year) - 1) + " after " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "_WR_AID_DISB_NO_ENR_ATH" in query and (year in query[:-8]) :
                do_query(query, date + " Athlete Disb Not Enrolled " + year + ".xls", directory,
                         ath_mail.attachments)

            if "_WR_AID_DISB_NO_ENR_FED" in query and (year in query[:-8]) :
                do_query(query, date + " Federal Disb Not Enrolled " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_AID_DISB_NO_ENR_SCH" in query and (year in query[:-8]) :
                do_query(query, date + " T 53 Sch Disb Not Enrolled " + year + ".xls", directory,
                         hj_mail.attachments)

            if "_WR_ALL_V4_V5_VER" in query and (year in query[:-8]) :
                do_query(query, date + " All Verification V4-V5 " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_AMERICORP_AWD_POST" in query and (year in query[:-8]) :
                do_query(query, date + " Americorp Awards " + year + ".xls", directory,
                         hk_mail.attachments)

            if "_WR_ATHLETE_NOT_DISB" in query and (year in query[:-8]) :
                do_query(query, date + " Athlete Not Disbursed " + year + ".xls", directory,
                         ath_mail.attachments)

            if "_WR_ATH_HRS_AFTR_CENSUS" in query and (year in query[:-8]) :
                do_query(query, date + " Ath Hours After Census " + year + ".xls", directory,
                         ath_mail.attachments)

            if "_WR_ATH_SF_TERM_BALANCE" in query and (year in query[:-8]) :
                do_query(query, date + " Athlete Tuition Fee Balance " + year + ".xls", directory,
                         ath_mail.attachments)

            if "_WR_AUDIT_CLSS_AID_DISB" in query and (year in query[:-8]) :
                do_query(query, date + " Audit Class Aid Disbursed " + year + ".xls", directory,
                         kkt_mail.attachments)

            if "_WR_ISA_PER_TERM" in query and (year in query[:-8]) :
                do_query(query, date + " ISA Per Term FISA" + year + ".xls", directory,
                         kkt_mail.attachments)  

            if "_WR_AWD_UG_NOW_GRAD_ATH" in query and (year in query[:-8]) :
                do_query(query, date + " Ath Awards past Grad Term " + year + ".xls", directory,
                         ath_mail.attachments)

            if "_WR_AWD_UG_NOW_GRAD_FC" in query and (year in query[:-8]) :
                do_query(query, date + " Federal Awards past Grad Term " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_AWD_UG_NOW_GRAD_SV" in query and (year in query[:-8]) :
                do_query(query, date + " Scholar Awards past Grad Term " + year + ".xls", directory,
                         hj_mail.attachments)

            if "_WR_CHKLST_STATUS_ERROR" in query and (year in query[:-8]) :
                do_query(query, date + " Checklist Status Error " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "WR_CMT_CDE_O_AGR_LMT_2" in query and year in query[:-8]:
                do_query(query, date + " Comment Code Over Aggregate No FATERM Req " + year + ".xls", directory,
                         loans_kkt_mail.attachments)

            if "_WR_DISB_ATH_FAILURE" in query and (year in query[:-8]) :
                do_query(query, date + " Authorization Failure 20" + year + ".xls", disb_failure_directory,
                         null_mail.attachments)

            if "_WR_DL_DISBURSED_LTHT" in query and (year in query[:-8]) :
                do_query(query, date + " DL Disbursed LTHT " + year + ".xls", directory,
                         kkt_mail.attachments)

            if "_WR_DL_EC_SUSPENDED" in query and (year in query[:-8]) :
                do_query(query, date + " DL Entrance Counseling Suspense " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "_WR_DL_ORIG_TRNS_PEND" in query and (year in query[:-8]) :
                do_query(query, date + " DL Orig Trans Pending " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "_WR_EFT_CONSENT_VERIF" in query and (year in query[:-8]) :
                do_query(query, date + " EFT Consent Verification 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_FAFSA_CKLST_INCMP" in query and (year in query[:-8]) :
                do_query(query, date + " PLUS FAFSA Incomplete " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if  "_WR_FALL_TOTAL_WDRN_DRP" in query and (year in query[:-8]) :
                do_query(query, date + " Fall Disb Total Withdrawn Drop " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if  "_WR_SPR_TOTAL_WDRN_DRP" in query and (year in query[:-8]) :
                do_query(query, date + " Spring Disb Total Withdrawn Drop " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if  "WR_SNGDO_CAMPUS" in query and year in query[:-8] :
                do_query(query, date + " Asian-SNGDO Campus " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if  "_WR_SUM_TOTAL_WDRN_DRP" in query and (year in query[:-8]) :
                do_query(query, date + " Summer Disb Total Withdrawn Drop " + year + " .xls", directory,
                         kkmt_mail.attachments)

            if "_WR_FARC_CHECKLIST" in query and (year in query[:-8]) :
                do_query(query, date + " FARC 30 Day Review " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_FARC_CMNT_CODES" in query and (year in query[:-8]) :
                do_query(query, date + " Initiated FARC w ISIR Cmnt Codes " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_FED_AID_OVERAWARD" in query and (year in query[:-8]) :
                do_query(query, date + " Federal Aid Overaward " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_FGED_ISIR_DEGREE" in query and (year in query[:-8]) :
                do_query(query, date + " FGED ISIR Degree 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if ("_WR_FPEL" + year + "_INITIATED_AWDED") in query:
                do_query(query, date + " FPEL" + year + " Initiated Pell.xls", directory,
                         kkt_mail.attachments)

            if "WR_FREV_GR_WS" in query and year in query:
                do_query(query, date + " Grad FREV with Work Study" + year + ".xls", directory,
                         kmt_mail.attachments)

            if "_WR_GENDER" in query and (year in query[:-8]) :
                do_query(query, date + " Gender Discrepancies 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_HEDU_PARAMEDIC" in query and (year in query[:-8]) :
                do_query(query, date + " HEDU Paramedic Class 20" + year + "F.xls", directory,
                         kkt_mail.attachments)

            if "R_HOME_SCHOOLED" in query and (year in query[:-8]) :
                do_query(query, date + " Home Schooled Check " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_HRS_DECREASE_ATH" in query and (year in query[:-8]) :
                do_query(query, date + " Hours Decrease Athlete " + year + ".xls", directory,
                         ath_mail.attachments)

            if "_WR_HRS_DECREASE_FC" in query and (year in query[:-8]) :
                do_query(query, date + " Hours Decrease FC " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_HRS_DECREASE_SV" in query and (year in query[:-8]) :
                do_query(query, date + " Hours Decrease SV " + year + ".xls", directory,
                         ashley_mail.attachments)

            if "_WR_FHST_I_HST_COMPLETE" in query and (year in query[:-8]) :
                do_query(query, date + " HS Transcript 'C' FHST" + year + " 'I'.xls", directory,
                         kkmt_mail.attachments)

            if "_WR_ISIR_AS_EFC" in query and (year in query[:-8]) :
                do_query(query, date + " ISIR Assumption EFC 20" + year + ".xls", directory,
                         mat_mail.attachments)

            if "_WR_ISIR_COR_ASSESSMENT" in query and (year in query[:-8]) :
                do_query(query, date + " ISIR Correction Assessment " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_ISIR_CORR_REJECT" in query and (year in query[:-8]) :
                do_query(query, date + " ISIR Correction Rejected " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_ISIR_DGR_ANSW_CHNG" in query and (year in query[:-8]) :
                do_query(query, date + " ISIR Degree Answer Change " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_ISIR_DEP_STAT_PRB" in query and (year in query[:-8]) :
                do_query(query, date + " ISIR Dependency 20" + year + ".xls", directory,
                         mat_mail.attachments)

            if "_WR_ISIR_REJECTED_CORR" in query and (year in query[:-8]) :
                do_query(query, date + " ISIR Rejected Corrections 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if ("UUFA_WR_ISIR_REJECT_CODES" in query and year in query[:-8]) \
                    | (("UUFA_WR_ISIR_REJECT_CODES_20") in query and (year in query[:-8])) :
                do_query(query, date + " Rejected ISIRs 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_ISIR_SS_MCH_NOT_CON" in query and (year in query[:-8]) :
                do_query(query, date + " SS Match Not Confirmed 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_ISIR_SUSPENSE" in query and (year in query[:-8]) :
                do_query(query, date + " ISIR Suspense " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_LEGAL_ALIEN_WORK" in query and (year in query[:-8]) :
                do_query(query, date + " Legal Alien Work 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_LN_ACCPT_STAF_31_32" in query and (year in query[:-8]) :
                do_query(query, date + " Stafford Accept Offer " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "_WR_LOAN_CENSUS_DATE" in query and (year in query[:-8]) :
                do_query(query, date + " Loans Census Date 20" + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "_WR_LN_FA907_1_REVISED" in query and (year in query[:-8]) :
                do_query(query, date + " Loan Disbursed Report " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "_WR_LN_FA907_2_REVISED" in query and (year in query[:-8]) :
                do_query(query, date + " Loan Not Disbursed Report " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "R_LOAN_ORIG_DEPT_REVIEW" in query and (year in query[:-8]) :
                do_query(query, date + " Loan ORIG DEPT RVW " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "_WR_LN_SENT_NO_RESPONSE" in query and (year in query[:-8]) :
                do_query(query, date + " Loan Sent No Response " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "_WR_LOAN_TRANSMIT_HOLD" in query and (year in query[:-8]) :
                do_query(query, date + " Loan Transmit Hold " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "_WR_LW_MD_DN_AW_NO_DISB" in query and (year in query[:-8]) :
                do_query(query, date + " LW MD DN Awards Not Disbursed " + year + ".xls", directory,
                         prof_kkt_mail.attachments)

            if "_WR_MNTGMR_AMCORP_OVRAW" in query and (year in query[:-8]) :
                do_query(query, date + " Montgomery Americorp Overaward " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_MULTIPLE_EMPLIDS" in query and (year in query[:-8]) :
                do_query(query, date + " Multiple EMPLIDS 20" + year + ".xls", directory,
                         sys_mail.attachments)

            if "_WR_NO_COMMENT_CODE" in query and (year in query[:-8]) :
                do_query(query, date + " Sub ISIR Checklist No ISIR Comment Code 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_NSLDS_LOAN_DATA" in query and (year in query[:-8]) :
                do_query(query, date + " NSLDS Loan Data .xls", directory,
                         loans_kkt_mail.attachments)

            if "_WR_OVRD_ACAD_LVL" in query and (year in query[:-8]) :
                do_query(query, date + " FA Term Override Acad Level " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_PA_EXPECT" in query and (year in query[:-8]) :
                do_query(query, date + " PA Expected Grad Date Blank " + year + ".xls", directory,
                         prof_kkt_mail.attachments)

            if "_WR_PA_FDEG_CHECKLIST" in query:
                do_query(query, date + " PA MPS FDEG Checklist" + year + "U.xls", directory,
                         prof_mail.attachments)

            if "_WR_PELL_AWRD_LOCK" in query and (year in query[:-8]) :
                do_query(query, date + " Pell Award Lock No FPEL" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_PELL_OVERPAYMENT" in query and (year in query[:-8]) :
                do_query(query, date + " Pell Ovpy Check NSLDS 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_PELL_SUMMER_NO_PELL" in query and (year in query[:-8]) :
                do_query(query, date + " Pell Summer No Pell 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "WR_PELL_SUMMER_AGGS" in query and (year in query[:-8]) :
                do_query(query, date + " Pell Aggregate Summer Report" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_PELL_TERM_FT" in query and (year in query[:-8]) :
                do_query(query, date + " Term Pell Awards FT 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_PELL_TERM_HT" in query and (year in query[:-8]) :
                do_query(query, date + " Term Pell Awards HT 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_PELL_TERM_LH" in query and (year in query[:-8]) :
                do_query(query, date + " Term Pell Awards LH 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_PELL_TERM_NL" in query and (year in query[:-8]) :
                do_query(query, date + " Term Pell Awards NL 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_PELL_TERM_TQ" in query and (year in query[:-8]) :
                do_query(query, date + " Term Pell Awards TQ 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_PERK_SPLIT_MISMATCH" in query and (year in query[:-8]) :
                do_query(query, date + " Perkins Plan Split Mismatch " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_PRK_LN_ACAD_LVL_CHG" in query and (year in query[:-8]) :
                do_query(query, date + " Perkins Awd With Acad Lvl Change " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "_WR_QUALITY_ASSURANCE" in query and (year in query[:-8]) :
                do_query(query, date + " QA Students Complete Verification 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "R_RT4_DROPPED_CLASSES" in query and (year in query[:-8]) :
                do_query(query, date + " RT4 Dropped Classes 20" + year + ".xls", directory,
                         kkt_mail.attachments)

            if "_WR_SCH_NOT_DISB" in query and (year in query[:-8]) :
                do_query(query, date + " Cash Non-Cash Sch Not Disb " + year + ".xls", directory,
                         hjjr_mail.attachments)

            if "_WR_SCHOLAR_TBP_NO_AWRD" in query and year in query[:-8]:
                do_query(query, date + " TBP NO Award " + year + ".xls", directory,
                         hjr_mail.attachments)

            if "_WR_GRAD_FELLOW" in query and year in query[:-8]:
                do_query(query, date + " Grad Fellowship " + year + ".xls", directory,
                         hjr_mail.attachments)

            if "_WR_SSR_MATCH_NOT_CNFRM" in query and (year in query[:-8]) :
                do_query(query, date + " SSR Not Confirmed 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_SSR_NOT_CNFRMD_VTRN" in query and (year in query[:-8]) :
                do_query(query, date + " VA Match SSR DB Override " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_SS_DB_OVERRIDE" in query and (year in query[:-8]) :
                do_query(query, date + " SS DB Override " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_SUB_ISIR_PACKAGED" in query and (year in query[:-8]) :
                do_query(query, date + " Subsequent ISIR Packaged 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_SUB_ISIR_REAWD_AID" in query and (year in query[:-8]) :
                do_query(query, date + " Canceled FCOR Complete " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_SUB_ISIR_SYSG" in query and (year in query[:-8]) :
                do_query(query, date + " Subsequent ISIR System Generated 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_SUB_ISIR_VERIFIED" in query and (year in query[:-8]) :
                do_query(query, date + " Subsequent ISIR Verified 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_SUMMER_NO_DL" in query and (year in query[:-8]) :
                do_query(query, date + " Summer Enroll No DL " + year + ".xls", directory,
                         loans_kkt_mail.attachments)

            if "_WR_SUMMER_PELL_LTHT" in query and (year in query[:-8]) :
                do_query(query, date + " Summer Pell LTHT " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_SSP_DOB_PRB_APPLCNT" in query and (year in query[:-8]) :
                do_query(query, date + " Suspense Applicant DOB Problem " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_SSP_NAME_PRB_APLCNT" in query and (year in query[:-8]) :
                do_query(query, date + " Suspense Applicant Name Problem " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_SSP_SSN_PRB_APLCNT" in query and (year in query[:-8]) :
                do_query(query, date + " Suspense Applicant SSN Problem " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_TERM_NSLDS_LOAN_YR" in query and (year in query[:-8]) :
                do_query(query, date + " NSLDS Loan Year Blank " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "_WR_TITLE_VII_MED_LOANS" in query and (year in query[:-8]) :
                do_query(query, date + " Title VII Medical Loans TILA 20" + year + ".xls", directory,
                         prof_kkt_mail.attachments)

            if "_WR_TRANSFER_ENT_CNS" in query and (year in query[:-8]) :
                do_query(query, date + " Transfer Students Entrance Counseling 20" + year + ".xls", directory,
                         loans_kkt_mail.attachments)

            if "_WR_TRANSFER_STU_FA_SP" in query and (year in query[:-8]) :
                do_query(query, date + " Transfer Students Fall-Spring 20" + year + ".xls", directory,
                         buttars_mail.attachments)

            if "_WR_UG_GR_DIR_LN_GR_TRM" in query and (year in query[:-8]) :
                do_query(query, date + " UG-GR Direct Ln Grad Term " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "_WR_UG_GR_PLUS_GR_TERM" in query and (year in query[:-8]) :
                do_query(query, date + " UG-GR PLUS Grad Term " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "WR_UAC_FASI_STATUS" in query and (year in query[:-8]) :
                do_query(query, date + " UAC FASI Status " + year + ".xls", directory,
                         kkt_mail.attachments)

            if "_WR_UAC_SNGDO" in query and (year in query[:-8]) :
                do_query(query, date + " UAC SNGDO Campus 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_UNDOCUMENTED_STUDENTS" in query and (year in query[:-8]) :
                do_query(query, date + " Undocumented Student Awards " + year + ".xls", directory,
                         kkt_mail.attachments)

            if "_WR_VERI_CHKLST_MISSING" in query and (year in query[:-8]) :
                do_query(query, date + " Verification Checklist Missing 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_VERI_INCOME_ADJ" in query and (year in query[:-8]) :
                do_query(query, date + " Income Adjustments 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_VER_NOT_CONSL" in query and (year in query[:-8]) :
                do_query(query, date + " Verification Not Consolidated 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_VETERAN_ACTIVE_DUTY" in query and (year in query[:-8]) :
                do_query(query, date + " Veteran Active Duty 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_VETERAN_NO_QUALIFY" in query and (year in query[:-8]) :
                do_query(query, date + " Veteran No Qualify 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_WEEKS_OF_INSTR_FIX" in query and (year in query[:-8]) :
                do_query(query, date + " Weeks of Instruction 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "_WR_DL_AY_SP_CANCELED" in query and (year in query[:-8]) :
                do_query(query, date + " DL AY SP Cancelled " + year + ".xls", directory,
                         loans_kkt_mail.attachments)

            if "_WR_LOAN_TRANSMIT_HOLD_13" in query:
                do_query(query, date + " Loan Transmit Hold 13.xls", directory,
                         loans_kt_mail.attachments)

            if "_WR_REJECT_CODE_ON_ISIR" in query and (year in query[:-8]) :
                do_query(query, date + " Rejected ISIR's " + year + ".xls", directory,
                         kmt_mail.attachments)

            if "_WR_RT4_FA_DROP_CLASSES" in query and (year in query[:-8]) :
                do_query(query, date + " RT4 Fall Drop Classes 20" + year + ".xls", directory,
                         kkt_mail.attachments)

            if "_WR_RT4_SP_DROP_CLASSES" in query and (year in query[:-8]) :
                do_query(query, date + " RT4 Spring Drop Classes 20" + year + ".xls", directory,
                         kkt_mail.attachments)

            if "_WR_RT4_SU_DROP_CLASSES" in query and (year in query[:-8]) :
                do_query(query, date + " RT4 Summer Drop Classes 20" + year + ".xls", directory,
                         kkt_mail.attachments)

            if "WR_AWARDS_OTHER_INST" in query and (year in query[:-8]) :
                do_query(query, date + " Checklist FAOI" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "WR_DEP_PRNT_SSN_RVW" in query and (year in query[:-8]) :
                do_query(query, date + " Parent SSN Review " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "WR_DN_LW_MD_AID_ATRB" in query and (year in query[:-8]) :
                do_query(query, date + " DN-LW-MD Student Aid Career " + year + ".xls", directory,
                         prof_kkt_mail.attachments)

            if "WR_FSEOG_NO_PELL" in query and (year in query[:-8]) :
                do_query(query, date + " DNFSEOG no Pell " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "WR_FT_CLASS_OVERRIDES" in query and (year in query[:-8]) :
                do_query(query, date + " Class Overrides " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "WR_GR_ACAD_LV_OUT_SYNC" in query and (year in query[:-8]) :
                do_query(query, date + " GR Academic Levels Out of Sync " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "WR_PELL_COA_DOUBLE" in query and (year in query[:-8]) :
                do_query(query, date + " PELL COA Double  " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "WR_PKG_AWD_NO_BDGT" in query and (year in query[:-8]) :
                do_query(query, date + " Award NO Budget for Term " + year + ".xls", directory,
                         kkt_mail.attachments)

            if "WR_SCH_TUITION_FEES" in query and (year in query[:-8]) :
                do_query(query, date + " Waiver-Scholar Tuition Fees " + year + ".xls", directory,
                         hj_mail.attachments)

            if "WR_SCHOL_GRAD_DATE" in query and (year in query[:-8]) :
                do_query(query, date + " Scholarship-Expected Grad Date  " + year + ".xls", directory,
                         hjr_mail.attachments)

            if "_WR_STDNT_NOT_PACKAGED" in query and (year in query[:-8]) :
                do_query(query, date + " Students Not Packaged " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "WR_SAVE_CTZNSHIP_VER" in query and (year in query[:-8]) :
                do_query(query, date + " SAVE SB81 CTZNSHP VERI " + year + ".xls", save_directory,
                         bk_mail.attachments)

            if "WR_ALL_C_FVRA_I_NO_COR" in query and (year in query[:-8]) :
                do_query(query, date + " FVRA Ini with no Correction " + year + ".xls", save_directory,
                         kkmt_mail.attachments)

            if "WR_CORRECTION_NOT_SENT" in query and (year in query[:-8]) :
                do_query(query, date + " Corrections Sent still Pending " + year + ".xls", save_directory,
                         kkmt_mail.attachments)

            # Manually run Queries
            if "_WR_LOAN_EFT_DETAIL_ERROR" in query:
                do_query(query, date + " Loan EFT Detail Error.xls", directory,
                         loans_kkt_mail.attachments)

            if "_WR_NSL_PROMISSORY_NOTE" in query and (year in query[:-8]) :
                do_query(query, date + " NSL Promissory Note " + year + ".xls", directory,
                         loans_kt_mail.attachments)

            if "UUFA_AP_RPKG_FPEL_AWARD_LCK" in query:
                do_query(query, date + " Pell Award Lock FPEL" + year + ".xls", directory,
                         loans_kkt_mail.attachments)

            if "WR_FAVR_I_NO_FCOR_ALL_C" in query:
                do_query(query, date + " FAVR I No FCOR all check Completed.xls", directory,
                         loans_kkt_mail.attachments)

            # Packaging queries that are being manually run.
            if "PRT_ATH_ACCEPT_FED_AID" in query and (year in query[:-8]) :
                do_query(query, date + " Athlete Accepted Federal Aid " + year + ".xls", packaging_directory,
                         ath_mail.attachments)

            if "PRT_ATH_AWD_CBA_GRANT" in query and (year in query[:-8]) :
                do_query(query, date + " Athlete Awarded CBA Grant " + year + ".xls", packaging_directory,
                         ath_mail.attachments)

            if "PRT_ATHLETE_GRAD_DATE" in query and (year in query[:-8]) :
                do_query(query, date + " Athlete Accepted Grad Date " + year + ".xls", packaging_directory,
                         ath_mail.attachments)

            if "PRT_ATH_OFFERED_FED_AID" in query and (year in query[:-8]) :
                do_query(query, date + " Athlete Offered Federal Aid " + year + ".xls", packaging_directory,
                         ath_mail.attachments)
    
    else:
        for query in os.listdir("."):
            if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if "_WR_ACAD_LVLS_OUT_SYNC" in query :
                    do_query(query, date + " UG Academic Levels Out of Sync " + year + ".xls", directory,
                             kkt_mail.attachments)

                if "_WR_ADV_FSOI_INITIATED" in query :
                    do_query(query, date + " FSOI Initiated  " + year + ".xls", directory,
                             kmt_mail.attachments)

                if "_WR_AGG_CK_MLT_YR_AWDED" in query :
                    do_query(query, date + " Student Pkgd for " + str(int(year) - 1) + " after " + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "_WR_AID_DISB_NO_ENR_ATH" in query :
                    do_query(query, date + " Athlete Disb Not Enrolled " + year + ".xls", directory,
                             ath_mail.attachments)

                if "_WR_AID_DISB_NO_ENR_FED" in query :
                    do_query(query, date + " Federal Disb Not Enrolled " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_AID_DISB_NO_ENR_SCH" in query :
                    do_query(query, date + " T 53 Sch Disb Not Enrolled " + year + ".xls", directory,
                             hj_mail.attachments)

                if "_WR_ALL_V4_V5_VER" in query :
                    do_query(query, date + " All Verification V4-V5 " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_AMERICORP_AWD_POST" in query :
                    do_query(query, date + " Americorp Awards " + year + ".xls", directory,
                             hk_mail.attachments)

                if "_WR_ATHLETE_NOT_DISB" in query :
                    do_query(query, date + " Athlete Not Disbursed " + year + ".xls", directory,
                             ath_mail.attachments)

                if "_WR_ATH_HRS_AFTR_CENSUS" in query :
                    do_query(query, date + " Ath Hours After Census " + year + ".xls", directory,
                             ath_mail.attachments)

                if "_WR_ATH_SF_TERM_BALANCE" in query :
                    do_query(query, date + " Athlete Tuition Fee Balance " + year + ".xls", directory,
                             ath_mail.attachments)

                if "_WR_AUDIT_CLSS_AID_DISB" in query :
                    do_query(query, date + " Audit Class Aid Disbursed " + year + ".xls", directory,
                             kkt_mail.attachments)

                if "_WR_ISA_PER_TERM" in query :
                    do_query(query, date + " ISA Per Term FISA" + year + ".xls", directory,
                             kkt_mail.attachments)  

                if "_WR_AWD_UG_NOW_GRAD_ATH" in query :
                    do_query(query, date + " Ath Awards past Grad Term " + year + ".xls", directory,
                             ath_mail.attachments)

                if "_WR_AWD_UG_NOW_GRAD_FC" in query :
                    do_query(query, date + " Federal Awards past Grad Term " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_AWD_UG_NOW_GRAD_SV" in query :
                    do_query(query, date + " Scholar Awards past Grad Term " + year + ".xls", directory,
                             hj_mail.attachments)

                if "_WR_CHKLST_STATUS_ERROR" in query :
                    do_query(query, date + " Checklist Status Error " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "WR_CMT_CDE_O_AGR_LMT_2" in query and year in query[:-8]:
                    do_query(query, date + " Comment Code Over Aggregate No FATERM Req " + year + ".xls", directory,
                             loans_kkt_mail.attachments)

                if "_WR_DISB_ATH_FAILURE" in query :
                    do_query(query, date + " Authorization Failure 20" + year + ".xls", disb_failure_directory,
                             null_mail.attachments)

                if "_WR_DL_DISBURSED_LTHT" in query :
                    do_query(query, date + " DL Disbursed LTHT " + year + ".xls", directory,
                             kkt_mail.attachments)

                if "_WR_DL_EC_SUSPENDED" in query :
                    do_query(query, date + " DL Entrance Counseling Suspense " + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "_WR_DL_ORIG_TRNS_PEND" in query :
                    do_query(query, date + " DL Orig Trans Pending " + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "_WR_EFT_CONSENT_VERIF" in query :
                    do_query(query, date + " EFT Consent Verification 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_FAFSA_CKLST_INCMP" in query :
                    do_query(query, date + " PLUS FAFSA Incomplete " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if  "_WR_FALL_TOTAL_WDRN_DRP" in query :
                    do_query(query, date + " Fall Disb Total Withdrawn Drop " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if  "_WR_SPR_TOTAL_WDRN_DRP" in query :
                    do_query(query, date + " Spring Disb Total Withdrawn Drop " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if  "WR_SNGDO_CAMPUS" in query and year in query[:-8] :
                    do_query(query, date + " Asian-SNGDO Campus " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if  "_WR_SUM_TOTAL_WDRN_DRP" in query :
                    do_query(query, date + " Summer Disb Total Withdrawn Drop " + year + " .xls", directory,
                             kkmt_mail.attachments)

                if "_WR_FARC_CHECKLIST" in query :
                    do_query(query, date + " FARC 30 Day Review " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_FARC_CMNT_CODES" in query :
                    do_query(query, date + " Initiated FARC w ISIR Cmnt Codes " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_FED_AID_OVERAWARD" in query :
                    do_query(query, date + " Federal Aid Overaward " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_FGED_ISIR_DEGREE" in query :
                    do_query(query, date + " FGED ISIR Degree 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if ("_WR_FPEL" + year + "_INITIATED_AWDED") in query:
                    do_query(query, date + " FPEL" + year + " Initiated Pell.xls", directory,
                             kkt_mail.attachments)

                if "WR_FREV_GR_WS" in query and year in query:
                    do_query(query, date + " Grad FREV with Work Study" + year + ".xls", directory,
                             kmt_mail.attachments)

                if "_WR_GENDER" in query :
                    do_query(query, date + " Gender Discrepancies 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_HEDU_PARAMEDIC" in query :
                    do_query(query, date + " HEDU Paramedic Class 20" + year + "F.xls", directory,
                             kkt_mail.attachments)

                if "R_HOME_SCHOOLED" in query :
                    do_query(query, date + " Home Schooled Check " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_HRS_DECREASE_ATH" in query :
                    do_query(query, date + " Hours Decrease Athlete " + year + ".xls", directory,
                             ath_mail.attachments)

                if "_WR_HRS_DECREASE_FC" in query :
                    do_query(query, date + " Hours Decrease FC " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_HRS_DECREASE_SV" in query :
                    do_query(query, date + " Hours Decrease SV " + year + ".xls", directory,
                             ashley_mail.attachments)

                if "_WR_FHST_I_HST_COMPLETE" in query :
                    do_query(query, date + " HS Transcript 'C' FHST" + year + " 'I'.xls", directory,
                             kkmt_mail.attachments)

                if "_WR_ISIR_AS_EFC" in query :
                    do_query(query, date + " ISIR Assumption EFC 20" + year + ".xls", directory,
                             mat_mail.attachments)

                if "_WR_ISIR_COR_ASSESSMENT" in query :
                    do_query(query, date + " ISIR Correction Assessment " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_ISIR_CORR_REJECT" in query :
                    do_query(query, date + " ISIR Correction Rejected " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_ISIR_DGR_ANSW_CHNG" in query :
                    do_query(query, date + " ISIR Degree Answer Change " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_ISIR_DEP_STAT_PRB" in query :
                    do_query(query, date + " ISIR Dependency 20" + year + ".xls", directory,
                             mat_mail.attachments)

                if "_WR_ISIR_REJECTED_CORR" in query :
                    do_query(query, date + " ISIR Rejected Corrections 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if ("UUFA_WR_ISIR_REJECT_CODES" in query and year in query[:-8]) \
                        | (("UUFA_WR_ISIR_REJECT_CODES_20") in query and (year in query[:-8])) :
                    do_query(query, date + " Rejected ISIRs 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_ISIR_SS_MCH_NOT_CON" in query :
                    do_query(query, date + " SS Match Not Confirmed 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_ISIR_SUSPENSE" in query :
                    do_query(query, date + " ISIR Suspense " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_LEGAL_ALIEN_WORK" in query :
                    do_query(query, date + " Legal Alien Work 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_LN_ACCPT_STAF_31_32" in query :
                    do_query(query, date + " Stafford Accept Offer " + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "_WR_LOAN_CENSUS_DATE" in query :
                    do_query(query, date + " Loans Census Date 20" + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "_WR_LN_FA907_1_REVISED" in query :
                    do_query(query, date + " Loan Disbursed Report " + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "_WR_LN_FA907_2_REVISED" in query :
                    do_query(query, date + " Loan Not Disbursed Report " + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "R_LOAN_ORIG_DEPT_REVIEW" in query :
                    do_query(query, date + " Loan ORIG DEPT RVW " + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "_WR_LN_SENT_NO_RESPONSE" in query :
                    do_query(query, date + " Loan Sent No Response " + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "_WR_LOAN_TRANSMIT_HOLD" in query :
                    do_query(query, date + " Loan Transmit Hold " + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "_WR_LW_MD_DN_AW_NO_DISB" in query :
                    do_query(query, date + " LW MD DN Awards Not Disbursed " + year + ".xls", directory,
                             prof_kkt_mail.attachments)

                if "_WR_MNTGMR_AMCORP_OVRAW" in query :
                    do_query(query, date + " Montgomery Americorp Overaward " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_MULTIPLE_EMPLIDS" in query :
                    do_query(query, date + " Multiple EMPLIDS 20" + year + ".xls", directory,
                             sys_mail.attachments)

                if "_WR_NO_COMMENT_CODE" in query :
                    do_query(query, date + " Sub ISIR Checklist No ISIR Comment Code 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_NSLDS_LOAN_DATA" in query :
                    do_query(query, date + " NSLDS Loan Data .xls", directory,
                             loans_kkt_mail.attachments)

                if "_WR_OVRD_ACAD_LVL" in query :
                    do_query(query, date + " FA Term Override Acad Level " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_PA_EXPECT" in query :
                    do_query(query, date + " PA Expected Grad Date Blank " + year + ".xls", directory,
                             prof_kkt_mail.attachments)

                if "_WR_PA_FDEG_CHECKLIST" in query:
                    do_query(query, date + " PA MPS FDEG Checklist" + year + "U.xls", directory,
                             prof_mail.attachments)

                if "_WR_PELL_AWRD_LOCK" in query :
                    do_query(query, date + " Pell Award Lock No FPEL" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_PELL_OVERPAYMENT" in query :
                    do_query(query, date + " Pell Ovpy Check NSLDS 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_PELL_SUMMER_NO_PELL" in query :
                    do_query(query, date + " Pell Summer No Pell 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "WR_PELL_SUMMER_AGGS" in query :
                    do_query(query, date + " Pell Aggregate Summer Report" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_PELL_TERM_FT" in query :
                    do_query(query, date + " Term Pell Awards FT 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_PELL_TERM_HT" in query :
                    do_query(query, date + " Term Pell Awards HT 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_PELL_TERM_LH" in query :
                    do_query(query, date + " Term Pell Awards LH 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_PELL_TERM_NL" in query :
                    do_query(query, date + " Term Pell Awards NL 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_PELL_TERM_TQ" in query :
                    do_query(query, date + " Term Pell Awards TQ 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_PERK_SPLIT_MISMATCH" in query :
                    do_query(query, date + " Perkins Plan Split Mismatch " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_PRK_LN_ACAD_LVL_CHG" in query :
                    do_query(query, date + " Perkins Awd With Acad Lvl Change " + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "_WR_QUALITY_ASSURANCE" in query :
                    do_query(query, date + " QA Students Complete Verification 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "R_RT4_DROPPED_CLASSES" in query :
                    do_query(query, date + " RT4 Dropped Classes 20" + year + ".xls", directory,
                             kkt_mail.attachments)

                if "_WR_SCH_NOT_DISB" in query :
                    do_query(query, date + " Cash Non-Cash Sch Not Disb " + year + ".xls", directory,
                             hjjr_mail.attachments)

                if "_WR_SCHOLAR_TBP_NO_AWRD" in query and year in query[:-8]:
                    do_query(query, date + " TBP NO Award " + year + ".xls", directory,
                             hjr_mail.attachments)

                if "_WR_GRAD_FELLOW" in query and year in query[:-8]:
                    do_query(query, date + " Grad Fellowship " + year + ".xls", directory,
                             hjr_mail.attachments)

                if "_WR_SSR_MATCH_NOT_CNFRM" in query :
                    do_query(query, date + " SSR Not Confirmed 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_SSR_NOT_CNFRMD_VTRN" in query :
                    do_query(query, date + " VA Match SSR DB Override " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_SS_DB_OVERRIDE" in query :
                    do_query(query, date + " SS DB Override " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_SUB_ISIR_PACKAGED" in query :
                    do_query(query, date + " Subsequent ISIR Packaged 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_SUB_ISIR_REAWD_AID" in query :
                    do_query(query, date + " Canceled FCOR Complete " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_SUB_ISIR_SYSG" in query :
                    do_query(query, date + " Subsequent ISIR System Generated 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_SUB_ISIR_VERIFIED" in query :
                    do_query(query, date + " Subsequent ISIR Verified 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_SUMMER_NO_DL" in query :
                    do_query(query, date + " Summer Enroll No DL " + year + ".xls", directory,
                             loans_kkt_mail.attachments)

                if "_WR_SUMMER_PELL_LTHT" in query :
                    do_query(query, date + " Summer Pell LTHT " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_SSP_DOB_PRB_APPLCNT" in query :
                    do_query(query, date + " Suspense Applicant DOB Problem " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_SSP_NAME_PRB_APLCNT" in query :
                    do_query(query, date + " Suspense Applicant Name Problem " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_SSP_SSN_PRB_APLCNT" in query :
                    do_query(query, date + " Suspense Applicant SSN Problem " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_TERM_NSLDS_LOAN_YR" in query :
                    do_query(query, date + " NSLDS Loan Year Blank " + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "_WR_TITLE_VII_MED_LOANS" in query :
                    do_query(query, date + " Title VII Medical Loans TILA 20" + year + ".xls", directory,
                             prof_kkt_mail.attachments)

                if "_WR_TRANSFER_ENT_CNS" in query :
                    do_query(query, date + " Transfer Students Entrance Counseling 20" + year + ".xls", directory,
                             loans_kkt_mail.attachments)

                if "_WR_TRANSFER_STU_FA_SP" in query :
                    do_query(query, date + " Transfer Students Fall-Spring 20" + year + ".xls", directory,
                             buttars_mail.attachments)

                if "_WR_UG_GR_DIR_LN_GR_TRM" in query :
                    do_query(query, date + " UG-GR Direct Ln Grad Term " + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "_WR_UG_GR_PLUS_GR_TERM" in query :
                    do_query(query, date + " UG-GR PLUS Grad Term " + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "WR_UAC_FASI_STATUS" in query :
                    do_query(query, date + " UAC FASI Status " + year + ".xls", directory,
                             kkt_mail.attachments)

                if "_WR_UAC_SNGDO" in query :
                    do_query(query, date + " UAC SNGDO Campus 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_UNDOCUMENTED_STUDENTS" in query :
                    do_query(query, date + " Undocumented Student Awards " + year + ".xls", directory,
                             kkt_mail.attachments)

                if "_WR_VERI_CHKLST_MISSING" in query :
                    do_query(query, date + " Verification Checklist Missing 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_VERI_INCOME_ADJ" in query :
                    do_query(query, date + " Income Adjustments 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_VER_NOT_CONSL" in query :
                    do_query(query, date + " Verification Not Consolidated 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_VETERAN_ACTIVE_DUTY" in query :
                    do_query(query, date + " Veteran Active Duty 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_VETERAN_NO_QUALIFY" in query :
                    do_query(query, date + " Veteran No Qualify 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_WEEKS_OF_INSTR_FIX" in query :
                    do_query(query, date + " Weeks of Instruction 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "_WR_DL_AY_SP_CANCELED" in query :
                    do_query(query, date + " DL AY SP Cancelled " + year + ".xls", directory,
                             loans_kkt_mail.attachments)

                if "_WR_LOAN_TRANSMIT_HOLD_13" in query:
                    do_query(query, date + " Loan Transmit Hold 13.xls", directory,
                             loans_kt_mail.attachments)

                if "_WR_REJECT_CODE_ON_ISIR" in query :
                    do_query(query, date + " Rejected ISIR's " + year + ".xls", directory,
                             kmt_mail.attachments)

                if "_WR_RT4_FA_DROP_CLASSES" in query :
                    do_query(query, date + " RT4 Fall Drop Classes 20" + year + ".xls", directory,
                             kkt_mail.attachments)

                if "_WR_RT4_SP_DROP_CLASSES" in query :
                    do_query(query, date + " RT4 Spring Drop Classes 20" + year + ".xls", directory,
                             kkt_mail.attachments)

                if "_WR_RT4_SU_DROP_CLASSES" in query :
                    do_query(query, date + " RT4 Summer Drop Classes 20" + year + ".xls", directory,
                             kkt_mail.attachments)

                if "WR_AWARDS_OTHER_INST" in query :
                    do_query(query, date + " Checklist FAOI" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "WR_DEP_PRNT_SSN_RVW" in query :
                    do_query(query, date + " Parent SSN Review " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "WR_DN_LW_MD_AID_ATRB" in query :
                    do_query(query, date + " DN-LW-MD Student Aid Career " + year + ".xls", directory,
                             prof_kkt_mail.attachments)

                if "WR_FSEOG_NO_PELL" in query :
                    do_query(query, date + " DNFSEOG no Pell " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "WR_FT_CLASS_OVERRIDES" in query :
                    do_query(query, date + " Class Overrides " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "WR_GR_ACAD_LV_OUT_SYNC" in query :
                    do_query(query, date + " GR Academic Levels Out of Sync " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "WR_PELL_COA_DOUBLE" in query :
                    do_query(query, date + " PELL COA Double  " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "WR_PKG_AWD_NO_BDGT" in query :
                    do_query(query, date + " Award NO Budget for Term " + year + ".xls", directory,
                             kkt_mail.attachments)

                if "WR_SCH_TUITION_FEES" in query :
                    do_query(query, date + " Waiver-Scholar Tuition Fees " + year + ".xls", directory,
                             hj_mail.attachments)

                if "WR_SCHOL_GRAD_DATE" in query :
                    do_query(query, date + " Scholarship-Expected Grad Date  " + year + ".xls", directory,
                             hjr_mail.attachments)

                if "_WR_STDNT_NOT_PACKAGED" in query :
                    do_query(query, date + " Students Not Packaged " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "WR_SAVE_CTZNSHIP_VER" in query :
                    do_query(query, date + " SAVE SB81 CTZNSHP VERI " + year + ".xls", save_directory,
                             bk_mail.attachments)

                if "WR_ALL_C_FVRA_I_NO_COR" in query :
                    do_query(query, date + " FVRA Ini with no Correction " + year + ".xls", save_directory,
                             kkmt_mail.attachments)

                if "WR_CORRECTION_NOT_SENT" in query :
                    do_query(query, date + " Corrections Sent still Pending " + year + ".xls", save_directory,
                             kkmt_mail.attachments)

                # Manually run Queries
                if "_WR_LOAN_EFT_DETAIL_ERROR" in query:
                    do_query(query, date + " Loan EFT Detail Error.xls", directory,
                             loans_kkt_mail.attachments)

                if "_WR_NSL_PROMISSORY_NOTE" in query :
                    do_query(query, date + " NSL Promissory Note " + year + ".xls", directory,
                             loans_kt_mail.attachments)

                if "UUFA_AP_RPKG_FPEL_AWARD_LCK" in query:
                    do_query(query, date + " Pell Award Lock FPEL" + year + ".xls", directory,
                             loans_kkt_mail.attachments)

                if "WR_FAVR_I_NO_FCOR_ALL_C" in query:
                    do_query(query, date + " FAVR I No FCOR all check Completed.xls", directory,
                             loans_kkt_mail.attachments)

                # Packaging queries that are being manually run.
                if "PRT_ATH_ACCEPT_FED_AID" in query :
                    do_query(query, date + " Athlete Accepted Federal Aid " + year + ".xls", packaging_directory,
                             ath_mail.attachments)

                if "PRT_ATH_AWD_CBA_GRANT" in query :
                    do_query(query, date + " Athlete Awarded CBA Grant " + year + ".xls", packaging_directory,
                             ath_mail.attachments)

                if "PRT_ATHLETE_GRAD_DATE" in query :
                    do_query(query, date + " Athlete Accepted Grad Date " + year + ".xls", packaging_directory,
                             ath_mail.attachments)

                if "PRT_ATH_OFFERED_FED_AID" in query :
                    do_query(query, date + " Athlete Offered Federal Aid " + year + ".xls", packaging_directory,
                             ath_mail.attachments)
