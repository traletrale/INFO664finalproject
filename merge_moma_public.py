import csv

moma_file = 'Documents/info664project/moma_earliest_dates.csv'
public_file = 'Documents/info664project/public.csv'
result_file = 'Documents/info664project/result.csv'

moma_artists = set()
public_artists = set()

with open(moma_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        moma_artists.add(row['artist'])

with open(public_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        public_artists.add(row['artist'])

with open(result_file, 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['source', 'title', 'artist', 'created', 'date', 'creditline']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    
    with open(moma_file, 'r', encoding='utf-8-sig') as f1:
        moma_reader = csv.DictReader(f1)
        for row in moma_reader:
            if row['artist'] in public_artists:
                writer.writerow({'source': 'moma', 'title': row['title'], 'artist': row['artist'], 'created': row['created'], 'date': row['date'], 'creditline': row['creditline']})

    with open(public_file, 'r', encoding='utf-8-sig') as f2:
        public_reader = csv.DictReader(f2)
        for row in public_reader:
            if row['artist'] in moma_artists:
                writer.writerow({'source': 'public', 'title': row['title'], 'artist': row['artist'], 'created': row['created'], 'date': row['date'], 'creditline': row['creditline']})

