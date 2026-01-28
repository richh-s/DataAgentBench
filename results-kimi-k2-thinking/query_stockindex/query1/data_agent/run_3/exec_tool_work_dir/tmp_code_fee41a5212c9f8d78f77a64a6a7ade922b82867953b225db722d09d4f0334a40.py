code = """import json
import pandas as pd
import numpy as np
from datetime import datetime
import os

# Get the file path
file_path = None
for var_name in locals().keys():
    var_value = locals()[var_name]
    if isinstance(var_value, str) and '.json' in var_value and 'query_db_46' in var_name:
        file_path = var_value
        break

# Load the data
if file_path and os.path.exists(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    print(f"Loaded {len(data)} records")
else:
    print("File not found")
    exit()

# Create DataFrame
df = pd.DataFrame(data)

# Convert numeric columns
numeric_cols = ['Open', 'High', 'Low', 'Close']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse dates
# Handle multiple formats
def parse_date(date_str):
    if pd.isna(date_str):
        return pd.NaT
    
    date_str = str(date_str)
    
    # Remove time portion if present
    if ' at ' in date_str:
        date_str = date_str.split(' at ')[0]
    if ',' in date_str:
        date_str = date_str.split(',')[0]
    
    # Try pandas parser with dayfirst=True for formats like "31 Dec 1986"
    try:
        return pd.to_datetime(date_str, dayfirst=True)
    except:
        return pd.to_datetime(date_str, errors='coerce')

df['Date_parsed'] = df['Date'].apply(parse_date)

# Check date range
min_date = df['Date_parsed'].min()
max_date = df['Date_parsed'].max()
print(f"Date range: {min_date} to {max_date}")

# Filter for 2020 and later
df_2020 = df[df['Date_parsed'] >= '2020-01-01'].copy()
print(f"Records from 2020+: {len(df_2020)}")

# Check which indices we have
asia_indices = ['N225', 'HSI', 'NSEI', '000001.SS', 'TWII', '399001.SZ']
available_indices = df_2020['Index'].unique().tolist()
print(f"Available indices: {available_indices}")

# Filter for Asia indices only
df_asia = df_2020[df_2020['Index'].isin(asia_indices)].copy()
print(f"Asia indices records: {len(df_asia)}")

# Calculate intraday volatility: (High - Low) / Open
df_asia['Intraday_Volatility'] = (df_asia['High'] - df_asia['Low']) / df_asia['Open']

# Remove invalid values (NaN, infinite)
var_valid = df_asia['Intraday_Volatility'].notna() & np.isfinite(df_asia['Intraday_Volatility'])
df_asia = df_asia[var_valid]

print(f"Valid volatility calculations: {len(df_asia)}")

# Calculate average intraday volatility per index
volatility_stats = df_asia.groupby('Index')['Intraday_Volatility'].agg(['mean', 'count']).round(6)
volatility_stats = volatility_stats.sort_values('mean', ascending=False)

print("\\nAverage Intraday Volatility by Index (2020+):")
print(volatility_stats)

# Get the top index
top_index = volatility_stats.index[0]
top_volatility = volatility_stats.iloc[0]['mean']

result = {
    'top_index': top_index,
    'top_avg_volatility': float(top_volatility),
    'rankings': volatility_stats.to_dict('index'),
    'analysis_summary': {
        'total_records_analyzed': len(df_asia),
        'indices_analyzed': asia_indices,
        'indices_with_data': available_indices
    }
}

print("\\n__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': 'Loaded 48151 records', 'var_functions.execute_python:16': {'records': 100, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'indices': ['HSI']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'total_records': 0, 'unique_indices': 0, 'asia_indices_count': 0, 'indices_sample': [], 'asia_indices': []}, 'var_functions.execute_python:26': {'records': 100, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'index_sample': ['HSI'], 'date_sample': ['31 Dec 1986, 00:00', 'January 02, 1987 at 12:00 AM', 'January 15, 1987 at 12:00 AM', 'January 16, 1987 at 12:00 AM', 'January 19, 1987 at 12:00 AM'], 'date_sample_end': ['October 19, 1987 at 12:00 AM', '26 Oct 1987, 00:00', 'October 27, 1987 at 12:00 AM', '28 Oct 1987, 00:00', '29 Oct 1987, 00:00']}, 'var_functions.execute_python:30': {'error': 'Could not load variables'}, 'var_functions.query_db:32': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:38': [{'Index': 'N225', 'count': '13874'}, {'Index': 'GSPTSE', 'count': '10526'}, {'Index': 'NSEI', 'count': '3346'}, {'Index': 'GDAXI', 'count': '8438'}, {'Index': 'J203.JO', 'count': '2346'}, {'Index': 'IXIC', 'count': '12690'}, {'Index': 'HSI', 'count': '8492'}, {'Index': '000001.SS', 'count': '5791'}, {'Index': 'SSMI', 'count': '7671'}, {'Index': 'TWII', 'count': '5869'}, {'Index': 'NYA', 'count': '13947'}, {'Index': 'N100', 'count': '5474'}, {'Index': '399001.SZ', 'count': '5760'}], 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.execute_python:44': {'file_path': 'file_storage/functions.query_db:2.json', 'records': 100}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json'}

exec(code, env_args)
