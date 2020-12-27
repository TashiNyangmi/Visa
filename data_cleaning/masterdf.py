import pandas as pd
import datetime as dt

file_names = pd.read_csv('file_names.csv') # a one dimensional(supposedly) list of file names
file_names = file_names['col1']


# 1) fixing some inconsistencies in naming conventions (in source data)

# december2017: replace 'Nationltity' w/ 'Nationality'
file_names[11] = 'december%202017%20-%20NIV%20Issuances%20by%20Nationlity%20and%20Visa%20Class'

# october2019: replace '202019%20-%20NIV w/ '202019%20NIV'
file_names[33] = 'october%202019%20NIV%20Issuances%20by%20Nationality%20and%20Visa%20Class'

# september2020: replace 'SEPTEMBER' w/ 'SEPT'
file_names[44] = 'sept%202020%20-%20NIV%20Issuances%20by%20Nationality%20and%20Visa%20Class'


# 2) missing months:

# drop jan2017 and feb 2017 because fiscal year starts March
# drop nov 2020 & dec 2020 because origin website has not updated yet
file_names = file_names[2:-2]  # omitting first 2 elements and the last 2 element

# fix indices
indices = range(0, len(file_names))  # Datatype: range
file_names.index = indices           # Assign ^^ to file_names's index


def masterdf(file_names):
    import datetime as dt

    # import all files from directory: csv_clean
    df_list = []
    for file_name in file_names:
        try:
            df_list.append(pd.read_csv(f'csv_clean/{file_name}.csv'))
        except:
            print(f'{file_name[:20]} not found')

    # creating a list of dates to iterate over while indexing DataFrames
    import datetime
    from dateutil.relativedelta import relativedelta
    date_list = []
    start_date = datetime.datetime(2017, 3, 1)  # 1st March 2017

    for month in range(len(df_list)):
        date_list.append(start_date + relativedelta(months=+(month)))

    # using the above created list of dates to index the DataFrame
    def df_indexing(df, counter):
        """return a DT indexed DataFrame"""
        df = df_list[counter]
        df['date'] = date_list[counter]
        df.set_index('date', inplace=True)
        return (df)

    # applying the above function to all DataFrames

    indexed_df = {}
    counter = 0
    for df in df_list:
        indexed_df[f'df{counter}'] = df_indexing(df, counter)  # returns an DT indexed DataFrame
        counter += 1

    # concatinating the DataFrames vertically
    master_df = pd.concat(list(indexed_df.values()), axis=0)

    return master_df


# export master_df as csv
master_df = masterdf(file_names=file_names)
master_df.to_csv('master_df.csv', sep=',')
