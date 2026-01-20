import pandas as pd

# Load the cleaned aggregated CSV file
df = pd.read_csv('api_data_aadhar_enrolment_aggregated.csv')

# Group by state and sum the age columns and total
state_aggregated = df.groupby('state', as_index=False).agg({
    'age_0_5': 'sum',
    'age_5_17': 'sum',
    'age_18_greater': 'sum',
    'total': 'sum'
}).astype({'age_0_5': 'int', 'age_5_17': 'int', 'age_18_greater': 'int', 'total': 'int'})

# Sort by state to maintain order
state_aggregated = state_aggregated.sort_values(by='state').reset_index(drop=True)

# Save to a new CSV file
state_aggregated.to_csv('api_data_aadhar_enrolment_state_aggregated.csv', index=False)

print("Data aggregated by state successfully!")
print(f"Original pincode-level rows: {len(df)}")
print(f"State-level aggregated rows: {len(state_aggregated)}")
print("\nFirst few rows of state-level aggregated data:")
print(state_aggregated.head(10))
