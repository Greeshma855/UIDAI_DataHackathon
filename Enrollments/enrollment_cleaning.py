import pandas as pd
import os

# Define the directory path
data_dir = "api_data_aadhar_enrolment"

# List of CSV files to merge
csv_files = [
    "api_data_aadhar_enrolment_0_500000.csv",
    "api_data_aadhar_enrolment_500000_1000000.csv",
    "api_data_aadhar_enrolment_1000000_1006029.csv"
]

# Read and merge all CSV files
dfs = []
for file in csv_files:
    file_path = os.path.join(data_dir, file)
    print(f"Loading {file}...")
    df_temp = pd.read_csv(file_path)
    dfs.append(df_temp)
    print(f"  Rows: {len(df_temp)}")

# Concatenate all dataframes
df = pd.concat(dfs, ignore_index=True)
print(f"\nTotal rows after merge: {len(df)}")

# Convert date column to datetime format for proper sorting (year, month, day)
df["date"] = pd.to_datetime(
    df["date"],
    format="%d-%m-%Y",
    errors="coerce"
)
print("Date column converted to datetime format")

# Sort by state, district, pincode, and then date
sort_columns = ["state", "district", "pincode", "date"]
# Filter to only columns that exist in the dataframe
sort_columns = [col for col in sort_columns if col in df.columns]
print(f"Sorting by: {sort_columns}")
df = df.sort_values(by=sort_columns, na_position='last')
df = df.reset_index(drop=True)

# Save merged dataset
output_file = "api_data_aadhar_enrolment_merged.csv"
df.to_csv(output_file, index=False, date_format='%Y-%m-%d')
print(f"Merged dataset saved to {output_file}")


# Ensure numeric columns
age_cols = ["age_0_5", "age_5_17", "age_18_greater"]
df[age_cols] = df[age_cols].apply(pd.to_numeric, errors="coerce").fillna(0)
