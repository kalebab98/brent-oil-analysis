# Brent Oil Price Analysis - Change Point Detection

**Birhan Energies Data Science Team**

### Project Overview

This project analyzes how major geopolitical and economic events affect Brent oil prices using Bayesian change point detection. The analysis covers 35+ years of daily oil price data (1987-2022) to identify structural breaks and correlate them with historical events.

### Business Objective

The main goal is to study how important events affect Brent oil prices, focusing on:
- Political decisions and conflicts in oil-producing regions
- Global economic sanctions
- OPEC policy changes
- Other major geopolitical events

This analysis provides insights for investors, analysts, and policymakers to better understand and react to oil price changes.

### Project Structure

```
brent-oil-analysis/
│
├── data/
│   └── key_events.csv                 
│
├── notebooks/
│   └── 01_eda_and_data_prep.ipynb
│   └──2a_bayesian_changepoint_model.ipynb
│   └──2b_insights_and_event_correlation.ipynb.ipynb
│   └──2c - Change Point Segment Analysis and Summary Statistics.ipynb
│
├── src/
│   └── analysis_script.py
├── frontend/
│   ├── package.json
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── App.js
│       ├── Dashboard.js
│       ├── index.js
│       └── styles/
│           └── Dashboard.css
├── backend/
│   ├── app.py        
│   └── data/
│       └── BrentOilPrices.csv
├── README.md                          # Overview of the repo and project structure
├── requirements.txt                   # Python dependencies (e.g., pandas, matplotlib, pymc3)
└── .gitignore                         # Ignore Jupyter checkpoints, data cache, 
```

### Key Features

- **Data Exploration**: Comprehensive analysis of 35+ years of Brent oil price data
- **Event Research**: Structured dataset of 20 key geopolitical and economic events
- **Bayesian Change Point Detection**: Using PyMC3 for statistical modeling
- **Interactive Dashboard**: Flask/React dashboard for stakeholder exploration

### Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd W10
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run initial analysis**:
   ```bash
   python analysis_script.py
   ```

### Data Sources

- **Brent Oil Prices**: Daily prices from May 20, 1987 to September 30, 2022
- **Events Dataset**: Research-based compilation of major events affecting oil markets

### Analysis Workflow

1. **Data Preprocessing**: Load and clean Brent oil price data
2. **Exploratory Analysis**: Analyze time series properties and create visualizations
3. **Event Research**: Compile structured dataset of key events
4. **Change Point Detection**: Implement Bayesian model using PyMC3
5. **Correlation Analysis**: Associate detected changes with historical events
6. **Dashboard Development**: Create interactive visualization platform

### Key Events Analyzed

The analysis includes 20 major events such as:
- Iraq-Kuwait conflict (1990-1991)
- 9/11 terrorist attacks (2001)
- Global financial crisis (2008)
- Arab Spring and Libya conflict (2011)
- OPEC production decisions (various dates)
- COVID-19 pandemic (2020)
- Russia-Ukraine war (2022)

# Task 2 – Bayesian Change Point Analysis on Brent Oil Prices

## Objective

Detect structural change points in the log returns of Brent oil prices using Bayesian statistical modeling with PyMC3.


---

## 🧠 Objectives

- Compute log returns from Brent oil prices.
- Detect structural break using visual inspection or statistical methods.
- Compare statistical properties (mean, std, skewness, kurtosis) before and after the change point.
- Visualize findings.

---

## 🧪 Methodology

### 1. Log Return Calculation  
Using the natural logarithm of daily prices:


---

### 2. Change Point Detection  
Identify an index where a significant change in volatility or trend is observed.

---

### 3. Summary Statistics  
Calculated for both pre- and post-change point periods:

- Mean  
- Standard Deviation  
- Skewness  
- Kurtosis  

---

### 4. Visualization

- Line plot of log returns.  
- Highlighted region showing structural break.

---

## 📊 Results Preview

| Metric      | Before Change Point | After Change Point |
|-------------|---------------------|--------------------|
| Mean        | ~0.000007           | ~0.0023            |
| Std. Dev.   | ~0.0238             | ~0.0416            |
| Skewness    | ~-0.62              | ~-4.19             |
| Kurtosis    | ~18.60              | ~103.23            |

> These results suggest a structural break leading to increased volatility in Brent oil prices.

---

## 🚀 How to Run

1. **Install dependencies**


2. **Run the analysis**


3. **View results**

- Plots saved in `results/`
- Summary stats printed to console or saved as JSON

---

## 🧩 Dependencies

- pandas  
- numpy  
- matplotlib  
- scipy  

*(Optional: Add `seaborn`, `ruptures`, or `changepy` for advanced change point detection.)*

---

## 📌 Notes

- This task sets the foundation for Task 3 (Dashboard) by preparing the statistical insights that will be visualized.
- Data source: *Add your data source here if public or link available.*
- Next step: Serve these results via Flask backend for the interactive dashboard.

---

### Task-3 (Interactive Dashboard)


# Task 3 – Interactive Dashboard for Brent Oil Prices and Change Point Visualization

## Objective

Develop a full-stack web application to visualize Brent oil prices, log returns, and detected change points with interactive filtering and summary statistics.

## Description

The dashboard allows users to:

- Visualize daily Brent crude oil prices and their log returns over time.
- See the Bayesian-inferred change point marked on the chart.
- Filter data by selectable date ranges.
- View descriptive statistics (mean, std dev, skewness, kurtosis) before and after the change point.

## Tech Stack

- **Frontend:** React, Recharts, React-Datepicker
- **Backend:** Flask with Flask-CORS for API
- **Communication:** RESTful API serving JSON data

## Backend Files

- `app.py` — Flask API serving endpoints:
  - `/api/data` — Returns log returns and prices.
  - `/api/change_point` — Returns detected change point index.
  - `/api/summary_stats` — Returns descriptive statistics before/after change point.
- `log_returns.npy` — Shared data file.

## Frontend Files

- `Dashboard.jsx` — Main React component with chart and controls.
- `App.js` — React entry point.
- `package.json` — Project dependencies.
![photo_2025-08-05_19-40-13](https://github.com/user-attachments/assets/fd430f0b-c62a-4bd6-8588-ab3fce49d03a)


## Installation & Setup

### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
