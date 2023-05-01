import csv

moma_file = 'Documents/info664project/moma.csv'
new_file = 'earliest_dates.csv'

artists = set()
earliest_dates = {}

with open(moma_file, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        artist = row['artist']
        date = row['date']
        if artist not in earliest_dates or date < earliest_dates[artist]['date']:
            earliest_dates[artist] = row
        artists.add(artist)

with open(new_file, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'artist', 'created', 'date', 'creditline', 'source'])
    writer.writeheader()
    for artist in artists:
        row = earliest_dates[artist]
        row['source'] = moma_file
        writer.writerow(row)
