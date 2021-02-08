from file_names import file_names


# USER DEFINED FUNCTIONS
def local_files(path='.', no_extension=True):
    """ Returns a list of files in a directory"""
    """
    Arguments:
    path: str, default = '.' 
    path to the directory to list file names of

    no_extension: boolean, default = True
    if true the extension is stripped out. 
    Note: This only works with that have 3 characters for extension
    """
    import os
    dir_file_names = []
    with os.scandir(path=path) as entries:
        for entry in entries:
            dir_file_names.append(entry.name)

    # stripping the extension
    if no_extension == True:
        dir_file_names = [name[:-4] for name in dir_file_names]
    return dir_file_names


# ---------------------------------------------------------------------#
target_dir = 'csv_clean'

source_files = file_names  # list of file_names that update with current date/year
target_files = local_files(path=target_dir)

# Subtracting target_files from source_files
download_list = [file for file in source_files if file not in target_files]