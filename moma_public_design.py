import os
import pandas as pd

# Get the path to the input CSV files
input_dir = os.path.dirname(os.path.abspath(__file__))
file1_path = os.path.join(input_dir, 'public_design_commission_outdoor_public_art_inventory.csv')
file2_path = os.path.join(input_dir, 'moma_artworks.csv')

# Read the two CSV files into pandas dataframes
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Check that both dataframes have the "artist" and "DateAcquired" columns
if ("artist" not in df1.columns or "artist" not in df2.columns or
        "DateAcquired" not in df1.columns or "DateAcquired" not in df2.columns):
    print("One or both dataframes do not have a 'artist' or 'DateAcquired' column.")
else:
    # Merge the two dataframes on the "artist" column
    merged_df = pd.merge(df1, df2, on='artist', how='outer', indicator=True)

    # Filter the merged dataframe to only include matching names
    matched_df = merged_df[merged_df['_merge'] == 'both'].drop(columns='_merge')

    # Add a "Source" column to indicate the source of each record
    matched_df.insert(0, 'Source', '')
    matched_df.loc[matched_df.isin(df1.values.tolist()).all(1), 'Source'] = 'File 1'
    matched_df.loc[matched_df.isin(df2.values.tolist()).all(1), 'Source'] = 'File 2'

    # Filter the second source dataframe to only include the earliest record for each artist
    df2_earliest = df2.loc[df2.groupby('artist')['DateAcquired'].idxmin()]

    # Merge the matched dataframe with the filtered second source dataframe
    result_df = pd.concat([matched_df, df2_earliest])

    # Check if there are any matching names
    if result_df.shape[0] > 0:
        print("There are matching names:")
        print(result_df)

        # Prompt the user to enter the output directory
        output_dir = input("Enter the output directory: ")

        # Write the results to a new CSV file in the specified output directory
        output_path = os.path.join(output_dir, 'results.csv')
        result_df.to_csv(output_path, index=False)

        print("Results written to '{}'.".format(output_path))
    else:
        print("There are no matching names.")

        # Prompt the user to enter the output directory
        output_dir = input("Enter the output directory: ")

        # Write an empty results file to the specified output directory
        output_path = os.path.join(output_dir, 'results.csv')
        with open(output_path, 'w'):
            pass

        print("Results file '{}' created with no matching names.".format(output_path))
