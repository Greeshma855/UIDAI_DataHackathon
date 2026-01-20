import pandas as pd

# Load the aggregated biometric CSV file
df = pd.read_csv('api_data_aadhar_biometric_aggregated.csv')

# Define state replacements
state_replacements = {
    'Andaman & Nicobar Islands': 'Andaman and Nicobar Islands',
    'Dadra & Nagar Haveli': 'Dadra and Nagar Haveli',
    'Jammu & Kashmir': 'Jammu and Kashmir',
    'Jammu And Kashmir': 'Jammu and Kashmir',
    'ODISHA': 'Odisha',
    'Orissa': 'Odisha',
    'WEST BENGAL': 'West Bengal',
    'West  Bengal': 'West Bengal',  # with extra space
    'West Bangal': 'West Bengal',
    'Puducherry': 'Pondicherry',
    'Dadra and Nagar Haveli and Daman and Diu': 'Dadra and Nagar Haveli'
}

# Define district replacements
district_replacements = {
    'Nicobars': 'Nicobar',
    'Anantapur': 'Ananthapur',
    'K.v. Rangareddy': 'K.V.Rangareddy',
    'Karim Nagar': 'Karimnagar',
    'Mahabub Nagar': 'Mahbubnagar',
    'Janjgir - Champa': 'Janjgir Champa',
    'Janjgir-champa': 'Janjgir Champa',
    'Ahmadabad': 'Ahmedabad',
    'Panch Mahals': 'Panchmahals',
    'Sabar Kantha': 'Sabarkantha',
    'Lahaul and Spiti': 'Lahul and Spiti',
    'Lahul & Spiti': 'Lahul and Spiti',
    'Bandipore': 'Bandipur',
    'Rajauri': 'Rajouri',
    'Garhwa *': 'Garhwa',
    'Hazaribag': 'Hazaribagh',
    'Pakaur': 'Pakur',
    'Palamau': 'Palamu',
    'Bellary': 'Ballari',
    'Bengaluru': 'Bangalore',
    'Bengaluru Rural': 'Bangalore Rural',
    'Chamarajanagar': 'Chamrajanagar',
    'Davangere': 'Davanagere',
    'Mysore': 'Mysuru',
    'Harda *': 'Harda',
    'Buldana': 'Buldhana',
    'Gondiya': 'Gondia',
    'ANGUL': 'Angul',
    'Baleswar': 'Baleshwar',
    'Baudh': 'Boudh',
}

# Replace state names
df['state'] = df['state'].replace(state_replacements)

# Replace district names
df['district'] = df['district'].replace(district_replacements)

# Save to a new CSV file
df.to_csv('api_data_aadhar_biometric_aggregated.csv', index=False)

print("Biometric data cleaned successfully!")
print(f"Total rows: {len(df)}")
print("\nFirst few rows of cleaned data:")
print(df.head(10))
