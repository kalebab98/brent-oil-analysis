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

