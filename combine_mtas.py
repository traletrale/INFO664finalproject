#combine mtas

import pandas as pd

# Read in the four CSV files
manhattan_df = pd.read_csv('Desktop/mta_manhattan.csv')
brooklyn_df = pd.read_csv('Desktop/mta_brooklyn.csv')
bronx_df = pd.read_csv('Desktop/mta_bronx.csv')
queens_df = pd.read_csv('Desktop/mta_queens.csv')

# Concatenate the four dataframes
all_df = pd.concat([manhattan_df, brooklyn_df, bronx_df, queens_df], ignore_index=True)

# Write the combined dataframe to a new CSV file
all_df.to_csv('mta_all.csv', index=False)
