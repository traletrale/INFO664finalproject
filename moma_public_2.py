import pandas as pd
import os

# Get the path to the input CSV files
input_dir = os.path.dirname(os.path.abspath(__file__))
file1_path = os.path.join(input_dir, 'public.csv')
file2_path = os.path.join(input_dir, 'moma.csv')

# Read the two CSV files into pandas dataframes
# Read the two CSV files into pandas dataframes
df1 = pd.read_csv(file1_path).assign(Source='public.csv')
df2 = pd.read_csv(file2_path).assign(Source='moma.csv')

# read in the data
public_data = pd.read_csv(public.csv)
museum_data = pd.read_csv(moma.csv)

# merge the data on the 'artists' column
merged_data = pd.merge(public_data, museum_data, on='artists', how='inner')

# select only the columns we want in the results csv
results_data = merged_data[['title_x', 'artists', 'created_x', 'date_x', 'creditline_x']]
results_data.columns = ['title', 'artist', 'created', 'date', 'creditline']
results_data['source'] = 'mixed'

# write the results to a new csv file
results_data.to_csv(results_file, index=False)

