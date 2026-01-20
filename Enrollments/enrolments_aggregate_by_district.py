import pandas as pd

# Load the cleaned aggregated CSV file
df = pd.read_csv('api_data_aadhar_enrolment_aggregated.csv')

# Group by state and district and sum the age columns and total
district_aggregated = df.groupby(['state', 'district'], as_index=False).agg({
    'age_0_5': 'sum',
    'age_5_17': 'sum',
    'age_18_greater': 'sum',
    'total': 'sum'
}).astype({'age_0_5': 'int', 'age_5_17': 'int', 'age_18_greater': 'int', 'total': 'int'})

# Sort by state and district to maintain order
district_aggregated = district_aggregated.sort_values(by=['state', 'district']).reset_index(drop=True)

# Save to a new CSV file
district_aggregated.to_csv('api_data_aadhar_enrolment_district_aggregated.csv', index=False)

print("Data aggregated by district successfully!")
print(f"Original pincode-level rows: {len(df)}")
print(f"District-level aggregated rows: {len(district_aggregated)}")
print("\nFirst few rows of district-level aggregated data:")
print(district_aggregated.head(10))
