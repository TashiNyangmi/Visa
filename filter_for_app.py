def visa_filter(returned_country, returned_year, returned_month, returned_visa_type):
    """filter the master_df.csv based on the given filters"""

    def wrangle_master_df():
        """ wrangle master_df for convenient filtering"""

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
        return master_df

    def filtering():
        """ actual filtering"""
        master_df = wrangle_master_df()
        result = master_df.copy().reset_index(drop=True) # drop the datetime index
        cols = list(result.columns)

        if returned_country != 'all':
            result = result[result['country'] == returned_country]
            cols.remove('country')

        if returned_month != 'all':
            result = result[result['month'] == returned_month]
            cols.remove('month')

        if returned_year != 'all':
            result = result[result['year'] == int(returned_year)]
            cols.remove('year')

        if returned_visa_type != 'all':
            result = result[result['visa_type'] == returned_visa_type]
            cols.remove('visa_type')

        result = result[cols].reset_index(drop=True)
        return result

    return filtering()  # returns a DataFrame
