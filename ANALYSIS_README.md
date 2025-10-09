# TV Energy Efficiency Data Analysis

## 📊 Overview

This project contains a comprehensive data analysis of **4,352 television models** registered in Australia, examining energy efficiency patterns, technology comparisons, and trends over time.

## 📁 Files Created

### HTML Pages
- **`analysis.html`** - Main data analysis page with all 6 visualizations and insights
- **`index.html`** - Home page (updated with navigation to Data Analysis)
- **`televisions.html`** - Televisions information page (updated navigation)
- **`aboutus.html`** - About Us page (updated navigation)

### Charts (in `charts/` directory)
1. **`chart1_screensize_vs_power.png`** - Screen Size vs Power Consumption (Scatter Plot)
2. **`chart2_technology_vs_power.png`** - Screen Technology vs Power (Box Plot)
3. **`chart3_starrating_vs_power.png`** - Star Rating vs Power (Scatter with Regression)
4. **`chart4_brand_efficiency.png`** - Brand Efficiency Ranking (Horizontal Bar Chart)
5. **`chart5_area_vs_stars_bubble.png`** - Screen Area vs Star Rating (Bubble Chart)
6. **`chart6_efficiency_trends.png`** - Efficiency Trends Over Time (Line Chart)

### Python Script
- **`create_charts.py`** - Script to generate all visualizations from the dataset

## 📈 Six Key Questions Answered

### 1️⃣ **Are modern TVs becoming less energy-efficient as they get larger?**
- **Variables:** Screen size (x) vs Average mode power (y), colored by technology
- **Finding:** Positive correlation exists, but modern technologies (OLED/LED) show improved efficiency even at larger sizes

### 2️⃣ **How does screen technology affect energy consumption?**
- **Variables:** Screen technology (x) vs Average mode power (y)
- **Finding:** OLED and LED TVs consistently consume less power than Plasma or older LCD models

### 3️⃣ **Do higher star ratings correspond to lower energy use?**
- **Variables:** Star rating (x) vs Average mode power (y)
- **Finding:** Strong negative correlation confirms the Energy Star rating system is valid and reliable

### 4️⃣ **Which brands lead in energy efficiency?**
- **Variables:** Brand (y) vs Average mode power (x)
- **Finding:** Significant brand differences exist; top performers maintain low power across all models

### 5️⃣ **Does larger screen area still mean lower efficiency?**
- **Variables:** Screen area (x), Star rating (y), bubble size = power, color = technology
- **Finding:** Technology has narrowed the gap; large screens can now achieve high efficiency ratings

### 6️⃣ **Are newer TV models becoming more efficient over time?**
- **Variables:** Year (x) vs Average mode power and Star rating (y)
- **Finding:** Clear upward trend in efficiency over time, reflecting successful energy standards

## 🔄 Regenerating Charts

If you need to regenerate the charts (e.g., with updated data):

1. **Ensure Python and required packages are installed:**
   ```bash
   pip install pandas matplotlib seaborn openpyxl
   ```

2. **Run the chart generation script:**
   ```bash
   python create_charts.py
   ```

3. **Charts will be saved in the `charts/` directory**

## 📊 Dataset Information

- **Source:** Book1.csv.xlsx
- **Total Records:** 4,352 TV models
- **Key Columns:**
  - `screensize` - Screen size in inches
  - `Screen_Area` - Screen area in square inches
  - `Screen_Tech` - Technology type (LCD, OLED, Plasma, etc.)
  - `Avg_mode_power` - Average power consumption in watts
  - `Star2` - Energy Star rating (1-8 scale)
  - `Brand_Reg` - Manufacturer brand
  - `ExpDate` - Model registration/expiry date

## 🎯 Key Insights Summary

### For Consumers:
- ✅ Choose TVs with 5+ star ratings for maximum efficiency
- ✅ Consider OLED or LED/LCD technologies
- ✅ Don't assume all large TVs are inefficient - check specific ratings
- ✅ Research brand efficiency track records
- ✅ Newer models tend to be more efficient

### For Industry:
- 📈 Continue investing in energy-efficient technologies
- 📈 Maintain transparency in energy rating systems
- 📈 Focus on reducing power in large-screen models
- 📈 Compete on efficiency as a differentiator

## 🌐 Viewing the Analysis

1. **Open `analysis.html` in a web browser**
2. Navigate through the website using the menu:
   - Home → General energy efficiency information
   - Televisions → TV-specific energy tips
   - **Data Analysis** → Comprehensive data visualizations
   - About Us → Company mission and context

## 🛠️ Technical Details

- **Visualization Library:** Matplotlib + Seaborn
- **Data Processing:** Pandas
- **Chart Resolution:** 300 DPI (high quality)
- **Color Scheme:** Husl palette for accessibility
- **Chart Format:** PNG images

## 📝 Notes

- All charts include descriptive titles and annotations
- Correlation coefficients are displayed where relevant
- Statistical insights are provided for each visualization
- Charts are optimized for both web viewing and printing

---

**Created by:** Rafid Al Jawad (102776293)  
**Last Updated:** October 9, 2025  
**Technology:** Python, Matplotlib, Seaborn, HTML/CSS/JavaScript

