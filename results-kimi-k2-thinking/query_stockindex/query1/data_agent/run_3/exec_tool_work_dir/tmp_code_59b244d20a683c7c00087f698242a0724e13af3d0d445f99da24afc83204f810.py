code = """import json
import pandas as pd
import re
from datetime import datetime

# Find the file path for the trade data
file_path = None
for k, v in list(locals().items()):
    if isinstance(v, str) and '.json' in v and 'query_db_18' in k:
        file_path = v
        break

# Load the data
with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Create DataFrame
df = pd.DataFrame(trade_data)

# Parse dates - handle various formats
def parse_date(date_str):
    if isinstance(date_str, (int, float)):
        return pd.to_datetime(date_str)
    
    # Remove time information for consistency
    date_str = str(date_str)
    date_part = date_str.split(' at ')[0].split(', ')[0]
    
    try:
        # Try various common formats
        formats = [
            '%Y-%m-%d',
            '%d %b %Y',
            '%B %d, %Y',
            '%b %d, %Y',
            '%m/%d/%Y',
            '%d/%m/%Y'
        ]
        for fmt in formats:
            try:
                return pd.to_datetime(date_part, format=fmt)
            except:
                continue
        # If none work, use pandas parser
        return pd.to_datetime(date_part, errors='coerce')
    except:
        return pd.to_datetime(date_part, errors='coerce')

# Apply date parsing
df['Date_parsed'] = df['Date'].apply(parse_date)

# Filter for dates since 2020
df_2020 = df[df['Date_parsed'] >= '2020-01-01'].copy()

# Get available indices
indices = df_2020['Index'].unique().tolist()

# Based on geographic knowledge, identify Asia indices
asia_indices = []
for idx in indices:
    idx_str = str(idx).upper()
    # Common Asia indices
    if any(x in idx_str for x in ['HSI', 'N225', 'NIFTY', 'KOSPI', 'TAIEX', 'SSE', 'SZSE', 'BSE', 'SENSEX', 'NSE', 'KSE', 'TWII']):
        asia_indices.append(idx)
    # China indices
    elif any(x in idx_str for x in ['.SS', '.SZ']):
        asia_indices.append(idx)
    # Japan
    elif idx_str in ['N225', '^N225']:
        asia_indices.append(idx)

print("__RESULT__:")
result = {
    'total_records_2020': len(df_2020),
    'all_indices': indices[:30],  # First 30 to see what we have
    'asia_indices': asia_indices
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': 'Loaded 48151 records', 'var_functions.execute_python:16': {'records': 100, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'indices': ['HSI']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
