


import csv

# Open the CSV file and create a reader object
with open('Documents/info664project/moma_education.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # Create a dictionary to store the earliest year for each source
    earliest_year = {'moma': {}, 'education': {}}

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

    # Print the statements for artists whose first acquisition was by MoMA
    for artist in earliest_year['moma']:
        moma_year = earliest_year['moma'][artist]
        education_year = earliest_year['education'].get(artist)

        if education_year is not None and education_year < moma_year:
            continue

        print(f"{artist} collected by moma in {moma_year}. Collected by education in {education_year}, {education_year - moma_year} years later.")

print (f"{education_year - moma_year}")


