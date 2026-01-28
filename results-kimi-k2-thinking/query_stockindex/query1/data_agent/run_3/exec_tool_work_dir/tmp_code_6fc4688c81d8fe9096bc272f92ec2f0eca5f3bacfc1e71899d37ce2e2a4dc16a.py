code = """import json
import pandas as pd
import re
from datetime import datetime

# Get the variables from storage - check all available variables
all_vars = list(locals().keys())

# Find the file path for query_db_18
file_path = None
for var in all_vars:
    if 'query_db_18' in var:
        file_path = locals()[var]
        break

# Load data
if file_path:
    with open(file_path, 'r') as f:
        trade_data = json.load(f)
else:
    # Try fallback approach based on pattern
    for var in all_vars:
        val = locals()[var]
        if isinstance(val, str) and '.json' in val:
            file_path = val
            with open(file_path, 'r') as f:
                trade_data = json.load(f)
            break

# Create DataFrame
df = pd.DataFrame(trade_data)

# Clean column names
df.columns = [col.strip() for col in df.columns]

# Convert to numeric
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['High'] = pd.to_numeric(df['High'], errors='coerce')
df['Low'] = pd.to_numeric(df['Low'], errors='coerce')

# Parse dates
def parse_date(date_val):
    try:
        if isinstance(date_val, str):
            # Remove time part if present
            date_part = date_val.split(' at ')[0].split(',')[0]
            return pd.to_datetime(date_part, errors='coerce')
        else:
            return pd.to_datetime(date_val, errors='coerce')
    except:
        return pd.NaT

df['Date_parsed'] = df['Date'].apply(parse_date)

# Filter for 2020+
df_recent = df[df['Date_parsed'] >= '2020-01-01'].copy()

# Get unique indices
indices = sorted(df_recent['Index'].unique().tolist())

# Identify Asia indices based on common symbols and patterns
asia_indices = []
for idx in indices:
    idx_upper = str(idx).upper()
    
    # Check for well-known Asia indices
    if any(symbol in idx_upper for symbol in [
        'HSI', 'N225', 'NIFTY', 'KOSPI', 'TAIEX', 
        'SSE', 'SHCOMP', 'SHANGHAI', 'SHENZHEN',
        'BSE', 'SENSEX', 'NSE', 'NSEI',
        'ASX', 'STI', 'KLSE', 'SET',
        'JKSE', 'PSEI', 'VNINDEX'
    ]):
        asia_indices.append(idx)
    # Check for China-specific patterns
    elif '.SS' in str(idx) or '.SZ' in str(idx):
        asia_indices.append(idx)

print("__RESULT__:")
print(json.dumps({
    'total_records': len(df_recent),
    'unique_indices': len(indices),
    'asia_indices_count': len(asia_indices),
    'indices_sample': indices[:50],  # Show first 50 to help identify Asia indices
    'asia_indices': asia_indices
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': 'Loaded 48151 records', 'var_functions.execute_python:16': {'records': 100, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'indices': ['HSI']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
