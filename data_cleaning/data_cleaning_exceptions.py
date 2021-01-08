# refactoring required
# run this after master_df
import pandas as pd
import numpy as np

df = pd.read_csv('master_df.csv', index_col = 'date', parse_dates = True)

df['country'] = df['country'].str.replace("Hong Kong S. A. R", "Hong Kong S.A.R")
df['country'] = df['country'].str.replace("China-Taiwan", "China - Taiwan")
df['country'] = df['country'].str.replace("China-mainland", "China - mainland") # replacing 1 with 2
df['country'] = df['country'].str.replace("China - Mainland", "China - mainland") # replacing 3 with 2
df['country'] = df['country'].str.title()
df['country'] = df['country'].str.replace("Nationlity", "Nationality")

df['country'] = np.where(df['country'] == "Non-Nationality Based Issuances" , "*Non-Nationality Based Issuances", df['country'])
df = df[~df['country'].str.lower().str.contains(" by ")]

df.to_csv('master_df.csv')
