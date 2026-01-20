import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the three state-aggregated CSV files
demographic_df = pd.read_csv('api_data_aadhar_demographic_state_aggregated.csv')
biometric_df = pd.read_csv('api_data_aadhar_biometric_state_aggregated.csv')
enrollment_df = pd.read_csv('api_data_aadhar_enrolment_state_aggregated.csv')

# Rename columns to distinguish them
demographic_df = demographic_df.rename(columns={'total': 'demographic_total'})
biometric_df = biometric_df.rename(columns={'total': 'biometric_total'})
enrollment_df = enrollment_df.rename(columns={'total': 'enrollment_total'})

# Merge all three dataframes by state
merged_df = demographic_df[['state', 'demographic_total']].merge(
    biometric_df[['state', 'biometric_total']], 
    on='state', 
    how='outer'
).merge(
    enrollment_df[['state', 'enrollment_total']], 
    on='state', 
    how='outer'
)

# Fill NaN values with 0
merged_df = merged_df.fillna(0)

# Calculate total updates (demographic + biometric)
merged_df['total_updates'] = merged_df['demographic_total'] + merged_df['biometric_total']

# Calculate Update Load Ratio
# Handle division by zero by replacing with 0
merged_df['update_load_ratio'] = merged_df.apply(
    lambda row: row['total_updates'] / row['enrollment_total'] if row['enrollment_total'] > 0 else 0,
    axis=1
)

# Sort by update load ratio in descending order
merged_df = merged_df.sort_values('update_load_ratio', ascending=False).reset_index(drop=True)

# Save the results
merged_df.to_csv('update_load_ratio_analysis.csv', index=False)

print("="*80)
print("UPDATE LOAD RATIO ANALYSIS")
print("="*80)
print("\nFormula: (Demographic Updates + Biometric Updates) / Enrollments")
print("\n" + merged_df.to_string(index=False))

# Calculate overall statistics
total_demographic = merged_df['demographic_total'].sum()
total_biometric = merged_df['biometric_total'].sum()
total_updates = merged_df['total_updates'].sum()
total_enrollment = merged_df['enrollment_total'].sum()
overall_ratio = total_updates / total_enrollment if total_enrollment > 0 else 0

print("\n" + "="*80)
print("OVERALL STATISTICS")
print("="*80)
print(f"Total Demographic Updates: {total_demographic:,.0f}")
print(f"Total Biometric Updates: {total_biometric:,.0f}")
print(f"Total Updates: {total_updates:,.0f}")
print(f"Total Enrollments: {total_enrollment:,.0f}")
print(f"Overall Update Load Ratio: {overall_ratio:.4f}")
print(f"\nInterpretation: For every 1 enrollment, there are {overall_ratio:.4f} updates on average")

# Create individual chart visualizations
states = merged_df['state']

# Chart 1: Bar chart of Update Load Ratio by state
fig1, ax1 = plt.subplots(figsize=(18, 8))
ratios = merged_df['update_load_ratio']
colors = plt.cm.RdYlGn_r(ratios / ratios.max())
bars = ax1.bar(states, ratios, color=colors, edgecolor='black', linewidth=0.5)
ax1.set_xlabel('State', fontsize=12, fontweight='bold')
ax1.set_ylabel('Update Load Ratio', fontsize=12, fontweight='bold')
ax1.set_title('Update Load Ratio by State\n(Demographic + Biometric Updates) / Enrollments', fontsize=14, fontweight='bold')
ax1.set_xticklabels(states, rotation=90, fontsize=9)
ax1.axhline(y=overall_ratio, color='red', linestyle='--', linewidth=2, label=f'Overall Ratio: {overall_ratio:.4f}')
ax1.legend(fontsize=10)
ax1.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('01_update_load_ratio_by_state.png', dpi=300, bbox_inches='tight')
print("\n✓ Chart 1 saved as '01_update_load_ratio_by_state.png'")
plt.close()

