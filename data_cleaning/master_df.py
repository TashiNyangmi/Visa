from file_names import file_names
import pandas as pd

# import the first dataframe
# march 2017
df = pd.read_csv(f'csv_clean/{file_names[0]}.csv')
df['date'] = file_name.replace('_', '-')  # create a column:date, replace _ with -
df['date']= pd.to_datetime(df['date'])  # convert column:date to Datatype: DateTime
df.set_index('date', inplace = True)


# import rest of the dataframes
for file_name in file_names[1:]:
    try:
        monthly_df = pd.read_csv(f'csv_clean/{file_name}.csv')  # read csv file
        monthly_df['date'] = file_name.replace('_', '-')  # create a column:date, replace _ with -
        monthly_df['date']= pd.to_datetime(monthly_df['date'])  # convert column:date to Datatype: DateTime
        monthly_df.set_index('date', inplace = True) # set column:date as Index
        df = df.append(monthly_df)
    except:
        print(f'{file_name}.csv not found')

# ========================================================================================== #

