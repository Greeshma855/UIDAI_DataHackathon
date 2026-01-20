import pandas as pd

# Load the cleaned aggregated biometric CSV file
df = pd.read_csv('api_data_aadhar_biometric_aggregated.csv')

# Group by state and district and sum the biometric columns and total
district_aggregated = df.groupby(['state', 'district'], as_index=False).agg({
    'bio_age_5_17': 'sum',
    'bio_age_17_': 'sum',
    'total': 'sum'
}).astype({'bio_age_5_17': 'int', 'bio_age_17_': 'int', 'total': 'int'})

# Sort by state and district to maintain order
district_aggregated = district_aggregated.sort_values(by=['state', 'district']).reset_index(drop=True)

# Save to a new CSV file
district_aggregated.to_csv('api_data_aadhar_biometric_district_aggregated.csv', index=False)

print("Biometric data aggregated by district successfully!")
print(f"Original pincode-level rows: {len(df)}")
print(f"District-level aggregated rows: {len(district_aggregated)}")
print("\nFirst few rows of district-level aggregated data:")
print(district_aggregated.head(10))
