
import csv

municipal_filename = 'Documents/info664project/municipal2.csv'
earliest_dates_filename = 'Documents/info664project/earliest_dates.csv'

municipal_data = {}

# Read the municipal data and group by source and artist
with open(municipal_filename, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        source = row['source']
        artist = row['artist']
        date = row['date']
        percent_funded = row['percent funded?']
        if artist in municipal_data:
            if source in municipal_data[artist]:
                municipal_data[artist][source].append({'date': date, 'percent funded?': percent_funded})
            else:
                municipal_data[artist][source] = [{'date': date, 'percent funded?': percent_funded}]
        else:
            municipal_data[artist] = {source: [{'date': date, 'percent funded?': percent_funded}]}

# Read the earliest dates data and filter for artists that appear in municipal data
earliest_dates_data = {}
with open(earliest_dates_filename, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        artist = row['artist']
        if artist in municipal_data:
            earliest_date = row['date']
            earliest_dates_data[artist] = earliest_date

# Print the results
for artist, sources in municipal_data.items():
    if artist in earliest_dates_data:
        earliest_date = earliest_dates_data[artist]
        for source, entries in sources.items():
            for entry in entries:
                municipal_date = entry['date']
                percent_funded = entry['percent funded?']
                if source == 'moma':
                    if earliest_date < municipal_date:
                        print(f"{source},{artist},moma {earliest_date},{source} {municipal_date},{percent_funded}")
                    else:
                        print(f"{source},{artist},{source} {municipal_date},moma {earliest_date},{percent_funded}")
                else:
                    if earliest_date > municipal_date:
                        print(f"{source},{artist},{source} {municipal_date},moma {earliest_date},{percent_funded}")
                    else:
                        print(f"{source},{artist},moma {earliest_date},{source} {municipal_date},{percent_funded}")
