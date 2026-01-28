code = """import json
import pandas as pd
import numpy as np
from datetime import datetime
import os

# Load data from file
file_path = None
for k, v in locals().items():
    if isinstance(v, str) and os.path.exists(v) and '.json' in v:
        file_path = v
        break

print(f"Loading data from: {file_path}")

with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Create DataFrame
df = pd.DataFrame(trade_data)

# Convert numeric columns
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['High'] = pd.to_numeric(df['High'], errors='coerce')
df['Low'] = pd.to_numeric(df['Low'], errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

# Parse dates - handle multiple format
def parse_date(date_str):
    if pd.isna(date_str):
        return pd.NaT
    
    date_str = str(date_str)
    
    # Remove time portion
    if ' at ' in date_str:
        date_str = date_str.split(' at ')[0]
    if ',' in date_str:
        date_str = date_str.split(',')[0]
    
    # Try parsing with different formats
    formats = [
        '%Y-%m-%d',
        '%d %b %Y',
        '%B %d %Y',
        '%b %d %Y',
        '%m/%d/%Y',
        '%Y/%m/%d'
    ]
    
    for fmt in formats:
        try:
            return pd.to_datetime(date_str, format=fmt)
        except:
            continue
    
    # Fallback to pandas parser
    return pd.to_datetime(date_str, errors='coerce', dayfirst=True)

df['Date_parsed'] = df['Date'].apply(parse_date)

# Filter for 2020 and later
df_2020 = df[df['Date_parsed'] >= '2020-01-01'].copy()

print(f"Total records: {len(df)}, Records from 2020+: {len(df_2020)}")

# Get unique indices
unique_indices = df_2020['Index'].unique().tolist()
print(f"Unique indices in 2020+ data: {unique_indices}")

# Define Asia indices based on exchange information and common knowledge
asia_index_mapping = {
    'Tokyo Stock Exchange': ['^N225', 'N225', 'NKY', 'N225.'],
    'Hong Kong Stock Exchange': ['^HSI', 'HSI'],
    'Shanghai Stock Exchange': ['000001.SS', '^SSEC', 'SSEC'],
    'Shenzhen Stock Exchange': ['399001.SZ', '^SZI', 'SZI'],
    'National Stock Exchange of India': ['^NSEI', 'NSEI', 'NIFTY', 'NIFTY50'],
    'Korea Exchange': ['^KS11', 'KS11', 'KOSPI'],
    'Taiwan Stock Exchange': ['^TWII', 'TWII', 'TAIEX']
}

# Flatten list of Asia index symbols
asia_symbols = []
for symbols in asia_index_mapping.values():
    asia_symbols.extend(symbols)

# Identify actual Asia indices in our data
def is_asia_index(idx):
    idx_str = str(idx).upper()
    for symbol in asia_symbols:
        if symbol.upper() in idx_str:
            return True
    # Check for country-specific patterns
    if any(pattern in idx_str for pattern in ['.SS', '.SZ']):  # China
        return True
    if any(pattern in idx_str for pattern in ['NIFTY', 'SENSEX', 'BSE']):  # India
        return True
    if any(pattern in idx_str for pattern in ['KOSPI', 'KS11']):  # Korea
        return True
    if any(pattern in idx_str for pattern in ['TAIEX', 'TWII']):  # Taiwan
        return True
    return False

# Filter for Asia indices
asia_indices = [idx for idx in unique_indices if is_asia_index(idx)]
print(f"Asia indices found: {asia_indices}")

# Filter data for Asia indices only
df_asia = df_2020[df_2020['Index'].isin(asia_indices)].copy()

# Calculate intraday volatility for each day
df_asia['Intraday_Volatility'] = (df_asia['High'] - df_asia['Low']) / df_asia['Open']

# Remove any infinite or NaN values
df_asia = df_asia[df_asia['Intraday_Volatility'].notna() & np.isfinite(df_asia['Intraday_Volatility'])]

print(f"Records with valid volatility: {len(df_asia)}")

# Calculate average intraday volatility per index
volatility_by_index = df_asia.groupby('Index')['Intraday_Volatility'].agg([
    'mean', 'std', 'count'
]).round(6)

# Sort by mean volatility
volatility_by_index = volatility_by_index.sort_values('mean', ascending=False)

print("Average intraday volatility by Asia index:")
print(volatility_by_index)

# Get the index with highest volatility
if len(volatility_by_index) > 0:
    top_index = volatility_by_index.index[0]
    top_volatility = volatility_by_index.iloc[0]['mean']
    
    result = {
        'top_index': top_index,
        'avg_intraday_volatility': float(top_volatility),
        'all_asia_indices': asia_indices,
        'volatility_rankings': volatility_by_index.to_dict('index')
    }
else:
    result = {'error': 'No Asia index data found for 2020+', 'asia_indices_checked': asia_indices}

print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': 'Loaded 48151 records', 'var_functions.execute_python:16': {'records': 100, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'indices': ['HSI']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'total_records': 0, 'unique_indices': 0, 'asia_indices_count': 0, 'indices_sample': [], 'asia_indices': []}, 'var_functions.execute_python:26': {'records': 100, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'index_sample': ['HSI'], 'date_sample': ['31 Dec 1986, 00:00', 'January 02, 1987 at 12:00 AM', 'January 15, 1987 at 12:00 AM', 'January 16, 1987 at 12:00 AM', 'January 19, 1987 at 12:00 AM'], 'date_sample_end': ['October 19, 1987 at 12:00 AM', '26 Oct 1987, 00:00', 'October 27, 1987 at 12:00 AM', '28 Oct 1987, 00:00', '29 Oct 1987, 00:00']}, 'var_functions.execute_python:30': {'error': 'Could not load variables'}, 'var_functions.query_db:32': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
