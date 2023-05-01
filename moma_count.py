import csv

artist_dict = {}

with open('Documents/info664project/moma.csv', newline='', encoding='utf-8') as csvfile:
    moma_reader = csv.DictReader(csvfile)
    for row in moma_reader:
        artist = row['artist']
        if artist not in artist_dict:
            artist_dict[artist] = 1
        else:
            artist_dict[artist] += 1

total_artists = len(artist_dict)
print(f"Total unique artists in moma.csv: {total_artists}")
