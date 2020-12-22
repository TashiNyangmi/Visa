from masterdf import masterdf

import pandas as pd

file_names = pd.read_csv('file_names.csv')
file_names = file_names['col1']

file_names[11] = 'december%202017%20-%20NIV%20Issuances%20by%20Nationlity%20and%20Visa%20Class'

# october2019: replace '202019%20-%20NIVw/ '202019%20NIV'
file_names[33] = 'october%202019%20NIV%20Issuances%20by%20Nationality%20and%20Visa%20Class'

# september2020: replace 'SEPTEMBER' w/ 'SEPT'
file_names[44] = 'sept%202020%20-%20NIV%20Issuances%20by%20Nationality%20and%20Visa%20Class'

# 2) missing months:

# drop jan2017 and feb 2017 because fiscal year starts March
# drop nov 2020 because origin website has not updated yet
file_names = file_names[2:-1]  # omitting first 2 elements and the last element

# fix indices
indices = range(0, len(file_names))
file_names.index = indices

master_df = masterdf(file_names = file_names)
print(master_df.head())