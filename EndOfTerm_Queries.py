# End of Term Queries - to be modified
# to be called in main
import os

def do_end_of_term_queries(test, date, year, query, renamed, aid_year_match):
    #global aid_year
    #term = 'F'
    #strm = "Error"
    #for query_name in os.listdir("."):
    #    if query_name.startswith("UUFA_EOT_ACAD_PLAN_RVW"):
    #        prompt = "Enter Term: (e.g. 2016U, 2017F, or 2032S):"
    #        while True:
    #            strm = str.upper(raw_input(prompt))
    #            aid_year = strm[2:4]
    #            term = strm[4]
    #            if term == 'S' or term == 'U' or term == 'F':
    #                break

    aid_year = str(int(year) - 1) + "-" + str(year)
    year = aid_year[-2:]
    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/SAP/', "20" + year))
    else:
        directory = os.path.realpath(os.path.join('O:\Systems\QUERIES/SAP/', "20" + year))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    move_directory = "SAP Reports"

    toggle = True

    if aid_year_match:
    #if ("22" in query_name.split("-")[0]):
        if True:
        #for query in os.listdir("."):
            if query.startswith("UUFA_EOT_ACAD_PLAN_RVW_FRAP"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_CBA_ACAD_PRG_BELOW_FT"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_CBA_UNDISBURSED"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_ALT_LOAN_SAP"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_LN_ORIG_FAIL_PENDING"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_LN_ACD_PRG_BLW_HT_UND"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_LN_ACD_PRG_BLW_HT_SUB"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_PRO_STDNT_SAP_WARNING"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_MED_SAP"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_FWS_WITH_NSI_HOLD"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_PELL_ACD_PRG_LES_THN"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_PELL_OFFERED_NOT_DIS"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_THESIS_STUDENT_NONRES"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_SCH_ACAD_PROG_REVIEW"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_SCH_ACD_PRG_REVIEW"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_SAP_AGGCP_DENTAL"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_SAP_AGGCP_LAW"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_SAP_AGGCP_MED"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_EU_FALL_GRADE"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_EU_SPRING_GRADE"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_EU_SUMMER_GRADE"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_PELL_ELG_ENRLL_NO_AWD"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_SAP_FSAP"):
                return (query, renamed, directory, move_directory)

            if query.startswith("UUFA_EOT_SCHOLAR_LEADER_CGPA"):
                return (query, renamed, directory, move_directory)

            if "EOT_WUE_ACAD_PROG_REV" in query:
                return (query, renamed, directory, move_directory)             
    else:
        if True:
        #for query in os.listdir("."):
            if toggle:
            #if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if query.startswith("UUFA_EOT_ACAD_PLAN_RVW_FRAP"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_CBA_ACAD_PRG_BELOW_FT"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_CBA_UNDISBURSED"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_ALT_LOAN_SAP"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_LN_ORIG_FAIL_PENDING"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_LN_ACD_PRG_BLW_HT_UND"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_LN_ACD_PRG_BLW_HT_SUB"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_PRO_STDNT_SAP_WARNING"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_MED_SAP"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_FWS_WITH_NSI_HOLD"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_PELL_ACD_PRG_LES_THN"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_PELL_OFFERED_NOT_DIS"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_THESIS_STUDENT_NONRES"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_SCH_ACAD_PROG_REVIEW"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_SCH_ACD_PRG_REVIEW"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_SAP_AGGCP_DENTAL"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_SAP_AGGCP_LAW"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_SAP_AGGCP_MED"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_EU_FALL_GRADE"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_EU_SPRING_GRADE"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_EU_SUMMER_GRADE"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_PELL_ELG_ENRLL_NO_AWD"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_SAP_FSAP"):
                    return (query, renamed, directory, move_directory)

                if query.startswith("UUFA_EOT_SCHOLAR_LEADER_CGPA"):
                    return (query, renamed, directory, move_directory)

                if "EOT_WUE_ACAD_PROG_REV" in query:
                    return (query, renamed, directory, move_directory)
    return "Empty"
