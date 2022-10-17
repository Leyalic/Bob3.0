# Budget Queries - to be modified 
# to be called in main

def do_budget_queries():
    global aid_year
    year = "23"
    for query_name in os.listdir("."):
        if "BR_BDGT" in query_name:
            if str(int(re.search(r'\d+', query_name).group())) == "22":
                year = "22"
            break
    aid_year = "20" + str(int(year) - 1) + "-20" + year
    # Create FOLDER variables to be used in Move() operation and establishes
    # the directory to save the files
    # using the date.
    # Create variables to be used in Move() operation.
    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/Budgets', aid_year, month_folder))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Budgets', aid_year, month_folder))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    # Change File_Name to be query AC it is received and _new_file_name to what
    # the new query should be.  Prefix date
    # will be added.
    
    if ("22" in query_name.split("-")[0]):
        for query in os.listdir("."):
            if query.startswith("UUFA_BR_ACAD_LVLS_OUT_SYNC") and (year in query[:-8]) :
                do_query(query, date + " GR Academic Levels Out of Sync " + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_BR_ATH_TUIT_INCR_NR") and (year in query[:-8]) :
                do_query(query, date + " Athlete Tuition Increase NR " + year + ".xls", directory,
                         ath_mail.attachments)

            if query.startswith("UUFA_BR_ATH_TUITION_INCRS") and (year in query[:-8]) :
                do_query(query, date + " Athlete Tuition Increase " + year + ".xls", directory,
                         ath_mail.attachments)

            if "_BR_BDGT_DOUBLE_BUDGETS" in query :
                do_query(query, date + " Double Budget " + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_BR_COA_LESS_HT") and (year in query[:-8]) :
                do_query(query, date + " PELL COA Less Than Half Time Enrollment " + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_BR_COA_TUIT_ZERO") and (year in query[:-8]) :
                do_query(query, date + " COA Tuition Amount Zero " + year + ".xls", directory,
                         kktv_mail.attachments)

            if query.startswith("UUFA_BR_DN_LW_MD_AID_ATRB") and (year in query[:-8]) :
                do_query(query, date + " DN-LW-MD Student Aid Career " + year + ".xls", directory,
                         prof_mail.attachments)

            if query.startswith("UUFA_BR_FT_CLASS_OVERRIDES") and (year in query[:-8]) :
                do_query(query, date + " Class Overrides " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if query.startswith("UUFA_BR_COA_ISIR_BDGT_DIFF") and (year in query[:-8]) :
                do_query(query, date + " COA ISIR Budget Mismatch " + year + ".xls", directory,
                         ath_kkmt_mail.attachments)

            if query.startswith("UUFA_BR_NO_BUDGET_ATTEND") and (year in query[:-8]) :
                do_query(query, date + " NO Budget Attend 20" + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_BR_PELL_COA_BLANK") and (year in query[:-8]) :
                do_query(query, date + " PELL COA Blank " + year + ".xls", directory,
                         acnt_kkt_mail.attachments)

            if (("BR_PELL_COA_CHECK" in query) and (year in query[:-8])) :
                do_query(query, date + " PELL COA Fix - COD Review " + year + ".xls", directory,
                         acnt_kkt_mail.attachments)


            if query.startswith("UUFA_BR_PELL_COA_DOUBLE") and (year in query[:-8]) :
                do_query(query, date + " PELL COA Double " + year + ".xls", directory,
                         kkt_mail.attachments)

            if "BR_PELL_COA_DBLD_WRNG" in query and (year in query[:-8]) :
                do_query(query, date + " PELL COA Double " + year + ".xls", directory,
                         null_mail.attachments)

            if query.startswith("FA_BR_PELL_COA_LESS_HT_20") and (year in query[:-8]) :
                do_query(query, date + " PELL COA Less HT Enrollment " + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_BR_PROC_STAT_RVW_STAT") and (year in query[:-8]) :
                do_query(query, date + " Reset Processing Status to 1 " + year + ".xls", directory,
                         ml_mail.attachments)

            if query.startswith("UUFA_BR_RES_NON_RES_BDGT") and (year in query[:-8]) :
                do_query(query, date + " Resident - Non-Resident Budget " + year + ".xls", directory,
                         kkt_mail.attachments)

            if query.startswith("UUFA_BR_SCH_TUITION_FEES_NR") and (year in query[:-8]) :
                do_query(query, date + " Waiver-Scholar Tuition Fees NR " + year + ".xls", directory,
                         hj_mail.attachments)

            if query.startswith("UUFA_BR_SCH_TUITION_ONLY_NR") and (year in query[:-8]) :
                do_query(query, date + " Waiver-Scholar Tuition Only NR " + year + ".xls", directory,
                         hj_mail.attachments)

            if query.startswith("UUFA_BR_SCHOLAR_TUIT_FEES") and (year in query[:-8]) :
                do_query(query, date + " Waiver-Scholar Tuition Fees Res " + year + ".xls", directory,
                         hj_mail.attachments)

            if query.startswith("UUFA_BR_SCHOLAR_TUIT_ONLY") and (year in query[:-8]) :
                do_query(query, date + " Waiver-Scholar Tuition Only Res " + year + ".xls", directory,
                         hj_mail.attachments)

            if query.startswith("FA_BR_UFORM_CHANGE_BUD_DUR") and (year in query[:-8]) :
                do_query(query, date + " Correct Budget Duration " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "BR_ACAD_LVLS_NOT_SYNC" in query and (year in query[:-8]) :
                do_query(query, date + " TRIAL Acad Levels out of SYNC " + year + ".xls", directory,
                         kkmt_mail.attachments)

            if "BR_ACAD_LVLS_NOT_SYNC" in query and (year in query[:-8]) :
                do_query(query, date + " TRIAL Acad Levels out of SYNC " + year + ".xls", directory,
                         kkmt_mail.attachments)
                
    else:
        for query in os.listdir("."):
            if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if query.startswith("UUFA_BR_ACAD_LVLS_OUT_SYNC")  :
                    do_query(query, date + " GR Academic Levels Out of Sync " + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_BR_ATH_TUIT_INCR_NR")  :
                    do_query(query, date + " Athlete Tuition Increase NR " + year + ".xls", directory,
                             ath_mail.attachments)

                if query.startswith("UUFA_BR_ATH_TUITION_INCRS")  :
                    do_query(query, date + " Athlete Tuition Increase " + year + ".xls", directory,
                             ath_mail.attachments)

                if "_BR_BDGT_DOUBLE_BUDGETS" in query :
                    do_query(query, date + " Double Budget " + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_BR_COA_LESS_HT")  :
                    do_query(query, date + " PELL COA Less Than Half Time Enrollment " + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_BR_COA_TUIT_ZERO")  :
                    do_query(query, date + " COA Tuition Amount Zero " + year + ".xls", directory,
                             kktv_mail.attachments)

                if query.startswith("UUFA_BR_DN_LW_MD_AID_ATRB")  :
                    do_query(query, date + " DN-LW-MD Student Aid Career " + year + ".xls", directory,
                             prof_mail.attachments)

                if query.startswith("UUFA_BR_FT_CLASS_OVERRIDES")  :
                    do_query(query, date + " Class Overrides " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if query.startswith("UUFA_BR_COA_ISIR_BDGT_DIFF")  :
                    do_query(query, date + " COA ISIR Budget Mismatch " + year + ".xls", directory,
                             ath_kkmt_mail.attachments)

                if query.startswith("UUFA_BR_NO_BUDGET_ATTEND")  :
                    do_query(query, date + " NO Budget Attend 20" + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_BR_PELL_COA_BLANK")  :
                    do_query(query, date + " PELL COA Blank " + year + ".xls", directory,
                             acnt_kkt_mail.attachments)

                if (("BR_PELL_COA_CHECK" in query) ) :
                    do_query(query, date + " PELL COA Fix - COD Review " + year + ".xls", directory,
                             acnt_kkt_mail.attachments)

                if query.startswith("UUFA_BR_PELL_COA_DOUBLE")  :
                    do_query(query, date + " PELL COA Double " + year + ".xls", directory,
                             kkt_mail.attachments)

                if "BR_PELL_COA_DBLD_WRNG" in query  :
                    do_query(query, date + " PELL COA Double " + year + ".xls", directory,
                             null_mail.attachments)

                if query.startswith("FA_BR_PELL_COA_LESS_HT_20")  :
                    do_query(query, date + " PELL COA Less HT Enrollment " + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_BR_PROC_STAT_RVW_STAT")  :
                    do_query(query, date + " Reset Processing Status to 1 " + year + ".xls", directory,
                             ml_mail.attachments)

                if query.startswith("UUFA_BR_RES_NON_RES_BDGT")  :
                    do_query(query, date + " Resident - Non-Resident Budget " + year + ".xls", directory,
                             kkt_mail.attachments)

                if query.startswith("UUFA_BR_SCH_TUITION_FEES_NR")  :
                    do_query(query, date + " Waiver-Scholar Tuition Fees NR " + year + ".xls", directory,
                             hj_mail.attachments)

                if query.startswith("UUFA_BR_SCH_TUITION_ONLY_NR")  :
                    do_query(query, date + " Waiver-Scholar Tuition Only NR " + year + ".xls", directory,
                             hj_mail.attachments)

                if query.startswith("UUFA_BR_SCHOLAR_TUIT_FEES")  :
                    do_query(query, date + " Waiver-Scholar Tuition Fees Res " + year + ".xls", directory,
                             hj_mail.attachments)

                if query.startswith("UUFA_BR_SCHOLAR_TUIT_ONLY")  :
                    do_query(query, date + " Waiver-Scholar Tuition Only Res " + year + ".xls", directory,
                             hj_mail.attachments)

                if query.startswith("FA_BR_UFORM_CHANGE_BUD_DUR")  :
                    do_query(query, date + " Correct Budget Duration " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "BR_ACAD_LVLS_NOT_SYNC" in query  :
                    do_query(query, date + " TRIAL Acad Levels out of SYNC " + year + ".xls", directory,
                             kkmt_mail.attachments)

                if "BR_ACAD_LVLS_NOT_SYNC" in query  :
                    do_query(query, date + " TRIAL Acad Levels out of SYNC " + year + ".xls", directory,
                             kkmt_mail.attachments)

    for mail_group in mail_groups:
        if(mail_group.attachments):
            mailer("", aid_year + " Budget Queries", mail_group.recipients,"", mail_group.attachments)
            del mail_group.attachments[:]
    
#Budget Testing Queries
def do_budget_test_queries():
    global aid_year
    for query_name in os.listdir("."):
        if query_name.startswith("UUFA_BUDGET"):
            year = str(int(re.search(r'\d+', query_name).group()))
            break
    aid_year = "20" + str(int(year) - 1) + "-20" + year

    # Create FOLDER variables to be used in Move() operation and establishes
    # the directory to save the files
    # using the date.
    # Create variables to be used in Move() operation.
    if test:
        directory = os.path.realpath(os.path.join('C:\Testing Bob/Budgets', aid_year, month_folder,"Wrong Budget Queries"))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Budgets', aid_year, month_folder, "Wrong Budget Queries"))

    if not os.path.isdir(directory):
        os.makedirs(directory)

    # Change File_Name to be query AC it is received and _new_file_name to what
    # the new query should be.  Prefix date
    # will be added.
    if ("22" in query_name.split("-")[0]):
        for query in os.listdir("."):
            if query.startswith("UUFA_BUDGET_20" + year + "_DN1"):
                do_query(query, date + " Wrong Budget - Dental 1.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_DN2"):
                do_query(query, date + " Wrong Budget - Dental 2.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_DN3"):
                do_query(query, date + " Wrong Budget - Dental 3.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_DN4"):
                do_query(query, date + " Wrong Budget - Dental 4.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_ACCTMAC"):
                do_query(query, date + " Wrong Budget - Accounting Masters.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_ARCHMAR"):
                do_query(query, date + " Wrong Budget - Architect Masters.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_BUSINESS"):
                do_query(query, date + " Wrong Budget - Grad Business.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_COMDIS"):
                do_query(query, date + " Wrong Budget - COMDIS.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_EAEMS"):
                do_query(query, date + " Wrong Budget - EAE.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_EDUCATION"):
                do_query(query, date + " Wrong Budget - Education.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_ED_PSYCH"):
                do_query(query, date + " Wrong Budget - ED Psychology.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_ENGINERING"):
                do_query(query, date + " Wrong Budget - Grad Engineering.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_FINE_ARTS"):
                do_query(query, date + " Wrong Budget - Fine Arts .xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_GENERAL_GR"):
                do_query(query, date + " Wrong Budget - General Grad .xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_GENETICS"):
                do_query(query, date + " Wrong Budget - Genetics.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_HEALTH"):
                do_query(query, date + " Wrong Budget - Health.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_PRO_HEALTH"):
                do_query(query, date + " Wrong Budget - Health Promotion .xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_HUMANITIES"):
                do_query(query, date + " Wrong Budget - Humanities.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_MBA_BUADMB"):
                do_query(query, date + " Wrong Budget - MBA - BUADMBA .xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_MD_SCIENCE"):
                do_query(query, date + " Wrong Budget - Medical Science .xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_MEDICAL"):
                do_query(query, date + " Wrong Budget - MD Graduate .xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_NURSING"):
                do_query(query, date + " Wrong Budget - Graduate Nursing .xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_PA"):
                do_query(query, date + " Wrong Budget - Physician Assistant .xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_PHARMACY"):
                do_query(query, date + " Wrong Budget - Pharmacy .xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_PLANNING"):
                do_query(query, date + " Wrong Budget - Planning.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_PMBAMBA"):
                do_query(query, date + " Wrong Budget - PMBAMBA.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_PUBLICPOLI"):
                do_query(query, date + " Wrong Budget - Public Policy.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_PUBLIC_ADM"):
                do_query(query, date + " Wrong Budget - Public Administration.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_SCIENCE"):
                do_query(query, date + " Wrong Budget - Science.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_SOC_BEHAV"):
                do_query(query, date + " Wrong Budget - Social and Behavioral.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_SW"):
                do_query(query, date + " Wrong Budget - Social Work.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_GR_XMBAMBA"):
                do_query(query, date + " Wrong Budget - XMBAMBA.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_LW1"):
                do_query(query, date + " Wrong Budget - Law 1.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_LW2"):
                do_query(query, date + " Wrong Budget - Law 2.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_LW3"):
                do_query(query, date + " Wrong Budget - Law 3.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_MD1"):
                do_query(query, date + " Wrong Budget - Med 1.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_MD2"):
                do_query(query, date + " Wrong Budget - Med 2.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_MD3"):
                do_query(query, date + " Wrong Budget - Med 3.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_MD4"):
                do_query(query, date + " Wrong Budget - Med 4.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_UNDERGRAD"):
                do_query(query, date + " Wrong Budget - Undergraduate.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_UG_BUSINESS"):
                do_query(query, date + " Wrong Budget - Undergraduate Business.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_UG_BUS_LTHT"):
                do_query(query, date + " Wrong Budget - Undergraduate Business LTHT.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_UG_ENGINERING"):
                do_query(query, date + " Wrong Budget - Undergraduate Engineering.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_UG_ENG_LTHT"):
                do_query(query, date + " Wrong Budget - Undergraduate Engineering LTHT.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_UG_LTHT"):
                do_query(query, date + " Wrong Budget - Undergraduate LTHT.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_UG_NURSE_LTHT"):
                do_query(query, date + " Wrong Budget - Undergraduate Nursing LTHT.xls", directory,
                         null_mail.attachments)

            if query.startswith("UUFA_BUDGET_20" + year + "_UG_NURSING"):
                do_query(query, date + " Wrong Budget - Undergraduate Nursing.xls", directory,
                         null_mail.attachments)
                
    else:
        for query in os.listdir("."):
            if(year not in query_name.split("-")[0]) and (str(int(year)-1) not in query_name.split("-")[0]):
                if query.startswith("UUFA_BUDGET_20" + year + "_DN1"):
                    do_query(query, date + " Wrong Budget - Dental 1.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_DN2"):
                    do_query(query, date + " Wrong Budget - Dental 2.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_DN3"):
                    do_query(query, date + " Wrong Budget - Dental 3.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_DN4"):
                    do_query(query, date + " Wrong Budget - Dental 4.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_ACCTMAC"):
                    do_query(query, date + " Wrong Budget - Accounting Masters.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_ARCHMAR"):
                    do_query(query, date + " Wrong Budget - Architect Masters.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_BUSINESS"):
                    do_query(query, date + " Wrong Budget - Grad Business.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_COMDIS"):
                    do_query(query, date + " Wrong Budget - COMDIS.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_EAEMS"):
                    do_query(query, date + " Wrong Budget - EAE.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_EDUCATION"):
                    do_query(query, date + " Wrong Budget - Education.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_ED_PSYCH"):
                    do_query(query, date + " Wrong Budget - ED Psychology.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_ENGINERING"):
                    do_query(query, date + " Wrong Budget - Grad Engineering.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_FINE_ARTS"):
                    do_query(query, date + " Wrong Budget - Fine Arts .xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_GENERAL_GR"):
                    do_query(query, date + " Wrong Budget - General Grad .xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_GENETICS"):
                    do_query(query, date + " Wrong Budget - Genetics.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_HEALTH"):
                    do_query(query, date + " Wrong Budget - Health.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_PRO_HEALTH"):
                    do_query(query, date + " Wrong Budget - Health Promotion .xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_HUMANITIES"):
                    do_query(query, date + " Wrong Budget - Humanities.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_MBA_BUADMB"):
                    do_query(query, date + " Wrong Budget - MBA - BUADMBA .xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_MD_SCIENCE"):
                    do_query(query, date + " Wrong Budget - Medical Science .xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_MEDICAL"):
                    do_query(query, date + " Wrong Budget - MD Graduate .xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_NURSING"):
                    do_query(query, date + " Wrong Budget - Graduate Nursing .xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_PA"):
                    do_query(query, date + " Wrong Budget - Physician Assistant .xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_PHARMACY"):
                    do_query(query, date + " Wrong Budget - Pharmacy .xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_PLANNING"):
                    do_query(query, date + " Wrong Budget - Planning.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_PMBAMBA"):
                    do_query(query, date + " Wrong Budget - PMBAMBA.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_PUBLICPOLI"):
                    do_query(query, date + " Wrong Budget - Public Policy.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_PUBLIC_ADM"):
                    do_query(query, date + " Wrong Budget - Public Administration.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_SCIENCE"):
                    do_query(query, date + " Wrong Budget - Science.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_SOC_BEHAV"):
                    do_query(query, date + " Wrong Budget - Social and Behavioral.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_SW"):
                    do_query(query, date + " Wrong Budget - Social Work.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_GR_XMBAMBA"):
                    do_query(query, date + " Wrong Budget - XMBAMBA.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_LW1"):
                    do_query(query, date + " Wrong Budget - Law 1.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_LW2"):
                    do_query(query, date + " Wrong Budget - Law 2.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_LW3"):
                    do_query(query, date + " Wrong Budget - Law 3.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_MD1"):
                    do_query(query, date + " Wrong Budget - Med 1.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_MD2"):
                    do_query(query, date + " Wrong Budget - Med 2.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_MD3"):
                    do_query(query, date + " Wrong Budget - Med 3.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_MD4"):
                    do_query(query, date + " Wrong Budget - Med 4.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_UNDERGRAD"):
                    do_query(query, date + " Wrong Budget - Undergraduate.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_UG_BUSINESS"):
                    do_query(query, date + " Wrong Budget - Undergraduate Business.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_UG_BUS_LTHT"):
                    do_query(query, date + " Wrong Budget - Undergraduate Business LTHT.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_UG_ENGINERING"):
                    do_query(query, date + " Wrong Budget - Undergraduate Engineering.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_UG_ENG_LTHT"):
                    do_query(query, date + " Wrong Budget - Undergraduate Engineering LTHT.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_UG_LTHT"):
                    do_query(query, date + " Wrong Budget - Undergraduate LTHT.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_UG_NURSE_LTHT"):
                    do_query(query, date + " Wrong Budget - Undergraduate Nursing LTHT.xls", directory,
                             null_mail.attachments)

                if query.startswith("UUFA_BUDGET_20" + year + "_UG_NURSING"):
                    do_query(query, date + " Wrong Budget - Undergraduate Nursing.xls", directory,
                             null_mail.attachments)
