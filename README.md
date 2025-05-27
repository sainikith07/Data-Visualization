
# 📊 Simple & Smart Data Analysis with Python

Welcome to the **Simple Data Science Toolkit** — a beginner-friendly project that helps you explore and visualize **massive datasets** across **finance, healthcare, census, geospatial, and time series** domains using easy Python code.

No complicated functions. No advanced machine learning. Just clear, readable code and real-world data.

---

## 🎯 What You'll Learn

✅ How to load real data from CSV files  
✅ How to view and understand large datasets  
✅ How to create beautiful charts: line, pie, histogram, heatmap, scatter  
✅ How to perform basic clustering  
✅ How to analyze trends over time using **Time Series**  
✅ How to explore health, finance, census, and geographic data

---

## 🧰 Tools Used

| Library     | Purpose                            |
|-------------|------------------------------------|
| `pandas`    | Reading and handling CSV files     |
| `matplotlib`| Plotting basic graphs              |
| `seaborn`   | Advanced statistical plots         |
| `sklearn`   | Clustering (KMeans)                |

Install them using:

```bash
pip install pandas matplotlib seaborn scikit-learn
```

---

## 📁 Project Overview

### 1. 📈 Time Series Analysis: Stock Market Trends

**File:** `time_series_plot.py`  
**Data:** `stock.csv`

📌 **What it does:**

- Reads daily stock prices
- Converts the `Date` column to datetime format
- Plots a **line graph** to show how the stock price changed over time

📊 **Why it matters:**  
This is useful to spot upward or downward trends, seasonality, or price spikes in the stock market.

---

### 2. 💰 Financial Data Analysis

**File:** `financial_analysis.py`  
**Data:** `finance.csv`

📌 **What it does:**

- Loads company financials like **Revenue**, **Profit**, **Assets**, and **Liabilities**
- Performs:
  - ✅ **KMeans Clustering**: Groups similar companies
  - 📉 **Histogram**: Shows distribution of revenue
  - 🔥 **Heatmap**: Highlights correlation between financial features
  - 🧭 **Scatter Plot**: Visualizes clustered companies

📊 **Why it matters:**  
This helps categorize companies and see how different financial metrics relate to each other.

---

### 3. 🏥 Healthcare Data Visualization

**File:** `healthcare_plot.py`  
**Data:** `healthcare.csv`

📌 **What it does:**

- Reads healthcare data (e.g. patients by disease or region)
- Shows:
  - 📈 **Line Chart** for patient trend over time
  - 🥧 **Pie Chart** showing disease or region distribution

📊 **Why it matters:**  
Helps hospitals or analysts identify health trends and allocate resources.

---

### 4. 🏛️ Census Data Analysis

**File:** `census_plot.py`  
**Data:** `census.csv`

📌 **What it does:**

- Loads population, age, and income data
- Visualizes:
  - 🧮 **Bar charts** for age/income groups
  - 🥧 **Pie charts** for region-wise population

📊 **Why it matters:**  
Understanding population distribution helps with policy making and development planning.

---

### 5. 🌍 Geospatial Data Plotting

**File:** `geospatial_plot.py`  
**Data:** `geo.csv`

📌 **What it does:**

- Plots data points on a 2D scatter map using `latitude` and `longitude`

📊 **Why it matters:**  
Geospatial visualizations help track locations (e.g., schools, hospitals, store branches).

---

### 6. 📊 Basic Data Acquisition and Plotting

**File:** `basic_plots.py`  
**Data:** Any CSV

📌 **What it does:**

- Reads a CSV file using `pandas`
- Displays first few rows and summary
- Plots:
  - 📈 Line Chart
  - 🥧 Pie Chart
  - 📊 Bar Chart

📊 **Why it matters:**  
Great starting point to visualize any new dataset quickly.

---

## 🗂 Folder Structure

```
📁 your_project/
│
├── time_series_plot.py
├── financial_analysis.py
├── healthcare_plot.py
├── census_plot.py
├── geospatial_plot.py
├── basic_plots.py
│
├── stock.csv
├── finance.csv
├── healthcare.csv
├── census.csv
├── geo.csv
```

---

## ▶️ How to Run

1. Save the `.py` files and `.csv` files in the same folder.
2. Open your terminal.
3. Run the script:

```bash
python time_series_plot.py
python financial_analysis.py
...
```

Each script will load the CSV, analyze the data, and show the graph!

---

## 🧠 Concepts Covered

| Concept               | Covered In                        |
|------------------------|------------------------------------|
| Time Series            | `time_series_plot.py`              |
| Clustering             | `financial_analysis.py`            |
| Histogram & Heatmap    | `financial_analysis.py`            |
| Pie & Line Chart       | All scripts                        |
| CSV Data Loading       | All scripts                        |
| Scatter Plot (Geo)     | `geospatial_plot.py`               |
| Basic Stats & Viewing  | All scripts using `pandas`         |

---

## 💡 Why This Project?

This project is perfect for:

- 📚 Students learning data science
- 🧪 Beginners practicing data analysis
- 💼 Professionals who want to analyze CSV files visually

---

## 🙌 Contributions

Feel free to:
- Add more datasets
- Improve the visualizations
- Share your insights!

---

## 📧 Contact

Need help or want to collaborate? Reach out!

📩 sainikith04@gmail.com  
🌐 (https://www.linkedin.com/in/sai-nikith-kaleru/)

---
