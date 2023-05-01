import csv

# Open the input CSV file
with open('Documents/info664project/merge_moma_education.csv', 'r') as infile:
    reader = csv.reader(infile)
    headers = next(reader)  # Read the header row

    # Create a set to store the unique rows
    unique_rows = set()

    # Loop through the rows in the input CSV file
    for row in reader:
        # Convert the row to a tuple and add it to the set
        unique_rows.add(tuple(row))

    # Convert the set back to a list of lists
    rows = [list(row) for row in unique_rows]

    # Add the header row to the list of rows
    rows.insert(0, headers)

# Write the output CSV file
with open('output.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(rows)












