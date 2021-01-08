def lists():
    import pandas as pd
    master_df = pd.read_csv('data_cleaning/master_df.csv')
    countries = list(master_df['country'].unique())
    years = ['2017', '2018', '2019', '2020']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
              'october', 'november', 'december']
    visa_types = list(master_df['visa_type'].unique())

    # adding the option to view all to each filter category
    countries.insert(0, 'all')
    years.insert(0, 'all')
    months.insert(0, 'all')
    visa_types.insert(0, 'all')

    return sorted(countries), years, months, sorted(visa_types)  # returns lists
