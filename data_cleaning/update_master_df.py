# updating module 3
# import pandas as pd
from final_cleaning import add_to_master_list

df = pd.read_csv('master_df.csv')
df.set_index('date', inplace=True)

for file_name in add_to_master_list:
    monthly_df = pd.read_csv(f'csv_clean/{file_name}.csv')  # read csv file
    monthly_df['date'] = file_name.replace('_', '-')  # create a column:date, replace _ with -
    monthly_df['date'] = pd.to_datetime(monthly_df['date'])  # convert column:date to Datatype: DateTime
    monthly_df.set_index('date', inplace=True)
    df = df.append(monthly_df)

df.to_csv('master_df.csv')