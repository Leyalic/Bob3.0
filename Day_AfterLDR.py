# Day After LDR Queries - to be modified
# to be called in main

def do_day_after_ldr():
    global aid_year
    for query_name in os.listdir("."):
        if query_name.startswith("UUFA_PRT_PELL_ELG_NO_PELL"):
            year = str(int(re.search(r'\d+', query_name).group()))
            break
    aid_year = "20" + str(int(year) - 1) + "-20" + year
    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/LDR', aid_year))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/LDR', aid_year))

    # the list 'my_path' should be populated with the FOLDER variables above.
    if not os.path.isdir(directory):
        os.makedirs(directory)

    # Change File_Name to be file as it is received and _new_file_name to what
    # the new file should be.  Prefix date
    # will be added.
    if ("22" in query_name.split("-")[0]):
        for query in os.listdir("."):
            if query.startswith("UUFA_LDR_MIN_ENROLLMENT_ATH"):
                do_query(query, date + " Minimum Enrollment Athlete.xls", directory,
                         ath_mail.attachments)

            if query.startswith("UUFA_LDR_MINIMUM_ENROLLMENT_FC"):
                do_query(query, date + " Minimum Enrollment FC (Federal & Campus Based Aid).xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_LDR_MINIMUM_ENROLLMENT_SV"):
                do_query(query, date + " Minimum Enrollment SV (Scholarships & Waivers).xls", directory,
                         hj_mail.attachments)

            if query.startswith("UUFA_LDR_PELL_AWARDS"):
                do_query(query, date + " Pell Awards.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_ATHLETE_AWARD_DISBURSED"):
                do_query(query, date + " Athlete Award Disbursed.xls", directory,
                         ath_mail.attachments)

            if query.startswith("UUFA_CBA_UNDISBURSED"):
                do_query(query, date + " CBA Undisbursed.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PELL_DL_MATH990"):
                do_query(query, date + " Pell-DL MATH 990.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PELL_DL_ELI575_ELI685"):
                do_query(query, date + " Pell-DL ELI575 ELI685.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PELL_ELIG_ENROLL_NO_AWARD"):
                do_query(query, date + " Pell Eligible Enrolled NO Award.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PELL_OFFERED_NOT_DISB"):
                do_query(query, date + " Pell Offered Not Disbursed.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_PELL_SUMMER_ENROLLMENT"):
                do_query(query, date + " Pell Summer Enrollment Check.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_THESIS_STUDENTS_NONRES"):
                do_query(query, date + " Thesis Students Non-Resident.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_REGISTERED_CENSUS_DATE"):
                do_query(query, date + " LDR FA Load Check.xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_SF_DISB_ATH_AWD_NOPOST"):
                do_query(query, date + " Athlete Awd Disb not Posted.xls", directory,
                         ath_mail.attachments)

            if query.startswith("UUFA_SF_DISB_WAIVER_AWD_NOPOST"):
                do_query(query, date + " Waiver Awd Disb Not Posted.xls", directory,
                         hj_mail.attachments)

            if query.startswith("UUFA_PRT_AWD_PLL_ELG_NO_PLL") and (year in query[:-8]) :
                do_query(query, date + " Pell Eligible No Pell 20" + year + ".xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_NO_MTRC_STU_ATH_BAL_OWING"):
                do_query(query, date + " Non-Matric Stu Athlete Balance Owing.xls", directory,
                         ath_mail.attachments)

            if query.startswith("UUFA_FATERM_SOURCE_N_AWD_ATH"):
                do_query(query, date + " NonTerm Source N Cancel Award Rvw - Athlete.xls", directory,
                         ath_mail.attachments)

            if query.startswith("UUFA_FATERM_SOURCE_N_AWD_SV"):
                do_query(query, date + " Term Source N Cancel Award Rvw - Scholarships.xls", directory,
                         ath_mail.attachments)

            if query.startswith("UUFA_PRT_PELL_ELG_NO_PELL"):
                do_query(query, date + " Pell Eligible No Pell " + year + ".xls", directory,
                         ath_mail.attachments)

            if query.startswith("UUFA_ATH_NO_MTRC_STU_BAL_OWING"):
                do_query(query, date + " Non-Matric Stu Athlete Balance Owing " + year + ".xls", directory,
                         ath_mail.attachments)
    else:
        for query in os.listdir("."):
            if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if query.startswith("UUFA_LDR_MIN_ENROLLMENT_ATH"):
                    do_query(query, date + " Minimum Enrollment Athlete.xls", directory,
                             ath_mail.attachments)

                if query.startswith("UUFA_LDR_MINIMUM_ENROLLMENT_FC"):
                    do_query(query, date + " Minimum Enrollment FC (Federal & Campus Based Aid).xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_LDR_MINIMUM_ENROLLMENT_SV"):
                    do_query(query, date + " Minimum Enrollment SV (Scholarships & Waivers).xls", directory,
                             hj_mail.attachments)

                if query.startswith("UUFA_LDR_PELL_AWARDS"):
                    do_query(query, date + " Pell Awards.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_ATHLETE_AWARD_DISBURSED"):
                    do_query(query, date + " Athlete Award Disbursed.xls", directory,
                             ath_mail.attachments)

                if query.startswith("UUFA_CBA_UNDISBURSED"):
                    do_query(query, date + " CBA Undisbursed.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PELL_DL_MATH990"):
                    do_query(query, date + " Pell-DL MATH 990.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PELL_DL_ELI575_ELI685"):
                    do_query(query, date + " Pell-DL ELI575 ELI685.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PELL_ELIG_ENROLL_NO_AWARD"):
                    do_query(query, date + " Pell Eligible Enrolled NO Award.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PELL_OFFERED_NOT_DISB"):
                    do_query(query, date + " Pell Offered Not Disbursed.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_PELL_SUMMER_ENROLLMENT"):
                    do_query(query, date + " Pell Summer Enrollment Check.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_THESIS_STUDENTS_NONRES"):
                    do_query(query, date + " Thesis Students Non-Resident.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_REGISTERED_CENSUS_DATE"):
                    do_query(query, date + " LDR FA Load Check.xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_SF_DISB_ATH_AWD_NOPOST"):
                    do_query(query, date + " Athlete Awd Disb not Posted.xls", directory,
                             ath_mail.attachments)

                if query.startswith("UUFA_SF_DISB_WAIVER_AWD_NOPOST"):
                    do_query(query, date + " Waiver Awd Disb Not Posted.xls", directory,
                             hj_mail.attachments)

                if query.startswith("UUFA_PRT_AWD_PLL_ELG_NO_PLL") and (year in query[:-8]) :
                    do_query(query, date + " Pell Eligible No Pell 20" + year + ".xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_NO_MTRC_STU_ATH_BAL_OWING"):
                    do_query(query, date + " Non-Matric Stu Athlete Balance Owing.xls", directory,
                             ath_mail.attachments)

                if query.startswith("UUFA_FATERM_SOURCE_N_AWD_ATH"):
                    do_query(query, date + " NonTerm Source N Cancel Award Rvw - Athlete.xls", directory,
                             ath_mail.attachments)

                if query.startswith("UUFA_FATERM_SOURCE_N_AWD_SV"):
                    do_query(query, date + " Term Source N Cancel Award Rvw - Scholarships.xls", directory,
                             ath_mail.attachments)

                if query.startswith("UUFA_PRT_PELL_ELG_NO_PELL"):
                    do_query(query, date + " Pell Eligible No Pell " + year + ".xls", directory,
                             ath_mail.attachments)

                if query.startswith("UUFA_ATH_NO_MTRC_STU_BAL_OWING"):
                    do_query(query, date + " Non-Matric Stu Athlete Balance Owing " + year + ".xls", directory,
                             ath_mail.attachments)

