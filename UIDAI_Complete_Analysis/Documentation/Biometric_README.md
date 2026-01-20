# Aadhar Biometric Data Analysis

This folder contains all biometric-related data processing scripts and CSV files.

## Files Structure

### Python Scripts
- `biometric_merge.py` - Merge biometric CSV files
- `biometric_transformation.py` - Data transformation and aggregation
- `biometric_clean_names.py` - Standardize state and district names
- `biometric_aggregate_by_district.py` - District-level aggregation
- `biometric_aggregate_by_state.py` - State-level aggregation
- `biometric_visualization.py` - Generates visualization charts (sorted highest to lowest)

### CSV Data Files
- `api_data_aadhar_biometric/` - Directory containing raw biometric CSV files
- `api_data_aadhar_biometric_merged.csv` - Merged biometric data
- `api_data_aadhar_biometric_aggregated.csv` - Pincode-level aggregation
- `api_data_aadhar_biometric_district_aggregated.csv` - District-level aggregation
- `api_data_aadhar_biometric_state_aggregated.csv` - State-level aggregation

### Chart Outputs (PNG Images)
- `01_biometric_grouped_by_age.png` - Grouped bar chart by age groups
- `02_biometric_stacked_by_age.png` - Stacked bar chart by age groups
- `03_biometric_total_by_state.png` - Total biometric sorted highest to lowest

## Execution Order

To process the biometric data, run scripts in this order:

```bash
python biometric_merge.py
python biometric_transformation.py
python biometric_clean_names.py
python biometric_aggregate_by_district.py
python biometric_aggregate_by_state.py
python biometric_visualization.py
```

## Data Summary

- **Total Biometric**: 712,783
- **Age Groups**:
  - 5-17: 350,775
  - 17+: 362,008

## Key States (by biometric count)

1. Uttar Pradesh - 102,654
2. Maharashtra - 94,695
3. Madhya Pradesh - 64,422
4. Tamil Nadu - 52,616
5. Bihar - 50,950
