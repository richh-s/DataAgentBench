code = """import json
import pandas as pd
from datetime import datetime

# Read the query result from the file
file_path = locals()['var_functions.query_db:2']
with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert data types with error handling
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'])
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Remove rows with invalid dates
df = df.dropna(subset=['Date'])

# Define index to country mapping based on common knowledge
index_country_mapping = {
    'N225': 'Japan',
    'HSI': 'Hong Kong',
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'GSPC': 'United States',
    'DJI': 'United States',
    'IXIC': 'United States',
    'GDAXI': 'Germany',
    'FCHI': 'France',
    'FTSE': 'United Kingdom',
    'NSEI': 'India',
    'N100': 'Netherlands',
    'OMXS30': 'Sweden',
    'IBEX': 'Spain',
    'MIB': 'Italy',
    'KS11': 'South Korea',
    'TWII': 'Taiwan',
    'AXJO': 'Australia',
    'MXX': 'Mexico',
    'BVSP': 'Brazil',
    'GSPTSE': 'Canada',
    'SSMI': 'Switzerland',
    'TA125.TA': 'Israel',
    'J203.JO': 'South Africa'
}

# Calculate returns for each index using dollar cost averaging
results = []

for idx in df['Index'].unique():
    idx_data = df[df['Index'] == idx].copy()
    idx_data = idx_data.sort_values('Date')
    
    # Filter data from 2000 onwards
    idx_data = idx_data[idx_data['Date'] >= '2000-01-01']
    
    if len(idx_data) < 30:  # Need sufficient data points
        continue
    
    # Group by month and get first price of each month
    idx_data['YearMonth'] = idx_data['Date'].dt.to_period('M')
    monthly_data = idx_data.groupby('YearMonth').first().reset_index()
    
    if len(monthly_data) < 12:
        continue
    
    # Calculate dollar cost averaging returns (invest $100 each month)
    total_invested = 0
    total_shares = 0
    
    for _, row in monthly_data.iterrows():
        total_invested += 100
        total_shares += 100 / row['CloseUSD']
    
    # Calculate final value and return
    final_price = monthly_data['CloseUSD'].iloc[-1]
    final_value = total_shares * final_price
    total_return_pct = ((final_value - total_invested) / total_invested) * 100
    
    # Get country for the index
    country = index_country_mapping.get(idx, 'Unknown')
    
    results.append({
        'Index': idx,
        'Country': country,
        'TotalReturnPct': round(total_return_pct, 2),
        'FinalValue': round(final_value, 2),
        'TotalInvested': total_invested,
        'Months': len(monthly_data)
    })

# Sort by total return percentage
results_sorted = sorted(results, key=lambda x: x['TotalReturnPct'], reverse=True)
top_5 = results_sorted[:5]

print('__RESULT__:')
print(json.dumps({
    'top_5_indices': top_5,
    'total_indices_analyzed': len(results)
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
