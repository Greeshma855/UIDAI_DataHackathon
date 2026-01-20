import pandas as pd
import os

# Merge demographic CSV files
demographic_dir = 'api_data_aadhar_demographic'
csv_files = sorted([f for f in os.listdir(demographic_dir) if f.endswith('.csv')])

print(f"Found {len(csv_files)} demographic CSV files")

# Read and concatenate all files
dfs = []
for file in csv_files:
    file_path = os.path.join(demographic_dir, file)
    print(f"Reading {file}...")
    df = pd.read_csv(file_path)
    dfs.append(df)

# Merge all dataframes
merged_df = pd.concat(dfs, ignore_index=True)

# Save merged file
merged_df.to_csv('api_data_aadhar_demographic_merged.csv', index=False)

print(f"\nMerged successfully!")
print(f"Total rows: {len(merged_df)}")
print(f"Columns: {list(merged_df.columns)}")
print(f"\nFirst few rows:")
print(merged_df.head())
