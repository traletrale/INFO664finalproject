


import csv

# Open the CSV file and create a reader object
with open('Documents/info664project/moma_education.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # Create a dictionary to store the earliest year for each source
    earliest_year = {'education': {}, 'moma': {}}

    # Loop through each row in the CSV file
    for row in reader:
        artist = row['artist']
        date_str = row['date']
        source = row['source']

        # Get the year from the date string, or skip this row if the date is missing or invalid
        try:
            year = int(date_str)
        except (ValueError, TypeError):
            continue

        # Update the earliest year for this artist and source if it's earlier than the current earliest year
        if artist not in earliest_year[source]:
            earliest_year[source][artist] = year
        elif year < earliest_year[source][artist]:
            earliest_year[source][artist] = year

    # Print the statements for artists whose first acquisition was by education
    for artist in earliest_year['education']:
        education_year = earliest_year['education'][artist]
        moma_year = earliest_year['moma'].get(artist)

        if moma_year is not None and moma_year < education_year:
            continue

        print(f"{artist} collected by education in {education_year}. Collected by moma in {moma_year}, {moma_year - education_year} years later.")

print (f"{moma_year - education_year}")