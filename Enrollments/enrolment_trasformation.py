import pandas as pd

# Load the merged CSV file
df = pd.read_csv('api_data_aadhar_enrolment_merged.csv')

# Group by pincode and calculate mean for age columns, keeping state and district
aggregated_df = df.groupby('pincode').agg({
    'state': 'first',
    'district': 'first',
    'age_0_5': 'mean',
    'age_5_17': 'mean',
    'age_18_greater': 'mean'
}).reset_index()

# Round the averaged values to integers
aggregated_df['age_0_5'] = aggregated_df['age_0_5'].round().astype(int)
aggregated_df['age_5_17'] = aggregated_df['age_5_17'].round().astype(int)
aggregated_df['age_18_greater'] = aggregated_df['age_18_greater'].round().astype(int)

# Add a total column that sums the averaged columns
aggregated_df['total'] = aggregated_df['age_0_5'] + aggregated_df['age_5_17'] + aggregated_df['age_18_greater']

# Reorder columns
aggregated_df = aggregated_df[['state', 'district', 'pincode', 'age_0_5', 'age_5_17', 'age_18_greater', 'total']]

# Sort by state, district, and pincode
aggregated_df = aggregated_df.sort_values(by=['state', 'district', 'pincode']).reset_index(drop=True)

# Save to a new CSV file
aggregated_df.to_csv('api_data_aadhar_enrolment_aggregated.csv', index=False)

print("Data aggregated successfully!")
print(f"Original rows: {len(df)}")
print(f"Aggregated rows: {len(aggregated_df)}")
print("\nFirst few rows of aggregated data:")
print(aggregated_df.head(10))
