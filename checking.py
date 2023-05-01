
import csv

filename = 'Documents/info664project/municipal2.csv'

# Check file encoding
with open(filename, 'rb') as f:
    
# Count occurrences of values in the source column
 percent_count = 0
 education_count = 0
 mta_count = 0
 public_count = 0

with open(filename, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['source'] == 'percent':
            percent_count += 1
        elif row['source'] == 'education':
            education_count += 1
        elif row['source'] == 'mta':
            mta_count += 1
        elif row['source'] == 'public':
            public_count += 1

print(f"Number of 'percent': {percent_count}")
print(f"Number of 'education': {education_count}")
print(f"Number of 'mta': {mta_count}")
print(f"Number of 'public': {public_count}")

import csv

municipal_filename = 'Documents/info664project/municipal2.csv'
earliest_dates_filename = 'Documents/info664project/earliest_dates.csv'

# Read the municipal data and group by source and artist
municipal_data = {}
with open(municipal_filename, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        source = row['source']
        artist = row['artist']
        date = row['date']
        percent_funded = row['percent funded?']
        if artist in municipal_data:
            municipal_data[artist][source] = {'date': date, 'percent_funded': percent_funded}
        else:
            municipal_data[artist] = {source: {'date': date, 'percent_funded': percent_funded}}

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
        for source in sources:
            municipal_date = sources[source]['date']
            percent_funded = sources[source]['percent_funded']
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


# import csv

# municipal_filename = 'Documents/info664project/municipal2.csv'
# earliest_dates_filename = 'Documents/info664project/earliest_dates.csv'

# # Read the municipal data and group by source and artist
# municipal_data = {}
# with open(municipal_filename, newline='', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         source = row['source']
#         artist = row['artist']
#         date = row['date']
#         if artist in municipal_data:
#             municipal_data[artist][source] = date
#         else:
#             municipal_data[artist] = {source: date}

# # Read the earliest dates data and filter for artists that appear in municipal data
# earliest_dates_data = {}
# with open(earliest_dates_filename, newline='', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         artist = row['artist']
#         if artist in municipal_data:
#             earliest_date = row['date']
#             earliest_dates_data[artist] = earliest_date

# # Print the results
# for artist, sources in municipal_data.items():
#     if artist in earliest_dates_data:
#         earliest_date = earliest_dates_data[artist]
#         for source in sources:
#             municipal_date = sources[source]
#             if source == 'moma':
#                 if earliest_date < municipal_date:
#                     print(f"{source} , {artist}, moma {earliest_date}, {source} {municipal_date}")
#                 else:
#                     print(f"{source} , {artist}, {source} {municipal_date}, moma {earliest_date}")
#             else:
#                 if earliest_date > municipal_date:
#                     print(f"{source} , {artist}, {source} {municipal_date}, moma {earliest_date}")
#                 else:
#                     print(f"{source} , {artist}, moma {earliest_date}, {source} {municipal_date}")
