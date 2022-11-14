# Daily Queries - to be modified based on AY and remove attachments
# to be called in MAIN
import os

def do_dailies(test, date, year, query, renamed):
    
    month_folder = date[:2] + "-20" + date[-2:]

    aid_year = str(int(year) - 1) + "-" + str(year)

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


    if not os.path.isdir(archive_directory):
        os.makedirs(archive_directory)
    if not os.path.isdir(royall_directory):
        os.makedirs(royall_directory)
    if not os.path.isdir(pell_directory):
        os.makedirs(pell_directory)
    if not os.path.isdir(disb_directory ):
        os.makedirs(disb_directory)
    if not os.path.isdir(refund_directory):
        os.makedirs(refund_directory)

    year = year[2:]

    move_directory = "Daily Reports"
    move_pell_directory = "Pell Reports"


    if "IL_ATHLETE_OVERAWARD" in query :
        return (query, renamed, archive_directory, move_directory) 

    if "IL_CMT_CDE_OVR_AGR_LMT" in query :
        return (query, renamed, archive_directory, move_directory)

    if "IL_COMMENT_CODE_298" in query :
        return (query, renamed, archive_directory, move_directory)

    if "IL_FDEG_FFBD_FBLK_FFBC" in query :
        return (query, renamed, archive_directory, move_directory)

    if "IL_COMPLETE_FDEG" in query :
        return (query, renamed, archive_directory, move_directory)

    if "IL_CORR_NOT_MARK_SENT" in query :
        return (query, renamed, archive_directory, move_directory)

    if "UUFA_IL_CORR_SENT_RJCT_CD1" in query :
        return (query, renamed, archive_directory, move_directory)

    if "IL_ATHLETE_RESIDENCY" in query :
        return (query, renamed, archive_directory, move_directory)
    
    if query.startswith("FA_IL_ENRL_GR_DATE_ERRORS") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_FBKP") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_FOUT") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("FA_IL_FP1B") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("FA_IL_FP2B") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("FA_IL_FP1N") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("FA_IL_FP2N") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_FPJ") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_ISIR_02_IND_UP_DWN") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_FEHU") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_IRS_DRT_02") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("FA_IL_ISIR_CMT_CODE_359_360") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_ISIR_GRD_I_UG_FATRM") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_ISIR_PRMARY_EFC_DIF") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_ISIR_LOADED_NOT_PKG") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_LN_EXP_GRAD_DATE") :
        return (query, renamed, archive_directory, move_directory)

    if (("STDT_WITH_FLPR_INIT") in query) :
        return (query, renamed, archive_directory, move_directory)
                
    if (("IL_STDT_WITH_FLNPR_INIT") in query) :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_NURSING_LOANS_TILA") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("FA_IL_OTHER_ATB_20") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("FA_IL_OTHER_ATTND") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_PELL_LEU_C") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_PELL_LEU_E") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_PELL_MAX_ELIG") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_SF_RFND_AWD_NO_POST") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_SUB_ISIR_NO_PACKAGE") :
        return (query, renamed, archive_directory, move_directory)

    if "IL_SUB_ISIR_SYSG" in query :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_VET_ACTV_DUTY_STAT") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_VER_I_SUB_SUSP_ISIR") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_V5_VER_AFTR_OTH_VER") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_UPDATED_SEC") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_FATN_INITIATED") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_FED_AID_OVERAWARD") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_ALL_ITEMS_OVERAWARD") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_FHST_I_HST_COMPLETE") :
        return (query, renamed, archive_directory, move_directory)

        #if query.startswith("ussf0034"): # Leave this one commented out?
        #    do_query(query, date + " " + query, refund_directory,
        #             aehjkkt_mail.attachments) 

    if query.startswith("UUFA_REFUND_HOLDS"):
        return (query, renamed, refund_directory, move_directory)

    if query.startswith("UUFA_IL_PKG_SCH_EXP_GRAD_FA") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_PKG_FED_EXP_GRAD_FA") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_FPEL") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_PACKAGING_C_NO_FED_AID") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_PERKINS_NOT_DISBURSED"):
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_ITM_TYPE_NOT_IN_NEXT_AY"):
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_FREV_CHECKLIST_INT") :
        return (query, renamed, archive_directory, move_directory)

    if query.startswith("UUFA_IL_FREV_DOES_NOT_EXIST") :
        return (query, renamed, archive_directory, move_directory)

    if "IL_STU_WITH_06_CODE" in query :
        return (query, renamed, archive_directory, move_directory)

    if "IL_GRNT_UG_5_YR_2BCH" in query :
        return (query, renamed, archive_directory, move_directory)

    if "IL_NSLDS_NO_MCH_DB_FLG" in query :
        return (query, renamed, archive_directory, move_directory)

    if "IL_FAVR_CHKLST_INT" in query :
        return (query, renamed, archive_directory, move_directory)

    if "QJ23029" in query :
        return(query, renamed, royall_directory, move_directory)

    if "IL_RES_NON_RES_BDGT" in query :
        return (query, renamed, archive_directory, move_directory)

    if "PELL_RPKG_VAR_FLAG_2" in query :
        return(query, renamed, pell_directory, move_pell_directory)

    if "IL_3RD_PARTY_EXCEPT" in query :
        return (query, renamed, archive_directory, move_directory)

    if "IL_3RD_PARTY_MAIN" in query and "SU" not in query :
        return (query, renamed, archive_directory, move_directory)

    if "IL_3RD_PARTY_NO_BDGT" in query :
        return (query, renamed, archive_directory, move_directory)

    if "IL_3RD_PARTY_MAIN_SU" in query :
        return (query, renamed, archive_directory, move_directory)

    if "PDQ_SAP_HOLD_DEL" in query:
        return (query, renamed, disb_directory, move_directory)

    if "SHOPPING_SHEET_UG" in query:
        return (query, renamed, disb_directory, move_directory)

    if "_IL_REPEAT_COURSES_FALL" in query :
        return (query, renamed, disb_directory, move_directory)

    if "_IL_REPEAT_COURSES_SPR" in query :
        return (query, renamed, disb_directory, move_directory)

    if "_IL_REPEAT_COURSES_SUM" in query :
        return (query, renamed, disb_directory, move_directory)

    if "_INCOMPLETE_CHECKLIST" in query:
        return (query, renamed, disb_directory, move_directory)

    if "IL_SUMMER_AWARDING" in query :
        return (query, renamed, disb_directory, move_directory)

    if "IL_ISIR_SSN_MISMATCH" in query :
        return (query, renamed, disb_directory, move_directory)

    return "Empty"


