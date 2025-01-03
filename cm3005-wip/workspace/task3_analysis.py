import pandas as pd

# Read CSV files
data1 = pd.read_csv('data/raw/dataset1.csv')
data2 = pd.read_csv('data/raw/dataset2.csv')

# Read specific CSV files from 'data/raw' folder
# ...

# Save results to a new CSV file
results = data1.merge(data2, how='inner', on='common_column')
results.to_csv('task3_results.csv', index=False)
