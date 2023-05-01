#attempt 1

import csv

import chardet


# Create sets to store artists from each CSV file
municipal_artists = set()
moma_artists = set()

with open('Documents/info664project/moma-earliest-dates.csv', encoding='ISO-8859-1') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)

# Read in municipal.csv and add artists to municipal_artists set
with open('Documents/info664project/municipal.csv',) as municipal_file:
    csv_reader = csv.DictReader(municipal_file)
    for row in csv_reader:
        municipal_artists.add(row['artist'])

# Read in moma_earliest_dates.csv and add artists to moma_artists set
with open('Documents/info664project/moma-earliest-dates.csv',) as moma_file:
    csv_reader = csv.DictReader(moma_file)
    for row in csv_reader:
        moma_artists.add(row['artist'])

# Find artists in both sets
common_artists = municipal_artists.intersection(moma_artists)

# Create dictionary to store artist information
artist_info = {}

# Read in municipal.csv again to get information on common artists
with open('municipal.csv', encoding='utf-8') as municipal_file:
    csv_reader = csv.DictReader(municipal_file)
    for row in csv_reader:
        if row['artist'] in common_artists:
            artist_info[row['artist']] = {
                'date_municipal': row['date'],
                'title': row['title'],
                'percent_funded': row['percent funded?']
            }

# Read in moma_earliest_dates.csv to get date for common artists
with open('Documents/info664project/moma-earliest-dates.csv', encoding='ISO-8859-1') as moma_file:
    csv_reader = csv.DictReader(moma_file)
    for row in csv_reader:
        if row['artist'] in common_artists:
            artist_info[row['artist']]['date_moma'] = row['date']

# Print out artist information
for artist, info in artist_info.items():
    print(artist)
    print('Municipal date:', info['date_municipal'])
    print('MoMA date:', info['date_moma'])
    print('Title:', info['title'])
    print('Percent funded:', info['percent_funded'])
    print()
