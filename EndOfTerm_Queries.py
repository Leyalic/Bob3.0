# End of Term Queries - to be modified
# to be called in main

def do_end_of_term_queries():
    global aid_year
    term = 'F'
    strm = "Error"
    for query_name in os.listdir("."):
        if query_name.startswith("UUFA_EOT_ACAD_PLAN_RVW"):
            prompt = "Enter Term: (e.g. 2016U, 2017F, or 2032S):"
            while True:
                strm = str.upper(raw_input(prompt))
                aid_year = strm[2:4]
                term = strm[4]
                if term == 'S' or term == 'U' or term == 'F':
                    break

    year = aid_year[-2:]
    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/SAP/', "20" + year + term))
    else:
        directory = os.path.realpath(os.path.join('O:\Systems\QUERIES/SAP/', "20" + year + term))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    if ("22" in query_name.split("-")[0]):
        for query in os.listdir("."):
            if query.startswith("UUFA_EOT_ACAD_PLAN_RVW_FRAP"):
                do_query(query, date + " Academic plan RVW FRAP " + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_EOT_CBA_ACAD_PRG_BELOW_FT"):
                do_query(query, date + " CBA Acad Prog below FT.xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_EOT_CBA_UNDISBURSED"):
                do_query(query, date + " CBA UNDISBURSED.xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_EOT_ALT_LOAN_SAP"):
                do_query(query, date + " Alt Loans Awards with SAP Holds.xls", directory,
                         loans_kkt_mail.attachments)

            if query.startswith("UUFA_EOT_LN_ORIG_FAIL_PENDING"):
                do_query(query, date + " Loans Originated Failed Pending.xls", directory,
                         loans_kt_mail.attachments)

            if query.startswith("UUFA_EOT_LN_ACD_PRG_BLW_HT_UND"):
                do_query(query, date + " Loan Acad Prog below HT Undisbursed.xls", directory,
                         loans_kt_mail.attachments)

            if query.startswith("UUFA_EOT_LN_ACD_PRG_BLW_HT_SUB"):
                do_query(query, date + " Loan Acad Prog below HT Subsq Disb.xls", directory,
                         loans_kt_mail.attachments)

            if query.startswith("UUFA_EOT_PRO_STDNT_SAP_WARNING"):
                do_query(query, date + " SAP Warning Professional Students.xls", directory,
                         loans_kt_mail.attachments)

            if query.startswith("UUFA_EOT_MED_SAP"):
                do_query(query, date + " Medical SAP Review.xls", directory,
                         prof_k_mail.attachments)

            if query.startswith("UUFA_EOT_FWS_WITH_NSI_HOLD"):
                do_query(query, date + " FWS with NSI Holds.xls", directory,
                         ben_mail.attachments)

            if query.startswith("UUFA_EOT_PELL_ACD_PRG_LES_THN"):
                do_query(query, date + " PELL Less Than FT.xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_EOT_PELL_OFFERED_NOT_DIS"):
                do_query(query, date + " Pell Offered Not Disbursed.xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_EOT_THESIS_STUDENT_NONRES"):
                do_query(query, date + " Thesis Students Non-Resident.xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_EOT_SCH_ACAD_PROG_REVIEW"):
                do_query(query, date + " Scholarship Academic Progress Review " + year + ".xls", directory,
                         jja_mail.attachments)

            if query.startswith("UUFA_EOT_SCH_ACD_PRG_REVIEW"):
                do_query(query, date + " All 70000792 Item types Academic Progress Review.xls", directory,
                         jja_mail.attachments)

            if query.startswith("UUFA_EOT_SAP_AGGCP_DENTAL"):
                do_query(query, date + " SAP Aggregate Dental Career.xls", directory,
                         prof_rk_mail.attachments)

            if query.startswith("UUFA_EOT_SAP_AGGCP_LAW"):
                do_query(query, date + " SAP Aggregate Law Career.xls", directory,
                         prof_rk_mail.attachments)

            if query.startswith("UUFA_EOT_SAP_AGGCP_MED"):
                do_query(query, date + " SAP Aggregate Med Career.xls", directory,
                         prof_rk_mail.attachments)

            if query.startswith("UUFA_EOT_EU_FALL_GRADE"):
                do_query(query, date + " EU Grade Fall.xls", directory,
                         kklt_mail.attachments)

            if query.startswith("UUFA_EOT_EU_SPRING_GRADE"):
                do_query(query, date + " EU Grade Spring.xls", directory,
                         kklt_mail.attachments)

            if query.startswith("UUFA_EOT_EU_SUMMER_GRADE"):
                do_query(query, date + " EU Grade Summer.xls", directory,
                         kklt_mail.attachments)

            if query.startswith("UUFA_EOT_PELL_ELG_ENRLL_NO_AWD"):
                do_query(query, date + " Pell Eligible Enrolled NO Award.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_EOT_SAP_FSAP"):
                do_query(query, date + " FSAP Students.xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_EOT_SCHOLAR_LEADER_CGPA"):
                do_query(query, date + " Scholarship CGPA Leadership.xls", directory,
                         jja_mail.attachments)

            if "EOT_WUE_ACAD_PROG_REV" in query:
                do_query(query, date + " WUE AcadProg Rvw 700007880038.xls", directory,
                         jja_mail.attachments)              
    else:
        for query in os.listdir("."):
            if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if query.startswith("UUFA_EOT_ACAD_PLAN_RVW_FRAP"):
                    do_query(query, date + " Academic plan RVW FRAP " + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_EOT_CBA_ACAD_PRG_BELOW_FT"):
                    do_query(query, date + " CBA Acad Prog below FT.xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_EOT_CBA_UNDISBURSED"):
                    do_query(query, date + " CBA UNDISBURSED.xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_EOT_ALT_LOAN_SAP"):
                    do_query(query, date + " Alt Loans Awards with SAP Holds.xls", directory,
                             loans_kkt_mail.attachments)

                if query.startswith("UUFA_EOT_LN_ORIG_FAIL_PENDING"):
                    do_query(query, date + " Loans Originated Failed Pending.xls", directory,
                             loans_kt_mail.attachments)

                if query.startswith("UUFA_EOT_LN_ACD_PRG_BLW_HT_UND"):
                    do_query(query, date + " Loan Acad Prog below HT Undisbursed.xls", directory,
                             loans_kt_mail.attachments)

                if query.startswith("UUFA_EOT_LN_ACD_PRG_BLW_HT_SUB"):
                    do_query(query, date + " Loan Acad Prog below HT Subsq Disb.xls", directory,
                             loans_kt_mail.attachments)

                if query.startswith("UUFA_EOT_PRO_STDNT_SAP_WARNING"):
                    do_query(query, date + " SAP Warning Professional Students.xls", directory,
                             loans_kt_mail.attachments)

                if query.startswith("UUFA_EOT_MED_SAP"):
                    do_query(query, date + " Medical SAP Review.xls", directory,
                             prof_k_mail.attachments)

                if query.startswith("UUFA_EOT_FWS_WITH_NSI_HOLD"):
                    do_query(query, date + " FWS with NSI Holds.xls", directory,
                             ben_mail.attachments)

                if query.startswith("UUFA_EOT_PELL_ACD_PRG_LES_THN"):
                    do_query(query, date + " PELL Less Than FT.xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_EOT_PELL_OFFERED_NOT_DIS"):
                    do_query(query, date + " Pell Offered Not Disbursed.xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_EOT_THESIS_STUDENT_NONRES"):
                    do_query(query, date + " Thesis Students Non-Resident.xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_EOT_SCH_ACAD_PROG_REVIEW"):
                    do_query(query, date + " Scholarship Academic Progress Review " + year + ".xls", directory,
                             jja_mail.attachments)

                if query.startswith("UUFA_EOT_SCH_ACD_PRG_REVIEW"):
                    do_query(query, date + " All 70000792 Item types Academic Progress Review.xls", directory,
                             jja_mail.attachments)

                if query.startswith("UUFA_EOT_SAP_AGGCP_DENTAL"):
                    do_query(query, date + " SAP Aggregate Dental Career.xls", directory,
                             prof_rk_mail.attachments)

                if query.startswith("UUFA_EOT_SAP_AGGCP_LAW"):
                    do_query(query, date + " SAP Aggregate Law Career.xls", directory,
                             prof_rk_mail.attachments)

                if query.startswith("UUFA_EOT_SAP_AGGCP_MED"):
                    do_query(query, date + " SAP Aggregate Med Career.xls", directory,
                             prof_rk_mail.attachments)

                if query.startswith("UUFA_EOT_EU_FALL_GRADE"):
                    do_query(query, date + " EU Grade Fall.xls", directory,
                             kklt_mail.attachments)

                if query.startswith("UUFA_EOT_EU_SPRING_GRADE"):
                    do_query(query, date + " EU Grade Spring.xls", directory,
                             kklt_mail.attachments)

                if query.startswith("UUFA_EOT_EU_SUMMER_GRADE"):
                    do_query(query, date + " EU Grade Summer.xls", directory,
                             kklt_mail.attachments)

                if query.startswith("UUFA_EOT_PELL_ELG_ENRLL_NO_AWD"):
                    do_query(query, date + " Pell Eligible Enrolled NO Award.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_EOT_SAP_FSAP"):
                    do_query(query, date + " FSAP Students.xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_EOT_SCHOLAR_LEADER_CGPA"):
                    do_query(query, date + " Scholarship CGPA Leadership.xls", directory,
                             jja_mail.attachments)

                if "EOT_WUE_ACAD_PROG_REV" in query:
                    do_query(query, date + " WUE AcadProg Rvw 700007880038.xls", directory,
                             jja_mail.attachments)

