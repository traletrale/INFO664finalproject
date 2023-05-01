#attempt 1
import csv

with open('Documents/info664project/municipal.csv', encoding='utf-8') as f1, open('Documents/info664project/moma_earliest_dates.csv', encoding='utf-8') as f2:
    municipal_data = csv.DictReader(f1)
    moma_data = csv.DictReader(f2)

    # Get set of artists in moma_data
    moma_artists = set()
    for row in moma_data:
        moma_artists.add(row['artist'])

    # Compare artists in municipal_data to artists in moma_data
    shared_artists = set()
    funded_artists = set()
    for row in municipal_data:
        if row['artist'] in moma_artists:
            shared_artists.add(row['artist'])
            if row['percent funded?'] == 'yes':
                funded_artists.add(row['artist'])

    # Get date and difference for shared artists
    for row in moma_data:
        if row['artist'] in shared_artists:
            print(f"Artist: {row['artist']}")
            print(f"Municipal Date: {row['date']}")
            print(f"MOMA Date: {row['date']}")
            date_difference = abs(int(row['date']) - int(row['date']))
            print(f"Date Difference: {date_difference}\n")

    # Print results
    print(f"Number of shared artists: {len(shared_artists)}")
    print(f"Number of funded shared artists: {len(funded_artists)}")
