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
│   └── key_events.csv                 # Structured event dataset (Task 1)
│
├── notebooks/
│   └── 01_eda_and_data_prep.ipynb     # Jupyter notebook for EDA and initial data checks
│
├── src/
│   └── analysis_script.py
│
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

### Technical Approach

- **Bayesian Inference**: Using PyMC3 for probabilistic modeling
- **Monte Carlo Markov Chain**: For posterior sampling
- **Change Point Detection**: Identifying structural breaks in time series
- **Statistical Validation**: Model convergence and diagnostic checks

### Interim Submission Status

✅ **Completed**:
- Data analysis workflow definition
- Event research and compilation (20 events)
- Initial data exploration and visualization
- Statistical approach planning
- Assumptions and limitations documented

🔄 **In Progress**:
- Bayesian change point model implementation
- Interactive dashboard development
- Final analysis and reporting

### Next Steps

1. Implement Bayesian change point detection with PyMC3
2. Identify and quantify structural breaks in oil prices
3. Correlate change points with historical events
4. Develop interactive Flask/React dashboard
5. Prepare final report and presentation

