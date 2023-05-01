import pandas as pd

# Load the cleaned_all_3.csv file into a pandas dataframe
df = pd.read_csv('Documents/info664project/cleaned_all_3.csv')

# Create a new dataframe that removes duplicates based on the "artist", "date", and "title" columns
df_no_duplicates = df.drop_duplicates(subset=['artist', 'date', 'title'], keep='first')

# Merge the two dataframes on the "title" column using an outer join
merged_df = pd.merge(df, df_no_duplicates[['title']], on='title', how='outer', suffixes=('', '_no_duplicates'))

# Fill missing values in the "title_no_duplicates" column with the corresponding "title" value
merged_df['title_no_duplicates'] = merged_df['title_no_duplicates'].fillna(merged_df['title'])

# Create a new column "funded by percent" that has "yes" if the row is a duplicate, and "no" if it is not
merged_df['funded by percent'] = merged_df.apply(lambda x: 'yes' if ((merged_df['artist'] == x['artist']) & (merged_df['date'] == x['date']) & (merged_df['title_no_duplicates'] == x['title_no_duplicates'])).sum() > 1 else 'no', axis=1)

# Drop the "title_no_duplicates" column
merged_df = merged_df.drop(columns=['title_no_duplicates'])

# Save the resulting dataframe to a new CSV file
merged_df.to_csv('new_file.csv', index=False)







#import pandas as pd

# Load the cleaned_all_3.csv file into a pandas dataframe
#df = pd.read_csv('Documents/info664project/cleaned_all_3.csv')

# Create a new dataframe that removes duplicates based on the "title" column
#df_no_duplicates = df.drop_duplicates(subset='title', keep='first')

# Merge the two dataframes on the "title" column using a left join
#merged_df = pd.merge(df, df_no_duplicates[['title']], on='title', how='left', suffixes=('', '_no_duplicates'))

# Create a new column "funded by percent" that has "yes" if the row is a duplicate, and "no" if it is not
#merged_df['funded by percent'] = merged_df['title'].duplicated().apply(lambda x: 'yes' if x else 'no')

# Save the resulting dataframe to a new CSV file
#merged_df.to_csv('new_file.csv', index=False)




#import pandas as pd

# Load the two CSV files into dataframes
#all_3_df = pd.read_csv('Documents/info664project/cleaned_all_3.csv')
#cleaned_percent_df = pd.read_csv('Documents/info664project/cleaned_percent.csv')

#print("Number of unique artists in 'all_3.csv':", all_3_df['artist'].nunique())
#print("Number of unique artists in 'cleaned_percent.csv':", cleaned_percent_df['artist'].nunique())

# Check for missing data in 'artist' column of 'all_3.csv'
#print("Number of missing artists in 'all_3.csv':", all_3_df['artist'].isnull().sum())

# Check how many times each artist appears in 'all_3.csv'
#print("Artist counts in 'all_3.csv':")
#print(all_3_df['artist'].value_counts())

#import pandas as pd

# Load the two cleaned CSV files into dataframes
#all_3_df = pd.read_csv('Documents/info664project/cleaned_all_3.csv')
#cleaned_percent_df = pd.read_csv('Documents/info664project/cleaned_percent.csv')

# Add a column to each dataframe indicating whether the artist is in both dataframes
#all_3_df['in_both'] = all_3_df['artist'].isin(cleaned_percent_df['artist'])
#cleaned_percent_df['in_both'] = cleaned_percent_df['artist'].isin(all_3_df['artist'])

# Concatenate the two dataframes and save the result as a new CSV file
#combined_df = pd.concat([all_3_df, cleaned_percent_df], axis=0)
#combined_df.to_csv('combined.csv', index=False)



 #Repeat for 'cleaned_percent.csv'

 #Find the set of unique artists in each dataframe
#all_3_artists = set(all_3_df['artist'].unique())
#cleaned_percent_artists = set(cleaned_percent_df['artist'].unique())

# Find the intersection of the two sets to get the artists in both dataframes
#artists_in_both = all_3_artists.intersection(cleaned_percent_artists)

# Print out the list of artists in both dataframes
#print("Artists in both 'all_3.csv' and 'cleaned_percent.csv':")
#for artist in artists_in_both:
#    print(artist)

#import pandas as pd

#Load the two CSV files into dataframes
#all_3_df = pd.read_csv('Documents/info664project/cleaned_all_3.csv')
#cleaned_percent_df = pd.read_csv('Documents/info664project/cleaned_percent.csv')

# Merge the two dataframes on the 'artist' column
#merged_df = pd.merge(all_3_df, cleaned_percent_df, on='artist', how='outer', suffixes=('_all_3', '_cleaned_percent'))

# Add a new column to indicate whether the artist is in both CSVs or not
#merged_df['in_both'] = ['yes' if pd.notna(row['count_all_3']) and pd.notna(row['count_cleaned_percent']) else 'no' for index, row in merged_df.iterrows()]

# Save the merged dataframe as a new CSV file
#merged_df.to_csv('merged.csv', index=False)

#print(merged_df.head())
#import pandas as pd

# Read in the two CSV files
#all_3 = pd.read_csv("Documents/info664project/all_3.csv")
#cleaned_percent = pd.read_csv("Documents/info664project/cleaned_percent.csv")

# Print out the number of artists in each file
#print("Number of artists in all_3:", len(all_3))
#print("Number of artists in cleaned_percent:", len(cleaned_percent))

# Print out the list of artists in each file
#print("Artists in all_3:", all_3["artist"].tolist())
#print("Artists in cleaned_percent:", cleaned_percent["artist"].tolist())

#import csv

# Read in the two CSV files
#with open('Documents/info664project/all_3.csv', newline='') as all_3_file, open('Documents/info664project/cleaned_percent.csv', newline='') as cleaned_percent_file:
#    all_3_reader = csv.reader(all_3_file)
#    cleaned_percent_reader = csv.reader(cleaned_percent_file)

    # Create a dictionary of artists in the cleaned_percent file
#    cleaned_percent_artists = {}
#    for row in cleaned_percent_reader:
#        cleaned_percent_artists[row[0]] = True

    # Create a new CSV file for the results
#    with open('all_3_with_percent.csv', 'w', newline='') as results_file:
#        writer = csv.writer(results_file)

        # Loop through the artists in the all_3 file and check if they appear in the cleaned_percent file
#        for row in all_3_reader:
#            if row[0] in cleaned_percent_artists:
#                writer.writerow(row + ['yes'])
#            else:
#                writer.writerow(row + ['no'])



