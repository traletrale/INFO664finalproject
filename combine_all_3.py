#combine all 3

import pandas as pd

# Read in the three CSV files
mta_df = pd.read_csv('Documents/info664project/mta_all.csv')
public_df = pd.read_csv('Documents/info664project/public.csv')
education_df = pd.read_csv('Documents/info664project/education.csv')

# Add a new column for the source CSV
mta_df['source'] = 'mta_all'
public_df['source'] = 'public'
education_df['source'] = 'education'

# Concatenate the three dataframes
all_df = pd.concat([mta_df, public_df, education_df], ignore_index=True)

# Write the merged dataframe to a new CSV file
all_df.to_csv('all_3.csv', index=False)
