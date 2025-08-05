from flask import Flask, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
from scipy import stats

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from React frontend

# === Load log_returns data ===
log_returns = np.load('log_returns.npy')  # Make sure this file exists in the same directory
tau = 8357  # Change point index from Bayesian model

# === Split returns ===
returns_before = log_returns[:tau]
returns_after = log_returns[tau:]

# === Summary stats ===
def summary_stats(data):
    return {
        "mean": float(np.mean(data)),
        "std": float(np.std(data, ddof=1)),
        "skewness": float(stats.skew(data)),
        "kurtosis": float(stats.kurtosis(data))
    }

@app.route('/api/data')
def get_log_returns():
    data = [{"log_returns": float(val)} for val in log_returns]
    return jsonify(data)

@app.route('/api/change_point')
def get_change_point():
    return jsonify({"change_point": tau})

@app.route('/api/summary_stats')
def get_summary_stats():
    return jsonify({
        "before": summary_stats(returns_before),
        "after": summary_stats(returns_after)
    })

@app.route('/')
def home():
    return "Flask backend is running. Visit /api/data, /api/change_point, or /api/summary_stats."

if __name__ == '__main__':
    app.run(debug=True)
