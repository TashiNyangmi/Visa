# Generating names of all pdf files starting March 2017 until current month -1.

# libraries
import pandas as pd
from datetime import datetime

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year

# ---------------------------------------------------------------------#

years = list(range(s_year, e_year + 1))  # e_year +1 because range is non inclusive of the ending number
months = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
          'august', 'september', 'october', 'november', 'december']

s_year = 2017
s_month = 'March'  # fiscal year starts on march

e_year = currentYear
e_month = months[currentMonth- 3] # two months back + 0 indexing: total = -3

# ---------------------------------------------------------------------#

file_names = [] # initialize a empty list of dataframes

for year in years:
    for month in months:
        file_name = f'{month}_{year}'
        file_names.append(file_name)
        if (year == e_year) and (month == e_month):
            break

# saving the list:file_names as dict >> DataFrame >> CSV
file_names_dict = {'col1': file_names}
df = pd.DataFrame(file_names_dict)
df.to_csv('file_names.csv', sep=',', index=False)