import csv

# Load the CSV file
with open('data/sample/Spotify_Youtube.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Check for missing values
missing_values = 0
for row in data:
    for value in row:
        if value == '':
            missing_values += 1
print("Missing values:", missing_values)

# Check for duplicate rows
duplicate_rows = 0
seen_rows = set()
for row in data:
    row_tuple = tuple(row)
    if row_tuple in seen_rows:
        duplicate_rows += 1
    seen_rows.add(row_tuple)
print("\nDuplicate rows:", duplicate_rows)

# Check for invalid values in the 'Danceability' column
invalid_values = 0
for row in data[1:]:  # Skip header row
    try:
        danceability = float(row[7])  # Assuming 'Danceability' is the 8th column
        if danceability < 0:
            invalid_values += 1
    except ValueError:
        pass
print("\nInvalid values in 'Danceability' column:", invalid_values)

# Calculate statistical measures
danceabilities = []
for row in data[1:]:  # Skip header row
    try:
        danceability = float(row[7])  # Assuming 'Danceability' is the 8th column
        danceabilities.append(danceability)
    except ValueError:
        pass
mean_danceability = sum(danceabilities) / len(danceabilities) if danceabilities else 0
std_dev_danceability = (sum((x - mean_danceability) ** 2 for x in danceabilities) / len(danceabilities)) ** 0.5 if danceabilities else 0
print("\nStatistical measures:")
print("Mean danceability:", mean_danceability)
print("Standard deviation of danceability:", std_dev_danceability)
