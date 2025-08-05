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

## Description

This task involves modeling the daily log returns of Brent crude oil prices to identify a significant change point where the statistical properties (mean and variance) of the returns change. The change point corresponds to an important structural shift in the market dynamics.

## Files

- `log_returns.npy` — Numpy array containing daily log returns.
- `change_point_model.py` — Python script implementing the Bayesian model using PyMC3.
- `summary_stats.py` — Utility functions to calculate descriptive statistics.
- `events_dataset.csv` — Dataset of key geopolitical and economic events for contextual reference.

## Methodology

- Model log returns as normally distributed before and after a latent change point.
- Estimate separate means and standard deviations for pre- and post-change regimes.
- Use Markov Chain Monte Carlo (MCMC) sampling via PyMC3 to infer posterior distributions.
- Identify the most probable change point index (τ).

## Dependencies

Install required Python packages:

```bash
pip install numpy pandas pymc3 scipy matplotlib
```

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
