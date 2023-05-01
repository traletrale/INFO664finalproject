#import pandas as pd

# Load the CSV file into a pandas DataFrame
#df = pd.read_csv('Documents/info664project/education.csv')

# Count the number of blank cells in the date column
#num_blank_cells = df['date'].isnull().sum()

# Print the result
#print(f"Number of blank cells in the date column: {num_blank_cells}")


# Count the number of entries that have 'ANONYMOUS' as the artist and a blank date
#num_anonymous_blank_date = ((df['artist'] == ' ANONYMOUS') & df['date'].isnull()).sum()

# Count the total number of entries that have ' ANONYMOUS' as the artist
#num_anonymous = (df['artist'] == ' ANONYMOUS').sum()

# Print the results
#print(f"Number of entries with 'ANONYMOUS' as the artist and a blank date: {num_anonymous_blank_date}")
#print(f"Number of entries with 'ANONYMOUS' as the artist: {num_anonymous}")

import csv

moma_file = 'Documents/info664project/moma_earliest_dates.csv'
education_file = 'Documents/info664project/education.csv'
result_file = 'Documents/info664project/merge_moma_education.csv'

moma_artists = set()
education_artists = set()

with open(moma_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        moma_artists.add(row['artist'])

with open(education_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        education_artists.add(row['artist'])

with open(result_file, 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['source', 'title', 'artist','date',]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    
    with open(moma_file, 'r', encoding='utf-8-sig') as f1:
        moma_reader = csv.DictReader(f1)
        for row in moma_reader:
            if row['artist'] in education_artists:
                writer.writerow({'source': 'moma', 'title': row['title'], 'artist': row['artist'],'date': row['date'],})

    with open(education_file, 'r', encoding='utf-8-sig') as f2:
        education_reader = csv.DictReader(f2)
        for row in education_reader:
            if row['artist'] in moma_artists:
                writer.writerow({'source': 'education', 'title': row['title'], 'artist': row['artist'], 'date': row['date'],})

