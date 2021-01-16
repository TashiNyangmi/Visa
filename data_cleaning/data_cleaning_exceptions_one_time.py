import pandas as pd
import numpy as np

df = pd.read_csv('master_df.csv', index_col = 'date', parse_dates = True)
df['visa_type'] = np.where(df['country'].isna(), df['visa_type'].str.strip("Sudan"), df['visa_type'])
df['country'] = np.where(df['country'].isna(), "Sudan", df['country'])

df.to_csv('master_df.csv')