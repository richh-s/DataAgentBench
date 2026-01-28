code = """import json
import pandas as pd

# Find and load the file
file_path = None
for k, v in locals().items():
    if isinstance(v, str) and '.json' in v:
        file_path = v
        break

with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Create DataFrame
df = pd.DataFrame(trade_data)

# Clean data
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['High'] = pd.to_numeric(df['High'], errors='coerce')
df['Low'] = pd.to_numeric(df['Low'], errors='coerce')

# Check date column - it might be in different format or named differently
print('Date column sample:', df['Date'].head().tolist())
print('All indices:', sorted(df['Index'].unique().tolist()))

# Try to understand the date range
df['Date_parsed'] = pd.to_datetime(df['Date'], errors='coerce')
print('Date range:', df['Date_parsed'].min(), 'to', df['Date_parsed'].max())

# Filter most recent data (last few years)
recent_df = df[df['Date_parsed'] >= '2018-01-01'].copy()
print('Recent records:', len(recent_df))

print("__RESULT__:")
print(json.dumps({
    'total_records': len(df),
    'recent_records': len(recent_df),
    'all_indices': sorted(df['Index'].unique().tolist()),
    'date_range': {
        'min': str(df['Date_parsed'].min()),
        'max': str(df['Date_parsed'].max())
    },
    'date_sample': df['Date'].head().tolist()
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': 'Loaded 48151 records', 'var_functions.execute_python:16': {'records': 100, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'indices': ['HSI']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'total_records': 0, 'unique_indices': 0, 'asia_indices_count': 0, 'indices_sample': [], 'asia_indices': []}}

exec(code, env_args)
