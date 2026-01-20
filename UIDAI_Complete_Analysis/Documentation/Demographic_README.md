# Aadhar Demographic Data Analysis

This folder contains all demographic-related data processing scripts and CSV files.

## Files Structure

### Python Scripts
- `demographic_clean_names.py` - Standardize state and district names
- `demographic_merge.py` - Merge demographic CSV files
- `demographic_transformation.py` - Data transformation and aggregation
- `demographic_aggregate_by_district.py` - District-level aggregation
- `demographic_aggregate_by_state.py` - State-level aggregation
- `demographic_visualization.py` - Generates visualization charts (sorted highest to lowest)

### CSV Data Files
- `api_data_aadhar_demographic/` - Directory containing raw demographic CSV files
- `api_data_aadhar_demographic_merged.csv` - Merged demographic data
- `api_data_aadhar_demographic_aggregated.csv` - Pincode-level aggregation
- `api_data_aadhar_demographic_district_aggregated.csv` - District-level aggregation
- `api_data_aadhar_demographic_state_aggregated.csv` - State-level aggregation

### Chart Outputs (PNG Images)
- `01_demographic_grouped_by_age.png` - Grouped bar chart by age groups
- `02_demographic_stacked_by_age.png` - Stacked bar chart by age groups
- `03_demographic_total_by_state.png` - Total demographics sorted highest to lowest

## Execution Order

To process the demographic data, run scripts in this order:

```bash
python demographic_merge.py
python demographic_transformation.py
python demographic_clean_names.py
python demographic_aggregate_by_district.py
python demographic_aggregate_by_state.py
python demographic_visualization.py
```

## Data Summary

- **Total Demographics**: 447,354
- **Age Groups**:
  - 5-17: 43,124
  - 17+: 404,230

## Key States (by demographic count)

1. Uttar Pradesh - 86,215
2. Maharashtra - 46,650
3. Bihar - 43,964
4. Rajasthan - 29,789
5. Madhya Pradesh - 29,123
