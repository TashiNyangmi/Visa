# Updating module 1
# Downloads new files from source
# Converts and cleans
# Next step: appending to master_df and exporting to master_df.csv
# importing UDFs
from pdf_downloader import pdf_downloader
from pdf_to_csv import pdf_to_csv
from csv_clean import csv_clean
from download_list import download_list  # list of file_names that update with current date/year


# --------------------------------------------------------------------------------#

# PDF DOWNLOADER
url = "https://travel.state.gov/content/travel/en/legal/visa-law0/visa-statistics/nonimmigrant-visa-statistics/monthly-nonimmigrant-visa-issuances.html"
folder_location = r'C:\Users\Tashi Nyangmi\Desktop\visa\data_cleaning\pdf_raw'

# downloading PDFs
pdf_downloader(url=url, folder_location=folder_location, download_list=download_list)

# --------------------------------------------------------------------------------#
# PDF TO CSV CONVERTER
source_dir = 'pdf_raw'
target_dir = 'csv_raw'

#  Converting pdf_raw to csv_raw
for file_name in download_list:
    input_file = f'{source_dir}/{file_name}.pdf'
    output_file = f'{target_dir}/{file_name}.csv'
    print(f'Converting {file_name[:20]} from pdf_raw to csv_raw')
    pdf_to_csv(input_file=input_file, output_file=output_file)
    print("------------------------------------------------")

# --------------------------------------------------------------------------------#

# CLEAN CSV (csv_raw to csv_clean)
source_dir = 'csv_raw'
target_dir = 'csv_clean'

#  Converting csv_raw to csv_clean
for file_name in download_list:
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
