def visa_filter(returned_country, returned_year, returned_month, returned_visa_type):
    """filter the master_df.csv based on the given filters"""
    import pandas as pd
    master_df = pd.read_csv('data_cleaning/master_df.csv', index_col='date')
    # Filtering data from master_df
    # - creating columns year and month out of the date index
    master_df.reset_index(inplace=True)  # convert index column:date to regular column:date
    master_df['date'] = pd.to_datetime(master_df['date'])  # convert datatype from string to datetime
    master_df['year'] = pd.DatetimeIndex(master_df['date']).year  # extract year number
    master_df['month'] = pd.DatetimeIndex(master_df['date']).month  # extract month number
    master_df['month'] = pd.to_datetime(master_df['month'],
                                        format='%m').dt.month_name()  # convert month number to month name
    master_df['month'] = master_df['month'].str.lower()  # lower case month names for consistency
    master_df.set_index('date', inplace=True)  # assign column:date as index

    # - actual filtering

    if returned_country == 'all':
        result = master_df.head()  # returning a DataFrame
    else:
        result = master_df[(master_df['country'] == returned_country) &
                           (master_df['visa_type'] == returned_visa_type) &
                           (master_df['month'] == returned_month) &
                           (master_df['year'] == int(returned_year))]
        result = result['number'].values[0]
    return result
