import pandas as pd

# Load the merged demographic CSV file
df = pd.read_csv('api_data_aadhar_demographic_merged.csv')

# Group by pincode and calculate mean for demographic age columns
aggregated_df = df.groupby('pincode').agg({
    'state': 'first',
    'district': 'first',
    'demo_age_5_17': 'mean',
    'demo_age_17_': 'mean'
}).reset_index()

# Round the averaged values to integers
aggregated_df['demo_age_5_17'] = aggregated_df['demo_age_5_17'].round().astype(int)
aggregated_df['demo_age_17_'] = aggregated_df['demo_age_17_'].round().astype(int)

# Add a total column that sums the averaged columns
aggregated_df['total'] = aggregated_df['demo_age_5_17'] + aggregated_df['demo_age_17_']

# Reorder columns
aggregated_df = aggregated_df[['state', 'district', 'pincode', 'demo_age_5_17', 'demo_age_17_', 'total']]

# Sort by state, district, and pincode
aggregated_df = aggregated_df.sort_values(by=['state', 'district', 'pincode']).reset_index(drop=True)

# Save to a new CSV file
aggregated_df.to_csv('api_data_aadhar_demographic_aggregated.csv', index=False)

print("Demographic data aggregated successfully!")
print(f"Original rows: {len(df)}")
print(f"Aggregated rows: {len(aggregated_df)}")
print("\nFirst few rows of aggregated data:")
print(aggregated_df.head(10))
