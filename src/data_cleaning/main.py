from pdf_to_csv import pdf_to_csv  # function
from csv_clean import csv_clean  # function
import pandas as pd

file_names_df = pd.read_csv('file_names.csv')
file_names = file_names_df['col1']  # Series

# -----------------------------------------------------------------------------------------------
# ISSUES:
# 1) filename inconsistencies:

# replace correct w/ incorrect
# december2017: replace 'nationality' w/ 'nationlity'
file_names[11] = 'december%202017%20-%20NIV%20Issuances%20by%20Nationlity%20and%20Visa%20Class'

# october2019: replace '202019%20-%20NIVw/ '202019%20NIV'
file_names[33] = 'october%202019%20NIV%20Issuances%20by%20Nationality%20and%20Visa%20Class'

# september2020: replace 'SEPTEMBER' w/ 'SEPT'
file_names[44] = 'sept%202020%20-%20NIV%20Issuances%20by%20Nationality%20and%20Visa%20Class'



# 2) missing months:

# drop jan2017 and feb 2017 because fiscal year starts March
# drop nov 2020 because origin website has not updated yet
file_names = file_names[2:-1]  # omitting first 2 elements and the last element
file_names = file_names[31:33] # delete
# -------------------------------------------------------------------------------------------------
for file_name in file_names:
    #  Converting pdf_raw to csv_raw
    input_file = f'pdf_raw/{file_name}.pdf'
    output_file = f'csv_raw/{file_name}.csv'
    print(f'Converting {file_name[:20]} from pdf_raw to csv_raw')
    pdf_to_csv(input_file=input_file, output_file=output_file)
    print("pdf to csv successful for ", file_name[:20])
    print("------------------------------------------------")

    #  Converting csv_raw to csv_clean
    input_file = f'csv_raw/{file_name}.csv'
    output_file = f'csv_clean/{file_name}.csv'
    print(f'Converting {file_name[:20]} from csv_raw to csv_clean')
    csv_clean(input_file=input_file, output_file=output_file)
    print("pdf cleaning successful for ", file_name[:20])
    print("=================================================")
    print('                                                 ')
