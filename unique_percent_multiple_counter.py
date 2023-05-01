

import pandas as pd

# Load the data into a DataFrame
df = pd.read_csv("Desktop/results2.csv")

# Count the number of unique artists
num_artists = len(df["artist"].unique())

# Count the number of entries for each artist
entry_counts = df["artist"].value_counts()

# Count the number of artists with more than one entry
multiple_entries_count = (entry_counts > 1).sum()

# Calculate the percentage of artists with more than one entry
percentage_multiple_entries = multiple_entries_count / num_artists * 100

# Sort the artists by the number of entries they have, from most to least
entry_counts = entry_counts.sort_values(ascending=False)

# Print the results
print("Number of unique artists: {}".format(num_artists))
print("{:.2f}% of the artists have more than one entry".format(percentage_multiple_entries))

print("Artists with multiple entries, from most to least:")
for artist, count in entry_counts.items():
    if count > 1:
        print(f"{artist}: {count} entries")
