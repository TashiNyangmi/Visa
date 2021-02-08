import pandas as pd
import numpy as np

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
    print(f'Converting {file_name} from pdf_raw to csv_raw')
    try:
        pdf_to_csv(input_file=input_file, output_file=output_file)
    except:
        print(f"{file_name} not found")
    print("------------------------------------------------")

# --------------------------------------------------------------------------------#

# CLEAN CSV (csv_raw to csv_clean)
source_dir = 'csv_raw'
target_dir = 'csv_clean'

#  Converting csv_raw to csv_clean
for file_name in download_list:
    input_file = f'{source_dir}/{file_name}.csv'
    output_file = f'{target_dir}/{file_name}.csv'
    print(f'Converting {file_name} from csv_raw to csv_clean')
    try:
        csv_clean(input_file=input_file, output_file=output_file)
        print("csv cleaning successful for ", file_name)

    except:
        print(f"{file_name} not found")
    print("=================================================")
    print('                                                 ')


# --------------------------------------------------------------------------------#
print("Performing final cleaning")
print("                 ")
for file_name in download_list:
    try:
        df = pd.read_csv(f'csv_clean/{file_name}.csv')

        df['country'] = df['country'].str.replace("Hong Kong S. A. R", "Hong Kong S.A.R")
        df['country'] = df['country'].str.replace("China-Taiwan", "China - Taiwan")
        df['country'] = df['country'].str.replace("China-mainland", "China - mainland")  # replacing 1 with 2
        df['country'] = df['country'].str.replace("China - Mainland", "China - mainland")  # replacing 3 with 2
        df['country'] = df['country'].str.title()
        df['country'] = df['country'].str.replace("Nationlity", "Nationality")

        df['country'] = np.where(df['country'] == "Non-Nationality Based Issuances", "*Non-Nationality Based Issuances",
                                 df['country'])
        df = df[~df['country'].str.lower().str.contains(" by ")]

        df.to_csv(f'{file_name}.csv')
        print(f'{file_name.csv} is ready to append with master_df.csv')

    except:
        print(f'{file_name} not found')


# --------------------------------------------------------------------------------#
# updating module 3
print('Updating master_df.csv')

df = pd.read_csv('master_df.csv')
df.set_index('date', inplace=True)

for file_name in download_list:
    try:
        monthly_df = pd.read_csv(f'csv_clean/{file_name}.csv')  # read csv file
        monthly_df['date'] = file_name.replace('_', '-')  # create a column:date, replace _ with -
        monthly_df['date'] = pd.to_datetime(monthly_df['date'])  # convert column:date to Datatype: DateTime
        monthly_df.set_index('date', inplace=True)
        df = df.append(monthly_df)
        print(f'{file_name} successfully appended to master_df.csv')
    except:
        print(f'{file_name} not found !!!')

df.to_csv('master_df.csv')