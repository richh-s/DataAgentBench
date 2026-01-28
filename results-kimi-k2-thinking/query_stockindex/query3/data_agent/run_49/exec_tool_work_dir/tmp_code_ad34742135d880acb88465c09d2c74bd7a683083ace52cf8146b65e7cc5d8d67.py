code = """import json, pandas as pd
import numpy as np

# Read trade data
file_path = locals()['var_functions.query_db:8']
with open(file_path, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Clean and convert data types
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Adj Close'] = pd.to_numeric(df['Adj Close'], errors='coerce')
df['CloseUSD'] = pd.to_numeric(df['CloseUSD'], errors='coerce')

# Remove rows with missing values
df = df.dropna()

# Sort by index and date
df = df.sort_values(['Index', 'Date'])

# Get the most recent date (end of period)
end_date = df['Date'].max()
print(f"End date: {end_date}")
print(f"Start date range: {df['Date'].min()}")

# Define country mapping based on index symbols and exchanges
country_map = {
    '000001.SS': 'China',
    '399001.SZ': 'China',
    'HSI': 'Hong Kong',
    'N225': 'Japan',
    'GDAXI': 'Germany',
    'N100': 'Netherlands',
    'IXIC': 'USA',
    'NYA': 'USA',
    'GSPTSE': 'Canada',
    'NSEI': 'India',
    'SSMI': 'Switzerland',
    'TWII': 'Taiwan',
    'J203.JO': 'South Africa'
}

# Simulate dollar-cost averaging for each index
def simulate_dca(df_index, monthly_investment=100):
    """Simulate monthly dollar-cost averaging"""
    # Get monthly data (first trading day of each month)
    monthly_data = df_index.groupby([df_index['Date'].dt.year, df_index['Date'].dt.month]).first().reset_index()
    
    if len(monthly_data) == 0:
        return 0, 0, 0
    
    # Calculate shares purchased each month (using CloseUSD)
    monthly_data['Shares'] = monthly_investment / monthly_data['CloseUSD']
    
    # Total investment
    total_invested = len(monthly_data) * monthly_investment
    
    # Total shares accumulated
    total_shares = monthly_data['Shares'].sum()
    
    # Current value (using most recent price)
    current_price = df_index['CloseUSD'].iloc[-1]
    current_value = total_shares * current_price
    
    # Return
    total_return = current_value - total_invested
    return_pct = (total_return / total_invested) * 100 if total_invested > 0 else 0
    
    return return_pct, total_return, total_invested

# Calculate returns for each index
results = []
for index in df['Index'].unique():
    df_idx = df[df['Index'] == index].copy()
    
    # Ensure data starts from 2000
    df_idx = df_idx[df_idx['Date'] >= '2000-01-01']
    
    if len(df_idx) < 12:  # Need at least 1 year of data
        continue
    
    # Calculate first trading day of each month
    df_idx['YearMonth'] = df_idx['Date'].dt.to_period('M')
    monthly_prices = df_idx.groupby('YearMonth').first().reset_index()
    
    if len(monthly_prices) < 12:
        continue
    
    # Simulate DCA
    monthly_investment = 100
    monthly_prices['Shares'] = monthly_investment / monthly_prices['CloseUSD']
    
    total_invested = len(monthly_prices) * monthly_investment
    total_shares = monthly_prices['Shares'].sum()
    current_price = df_idx['CloseUSD'].iloc[-1]
    current_value = total_shares * current_price
    
    total_return = current_value - total_invested
    return_pct = (total_return / total_invested) * 100
    
    country = country_map.get(index, 'Unknown')
    
    results.append({
        'Index': index,
        'Country': country,
        'Total_Invested': total_invested,
        'Current_Value': current_value,
        'Total_Return': total_return,
        'Return_Percentage': return_pct,
        'Months': len(monthly_prices),
        'Total_Shares': total_shares
    })

# Sort by return percentage
results_df = pd.DataFrame(results)
results_df = results_df.sort_values('Return_Percentage', ascending=False)

print('Number of indices analyzed:', len(results_df))
print('\nTop 10 indices by return:')
print(results_df[['Index', 'Country', 'Return_Percentage', 'Total_Return', 'Months']].head(10).to_string())

# Save results for next steps
top_5 = results_df.head(5)

print('__RESULT__:')
print(top_5.to_json(orient='records', indent=2))"""

env_args = {'var_functions.list_db:0': ['index_trade'], 'var_functions.list_db:2': ['index_info'], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:20': {'count': 67948, 'indices': ['J203.JO', 'TWII', 'GSPTSE', 'NYA', 'GDAXI', 'HSI', 'N225', 'IXIC', 'NSEI', 'N100', '399001.SZ', 'SSMI', '000001.SS']}}

exec(code, env_args)
