# updating module 2
import pandas as pd
import numpy as np
from download_and_clean import final_cleaning_list

add_to_master_list = []
final_cleaning_list = ['december_2020']
for file_name in final_cleaning_list:
    try:
        df = pd.read_csv(f'{file_name}')

        df['country'] = df['country'].str.replace("Hong Kong S. A. R", "Hong Kong S.A.R")
        df['country'] = df['country'].str.replace("China-Taiwan", "China - Taiwan")
        df['country'] = df['country'].str.replace("China-mainland", "China - mainland")  # replacing 1 with 2
        df['country'] = df['country'].str.replace("China - Mainland", "China - mainland")  # replacing 3 with 2
        df['country'] = df['country'].str.title()
        df['country'] = df['country'].str.replace("Nationlity", "Nationality")

        df['country'] = np.where(df['country'] == "Non-Nationality Based Issuances", "*Non-Nationality Based Issuances",
                                 df['country'])
        df = df[~df['country'].str.lower().str.contains(" by ")]

        df.to_csv(f'{file_name}.csv')
        print(f'{file_name.csv} is ready to append with master_df.csv')
        add_to_master_list.append(file_name)
    except:
        print(f'{file_name} not found')
