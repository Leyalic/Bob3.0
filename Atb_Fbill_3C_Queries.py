# ATB, FBILL, 3C Queries - to be modified
# to be called in main

def do_atb_fb_3c_queries():
    global aid_year
    year = "23"
    aid_year = "20" + str(int(year) - 1) + "-20" + year

    if test:
        directory = os.path.realpath(os.path.join('C:/Testing Bob/QUERIES/3C Queries'))
        atb_directory = os.path.realpath(os.path.join('C:/Testing Bob/QUERIES\ATB'))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/3C Queries'))
        atb_directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/ATB'))

    # the list 'my_path' should be populated with the FOLDER variables above.
    if not os.path.isdir(directory):
        os.makedirs(directory)
    if not os.path.isdir(atb_directory):
        os.makedirs(atb_directory)

    # Change File_Name to be file as it is received and _new_file_name to what
    # the new file should be.  Prefix date
    # will be added.
    for query in os.listdir("."):
        if ("UUFA_ADD_FDLP" in query):
            do_query(query, date + " ADD FDLP" + year + ".xls", directory,
                     null_mail.attachments)
        if ("UUFA_ADD_FGLO" in query):
            do_query(query, date + " ADD FGLO" + year + ".xls", directory,
                     null_mail.attachments)
        if ("UUFA_ADD_FHST" in query):
            do_query(query, date + " ADD FHST" + year + ".xls", directory,
                     null_mail.attachments)
        if ("UUFA_ADD_FMPN" in query):
            do_query(query, date + " ADD FMPN" + year + ".xls", directory,
                     null_mail.attachments)
        if ("UUFA_ADD_FNON" in query):
            do_query(query, date + " ADD FNON" + year + ".xls", directory,
                     null_mail.attachments)
        if ("UUFA_ADD_FTYN" in query):
            do_query(query, date + " ADD FTYN" + year + ".xls", directory,
                     null_mail.attachments)
        if ("UUFA_ADD_FULO" in query):
            do_query(query, date + " ADD FULO" + year + ".xls", directory,
                     null_mail.attachments)
        if ("UUFA_ADD_FLPR" in query):
            do_query(query, date + " ADD FLPR" + year + ".xls", directory,
                     null_mail.attachments)
        if ("UUFA_COMPLETE_FDLP" in query):
            do_query(query, date + " COMPLETE FDLP" + year + ".xls", directory,
                     null_mail.attachments)
        if ("UUFA_COMPLETE_FGLO" in query):
            do_query(query, date + " COMPLETE FGLO" + year + ".xls", directory,
                     null_mail.attachments)
        if ("UUFA_COMPLETE_FHST" in query):
            do_query(query, date + " COMPLETE FHST" + year + ".xls", directory,
                     null_mail.attachments)
        if ("UUFA_COMPLETE_FMPN" in query):
            do_query(query, date + " COMPLETE FMPN" + year + ".xls", directory,
                     null_mail.attachments)
        if ("UUFA_COMPLETE_FNON" in query) :
            do_query(query, date + " COMPLETE FNON" + year + ".xls", directory,
                     null_mail.attachments)
        if ("UUFA_COMPLETE_FULO" in query):
            do_query(query, date + " COMPLETE FULO" + year + ".xls", directory,
                     null_mail.attachments)
        if ("UUFA_HS_06_AFTER_ATB" in query):
            do_query(query, date + " ATB High School Code 06.xls", atb_directory,
                     null_mail.attachments)
        if ("UUFA_HS_04_AFTER_ATB" in query):
            do_query(query, date + " ATB Home School Code 04.xls", atb_directory,
                     null_mail.attachments)
        if ("UUFA_GED_07_AFTER_ATB" in query):
            do_query(query, date + " ATB New ISIRs GED 07.xls", atb_directory,
                     null_mail.attachments)
        if ("UUFA_ATB_ISIR_NOT_MATCH" in query):
            do_query(query, date + " ISIR Not Match SEC.xls", atb_directory,
                     kkmt_mail.attachments)
        if ("UUFA_ATB_SEQUENCE_DIFFERENCE" in query):
            do_query(query, date + " SEC Sequence Difference.xls", atb_directory,
                         kkmt_mail.attachments)
