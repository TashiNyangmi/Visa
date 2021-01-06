import os

from file_names import file_names  # list of file_names that update with current date/year
# importing UDFs
from pdf_downloader import pdf_downloader
from pdf_to_csv import pdf_to_csv
from csv_clean import csv_clean


# --------------------------------------------------------------------------------#

# USER DEFINED FUNCTIONS
def local_files(path='.', no_extension=True):
    """list of files in local machine"""
    dir_file_names = []
    with os.scandir(path=path) as entries:
        for entry in entries:
            dir_file_names.append(entry.name)
    if no_extension == True:
        dir_file_names = [name[:-4] for name in dir_file_names]  # stripping the extension
    return dir_file_names


def list_difference(big_list, small_list):
    """returns difference of two lists"""
    difference = []
    for b in big_list:
        if b not in small_list:
            difference.append(b)
    return difference


# --------------------------------------------------------------------------------#

# PDF DOWNLOADER
target_dir = 'pdf_raw'

url = "https://travel.state.gov/content/travel/en/legal/visa-law0/visa-statistics/nonimmigrant-visa-statistics/monthly-nonimmigrant-visa-issuances.html"
folder_location = r'C:\Users\Tashi Nyangmi\Desktop\visa\data_cleaning\pdf_raw'
download_list = list_difference(file_names, local_files(path=target_dir))

# downloading PDFs
pdf_downloader(url=url, folder_location=folder_location, download_list=download_list)

# --------------------------------------------------------------------------------#
# PDF TO CSV CONVERTER
source_dir = 'pdf_raw'
target_dir = 'csv_raw'

source_files = local_files(path=source_dir)
target_files = local_files(path=target_dir)

convert_list = list_difference(source_files, target_files)
print(convert_list)

#  Converting pdf_raw to csv_raw
for file_name in convert_list:
    input_file = f'{source_dir}/{file_name}.pdf'
    output_file = f'{target_dir}/{file_name}.csv'
    print(f'Converting {file_name[:20]} from pdf_raw to csv_raw')
    pdf_to_csv(input_file=input_file, output_file=output_file)
    print("------------------------------------------------")

# --------------------------------------------------------------------------------#

# CLEAN CSV (csv_raw to csv_clean)
source_dir = 'csv_raw'
target_dir = 'csv_clean'

source_files = local_files(path=source_dir)
target_files = local_files(path=target_dir)

convert_list = list_difference(source_files, target_files)
print(convert_list)

#  Converting csv_raw to csv_clean
for file_name in convert_list:
    input_file = f'{source_dir}/{file_name}.csv'
    output_file = f'{target_dir}/{file_name}.csv'
    print(f'Converting {file_name[:20]} from csv_raw to csv_clean')
    try:
        csv_clean(input_file=input_file, output_file=output_file)
        print("pdf cleaning successful for ", file_name[:20])
    except:
        print("File not found")
    print("=================================================")
    print('                                                 ')

# --------------------------------------------------------------------------------#
