import csv
from datetime import datetime

moma_artists = set()
moma_dates = {}
moma_sources = {}

with open('Documents/info664project/earliest_dates.csv', newline='', encoding='utf-8') as moma_file:
    csv_reader = csv.DictReader(moma_file)
    for row in csv_reader:
        artist = row['artist']
        date = row['date']
        moma_artists.add(artist)
        moma_dates[artist] = date
        moma_sources[artist] = 'moma'

with open('Documents/info664project/municipal.csv', newline='', encoding='utf-8') as municipal_file:
    csv_reader = csv.DictReader(municipal_file)
    for row in csv_reader:
        artist = row['artist']
        date = row['date']
        percent_funded = row['percent funded?']
        if artist in moma_artists:
            source = 'moma'
            moma_date = datetime.strptime(moma_dates[artist], '%Y-%m-%d')
            municipal_date = datetime.strptime(date, '%Y')
            if municipal_date < moma_date:
                date1 = municipal_date
                date2 = moma_date
            else:
                date1 = moma_date
                date2 = municipal_date
            diff_years = date2.year - date1.year - ((date2.month, date2.day) < (date1.month, date1.day))
            print(f"{artist}, {title}, {source}, {percent_funded}, {date1.strftime('%Y-%m-%d')}, {date2.strftime('%Y-%m-%d')}, {diff_years}")
        else:
            source = 'municipal'
            print(f"{artist}, {source}, {percent_funded}, {date},")





















# import csv

# # create set of artists in moma csv
# moma_artists = set()
# with open('Documents/info664project/earliest_dates.csv', ) as moma_file:
#     csv_reader = csv.DictReader(moma_file)
#     for row in csv_reader:
#         moma_artists.add(row['artist'])

# # compare with municipal csv
# with open('Documents/info664project/municipal.csv', ) as mun_file:
#     csv_reader = csv.DictReader(mun_file)
#     for row in csv_reader:
#         artist = row['artist']
#         if artist in moma_artists:
#             percent_funded = row['percent funded?']
#             date_moma = ""
#             date_mun = row['date']
#             with open('Documents/info664project/earliest_dates.csv', ) as moma_file:
#                 csv_reader_moma = csv.DictReader(moma_file)
#                 for row_moma in csv_reader_moma:
#                     if row_moma['artist'] == artist:
#                         date_moma = row_moma['date']
#                         break
#             print(f"{artist}, Percent Funded: {percent_funded}, MOMA: {date_moma}, Municipal: {date_mun}")




# import csv

# with open('Documents/info664project/earliest_dates.csv', 'rb') as f:
#     csv_reader = csv.DictReader((line.decode('utf-8') for line in f), delimiter=',')

#     for row in csv_reader:
#         print(row)


# #attempt 1
# import csv

# with open('Documents/info664project/municipal.csv', ) as f1, open('Documents/info664project/earliest_dates.csv', ) as f2:
#     municipal_data = csv.DictReader(f1)
#     moma_data = csv.DictReader(f2)

#     # Get set of artists in moma_data
#     moma_artists = set()
#     for row in moma_data:
#         moma_artists.add(row['artist'])

#     # Compare artists in municipal_data to artists in moma_data
#     shared_artists = set()
#     funded_artists = set()
#     for row in municipal_data:
#         if row['artist'] in moma_artists:
#             shared_artists.add(row['artist'])
#             if row['percent funded?'] == 'yes':
#                 funded_artists.add(row['artist'])

#     # Get date and difference for shared artists
#     for row in moma_data:
#         if row['artist'] in shared_artists:
#             print(f"Artist: {row['artist']}")
#             print(f"Municipal Date: {row['date']}")
#             print(f"MOMA Date: {row['date']}")
#             date_difference = abs(int(row['date']) - int(row['date']))
#             print(f"Date Difference: {date_difference}\n")

#     # Print results
#     print(f"Number of shared artists: {len(shared_artists)}")
#     print(f"Number of funded shared artists: {len(funded_artists)}")
