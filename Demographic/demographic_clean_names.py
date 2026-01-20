import pandas as pd

# Load the aggregated demographic CSV file
df = pd.read_csv('api_data_aadhar_demographic_aggregated.csv')

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
    'Khorda': 'Khordha',
    'NUAPADA': 'Nuapada',
    'Sundargarh': 'Sundergarh',
    'S.A.S Nagar(Mohali)': 'SAS Nagar (Mohali)',
    'Jhunjhunun': 'Jhunjhunu',
    'Tirupattur': 'Tirupathur',
    'Bulandshahr': 'Bulandshahar',
    'Kushi Nagar': 'Kushinagar',
    'Siddharth Nagar': 'Siddharthnagar',
    'Hardwar': 'Haridwar',
    'Darjiling': 'Darjeeling',
    'Hooghiy': 'Hooghly',
    'HOOGHLY': 'Hooghly',
    'HOWRAH': 'Howrah',
    'KOLKATA': 'Kolkata',
    'MALDA': 'Malda',
    'Purulia': 'Puruliya'
}

# Apply state replacements
df['state'] = df['state'].replace(state_replacements)

# Apply district replacements
df['district'] = df['district'].replace(district_replacements)

# Save to the same file
df.to_csv('api_data_aadhar_demographic_aggregated.csv', index=False)

print("Demographic state and district names standardized successfully!")
print(f"Total rows: {len(df)}")
print("\nCleaning complete!")
