# Mid-Repackaging Queries
import os

def do_mid_repack_queries(test, year, query, renamed):

    aid_year = str(int(year) - 1) + "-" + str(year)

    if test:
        directory = os.path.realpath(os.path.join('C:/QueryRunnerProj/Testing/Test/Pell Repackaging', aid_year))
    else:
        directory = os.path.realpath(os.path.join('O:/Systems/QUERIES/Pell Repackaging', aid_year))

    if not os.path.isdir(directory):
        os.makedirs(directory)


    move_directory = "Pell Reports"

    # FORMAT: return (query, renamed, archive_directory, UOSFA_folder)
    # query: The original file name
    # renamed: The name the file should have after being moved
    # archive_directory: The folder the file will be copied to
    # UOSFA_folder: The name of the folder the renamed file should be moved to
    # - (eg. "Budget Reports", "SAP Reports", "Unknown Reports") 
    # - put "None" if it shouldn't be moved to a folder in 'O:/UOSFA Reports/'

    if query.startswith("UUFA_MP_RPKG_AID_PROC_STATUS_4"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_MP_RPKG_AWD_STRM_INACTIVE"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_MP_RPKG_FCIT"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_MP_RPKG_FDR"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_MP_RPKG_FOVP_FARC_I"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_MP_RPKG_ISIR_CMT_346_347"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_MP_RPKG_LEAVE"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_MP_RPKG_TOTAL_WDRN_DRP"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_MP_RPKG_TOTAL_WTHDRN_DRP"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_MP_RPKG_VAR_1_2"):
        return (query, renamed, directory, move_directory)

    if query.startswith("UUFA_MP_RPKG_VER_UNFLAG"):
        return (query, renamed, directory, move_directory)

    return "Empty" #Leave as last line
