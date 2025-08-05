# Brent Oil Price Analysis - Change Point Detection

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

