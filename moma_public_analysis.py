import csv

# read in the result.csv file
with open('Documents/info664project/moma_public.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    entries = [entry for entry in reader]

# get the unique artists
artists = set([entry['artist'] for entry in entries])

# initialize counters
total_artists = len(artists)
earlier_moma_count = 0
earlier_public_count = 0

# loop over artists
for artist in artists:
    # filter entries for artist
    artist_entries = [entry for entry in entries if entry['artist'] == artist]
    
    # find earliest moma date
    moma_dates = [entry['date'] for entry in artist_entries if entry['source'] == 'moma']
    earliest_moma_date = min(moma_dates)
    
    # find earliest public date
    public_dates = [entry['date'] for entry in artist_entries if entry['source'] == 'public']
    earliest_public_date = min(public_dates)
    
    # compare dates
    if earliest_moma_date < earliest_public_date:
        earlier_moma_count += 1
    elif earliest_public_date < earliest_moma_date:
        earlier_public_count += 1


# print results
print('Total artists:', total_artists)
print('Artists with earlier date for moma source:', earlier_moma_count)
print('Artists with earlier date for public source:', earlier_public_count)



