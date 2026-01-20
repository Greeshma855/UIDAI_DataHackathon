import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
df = pd.read_csv('api_data_aadhar_demographic_state_aggregated.csv')

# Sort by total from highest to lowest
df = df.sort_values('total', ascending=False).reset_index(drop=True)

# Print summary statistics
print("\n" + "="*60)
print("DEMOGRAPHIC SUMMARY BY STATE (SORTED BY TOTAL)")
print("="*60)
print(df.to_string(index=False))
print("\n" + "="*60)
print("SUMMARY STATISTICS")
print("="*60)
print(f"Total Demographics (All States): {df['total'].sum()}")
print(f"Age 5-17: {df['demo_age_5_17'].sum()}")
print(f"Age 17+: {df['demo_age_17_'].sum()}")
print(f"\nState with highest demographics: {df.loc[df['total'].idxmax(), 'state']} ({df['total'].max()})")
print(f"State with lowest demographics: {df.loc[df['total'].idxmin(), 'state']} ({df['total'].min()})")

states = df['state']

# Chart 1: Grouped bar chart for age-wise demographic by state
fig1, ax1 = plt.subplots(figsize=(18, 8))
x = np.arange(len(states))
width = 0.35

bars1 = ax1.bar(x - width/2, df['demo_age_5_17'], width, label='demo_age_5_17', color='#FF6B6B')
bars2 = ax1.bar(x + width/2, df['demo_age_17_'], width, label='demo_age_17_', color='#4ECDC4')

ax1.set_xlabel('State', fontsize=12, fontweight='bold')
ax1.set_ylabel('Demographic Count', fontsize=12, fontweight='bold')
ax1.set_title('Aadhar Demographics by State and Age Group (Grouped Bar Chart - Sorted by Total)', fontsize=14, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(states, rotation=90, fontsize=9)
ax1.legend(fontsize=10)
ax1.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('01_demographic_grouped_by_age.png', dpi=300, bbox_inches='tight')
print("\n✓ Chart 1 saved as '01_demographic_grouped_by_age.png'")
plt.close()

# Chart 2: Stacked bar chart for total demographics with age breakdown
fig2, ax2 = plt.subplots(figsize=(18, 8))
bars_5_17 = ax2.bar(states, df['demo_age_5_17'], label='demo_age_5_17', color='#FF6B6B')
bars_17_g = ax2.bar(states, df['demo_age_17_'], 
                     bottom=df['demo_age_5_17'], 
                     label='demo_age_17_', color='#4ECDC4')

ax2.set_xlabel('State', fontsize=12, fontweight='bold')
ax2.set_ylabel('Demographic Count', fontsize=12, fontweight='bold')
ax2.set_title('Aadhar Demographics by State (Stacked Bar Chart - Sorted by Total)', fontsize=14, fontweight='bold')
ax2.set_xticklabels(states, rotation=90, fontsize=9)
ax2.legend(fontsize=10)
ax2.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('02_demographic_stacked_by_age.png', dpi=300, bbox_inches='tight')
print("✓ Chart 2 saved as '02_demographic_stacked_by_age.png'")
plt.close()

# Chart 3: Total demographics by state (simple bar chart)
fig3, ax3 = plt.subplots(figsize=(18, 8))
colors = plt.cm.viridis(np.linspace(0, 1, len(states)))
bars = ax3.bar(states, df['total'], color=colors, edgecolor='black', linewidth=0.5)
ax3.set_xlabel('State', fontsize=12, fontweight='bold')
ax3.set_ylabel('Total Demographic Count', fontsize=12, fontweight='bold')
ax3.set_title('Total Aadhar Demographics by State (Sorted Highest to Lowest)', fontsize=14, fontweight='bold')
ax3.set_xticklabels(states, rotation=90, fontsize=9)
ax3.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.savefig('03_demographic_total_by_state.png', dpi=300, bbox_inches='tight')
print("✓ Chart 3 saved as '03_demographic_total_by_state.png'")
plt.close()

print("\n" + "="*60)
print("All demographic charts saved successfully!")
print("="*60)
