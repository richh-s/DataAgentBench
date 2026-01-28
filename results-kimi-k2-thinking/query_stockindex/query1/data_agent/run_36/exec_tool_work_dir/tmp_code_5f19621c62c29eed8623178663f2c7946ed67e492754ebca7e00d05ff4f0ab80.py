code = """import pandas as pd
import json

# Load the query results
index_info = var_functions.query_db:0
# The trade data is large so it's stored as a file path
trade_data_file = var_functions.query_db:2

# Load the full trade data
trade_data = pd.read_json(trade_data_file)

# Normalize column names
trade_data.columns = [col.strip() for col in trade_data.columns]

# Convert Date to datetime and filter for year >= 2020
trade_data['Date'] = pd.to_datetime(trade_data['Date'])
trade_data_filtered = trade_data[trade_data['Date'] >= '2020-01-01'].copy()

# Calculate intraday volatility for each day
trade_data_filtered['Intraday_Volatility'] = (trade_data_filtered['High'] - trade_data_filtered['Low']) / trade_data_filtered['Open']

# Map exchanges to their index symbols
exchange_to_index = {
    'Tokyo Stock Exchange': 'N225',
    'Hong Kong Stock Exchange': 'HSI', 
    'Shanghai Stock Exchange': '000001.SS',
    'Shenzhen Stock Exchange': '399001.SZ',
    'National Stock Exchange of India': 'NSEI',
    'Korea Exchange': ['KS11', 'KSC', 'KOSPI'],  # Common symbols for Korea
    'Taiwan Stock Exchange': ['TWII', 'TAIEX']   # Common symbols for Taiwan
}

# Flatten the mapping
flat_mapping = {}
for exchange, symbols in exchange_to_index.items():
    if isinstance(symbols, list):
        for symbol in symbols:
            flat_mapping[symbol] = exchange
    else:
        flat_mapping[symbols] = exchange

# Find all unique Asian indices in the data
all_indices = trade_data_filtered['Index'].unique()

# Identify which are Asian based on common index symbols
asian_indices = []
for idx in all_indices:
    for symbol in flat_mapping.keys():
        if idx == symbol or str(idx).startswith(symbol):
            asian_indices.append(idx)
            break

# Remove duplicates
asian_indices = list(set(asian_indices))

# Calculate average intraday volatility for each Asian index
volatility_results = []
for idx in asian_indices:
    idx_data = trade_data_filtered[trade_data_filtered['Index'] == idx]
    if not idx_data.empty:
        avg_volatility = idx_data['Intraday_Volatility'].mean()
        volatility_results.append({
            'Index': idx,
            'Exchange': flat_mapping.get(idx, 'Unknown'),
            'Avg_Intraday_Volatility': avg_volatility,
            'Trading_Days': len(idx_data)
        })

# Sort by volatility descending
volatility_results = sorted(volatility_results, key=lambda x: x['Avg_Intraday_Volatility'], reverse=True)

# Print results
result = json.dumps(volatility_results[:10], indent=2)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
