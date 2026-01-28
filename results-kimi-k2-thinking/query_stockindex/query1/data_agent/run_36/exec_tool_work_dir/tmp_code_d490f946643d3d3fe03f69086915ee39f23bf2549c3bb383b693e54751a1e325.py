code = """import pandas as pd
import json

# Access stored variables properly
index_info = locals()['var_functions.query_db:0']
trade_data_file = locals()['var_functions.query_db:2']

# Load trade data
with open(trade_data_file, 'r') as f:
    trade_data_list = json.load(f)

# Convert to DataFrame
trade_df = pd.DataFrame(trade_data_list)

# Calculate intraday volatility
trade_df['Intraday_Volatility'] = (trade_df['High'] - trade_df['Low']) / trade_df['Open']

# Identify Asian indices based on common symbols and exchanges
asian_index_symbols = ['N225', 'HSI', '000001.SS', '399001.SZ', 'NSEI', 'TWII', 'KS11', 'KOSPI', 'BSESN']

# Filter for Asian indices
asian_indices = [idx for idx in trade_df['Index'].unique() if idx in asian_index_symbols]

# Calculate average volatility for each Asian index
results = []
for idx in asian_indices:
    idx_data = trade_df[trade_df['Index'] == idx]
    if not idx_data.empty and len(idx_data) > 0:
        avg_vol = idx_data['Intraday_Volatility'].mean()
        if not pd.isna(avg_vol):
            results.append({
                'Index': idx,
                'Average_Intraday_Volatility': float(avg_vol),
                'Trading_Days': len(idx_data)
            })

# Sort by volatility descending
results_sorted = sorted(results, key=lambda x: x['Average_Intraday_Volatility'], reverse=True)

print('__RESULT__:')
print(json.dumps(results_sorted[:10], indent=2))"""

env_args = {'var_functions.query_db:0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': []}

exec(code, env_args)