# Chart 2: Bar chart comparing Updates vs Enrollments
fig2, ax2 = plt.subplots(figsize=(10, 8))
categories = ['Total Updates', 'Total Enrollments']
values = [total_updates, total_enrollment]
colors_comp = ['#FF6B6B', '#4ECDC4']
bars = ax2.bar(categories, values, color=colors_comp, edgecolor='black', linewidth=2)
ax2.set_ylabel('Count', fontsize=12, fontweight='bold')
ax2.set_title('Total Updates vs Total Enrollments', fontsize=14, fontweight='bold')
ax2.grid(axis='y', alpha=0.3)
# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height):,.0f}',
            ha='center', va='bottom', fontweight='bold', fontsize=12)
plt.tight_layout()
plt.savefig('02_updates_vs_enrollments.png', dpi=300, bbox_inches='tight')
print("✓ Chart 2 saved as '02_updates_vs_enrollments.png'")
plt.close()

# Chart 3: Pie chart of Demographic vs Biometric Updates
fig3, ax3 = plt.subplots(figsize=(10, 8))
sizes_updates = [total_demographic, total_biometric]
labels_updates = [f'Demographic\n{total_demographic:,.0f}', f'Biometric\n{total_biometric:,.0f}']
colors_updates = ['#FF6B6B', '#45B7D1']
wedges, texts, autotexts = ax3.pie(sizes_updates, labels=labels_updates, colors=colors_updates, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 11})
ax3.set_title('Demographic vs Biometric Updates', fontsize=14, fontweight='bold')
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(12)
plt.tight_layout()
plt.savefig('03_demographic_vs_biometric_updates.png', dpi=300, bbox_inches='tight')
print("✓ Chart 3 saved as '03_demographic_vs_biometric_updates.png'")
plt.close()

# Chart 4: Stacked bar chart - Updates composition by state (sorted by update load ratio)
fig4, ax4 = plt.subplots(figsize=(18, 8))
x = np.arange(len(states))
width = 0.6
bars1 = ax4.bar(x, merged_df['demographic_total'], width, label='Demographic Updates', color='#FF6B6B')
bars2 = ax4.bar(x, merged_df['biometric_total'], width, bottom=merged_df['demographic_total'], 
                label='Biometric Updates', color='#45B7D1')
ax4.set_xlabel('State', fontsize=12, fontweight='bold')
ax4.set_ylabel('Number of Updates', fontsize=12, fontweight='bold')
ax4.set_title('Update Composition by State - Sorted by Update Load Ratio (Highest to Lowest)', fontsize=14, fontweight='bold')
ax4.set_xticks(x)
ax4.set_xticklabels(states, rotation=90, fontsize=9)
ax4.legend(fontsize=10)
ax4.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('04_update_composition_by_state.png', dpi=300, bbox_inches='tight')
print("✓ Chart 4 saved as '04_update_composition_by_state.png'")
plt.close()

print("\n" + "="*80)
print("All charts have been saved successfully!")
print("="*80)
print("\n" + "="*80)
print("TOP 10 STATES WITH HIGHEST UPDATE LOAD RATIO")
print("="*80)
top_10 = merged_df.head(10)[['state', 'demographic_total', 'biometric_total', 'enrollment_total', 'update_load_ratio']]
for idx, row in top_10.iterrows():
    print(f"{idx+1}. {row['state']}: {row['update_load_ratio']:.4f} (Demo: {row['demographic_total']:.0f}, Bio: {row['biometric_total']:.0f}, Enrollments: {row['enrollment_total']:.0f})")

print("\n" + "="*80)
print("BOTTOM 10 STATES WITH LOWEST UPDATE LOAD RATIO")
print("="*80)
bottom_10 = merged_df.tail(10)[['state', 'demographic_total', 'biometric_total', 'enrollment_total', 'update_load_ratio']]
for idx, (orig_idx, row) in enumerate(bottom_10.iterrows()):
    print(f"{idx+1}. {row['state']}: {row['update_load_ratio']:.4f} (Demo: {row['demographic_total']:.0f}, Bio: {row['biometric_total']:.0f}, Enrollments: {row['enrollment_total']:.0f})")
