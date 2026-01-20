import pandas as pd

# Load the cleaned aggregated biometric CSV file
df = pd.read_csv('api_data_aadhar_biometric_aggregated.csv')

# Group by state and sum the biometric columns and total
state_aggregated = df.groupby('state', as_index=False).agg({
    'bio_age_5_17': 'sum',
    'bio_age_17_': 'sum',
    'total': 'sum'
}).astype({'bio_age_5_17': 'int', 'bio_age_17_': 'int', 'total': 'int'})

# Sort by state to maintain order
state_aggregated = state_aggregated.sort_values(by='state').reset_index(drop=True)

# Save to a new CSV file
state_aggregated.to_csv('api_data_aadhar_biometric_state_aggregated.csv', index=False)

print("Biometric data aggregated by state successfully!")
print(f"Original pincode-level rows: {len(df)}")
print(f"State-level aggregated rows: {len(state_aggregated)}")
print("\nFirst few rows of state-level aggregated data:")
print(state_aggregated.head(10))
