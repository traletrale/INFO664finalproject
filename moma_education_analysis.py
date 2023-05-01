import csv

# Open the education.csv file
with open('Documents/info664project/moma_education.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Create a list of valid years
    valid_years = []
    
    for row in reader:
        # Get the year from the date string, or skip this row if the date is missing or invalid
        try:
            year = int(row['date'])
            valid_years.append(year)
        except (ValueError, TypeError):
            pass
    
    if valid_years:
        # Calculate the earliest education year
        earliest_education_year = min(valid_years)
    else:
        # Handle the case where there are no valid years
        earliest_education_year = None
    

# read in the result.csv file
with open('Documents/info664project/moma_education.csv', newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    entries = [entry for entry in reader]

# get the unique artists
artists = set([entry['artist'] for entry in entries])

# initialize counters
total_artists = len(artists)
earlier_moma_count = 0
earlier_education_count = 0

# loop over artists
for artist in artists:
    # filter entries for artist
    artist_entries = [entry for entry in entries if entry['artist'] == artist]
    
    # find earliest moma date
    moma_dates = [entry['date'] for entry in artist_entries if entry['source'] == 'moma']
    earliest_moma_date = min(moma_dates)
    
    # find earliest education date
    education_dates = [entry['date'] for entry in artist_entries if entry['source'] == 'education']
    earliest_education_date = min(education_dates)
    
    # compare dates
    if earliest_moma_date < earliest_education_date:
        earlier_moma_count += 1
    elif earliest_education_date < earliest_moma_date:
        earlier_education_count += 1


# print results
print('Total artists:', total_artists)
print('Artists with earlier date for moma source:', earlier_moma_count)
print('Artists with earlier date for education source:', earlier_education_count)
