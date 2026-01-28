code = """import pandas as pd
import json

# Load index_info data
index_info = locals()['var_functions.query_db:0']

# Load trade data using the correct variable
# Check what var_functions.query_db:2 actually is
trade_data_var = locals()['var_functions.query_db:2']

# Load trade data appropriately
if isinstance(trade_data_var, str) and '.json' in trade_data_var:
    # It's a file path
    with open(trade_data_var, 'r') as f:
        trade_data_list = json.load(f)
else:
    trade_data_list = trade_data_var

# Convert to DataFrame
trade_df = pd.DataFrame(trade_data_list)

# Convert numeric columns to proper types (they may be strings)
numeric_cols = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'CloseUSD']
for col in numeric_cols:
    trade_df[col] = pd.to_numeric(trade_df[col], errors='coerce')

# Convert Date to datetime
trade_df['Date'] = pd.to_datetime(trade_df['Date'])

# Calculate intraday volatility for each trading day
trade_df['Intraday_Volatility'] = (trade_df['High'] - trade_df['Low']) / trade_df['Open']

# Identify Asian indices based on common symbols
asian_symbols = ['N225', 'HSI', '000001.SS', '399001.SZ', 'NSEI', 'TWII', 'BSESN', 'KS11']

# Check which Asian indices are actually in the data
available_indices = trade_df['Index'].unique()
asian_indices_present = [idx for idx in available_indices if idx in asian_symbols]

# Calculate average intraday volatility for each Asian index
volatility_results = []
for idx in asian_indices_present:
    idx_data = trade_df[trade_df['Index'] == idx]
    
    # Filter for data from 2020 onwards
    idx_data_2020plus = idx_data[idx_data['Date'] >= '2020-01-01']
    
    if len(idx_data_2020plus) > 0:
        avg_volatility = idx_data_2020plus['Intraday_Volatility'].mean()
        
        if not pd.isna(avg_volatility):
            volatility_results.append({
                'Index': idx,
                'Average_Intraday_Volatility': float(avg_volatility),
                'Trading_Days_Since_2020': len(idx_data_2020plus)
            })

# Sort by average intraday volatility descending
volatility_results_sorted = sorted(volatility_results, 
                                   key=lambda x: x['Average_Intraday_Volatility'], 
                                   reverse=True)

print('__RESULT__:')
print(json.dumps(volatility_results_sorted, indent=2))"""

env_args = {'var_functions.query_db:0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': [], 'var_functions.execute_python:14': {'available_keys': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.execute_python:6']}}

exec(code, env_args)
