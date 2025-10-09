"""
Energy Efficient Television Analysis
Creates 6 visualizations from TV energy consumption dataset
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for better-looking charts
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Load the dataset
print("Loading dataset...")
df = pd.read_excel('Book1.csv.xlsx')

# Display basic info about the dataset
print("\nDataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())
print("\nFirst few rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)
print("\nBasic statistics:")
print(df.describe())

# Create output directory for charts
import os
if not os.path.exists('charts'):
    os.makedirs('charts')

# ============================================================================
# CHART 1: Scatter Plot - Screen Size vs Power Consumption
# ============================================================================
print("\n[1/6] Creating Chart 1: Screen Size vs Power Consumption...")

plt.figure(figsize=(12, 7))
if 'Screen_Tech' in df.columns:
    technologies = df['Screen_Tech'].unique()
    for tech in technologies:
        mask = df['Screen_Tech'] == tech
        plt.scatter(df[mask]['screensize'], df[mask]['Avg_mode_power'], 
                   label=tech, alpha=0.6, s=100, edgecolors='black', linewidth=0.5)
else:
    plt.scatter(df['screensize'], df['Avg_mode_power'], 
               alpha=0.6, s=100, edgecolors='black', linewidth=0.5)

plt.xlabel('Screen Size (inches)', fontsize=12, fontweight='bold')
plt.ylabel('Average Mode Power (Watts)', fontsize=12, fontweight='bold')
plt.title('TV Screen Size vs Energy Consumption\n"As screen size increases, energy consumption tends to rise"', 
          fontsize=14, fontweight='bold', pad=20)
plt.legend(title='Screen Technology', loc='upper left', framealpha=0.9)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('charts/chart1_screensize_vs_power.png', dpi=300, bbox_inches='tight')
plt.close()
print("[OK] Chart 1 saved: charts/chart1_screensize_vs_power.png")

# ============================================================================
# CHART 2: Box Plot - Screen Technology vs Power Consumption
# ============================================================================
print("\n[2/6] Creating Chart 2: Screen Technology vs Power Consumption...")

plt.figure(figsize=(12, 7))
if 'Screen_Tech' in df.columns:
    # Create box plot
    box_data = [df[df['Screen_Tech'] == tech]['Avg_mode_power'].dropna() 
                for tech in df['Screen_Tech'].unique()]
    bp = plt.boxplot(box_data, labels=df['Screen_Tech'].unique(), 
                     patch_artist=True, showmeans=True)
    
    # Color the boxes
    colors = sns.color_palette("husl", len(bp['boxes']))
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    # Overlay average Star2 if available
    if 'Star2' in df.columns:
        avg_stars = df.groupby('Screen_Tech')['Star2'].mean()
        ax2 = plt.twinx()
        ax2.plot(range(1, len(avg_stars)+1), avg_stars.values, 
                'ro-', linewidth=2, markersize=10, label='Avg Star Rating')
        ax2.set_ylabel('Average Star Rating', fontsize=12, fontweight='bold', color='red')
        ax2.tick_params(axis='y', labelcolor='red')
        ax2.legend(loc='upper right')

plt.xlabel('Screen Technology', fontsize=12, fontweight='bold')
plt.ylabel('Average Mode Power (Watts)', fontsize=12, fontweight='bold')
plt.title('Screen Technology Impact on Energy Consumption\n"Screen technology is a major determinant of efficiency"', 
          fontsize=14, fontweight='bold', pad=20)
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('charts/chart2_technology_vs_power.png', dpi=300, bbox_inches='tight')
plt.close()
print("[OK] Chart 2 saved: charts/chart2_technology_vs_power.png")

# ============================================================================
# CHART 3: Scatter Plot with Regression - Star Ratings vs Power Consumption
# ============================================================================
print("\n[3/6] Creating Chart 3: Star Ratings vs Power Consumption...")

plt.figure(figsize=(12, 7))
if 'Star2' in df.columns:
    # Remove NaN values for correlation
    valid_data = df[['Star2', 'Avg_mode_power']].dropna()
    
    plt.scatter(valid_data['Star2'], valid_data['Avg_mode_power'], 
               alpha=0.5, s=100, edgecolors='black', linewidth=0.5)
    
    # Add regression line
    z = np.polyfit(valid_data['Star2'], valid_data['Avg_mode_power'], 1)
    p = np.poly1d(z)
    x_line = np.linspace(valid_data['Star2'].min(), valid_data['Star2'].max(), 100)
    plt.plot(x_line, p(x_line), "r--", linewidth=3, label=f'Trend: y={z[0]:.2f}x+{z[1]:.2f}')
    
    # Calculate correlation
    correlation = valid_data['Star2'].corr(valid_data['Avg_mode_power'])
    plt.text(0.05, 0.95, f'Correlation: {correlation:.3f}', 
            transform=plt.gca().transAxes, fontsize=12, 
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.xlabel('Energy Star Rating', fontsize=12, fontweight='bold')
plt.ylabel('Average Mode Power (Watts)', fontsize=12, fontweight='bold')
plt.title('Star Rating Validity Check\n"Higher ratings align with lower consumption"', 
          fontsize=14, fontweight='bold', pad=20)
plt.legend(loc='upper right', framealpha=0.9)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('charts/chart3_starrating_vs_power.png', dpi=300, bbox_inches='tight')
plt.close()
print("[OK] Chart 3 saved: charts/chart3_starrating_vs_power.png")

# ============================================================================
# CHART 4: Horizontal Bar Chart - Brand Efficiency Comparison
# ============================================================================
print("\n[4/6] Creating Chart 4: Brand Efficiency Comparison...")

plt.figure(figsize=(12, 10))
if 'Brand_Reg' in df.columns:
    # Calculate average power by brand
    brand_avg = df.groupby('Brand_Reg')['Avg_mode_power'].mean().sort_values()
    
    # Get top 20 brands if there are many
    if len(brand_avg) > 20:
        brand_avg = brand_avg.head(20)
    
    # Create color map based on efficiency (green = efficient, red = inefficient)
    colors = plt.cm.RdYlGn_r(np.linspace(0.2, 0.8, len(brand_avg)))
    
    bars = plt.barh(range(len(brand_avg)), brand_avg.values, color=colors, 
                    edgecolor='black', linewidth=0.5)
    plt.yticks(range(len(brand_avg)), brand_avg.index)
    
    # Add value labels
    for i, (bar, value) in enumerate(zip(bars, brand_avg.values)):
        plt.text(value + 1, i, f'{value:.1f}W', 
                va='center', fontsize=9, fontweight='bold')
    
    # Add average star rating if available
    if 'Star2' in df.columns:
        avg_stars = df.groupby('Brand_Reg')['Star2'].mean()
        for i, brand in enumerate(brand_avg.index):
            if brand in avg_stars.index:
                plt.text(5, i, f'⭐{avg_stars[brand]:.1f}', 
                        va='center', fontsize=8, color='blue')

plt.xlabel('Average Mode Power (Watts)', fontsize=12, fontweight='bold')
plt.ylabel('Brand', fontsize=12, fontweight='bold')
plt.title('Brand Energy Efficiency Ranking (Most Efficient First)\n"Top brands maintain low power across all models"', 
          fontsize=14, fontweight='bold', pad=20)
plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig('charts/chart4_brand_efficiency.png', dpi=300, bbox_inches='tight')
plt.close()
print("[OK] Chart 4 saved: charts/chart4_brand_efficiency.png")

# ============================================================================
# CHART 5: Bubble Chart - Screen Area vs Star Rating
# ============================================================================
print("\n[5/6] Creating Chart 5: Screen Area vs Star Rating (Bubble Chart)...")

plt.figure(figsize=(14, 8))
if 'Screen_Area' in df.columns and 'Star2' in df.columns:
    valid_data = df[['Screen_Area', 'Star2', 'Avg_mode_power', 'Screen_Tech']].dropna()
    
    # Create color map for technologies
    if 'Screen_Tech' in valid_data.columns:
        technologies = valid_data['Screen_Tech'].unique()
        colors_map = dict(zip(technologies, sns.color_palette("husl", len(technologies))))
        colors = [colors_map[tech] for tech in valid_data['Screen_Tech']]
    else:
        colors = 'blue'
    
    # Create bubble chart
    scatter = plt.scatter(valid_data['Screen_Area'], valid_data['Star2'], 
                         s=valid_data['Avg_mode_power']*2,  # Bubble size based on power
                         c=colors, alpha=0.6, edgecolors='black', linewidth=0.5)
    
    # Create legend for technologies
    if 'Screen_Tech' in valid_data.columns:
        for tech, color in colors_map.items():
            plt.scatter([], [], c=[color], s=100, label=tech, alpha=0.6, edgecolors='black')
        plt.legend(title='Screen Technology', loc='lower right', framealpha=0.9)
    
    # Add size legend (for power consumption)
    for power in [50, 100, 150, 200]:
        plt.scatter([], [], c='gray', s=power*2, alpha=0.6, 
                   label=f'{power}W', edgecolors='black')
    plt.legend(title='Power (bubble size)', loc='upper left', framealpha=0.9, ncol=2)

plt.xlabel('Screen Area (sq. inches)', fontsize=12, fontweight='bold')
plt.ylabel('Energy Star Rating', fontsize=12, fontweight='bold')
plt.title('Screen Area vs Efficiency: Technology Impact\n"Even large screens can achieve high efficiency — technology has narrowed the gap"', 
          fontsize=14, fontweight='bold', pad=20)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('charts/chart5_area_vs_stars_bubble.png', dpi=300, bbox_inches='tight')
plt.close()
print("[OK] Chart 5 saved: charts/chart5_area_vs_stars_bubble.png")

# ============================================================================
# CHART 6: Line Chart - Efficiency Trends Over Time
# ============================================================================
print("\n[6/6] Creating Chart 6: Efficiency Trends Over Time...")

plt.figure(figsize=(14, 7))
if 'ExpDate' in df.columns:
    # Convert ExpDate to datetime and extract year
    df['Year'] = pd.to_datetime(df['ExpDate'], errors='coerce').dt.year
    
    # Remove NaN years
    yearly_data = df[df['Year'].notna()].copy()
    
    # Calculate yearly averages
    yearly_power = yearly_data.groupby('Year')['Avg_mode_power'].mean()
    
    # Plot power trend
    ax1 = plt.gca()
    line1 = ax1.plot(yearly_power.index, yearly_power.values, 
                     'b-o', linewidth=3, markersize=8, label='Avg Power Consumption')
    ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Average Mode Power (Watts)', fontsize=12, fontweight='bold', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.grid(True, alpha=0.3)
    
    # Add star rating trend if available
    if 'Star2' in yearly_data.columns:
        yearly_stars = yearly_data.groupby('Year')['Star2'].mean()
        ax2 = ax1.twinx()
        line2 = ax2.plot(yearly_stars.index, yearly_stars.values, 
                        'r-s', linewidth=3, markersize=8, label='Avg Star Rating')
        ax2.set_ylabel('Average Star Rating', fontsize=12, fontweight='bold', color='red')
        ax2.tick_params(axis='y', labelcolor='red')
        
        # Combine legends
        lines = line1 + line2
        labels = [l.get_label() for l in lines]
        ax1.legend(lines, labels, loc='upper left', framealpha=0.9, fontsize=11)
    else:
        ax1.legend(loc='upper left', framealpha=0.9, fontsize=11)

plt.title('Television Efficiency Trends Over Time\n"TV models have improved in efficiency — reflecting successful energy standards"', 
          fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('charts/chart6_efficiency_trends.png', dpi=300, bbox_inches='tight')
plt.close()
print("[OK] Chart 6 saved: charts/chart6_efficiency_trends.png")

print("\n" + "="*60)
print("ALL CHARTS COMPLETED SUCCESSFULLY!")
print("="*60)
print("\nCharts saved in 'charts/' directory:")
print("  1. chart1_screensize_vs_power.png")
print("  2. chart2_technology_vs_power.png")
print("  3. chart3_starrating_vs_power.png")
print("  4. chart4_brand_efficiency.png")
print("  5. chart5_area_vs_stars_bubble.png")
print("  6. chart6_efficiency_trends.png")
print("\n" + "="*60)

