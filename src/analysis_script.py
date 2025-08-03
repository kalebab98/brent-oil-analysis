import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for better plot
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

def load_and_explore_data():
    """
    Load Brent oil price data and perform initial exploration
    """
    print("=== Brent Oil Price Analysis - Data Exploration ===")
    
    # Load the data
    try:
        df = pd.read_csv('Data/BrentOilPrices.csv')
        print(f"✓ Data loaded successfully: {len(df)} records")
        print(f"✓ Date range: {df['Date'].min()} to {df['Date'].max()}")
        print(f"✓ Price range: ${df['Price'].min():.2f} to ${df['Price'].max():.2f}")
        
        # Convert date format
        df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y', errors='coerce')
        df = df.dropna()
        
        # Sort by date
        df = df.sort_values('Date').reset_index(drop=True)
        
        return df
        
    except Exception as e:
        print(f"✗ Error loading data: {e}")
        return None

def analyze_time_series_properties(df):
    """
    Analyze key time series properties
    """
    print("\n=== Time Series Properties Analysis ===")
    
    # Calculate basic statistics
    print(f"Mean price: ${df['Price'].mean():.2f}")
    print(f"Standard deviation: ${df['Price'].std():.2f}")
    print(f"Coefficient of variation: {df['Price'].std()/df['Price'].mean():.2f}")
    
    # Calculate log returns for stationarity analysis
    df['Log_Returns'] = np.log(df['Price'] / df['Price'].shift(1))
    df = df.dropna()
    
    print(f"Log returns mean: {df['Log_Returns'].mean():.4f}")
    print(f"Log returns std: {df['Log_Returns'].std():.4f}")
    
    return df

def create_initial_visualizations(df):
    """
    Create initial visualizations for the data
    """
    print("\n=== Creating Initial Visualizations ===")
    
    # Create figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # 1. Price over time
    axes[0, 0].plot(df['Date'], df['Price'], linewidth=0.5, alpha=0.7)
    axes[0, 0].set_title('Brent Oil Prices Over Time')
    axes[0, 0].set_xlabel('Date')
    axes[0, 0].set_ylabel('Price (USD/barrel)')
    axes[0, 0].grid(True, alpha=0.3)
    
    # 2. Log returns over time
    axes[0, 1].plot(df['Date'], df['Log_Returns'], linewidth=0.5, alpha=0.7)
    axes[0, 1].set_title('Log Returns Over Time')
    axes[0, 1].set_xlabel('Date')
    axes[0, 1].set_ylabel('Log Returns')
    axes[0, 1].grid(True, alpha=0.3)
    
    # 3. Price distribution
    axes[1, 0].hist(df['Price'], bins=50, alpha=0.7, edgecolor='black')
    axes[1, 0].set_title('Price Distribution')
    axes[1, 0].set_xlabel('Price (USD/barrel)')
    axes[1, 0].set_ylabel('Frequency')
    
    # 4. Log returns distribution
    axes[1, 1].hist(df['Log_Returns'], bins=50, alpha=0.7, edgecolor='black')
    axes[1, 1].set_title('Log Returns Distribution')
    axes[1, 1].set_xlabel('Log Returns')
    axes[1, 1].set_ylabel('Frequency')
    
    plt.tight_layout()
    plt.savefig('initial_analysis.png', dpi=300, bbox_inches='tight')
    print("✓ Visualizations saved as 'initial_analysis.png'")
    
    return fig

def load_events_data():
    """
    Load the events dataset
    """
    print("\n=== Loading Events Dataset ===")
    
    try:
        # Try with default settings first
        events_df = pd.read_csv('events_dataset.csv')
        events_df['Date'] = pd.to_datetime(events_df['Date'])
        print(f"✓ Events dataset loaded: {len(events_df)} events")
        print("\nKey Events Summary:")
        for _, event in events_df.iterrows():
            print(f"  {event['Date'].strftime('%Y-%m-%d')}: {event['Event_Description']}")
        
        return events_df
        
    except Exception as e:
        print(f"✗ Error loading events data: {e}")
        print("Trying alternative parsing method...")
        try:
            # Try with python engine for better CSV handling
            events_df = pd.read_csv('events_dataset.csv', engine='python')
            events_df['Date'] = pd.to_datetime(events_df['Date'])
            print(f"✓ Events dataset loaded: {len(events_df)} events")
            print("\nKey Events Summary:")
            for _, event in events_df.iterrows():
                print(f"  {event['Date'].strftime('%Y-%m-%d')}: {event['Event_Description']}")
            
            return events_df
            
        except Exception as e2:
            print(f"✗ Alternative method also failed: {e2}")
            return None

def main():
    """
    Main analysis workflow
    """
    print("Brent Oil Price Analysis - Interim Submission")
    print("=" * 50)
    
    # Load and explore data
    df = load_and_explore_data()
    if df is None:
        return
    
    # Analyze time series properties
    df = analyze_time_series_properties(df)
    
    # Create visualizations
    create_initial_visualizations(df)
    
    # Load events data
    events_df = load_events_data()
    
    print("\n=== Analysis Summary ===")
    print("✓ Data exploration completed")
    print("✓ Time series properties analyzed")
    print("✓ Initial visualizations created")
    print("✓ Events dataset prepared")
    print("\nNext steps:")
    print("1. Implement Bayesian change point detection with PyMC3")
    print("2. Identify structural breaks in the price series")
    print("3. Correlate change points with historical events")
    print("4. Develop interactive dashboard")

if __name__ == "__main__":
    main() 