def csv_clean(input_file, output_file):
    """Split the column into 3 separate columns"""
    import pandas as pd
    import numpy as np

    col_names = ['country_raw', 'visa_type_raw', 'number_raw']
    df = pd.read_csv(input_file,
                     names=col_names)

    # extract country, visa_type, and number from the single column containing all three

    def split_country(column):
        column = column.str.split().str[:-2]
        column = column.apply(lambda x: ' '.join(map(str, x)))
        return column

    def split_visa_type(column):
        column = column.str.split().str[-2:-1]
        column = column.apply(lambda x: ' '.join(map(str, x)))
        return column

    def split_number(column):
        column = column.str.split().str[-1:]
        column = column.apply(lambda x: ' '.join(map(str, x)))
        return column

    df['country'] = np.where(df['visa_type_raw'].isnull(), split_country(df['country_raw']), df['country_raw'])
    df['visa_type'] = np.where(df['visa_type_raw'].isnull(), split_visa_type(df['country_raw']), df['visa_type_raw'])
    df['number'] = np.where(df['visa_type_raw'].isnull(), split_number(df['country_raw']), df['number_raw'])

    # Drop the raw columns
    df = df.drop(labels=['country_raw', 'visa_type_raw', 'number_raw'], axis=1)

    # Drop the title rows
    df = df[df['number'].apply(lambda x: x.isnumeric())]

    # Convert column: number to datatype int64
    df['number'] = df['number'].astype('int64', copy=False)

    # Reindex the DataFrame
    df = df.reset_index(drop=True)

    df.to_csv(output_file, sep=',', index=False)
    return
