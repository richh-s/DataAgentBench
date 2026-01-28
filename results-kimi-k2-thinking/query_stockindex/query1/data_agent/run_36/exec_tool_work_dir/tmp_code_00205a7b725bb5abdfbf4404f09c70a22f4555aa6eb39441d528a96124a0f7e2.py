code = """import pandas as pd
import json

# Load the query results using correct variable access
index_info = locals()['var_functions.query_db:0']

# The trade data is stored as a file path
trade_data_file = locals()['var_functions.query_db:2']

# Load the full trade data
with open(trade_data_file, 'r') as f:
    trade_data = pd.read_json(f)

# Normalize column names
trade_data.columns = [col.strip() for col in trade_data.columns]

# Convert Date to datetime and filter for year >= 2020
trade_data['Date'] = pd.to_datetime(trade_data['Date'])
trade_data_filtered = trade_data[trade_data['Date'] >= '2020-01-01'].copy()

# Calculate intraday volatility for each day
trade_data_filtered['Intraday_Volatility'] = (trade_data_filtered['High'] - trade_data_filtered['Low']) / trade_data_filtered['Open']

# Map exchanges to their major index symbols
exchange_to_index = {
    'Tokyo Stock Exchange': 'N225',
    'Hong Kong Stock Exchange': 'HSI', 
    'Shanghai Stock Exchange': '000001.SS',
    'Shenzhen Stock Exchange': '399001.SZ',
    'National Stock Exchange of India': 'NSEI',
    'Korea Exchange': ['KS11', 'KSPI'],  # Common symbols for Korea
    'Taiwan Stock Exchange': ['TWII', 'TAIEX', 'TWSE']  # Common symbols for Taiwan
}

# Find all unique Asian indices in the data
all_indices = trade_data_filtered['Index'].unique()

# Identify Asian indices by matching with our mapping
asian_indices = []
for idx in all_indices:
    found_asian = False
    for exchange, symbols in exchange_to_index.items():
        if isinstance(symbols, list):
            if idx in symbols or any(str(idx).startswith(sym) for sym in symbols):
                asian_indices.append(idx)
                found_asian = True
                break
        else:
            if idx == symbols or str(idx).startswith(symbols):
                asian_indices.append(idx)
                found_asian = True
                break
    
# Add more indices that might exist
additional_asian = ['N225', 'HSI', '000001.SS', '399001.SZ', 'NSEI', 'TWII', 'KOSPI', 'KS11', 'KSPI', 'BSESN', 'JKSE']
asian_indices.extend([idx for idx in all_indices if idx in additional_asian])

# Remove duplicates
asian_indices = list(set(asian_indices))

# Calculate average intraday volatility for each Asian index
volatility_results = []
flat_mapping = {}

# Create flat mapping for reference
for exchange, symbols in exchange_to_index.items():
    if isinstance(symbols, list):
        for sym in symbols:
            flat_mapping[sym] = exchange
    else:
        flat_mapping[symbols] = exchange

for idx in asian_indices:
    idx_data = trade_data_filtered[trade_data_filtered['Index'] == idx]
    if not idx_data.empty and len(idx_data) >= 50:  # Ensure sufficient data
        avg_volatility = idx_data['Intraday_Volatility'].mean()
        if not pd.isna(avg_volatility):
            volatility_results.append({
                'Index': idx,
                'Exchange': flat_mapping.get(idx, 'Asia Region'),
                'Avg_Intraday_Volatility': float(avg_volatility),
                'Trading_Days': int(len(idx_data))
            })

# Sort by volatility descending
volatility_results = sorted(volatility_results, key=lambda x: x['Avg_Intraday_Volatility'], reverse=True)

# Print the top results
result = json.dumps(volatility_results[:15], indent=2)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
