

import csv

moma_file = 'Documents/info664project/earliest_dates.csv'
municipal_file = 'Documents/info664project/municipal.csv'
result_file = 'Documents/info664project/merge_moma_municipal.csv'

moma_artists = set()
municipal_artists = set()

with open(moma_file, 'r', ) as f:
    reader = csv.DictReader(f)
    for row in reader:
        moma_artists.add(row['artist'])

with open(municipal_file, 'r', ) as f:
    reader = csv.DictReader(f)
    for row in reader:
        municipal_artists.add(row['artist'])

with open(result_file, 'w', newline='', ) as f:
    fieldnames = ['source', 'title', 'artist','date',]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    
    with open(moma_file, 'r', ) as f1:
        moma_reader = csv.DictReader(f1)
        for row in moma_reader:
            if row['artist'] in municipal_artists:
                writer.writerow({'source': 'moma', 'title': row['title'], 'artist': row['artist'],'date': row['date'],})

    with open(municipal_file, 'r', ) as f2:
        education_reader = csv.DictReader(f2)
        for row in education_reader:
            if row['artist'] in moma_artists:
                writer.writerow({'source': 'education', 'title': row['title'], 'artist': row['artist'], 'date': row['date'],})

