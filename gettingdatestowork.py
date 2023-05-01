
import csv

# Open the education.csv file
with open('Documents/info664project/merge_moma_education.csv', 'r') as file:
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
    
    # Print the earliest education year
    print(earliest_education_year)


