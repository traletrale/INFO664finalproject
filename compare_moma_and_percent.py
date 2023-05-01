import os
import pandas as pd

# Get the path to the input CSV files
input_dir = os.path.dirname(os.path.abspath(__file__))
file1_path = os.path.join(input_dir, 'completed_percent_for_art_projects.csv')
file2_path = os.path.join(input_dir, 'moma_artworks.csv')

# Read the two CSV files into pandas dataframes
df1 = pd.read_csv(file1_path).assign(Source='completed_percent_for_art_projects.csv')
df2 = pd.read_csv(file2_path).assign(Source='moma_artworks.csv')

# Concatenate the two dataframes
concatenated_df = pd.concat([df1, df2], ignore_index=True)

# Merge the two dataframes on the "Name" column
merged_df = concatenated_df.loc[concatenated_df.duplicated(subset=['artist'], keep=False)]


# Check if there are any matching names
if merged_df.shape[0] > 0:
    print("There are matching names:")
    print(merged_df)
    
    # Prompt the user to enter the output directory

    output_dir = input("Enter the output directory: info664project")
    
    # Write the results to a new CSV file in the specified output directory
    output_path = os.path.join(output_dir, 'results.csv')
    merged_df.to_csv(output_path, index=False)
    
    print("Results written to '{}'.".format(output_path))
else:
    print("There are no matching names.")

