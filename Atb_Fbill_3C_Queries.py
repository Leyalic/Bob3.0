# ATB, FBILL, 3C Queries - to be modified
# to be called in main
import os

def do_atb_fb_3c_queries(test, date, year, query, renamed):
    #global aid_year
    #year = "23"
    #aid_year = "20" + str(int(year) - 1) + "-20" + year

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

    year = year[2:]

    move_directory = "Daily Reports"
    other_directory = "Daily Reports"

    # Change File_Name to be file as it is received and _new_file_name to what
    # the new file should be.  Prefix date
    # will be added.
    if True:
    #for query in os.listdir("."):
        if ("UUFA_ADD_FDLP" in query):
            return (query, renamed, directory, move_directory)
        if ("UUFA_ADD_FGLO" in query):
            return (query, renamed, directory, move_directory)
        if ("UUFA_ADD_FHST" in query):
            return (query, renamed, directory, move_directory)
        if ("UUFA_ADD_FMPN" in query):
            return (query, renamed, directory, move_directory)
        if ("UUFA_ADD_FNON" in query):
            return (query, renamed, directory, move_directory)
        if ("UUFA_ADD_FTYN" in query):
            return (query, renamed, directory, move_directory)
        if ("UUFA_ADD_FULO" in query):
            return (query, renamed, directory, move_directory)
        if ("UUFA_ADD_FLPR" in query):
            return (query, renamed, directory, move_directory)
        if ("UUFA_COMPLETE_FDLP" in query):
            return (query, renamed, directory, move_directory)
        if ("UUFA_COMPLETE_FGLO" in query):
            return (query, renamed, directory, move_directory)
        if ("UUFA_COMPLETE_FHST" in query):
            return (query, renamed, directory, move_directory)
        if ("UUFA_COMPLETE_FMPN" in query):
            return (query, renamed, directory, move_directory)
        if ("UUFA_COMPLETE_FNON" in query) :
            return (query, renamed, directory, move_directory)
        if ("UUFA_COMPLETE_FULO" in query):
            return (query, renamed, directory, move_directory)
        if ("UUFA_HS_06_AFTER_ATB" in query):
            return (query, renamed, atb_directory, other_directory)
        if ("UUFA_HS_04_AFTER_ATB" in query):
            return (query, renamed, atb_directory, other_directory)
        if ("UUFA_GED_07_AFTER_ATB" in query):
            return (query, renamed, atb_directory, other_directory)
        if ("UUFA_ATB_ISIR_NOT_MATCH" in query):
            return (query, renamed, atb_directory, other_directory)
        if ("UUFA_ATB_SEQUENCE_DIFFERENCE" in query):
            return (query, renamed, atb_directory, other_directory)
    return "Empty"