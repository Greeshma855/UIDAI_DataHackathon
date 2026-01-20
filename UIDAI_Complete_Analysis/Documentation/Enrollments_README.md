# Aadhar Enrollment Data Analysis

This folder contains all enrollment-related data processing scripts and CSV files.

## Files Structure

### Python Scripts
- `enrollment_cleaning.py` - Data cleaning and preprocessing
- `enrolment_trasformation.py` - Data transformation and aggregation
- `enrollment_visualization.py` - Generates visualization charts (sorted highest to lowest)

### CSV Data Files
- `api_data_aadhar_enrolment/` - Directory containing raw enrollment CSV files
- `api_data_aadhar_enrolment_merged.csv` - Merged enrollment data
- `api_data_aadhar_enrolment_aggregated.csv` - Pincode-level aggregation
- `api_data_aadhar_enrolment_district_aggregated.csv` - District-level aggregation
- `api_data_aadhar_enrolment_state_aggregated.csv` - State-level aggregation

### Chart Outputs (PNG Images)
- `01_enrollment_grouped_by_age.png` - Grouped bar chart by age groups
- `02_enrollment_stacked_by_age.png` - Stacked bar chart by age groups
- `03_enrollment_total_by_state.png` - Total enrollment sorted highest to lowest

## Execution Order

To process the enrollment data, run scripts in this order:

```bash
python enrollment_cleaning.py
python enrolment_trasformation.py
python enrollment_visualization.py
```

## Data Summary

- **Total Enrollments**: 77,382
- **Age Groups**: 
  - 0-5: 53,227
  - 5-17: 22,443
  - 18+: 1,712

## Key States (by enrollment count)

1. Uttar Pradesh - 13,569
2. Bihar - 7,977
3. Madhya Pradesh - 6,773
4. Maharashtra - 5,366
5. Rajasthan - 5,288
