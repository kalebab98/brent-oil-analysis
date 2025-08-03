# Interim Report: Brent Oil Price Analysis
## Week 10 Challenge - Birhan Energies

**Date:** August 1, 2025  
**Team:** Data Science Team  
**Project:** Change Point Analysis of Brent Oil Prices

---

## Task 1: Laying the Foundation for Analysis

### 1.1 Data Analysis Workflow

#### Planned Analysis Steps:

1. **Data Exploration and Preprocessing**
   - Load and clean Brent oil price data (May 1987 - September 2022)
   - Convert date formats and handle missing values
   - Perform initial exploratory data analysis (EDA)
   - Analyze time series properties (trend, seasonality, stationarity)

2. **Event Research and Compilation**
   - Research major geopolitical events, OPEC decisions, and economic shocks
   - Compile structured dataset with at least 10-15 key events
   - Map events to approximate dates for correlation analysis

3. **Statistical Analysis**
   - Implement Bayesian Change Point detection using PyMC3
   - Identify structural breaks in the price series
   - Quantify impact of detected changes
   - Associate change points with researched events

4. **Model Validation and Interpretation**
   - Check model convergence and diagnostics
   - Interpret posterior distributions
   - Validate findings against historical context

5. **Dashboard Development**
   - Create interactive Flask/React dashboard
   - Visualize change points and event correlations
   - Provide filtering and exploration capabilities

#### Assumptions and Limitations:

**Key Assumptions:**
- Oil price changes are primarily driven by major geopolitical and economic events
- The Bayesian change point model can adequately capture structural breaks
- Historical events have immediate or short-term impacts on oil prices
- The relationship between events and price changes is consistent over time

**Critical Limitations:**
- **Correlation vs Causation:** This analysis identifies statistical correlations between events and price changes, but cannot definitively prove causation. Multiple factors influence oil prices simultaneously, and the model may not capture all confounding variables.
- **Event Timing:** The exact timing of events and their market impact may not align perfectly due to market anticipation and delayed reactions.
- **Model Simplification:** The change point model assumes discrete structural breaks, while real-world impacts may be more gradual.
- **Data Quality:** Historical event data may be incomplete or subject to interpretation bias.

### 1.2 Understanding the Model and Data

#### Time Series Properties Analysis:
- **Data Range:** 35+ years of daily Brent oil prices (1987-2022)
- **Expected Properties:** Non-stationary series with trends, volatility clustering, and structural breaks
- **Modeling Approach:** Will convert to log returns for stationarity and use Bayesian change point detection

#### Change Point Model Purpose:
- Identify statistically significant structural breaks in oil price behavior
- Detect changes in mean price levels and volatility regimes
- Provide probabilistic estimates of when changes occurred
- Quantify the magnitude of changes before and after breakpoints

#### Expected Outputs:
- **Change Point Dates:** Posterior distributions of most probable change dates
- **Parameter Changes:** Mean price levels and volatility before/after changes
- **Uncertainty Quantification:** Credible intervals for all estimates
- **Event Associations:** Correlation between detected changes and historical events

#### Model Limitations:
- Assumes discrete structural breaks (may miss gradual changes)
- Requires sufficient data before/after change points
- May not capture complex multi-factor interactions
- Limited to the specific time series properties modeled

### 1.3 Communication Strategy

#### Target Stakeholders:
- **Investors:** Risk management and investment timing insights
- **Policymakers:** Economic stability and energy security planning
- **Energy Companies:** Supply chain and operational planning
- **Analysts:** Market research and forecasting support

#### Communication Channels:
- **Interactive Dashboard:** Primary delivery mechanism for exploration
- **Technical Report:** Detailed methodology and findings
- **Executive Summary:** High-level insights for decision-makers
- **GitHub Repository:** Code transparency and reproducibility

---

## Next Steps for Task 2:
1. Complete event research and compile structured dataset
2. Implement Bayesian change point model in PyMC3
3. Perform comprehensive analysis and interpretation
4. Develop interactive dashboard
5. Prepare final report and presentation

**Estimated Completion:** August 5, 2025 