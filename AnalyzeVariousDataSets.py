import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

# Set plot style
sns.set(style="whitegrid")

# -----------------------------
# Finance Data Visualization
# -----------------------------
# Read finance data from CSV (make sure it has 'Date' and 'Close' columns)
finance_df = pd.read_csv('finance.csv', parse_dates=['Date'])

# Plot Close price over time
plt.figure(figsize=(8, 4))
plt.plot(finance_df['Date'], finance_df['Close'], marker='o')
plt.title('Stock Price Over Time')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.grid(True)
plt.show()

# -----------------------------
# Health Care Data Visualization
# -----------------------------
# Read healthcare data (must have 'Gender' and 'BloodPressure')
health_df = pd.read_csv('healthcare.csv')

# Create boxplot for blood pressure by gender
plt.figure(figsize=(6, 4))
sns.boxplot(x='Gender', y='BloodPressure', data=health_df)
plt.title('Blood Pressure by Gender')
plt.show()

# -----------------------------
# Census Data Visualization
# -----------------------------
# Read census data (must have 'Region' and 'Population')
census_df = pd.read_csv('census.csv')

# Bar chart for population by region
plt.figure(figsize=(6, 4))
sns.barplot(x='Region', y='Population', data=census_df)
plt.title('Population by Region')
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# Geospatial Data Visualization
# -----------------------------
# Read shapefile using GeoPandas (make sure it's in the same folder or provide full path)
geo_df = gpd.read_file('geodata.shp')

# Plot geospatial data (color by 'Population' if it exists)
if 'Population' in geo_df.columns:
    geo_df.plot(column='Population', cmap='viridis', legend=True, figsize=(10, 6))
else:
    geo_df.plot(figsize=(10, 6))

plt.title('Geospatial Data Visualization')
plt.axis('off')
plt.show()
