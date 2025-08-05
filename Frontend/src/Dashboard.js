import React, { useEffect, useState } from 'react';
import {
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ReferenceLine
} from 'recharts';
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';

function Dashboard() {
  const [data, setData] = useState([]);
  const [changePoint, setChangePoint] = useState(null);
  const [summaryStats, setSummaryStats] = useState(null);
  const [startDate, setStartDate] = useState(null);
  const [endDate, setEndDate] = useState(null);
  const [loading, setLoading] = useState(true);

  // Load data
  const fetchData = async () => {
    try {
      const url = new URL('http://127.0.0.1:5000/api/data');
      if (startDate) url.searchParams.append('start_date', startDate.toISOString().split('T')[0]);
      if (endDate) url.searchParams.append('end_date', endDate.toISOString().split('T')[0]);

      const res = await fetch(url);
      const json = await res.json();
      setData(json);
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally {
      setLoading(false);
    }
  };

  // Load change point
  const fetchChangePoint = async () => {
    const res = await fetch('http://127.0.0.1:5000/api/change_point');
    const json = await res.json();
    setChangePoint(json.change_point_index);
  };

  // Load stats
  const fetchSummaryStats = async () => {
    const res = await fetch('http://127.0.0.1:5000/api/summary_stats');
    const json = await res.json();
    setSummaryStats(json);
  };

  useEffect(() => {
    fetchData();
    fetchChangePoint();
    fetchSummaryStats();
  }, [startDate, endDate]);

  return (
    <div style={{ padding: '20px' }}>
      <h1>📊 Brent Oil Log Returns Dashboard</h1>

      <div style={{ marginBottom: 20 }}>
        <label>Select Date Range: </label><br />
        <DatePicker
          selected={startDate}
          onChange={(date) => setStartDate(date)}
          placeholderText="Start Date"
        />
        {' '}to{' '}
        <DatePicker
          selected={endDate}
          onChange={(date) => setEndDate(date)}
          placeholderText="End Date"
        />
        <button onClick={fetchData} style={{ marginLeft: 10 }}>Apply</button>
      </div>

      {loading ? (
        <p>Loading data...</p>
      ) : (
        <>
          <h2>📈 Historical Price and Log Returns</h2>
          <LineChart width={900} height={400} data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="Date" minTickGap={20} />
            <YAxis yAxisId="left" orientation="left" label={{ value: 'Price', angle: -90, position: 'insideLeft' }} />
            <YAxis yAxisId="right" orientation="right" label={{ value: 'Log Return', angle: 90, position: 'insideRight' }} />
            <Tooltip />
            <Legend />
            <Line yAxisId="left" type="monotone" dataKey="Price" stroke="#8884d8" dot={false} name="Brent Price" />
            <Line yAxisId="right" type="monotone" dataKey="log_returns" stroke="#82ca9d" dot={false} name="Log Returns" />
            {changePoint !== null && changePoint < data.length && (
              <ReferenceLine x={data[changePoint]?.Date} stroke="red" label="Change Point" />
            )}
          </LineChart>

          <h2>📊 Summary Statistics</h2>
          {summaryStats && (
            <div>
              <h4>Before Change Point</h4>
              <ul>
                <li><b>Mean:</b> {summaryStats.before.mean.toFixed(6)}</li>
                <li><b>Std Dev:</b> {summaryStats.before.std.toFixed(6)}</li>
                <li><b>Skewness:</b> {summaryStats.before.skewness.toFixed(4)}</li>
                <li><b>Kurtosis:</b> {summaryStats.before.kurtosis.toFixed(2)}</li>
              </ul>

              <h4>After Change Point</h4>
              <ul>
                <li><b>Mean:</b> {summaryStats.after.mean.toFixed(6)}</li>
                <li><b>Std Dev:</b> {summaryStats.after.std.toFixed(6)}</li>
                <li><b>Skewness:</b> {summaryStats.after.skewness.toFixed(4)}</li>
                <li><b>Kurtosis:</b> {summaryStats.after.kurtosis.toFixed(2)}</li>
              </ul>
            </div>
          )}
        </>
      )}
    </div>
  );
}

export default Dashboard;
