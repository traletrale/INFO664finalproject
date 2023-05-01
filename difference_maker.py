import csv
from datetime import datetime

# Open the input CSV file
with open('Documents/info664project/moma_education.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    # Create two new CSV files
    moma_file = open('moma_first.csv', 'w', newline='')
    education_file = open('education_first.csv', 'w', newline='')

    # Define the fieldnames for the new CSV files
    moma_fieldnames = ['artist', 'title', 'date', 'medium', 'dimensions', 'source', 'second_source', 'difference']
    education_fieldnames = ['artist', 'title', 'date', 'medium', 'dimensions', 'source', 'second_source', 'difference']

    # Create the CSV writers for the new files
    moma_writer = csv.DictWriter(moma_file, fieldnames=moma_fieldnames)
    education_writer = csv.DictWriter(education_file, fieldnames=education_fieldnames)

    # Write the headers for the new CSV files
    moma_writer.writeheader()
    education_writer.writeheader()

    # Loop through each row in the input CSV file
    for row in reader:
        # Check if the row has a valid date
        try:
            date = datetime.strptime(row['date'], '%Y')
        except (ValueError, TypeError):
            continue

        # Check if the row has both sources
        if not row['second_source']:
            continue

        # Get the earliest year and source for the artist
        artist = row['artist']
        source = row['source']
        second_source = row['second_source']
        earliest_year = date.year
        earliest_source = source

        second_date = None
        second_year = None
        second_difference = None

        # Loop through the rest of the rows to find the second source and year for the artist
        for next_row in reader:
            # Check if the next row is for the same artist
            if next_row['artist'] != artist:
                break

            # Check if the next row has a valid date
            try:
                next_date = datetime.strptime(next_row['date'], '%Y')
            except (ValueError, TypeError):
                continue

            # Check if the next row has the second source
            if next_row['source'] == second_source:
                second_date = next_date
                second_year = second_date.year
                second_difference = second_year - earliest_year
                break

            # Check if the next row has an earlier source
            if next_row['source'] == source and next_date.year < earliest_year:
                earliest_year = next_date.year
                earliest_source = source

        # Write the row to the appropriate CSV file
        if earliest_source == 'moma':
            moma_writer.writerow({
                'artist': row['artist'],
                'title': row['title'],
                'date': row['date'],
                'medium': row['medium'],
                'dimensions': row['dimensions'],
                'source': row['source'],
                'second_source': row['second_source'],
                'difference': second_difference
            })
        else:
            education_writer.writerow({
                'artist': row['artist'],
                'title': row['title'],
                'date': row['date'],
                'medium': row['medium'],
                'dimensions': row['dimensions'],
                'source': row['source']
                })
