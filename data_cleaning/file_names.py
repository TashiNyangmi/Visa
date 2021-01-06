# Generating names of all pdf files starting March 2017 until current month -1.

# libraries
import pandas as pd
from datetime import datetime

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year

# ---------------------------------------------------------------------#

s_year = 2017
e_year = currentYear
years = list(range(s_year, e_year + 1))  # e_year +1 because range is non inclusive of the ending number

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
          'august', 'september', 'october', 'november', 'december']
e_month = months[currentMonth - 1]  # from int to str, -1 because of zero indexing

# ---------------------------------------------------------------------#

file_names = []  # initialize a empty list of dataframes

for year in years:
    for month in months:
        file_name = f'{month}_{year}'
        file_names.append(file_name)
        if (year == e_year) and (month == e_month):
            break

# file names to remove
missing = ['january_2017', 'february_2017']  # data starts at march 2017 in the target webpage

for elem in missing:
    file_names.remove(elem)

# ====================================================================#
