# Generating names of all pdf files starting March 2017 until current month -1.

# libraries
import pandas as pd
from datetime import datetime

currentDay = datetime.now().day
currentMonth = datetime.now().month
currentYear = datetime.now().year

months = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
          'august', 'september', 'october', 'november', 'december']

s_year = 2017
s_month = 'March'  # fiscal year starts on march

e_year = currentYear
if currentDay > 20:
    # assuming that the data for the previous month takes atleast 20 days to get uploaded to the official website
    e_month = months[currentMonth - 1]
else:
    e_month = months[currentMonth - 1 - 1]

# ---------------------------------------------------------------------#
years = list(range(s_year, e_year + 1))  # e_year +1 because range is non inclusive of the ending number

# initialize a list of dataframes
file_names = []


for year in years:
    for month in months:
        file_name = '{}%20{}%20-%20NIV%20Issuances%20by%20Nationality%20and%20Visa%20Class'.format(month, year)
        file_names.append(file_name)
        if (year == e_year) and (month == e_month):
            break
    if (year == e_year) and (month == e_month):
        break

# saving the file_names list as pdf and then as csv file

file_names_dict = {'col1': file_names}
df = pd.DataFrame(file_names_dict)

df.to_csv('file_names.csv', sep=',', index=False)

