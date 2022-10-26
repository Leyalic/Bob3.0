# Daily Queries - to be modified based on AY and remove attachments
# to be called in MAIN

def do_dailies():
    move_directory = "Daily Reports"

    year = "23"
    aid_year = "20" + str(int(year) - 1) + "-20" + year
    for query_name in os.listdir("."):
        if query_name.startswith("UUFA_IL_ALL_ITEMS_OVERAWARD"):
            if "22" in query_name.split("-")[0]:
                year = "22"
            break
    aid_year = "20" + str(int(year) - 1) + "-20" + year
    if test:
        archive_directory = os.path.realpath(os.path.join('C:\Testing Bob/Daily', aid_year, month_folder))
        royall_directory = os.path.realpath('C:\Testing Bob/Royall')
        pell_directory = os.path.realpath(os.path.join('C:\Testing Bob/QUERIES\Pell Repackaging', aid_year))
        disb_directory = os.path.realpath('C:\Testing Bob\QUERIES\Disbursement\Pre-Disbursement Queries')
        refund_directory = os.path.realpath(os.path.join('C:\Testing Bob/QUERIES\Refund Credit Holds', month_folder))
    else:
        archive_directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Daily', aid_year, month_folder))
        royall_directory = os.path.realpath('O:/Systems/Royall')
        pell_directory = os.path.realpath(os.path.join('O:\Systems\QUERIES\Pell Repackaging', aid_year))
        disb_directory = os.path.realpath("O:\Systems\QUERIES\Disbursement\Pre-Disbursement Queries")
        refund_directory = os.path.realpath(os.path.join('O:\Systems\QUERIES\Refund Credit Holds', month_folder))

    # the list 'my_path' should be populated with the FOLDER variables above.
    #if not os.path.isdir(directory):
    #    os.makedirs(directory)
    #if not os.path.isdir(royall_directory):
    #    os.makedirs(royall_directory)
    #if not os.path.isdir(pell_directory):
    #    os.makedirs(pell_directory)
    #if not os.path.isdir(disb_directory ):
    #    os.makedirs(disb_directory)
    #if not os.path.isdir(refund_directory):
    #    os.makedirs(refund_directory)

    # Change File_Name to be file as it is received and _new_file_name to what
    # the new file should be.  Prefix date will be added.
    if ("22" in query_name.split("-")[0]):
        for query in os.listdir("."):

            # NEW FORMAT
            #if "IL_ATHLETE_OVERAWARD" in query and year in query[:-8]:
            #       return (query, date + query + year + ".xls", archive_directory, move_directory) 

            if "IL_ATHLETE_OVERAWARD" in query and year in query[:-8]:
                do_query(query, date + " Athlete Aid Overaward " + year + ".xls", archive_directory,
                         ath_mail.attachments) 

            if "IL_CMT_CDE_OVR_AGR_LMT" in query and year in query[:-8]:
                do_query(query, date + " Comment Code Over Aggregate " + year + ".xls", archive_directory,
                         loans_kt_mail.attachments)

            if "IL_COMMENT_CODE_298" in query :
                do_query(query, date + " IASG - Pell Eligible 20" + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if "IL_FDEG_FFBD_FBLK_FFBC" in query :
                do_query(query, date + " Complete FDEG FFBD FBLK FFBC " + year + ".xls", archive_directory,
                         prof_kmt_mail.attachments)

            if "IL_COMPLETE_FDEG" in query :
                do_query(query, date + " FDEG Update 20" + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if "IL_CORR_NOT_MARK_SENT" in query :
                do_query(query, date + " Corrections not Marked to Sent 20" + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if "UUFA_IL_CORR_SENT_RJCT_CD1" in query :
                do_query(query, date + " Correction Sent Reject Code 1 20" + year + ".xls", archive_directory,
                         kkmt_mail.attachments)

            if "IL_ATHLETE_RESIDENCY" in query :
                do_query(query, date + " ATH Res Change " + year + ".xls", archive_directory,
                         ath_mail.attachments)
    
            if query.startswith("FA_IL_ENRL_GR_DATE_ERRORS") :
                do_query(query, date + " Place FDIP" + year + " Checklist 20" + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("UUFA_IL_FBKP") :
                do_query(query, date + " FBKP" + year + " Checklist Initiated.xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("UUFA_IL_FOUT") :
                do_query(query, date + " Outside Resources 20" + year + ".xls", archive_directory,
                         hjr_mail.attachments)

            if query.startswith("FA_IL_FP1B") :
                do_query(query, date + " FP1B" + year + " Checklist " + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("FA_IL_FP2B") :
                do_query(query, date + " FP2B" + year + " Checklist " + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("FA_IL_FP1N") :
                do_query(query, date + " FP1N" + year + " Checklist " + year + ".xls", archive_directory,
                         hjr_mail.attachments)

            if query.startswith("FA_IL_FP2N") :
                do_query(query, date + " FP2N" + year + " Checklist " + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("UUFA_IL_FPJ") :
                do_query(query, date + " FPJ" + year + " Checklist 20" + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("UUFA_IL_ISIR_02_IND_UP_DWN") :
                do_query(query, date + " ISIR Service IND UP Down 20" + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("UUFA_IL_FEHU") :
                do_query(query, date + " Initiated FEHU" + year + " Checklist.xls", archive_directory,
                         kt_mail.attachments)

            if query.startswith("UUFA_IL_IRS_DRT_02") :
                do_query(query, date + " IRS Data Retrieval Equal to 02 " + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("FA_IL_ISIR_CMT_CODE_359_360") :
                do_query(query, date + " ISIR Comment Code 359 or 360 " + year + ".xls", archive_directory,
                         kt_mail.attachments)

            if query.startswith("UUFA_IL_ISIR_GRD_I_UG_FATRM") :
                do_query(query, date + " ISIR Graduate Independent UG FATERM 20" + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("UUFA_IL_ISIR_PRMARY_EFC_DIF") :
                do_query(query, date + " Primary EFC Difference 20" + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("UUFA_IL_ISIR_LOADED_NOT_PKG") :
                do_query(query, date + " ISIR Loaded Not Packaged 20" + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("UUFA_IL_LN_EXP_GRAD_DATE") :
                do_query(query, date + " Loan Awd No FLPR Grad Date " + year + ".xls", archive_directory,
                         loans_kt_mail.attachments)

            if (("STDT_WITH_FLPR_INIT") in query) :
                do_query(query, date + " Students with FLPR Initiated.xls", archive_directory,
                         loans_kt_mail.attachments)
                
            if (("IL_STDT_WITH_FLNPR_INIT") in query) :
                do_query(query, date + " Students with FLNPR Initiated.xls", archive_directory,
                         loans_kt_mail.attachments)

            if query.startswith("UUFA_IL_NURSING_LOANS_TILA") :
                do_query(query, date + " Nursing Loans 20" + year + ".xls", archive_directory,
                         loans_kt_mail.attachments)

            if query.startswith("FA_IL_OTHER_ATB_20") :
                do_query(query, date + " ISIR Other ATB 20" + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("FA_IL_OTHER_ATTND") :
                do_query(query, date + " Attend Other Institution 20" + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("UUFA_IL_PELL_LEU_C") :
                do_query(query, date + " Pell LEU Limit Flag C " + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("UUFA_IL_PELL_LEU_E") :
                do_query(query, date + " Pell LEU Limit Flag E " + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("UUFA_IL_PELL_MAX_ELIG") :
                do_query(query, date + " Pell Max Eligibility " + year + ".xls", archive_directory,
                         kt_mail.attachments)

            if query.startswith("UUFA_IL_SF_RFND_AWD_NO_POST") :
                do_query(query, date + " Refund Post Third Party 20" + year + ".xls", archive_directory,
                         hjr_mail.attachments)

            if query.startswith("UUFA_IL_SUB_ISIR_NO_PACKAGE") :
                do_query(query, date + " Subsequent ISIR Not Package Not Verified 20" + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if "IL_SUB_ISIR_SYSG" in query :
                do_query(query, date + " Subsequent ISIR System Generated 20" + year + ".xls", archive_directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_IL_VET_ACTV_DUTY_STAT") :
                do_query(query, date + " Veteran Active Duty Status 20" + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("UUFA_IL_VER_I_SUB_SUSP_ISIR") :
                do_query(query, date + " FAVR Initiated Susp ISIR Psbl DRT " + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("UUFA_IL_V5_VER_AFTR_OTH_VER") :
                do_query(query, date + " Selected for V5 after other Ver " + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("UUFA_IL_UPDATED_SEC") :
                do_query(query, date + " New ISIR Updated ATB " + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("UUFA_IL_FATN_INITIATED") :
                do_query(query, date + " Review FATN Checklist 20" + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("UUFA_IL_FED_AID_OVERAWARD") :
                do_query(query, date + " Federal Aid Overaward " + year + ".xls", archive_directory,
                         kmmt_mail.attachments)

            if query.startswith("UUFA_IL_ALL_ITEMS_OVERAWARD") :
                do_query(query, date + " All Items Overaward " + year + ".xls", archive_directory,
                         kmmt_mail.attachments)

            if query.startswith("UUFA_IL_FHST_I_HST_COMPLETE") :
                do_query(query, date + " HS Transcript 'C' FHST" + year + " I.xls", archive_directory,
                         kmt_mail.attachments)

            # if query.startswith("ussf0034"):
            #     do_query(query, date + " " + query, refund_directory,
            #              aehjkkt_mail.attachments)

            if query.startswith("UUFA_REFUND_HOLDS"):
                do_query(query, date + " " + query, refund_directory,
                         null_mail.attachments)

            if query.startswith("UUFA_IL_PKG_SCH_EXP_GRAD_FA") :
                do_query(query, date + " Scholarship Aid Grad Date Fall 20" + year + ".xls", archive_directory,
                         hj_mail.attachments)

            if query.startswith("UUFA_IL_PKG_FED_EXP_GRAD_FA") :
                do_query(query, date + " Accepted Federal Aid Grad Date Fall " + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("UUFA_IL_FPEL") :
                do_query(query, date + " FPEL" + year + " No Database Match.xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("UUFA_PACKAGING_C_NO_FED_AID") :
                do_query(query, date + " Packaging C 71%-72% No Fed Aid " + year + ".xls", archive_directory,
                         sys_mail.attachments)

            if query.startswith("UUFA_PERKINS_NOT_DISBURSED"):
                do_query(query, date + " Perkins Not Disbursed " + year + ".xls", archive_directory,
                         loans_kt_mail.attachments)

            if query.startswith("UUFA_ITM_TYPE_NOT_IN_NEXT_AY"):
                do_query(query, date + " Item Types in " + str(int(year) - 1) + " not in " + year + ".xls", archive_directory,
                         mat_mail.attachments)

            if query.startswith("UUFA_IL_FREV_CHECKLIST_INT") :
                do_query(query, date + " FREV Checklist Initiated " + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if query.startswith("UUFA_IL_FREV_DOES_NOT_EXIST") :
                do_query(query, date + " FREV Does Not Exist 20" + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if "IL_STU_WITH_06_CODE" in query and year in query[:-8]:
                do_query(query, date + " Students with Code 06 " + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if "IL_GRNT_UG_5_YR_2BCH" in query and year in query[:-8]:
                do_query(query, date + " UG 5th YR 2ND Bachelor" + year + ".xls", archive_directory,
                         kt_mail.attachments)

            if "IL_NSLDS_NO_MCH_DB_FLG" in query :
                do_query(query, date + " NSLDS No Match DB Flag " + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if "IL_FAVR_CHKLST_INT" in query :
                do_query(query, date + " FAVR Checklist Initiated " + year + ".xls", archive_directory,
                         kmt_mail.attachments)

            if "QJ23029" in query :
                do_query(query, query, royall_directory,
                         null_mail.attachments)

            if "IL_RES_NON_RES_BDGT" in query :
                do_query(query, date + " Resident - Non-Resident Budget " + year + ".xls", archive_directory,
                         kkt_mail.attachments)

            if "PELL_RPKG_VAR_FLAG_2" in query :
                do_query(query, date + " PELL RPKG Var Flag 2.xls", pell_directory,
                         null_mail.attachments)

            if "IL_3RD_PARTY_EXCEPT" in query :
                do_query(query, date + " Third Party Change Exceptions " + year + ".xls", archive_directory,
                         hjr_mail.attachments)

            if "IL_3RD_PARTY_MAIN" in query and "SU" not in query :
                do_query(query, date + " Third Party Main Report " + year + ".xls", archive_directory,
                         hjr_mail.attachments)

            if "IL_3RD_PARTY_NO_BDGT" in query :
                do_query(query, date + " Third Party No Budget " + year + ".xls", archive_directory,
                         hjr_mail.attachments)

            if "IL_3RD_PARTY_MAIN_SU" in query :
                do_query(query, date + " Third Party Main Rpt Summer " + year + ".xls", archive_directory,
                         hjr_mail.attachments)

            if "PDQ_SAP_HOLD_DEL" in query:
                do_query(query, date + " Offers with Previous SAP " + year + ".xls", disb_directory,
                         null_mail.attachments)

            if "SHOPPING_SHEET_UG" in query:
                do_query(query, date + " Shopping Sheet Group List " + year + ".xls", disb_directory,
                         null_mail.attachments)

            if "_IL_REPEAT_COURSES_FALL" in query and (year in query[:-8]):
                do_query(query, date + " Repeat Courses Fall " + year + ".xls", disb_directory,
                         bkk_mail.attachments)

            if "_IL_REPEAT_COURSES_SPR" in query and (year in query[:-8]):
                do_query(query, date + " Repeat Courses Spring " + year + ".xls", disb_directory,
                         bkk_mail.attachments)

            if "_IL_REPEAT_COURSES_SUM" in query and (year in query[:-8]):
                do_query(query, date + " Repeat Courses Summer " + year + ".xls", disb_directory,
                         bkk_mail.attachments)

            if "_INCOMPLETE_CHECKLIST" in query:
                do_query(query, date + " famil2 " + year + ".xls", disb_directory,
                         null_mail.attachments)

            if "IL_SUMMER_AWARDING" in query and (year in query[:-8]):
                do_query(query, date + " Summer Awarding " + year + ".xls", disb_directory,
                         ckkls_mail.attachments)

            if "IL_ISIR_SSN_MISMATCH" in query and (year in query[:-8]):
                do_query(query, date + " ISIR SSN Mismatch " + year + ".xls", disb_directory,
                         kmt_mail.attachments)
    else:
        for query in os.listdir("."):
            if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if "IL_ATHLETE_OVERAWARD" in query :
                    do_query(query, date + " Athlete Aid Overaward " + year + ".xls", archive_directory,
                             ath_mail.attachments) 
                    
                if "SHOPPING_SHEET_UG" in query:
                    do_query(query, date + " Shopping Sheet Group List " + year + ".xls", disb_directory,
                         null_mail.attachments)

                if "IL_CMT_CDE_OVR_AGR_LMT" in query :
                    do_query(query, date + " Comment Code Over Aggregate " + year + ".xls", archive_directory,
                             loans_kt_mail.attachments)

                if query.startswith("UUFA_REFUND_HOLDS"):
                    do_query(query, date + " " + query, refund_directory,
                             null_mail.attachments)

                if "PDQ_SAP_HOLD_DEL" in query:
                    do_query(query, date + " Offers with Previous SAP " + year + ".xls", disb_directory,
                             null_mail.attachments)

                if "IL_COMMENT_CODE_298" in query :
                    do_query(query, date + " IASG - Pell Eligible 20" + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if "IL_FDEG_FFBD_FBLK_FFBC" in query :
                    do_query(query, date + " Complete FDEG FFBD FBLK FFBC " + year + ".xls", archive_directory,
                             prof_kmt_mail.attachments)

                if "IL_COMPLETE_FDEG" in query :
                    do_query(query, date + " FDEG Update 20" + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if "IL_CORR_NOT_MARK_SENT" in query :
                    do_query(query, date + " Corrections not Marked to Sent 20" + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if "UUFA_IL_CORR_SENT_RJCT_CD1" in query :
                    do_query(query, date + " Correction Sent Reject Code 1 20" + year + ".xls", archive_directory,
                             kkmt_mail.attachments)

                if "IL_ATHLETE_RESIDENCY" in query :
                    do_query(query, date + " ATH Res Change " + year + ".xls", archive_directory,
                             ath_mail.attachments)

                if query.startswith("FA_IL_ENRL_GR_DATE_ERRORS") :
                    do_query(query, date + " Place FDIP" + year + " Checklist 20" + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_IL_FBKP") :
                    do_query(query, date + " FBKP" + year + " Checklist Initiated.xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_IL_FOUT") :
                    do_query(query, date + " Outside Resources 20" + year + ".xls", archive_directory,
                             hjr_mail.attachments)

                if query.startswith("FA_IL_FP1B") :
                    do_query(query, date + " FP1B" + year + " Checklist " + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("FA_IL_FP2B") :
                    do_query(query, date + " FP2B" + year + " Checklist " + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("FA_IL_FP1N") :
                    do_query(query, date + " FP1N" + year + " Checklist " + year + ".xls", archive_directory,
                             hjr_mail.attachments)

                if query.startswith("FA_IL_FP2N") :
                    do_query(query, date + " FP2N" + year + " Checklist " + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_IL_FPJ") :
                    do_query(query, date + " FPJ" + year + " Checklist 20" + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_IL_ISIR_02_IND_UP_DWN") :
                    do_query(query, date + " ISIR Service IND UP Down 20" + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_IL_FEHU") :
                    do_query(query, date + " Initiated FEHU" + year + " Checklist.xls", archive_directory,
                             kt_mail.attachments)

                if query.startswith("UUFA_IL_IRS_DRT_02") :
                    do_query(query, date + " IRS Data Retrieval Equal to 02 " + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("FA_IL_ISIR_CMT_CODE_359_360") :
                    do_query(query, date + " ISIR Comment Code 359 or 360 " + year + ".xls", archive_directory,
                             kt_mail.attachments)

                if query.startswith("UUFA_IL_ISIR_GRD_I_UG_FATRM") :
                    do_query(query, date + " ISIR Graduate Independent UG FATERM 20" + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_IL_ISIR_PRMARY_EFC_DIF") :
                    do_query(query, date + " Primary EFC Difference 20" + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_IL_ISIR_LOADED_NOT_PKG") :
                    do_query(query, date + " ISIR Loaded Not Packaged 20" + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_IL_LN_EXP_GRAD_DATE") :
                    do_query(query, date + " Loan Awd No FLPR Grad Date " + year + ".xls", archive_directory,
                             loans_kt_mail.attachments)

                if (("STDT_WITH_FLPR_INIT") in query) :
                    do_query(query, date + " Students with FLPR Initiated.xls", archive_directory,
                             loans_kt_mail.attachments)

                if query.startswith("UUFA_IL_NURSING_LOANS_TILA") :
                    do_query(query, date + " Nursing Loans 20" + year + ".xls", archive_directory,
                             loans_kt_mail.attachments)

                if query.startswith("FA_IL_OTHER_ATB_20") :
                    do_query(query, date + " ISIR Other ATB 20" + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("FA_IL_OTHER_ATTND") :
                    do_query(query, date + " Attend Other Institution 20" + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_IL_PELL_LEU_C") :
                    do_query(query, date + " Pell LEU Limit Flag C " + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_IL_PELL_LEU_E") :
                    do_query(query, date + " Pell LEU Limit Flag E " + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_IL_PELL_MAX_ELIG") :
                    do_query(query, date + " Pell Max Eligibility " + year + ".xls", archive_directory,
                             kt_mail.attachments)

                if query.startswith("UUFA_IL_SF_RFND_AWD_NO_POST") :
                    do_query(query, date + " Refund Post Third Party 20" + year + ".xls", archive_directory,
                             hjr_mail.attachments)

                if query.startswith("UUFA_IL_SUB_ISIR_NO_PACKAGE") :
                    do_query(query, date + " Subsequent ISIR Not Package Not Verified 20" + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if "IL_SUB_ISIR_SYSG" in query :
                    do_query(query, date + " Subsequent ISIR System Generated 20" + year + ".xls", archive_directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_IL_VET_ACTV_DUTY_STAT") :
                    do_query(query, date + " Veteran Active Duty Status 20" + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_IL_VER_I_SUB_SUSP_ISIR") :
                    do_query(query, date + " FAVR Initiated Susp ISIR Psbl DRT " + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_IL_V5_VER_AFTR_OTH_VER") :
                    do_query(query, date + " Selected for V5 after other Ver " + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_IL_UPDATED_SEC") :
                    do_query(query, date + " New ISIR Updated ATB " + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_IL_FATN_INITIATED") :
                    do_query(query, date + " Review FATN Checklist 20" + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_IL_FED_AID_OVERAWARD") :
                    do_query(query, date + " Federal Aid Overaward " + year + ".xls", archive_directory,
                             kmmt_mail.attachments)

                if query.startswith("UUFA_IL_ALL_ITEMS_OVERAWARD") :
                    do_query(query, date + " All Items Overaward " + year + ".xls", archive_directory,
                             kmmt_mail.attachments)

                if query.startswith("UUFA_IL_FHST_I_HST_COMPLETE") :
                    do_query(query, date + " HS Transcript 'C' FHST" + year + " I.xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_IL_PKG_SCH_EXP_GRAD_FA") :
                    do_query(query, date + " Scholarship Aid Grad Date Fall 20" + year + ".xls", archive_directory,
                             hj_mail.attachments)

                if query.startswith("UUFA_IL_PKG_FED_EXP_GRAD_FA") :
                    do_query(query, date + " Accepted Federal Aid Grad Date Fall " + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_IL_FPEL") :
                    do_query(query, date + " FPEL" + year + " No Database Match.xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_PACKAGING_C_NO_FED_AID") :
                    do_query(query, date + " Packaging C 71%-72% No Fed Aid " + year + ".xls", archive_directory,
                             sys_mail.attachments)

                if query.startswith("UUFA_IL_FREV_CHECKLIST_INT") :
                    do_query(query, date + " FREV Checklist Initiated " + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if query.startswith("UUFA_IL_FREV_DOES_NOT_EXIST") :
                    do_query(query, date + " FREV Does Not Exist 20" + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if "IL_STU_WITH_06_CODE" in query :
                    do_query(query, date + " Students with Code 06 " + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if "IL_GRNT_UG_5_YR_2BCH" in query :
                    do_query(query, date + " UG 5th YR 2ND Bachelor.xls", archive_directory,
                             kt_mail.attachments)

                if "IL_NSLDS_NO_MCH_DB_FLG" in query :
                    do_query(query, date + " NSLDS No Match DB Flag " + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if "IL_FAVR_CHKLST_INT" in query :
                    do_query(query, date + " FAVR Checklist Initiated " + year + ".xls", archive_directory,
                             kmt_mail.attachments)

                if "IL_RES_NON_RES_BDGT" in query :
                    do_query(query, date + " Resident - Non-Resident Budget " + year + ".xls", archive_directory,
                             kkt_mail.attachments)

                if "IL_3RD_PARTY_EXCEPT" in query :
                    do_query(query, date + " Third Party Change Exceptions " + year + ".xls", archive_directory,
                             hjr_mail.attachments)

                if "IL_3RD_PARTY_MAIN" in query  and "SU" not in query :
                    do_query(query, date + " Third Party Main Report " + year + ".xls", archive_directory,
                             hjr_mail.attachments)

                if "IL_3RD_PARTY_NO_BDGT" in query :
                    do_query(query, date + " Third Party No Budget " + year + ".xls", archive_directory,
                             hjr_mail.attachments)

                if "IL_3RD_PARTY_MAIN_SU" in query :
                    do_query(query, date + " Third Party Main Rpt Summer " + year + ".xls", archive_directory,
                             hjr_mail.attachments)

                if "_IL_REPEAT_COURSES_FALL" in query :
                    do_query(query, date + " Repeat Courses Fall " + year + ".xls", disb_directory,
                             bkk_mail.attachments)

                if "_IL_REPEAT_COURSES_SPR" in query :
                    do_query(query, date + " Repeat Courses Spring " + year + ".xls", disb_directory,
                             bkk_mail.attachments)

                if "_IL_REPEAT_COURSES_SUM" in query :
                    do_query(query, date + " Repeat Courses Summer " + year + ".xls", disb_directory,
                             bkk_mail.attachments)

                if "IL_SUMMER_AWARDING" in query :
                    do_query(query, date + " Summer Awarding " + year + ".xls", disb_directory,
                             ckkls_mail.attachments)

                if "IL_ISIR_SSN_MISMATCH" in query :
                    do_query(query, date + " ISIR SSN Mismatch " + year + ".xls", disb_directory,
                             kmt_mail.attachments)
                    
                if "_INCOMPLETE_CHECKLIST" in query:
                    do_query(query, date + " famil2 " + year + ".xls", disb_directory,
                         null_mail.attachments)

