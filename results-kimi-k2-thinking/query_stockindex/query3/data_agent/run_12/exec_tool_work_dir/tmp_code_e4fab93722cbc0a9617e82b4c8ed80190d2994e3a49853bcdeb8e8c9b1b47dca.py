code = """import json
import pandas as pd
from datetime import datetime
import numpy as np

# Load the data from the file
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Parse dates
df['Date'] = pd.to_datetime(df['Date'])
df['YearMonth'] = df['Date'].dt.to_period('M')

# For each index, find the closing price on the last trading day of each month
monthly_prices = df.groupby(['Index', 'YearMonth']).agg({
    'CloseUSD': 'last',
    'Date': 'last'
}).reset_index()

# Dictionary to map index symbols to countries
index_to_country = {
    'N225': 'Japan',
    'NYA': 'United States',
    'IXIC': 'United States',
    'GSPTSE': 'Canada',
    'HSI': 'Hong Kong',
    'GDAXI': 'Germany',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    '399001.SZ': 'China',
    '000001.SS': 'China',
    'N100': 'Eurozone',
    'NSEI': 'India',
    'J203.JO': 'South Africa'
}

# Dictionary to map index symbols to exchange names for context
index_to_exchange = {
    'N225': 'Tokyo Stock Exchange',
    'NYA': 'New York Stock Exchange',
    'IXIC': 'NASDAQ',
    'GSPTSE': 'Toronto Stock Exchange',
    'HSI': 'Hong Kong Stock Exchange',
    'GDAXI': 'Frankfurt Stock Exchange',
    'SSMI': 'SIX Swiss Exchange',
    'TWII': 'Taiwan Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange',
    'N100': 'Euronext',
    'NSEI': 'National Stock Exchange of India',
    'J203.JO': 'Johannesburg Stock Exchange'
}

# Calculate returns for each index using dollar-cost averaging
results = []
monthly_investment = 100  # Invest $100 each month

for index in index_to_country.keys():
    index_data = monthly_prices[monthly_prices['Index'] == index].copy()
    index_data = index_data.sort_values('YearMonth')
    
    # Start from 2000-01
    start_period = pd.Period('2000-01', 'M')
    index_data = index_data[index_data['YearMonth'] >= start_period]
    
    if len(index_data) == 0:
        continue
    
    # Simulate dollar-cost averaging
    total_invested = 0
    total_shares = 0
    
    for _, row in index_data.iterrows():
        price = float(row['CloseUSD'])
        if price > 0:
            shares_bought = monthly_investment / price
            total_shares += shares_bought
            total_invested += monthly_investment
    
    # Calculate final portfolio value
    if len(index_data) > 0 and total_invested > 0:
        final_price = float(index_data.iloc[-1]['CloseUSD'])
        final_value = total_shares * final_price
        total_return = (final_value - total_invested) / total_invested * 100
        
        start_date = index_data.iloc[0]['YearMonth']
        end_date = index_data.iloc[-1]['YearMonth']
        
        results.append({
            'Index': index,
            'Country': index_to_country[index],
            'Exchange': index_to_exchange[index],
            'TotalInvested': total_invested,
            'FinalValue': final_value,
            'TotalReturn': total_return,
            'StartPeriod': str(start_date),
            'EndPeriod': str(end_date),
            'NumMonths': len(index_data)
        })

# Sort by total return descending
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('TotalReturn', ascending=False)

print('__RESULT__:')
print(json.dumps({
    'indices_count': len(results_df),
    'top_5_indices': results_df.head(5).to_dict('records'),
    'all_indices_sorted': results_df.to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'N225', 'count': '7979'}, {'Index': 'NYA', 'count': '7960'}, {'Index': 'IXIC', 'count': '7351'}, {'Index': 'GSPTSE', 'count': '6506'}, {'Index': 'HSI', 'count': '5604'}, {'Index': 'GDAXI', 'count': '5590'}, {'Index': 'SSMI', 'count': '5188'}, {'Index': 'TWII', 'count': '4385'}, {'Index': '399001.SZ', 'count': '4355'}, {'Index': '000001.SS', 'count': '4354'}, {'Index': 'N100', 'count': '4245'}, {'Index': 'NSEI', 'count': '2577'}, {'Index': 'J203.JO', 'count': '1854'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'shape': [21342, 3], 'columns': ['Index', 'Date', 'CloseUSD'], 'unique_indices': 13, 'date_min': '2000-01-03 00:00:00', 'date_max': '2021-06-02 00:00:00'}}

exec(code, env_args)
