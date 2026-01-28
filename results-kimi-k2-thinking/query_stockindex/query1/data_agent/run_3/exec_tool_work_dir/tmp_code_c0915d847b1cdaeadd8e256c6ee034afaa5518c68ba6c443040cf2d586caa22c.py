code = """import json
import pandas as pd
import numpy as np

# Find the data file
file_path = None
for k, v in locals().items():
    if isinstance(v, str) and '.json' in v:
        file_path = v
        break

# Get the data
with open(file_path, 'r') as f:
    trade_data = json.load(f)

# Create DataFrame
df = pd.DataFrame(trade_data)

# Convert to numeric
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['High'] = pd.to_numeric(df['High'], errors='coerce')
df['Low'] = pd.to_numeric(df['Low'], errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

# Parse dates
def parse_date(date_val):
    if pd.isna(date_val):
        return pd.NaT
    
    date_str = str(date_val)
    
    # Remove time if present
    if ' at ' in date_str:
        date_str = date_str.split(' at ')[0]
    if ',' in date_str:
        date_str = date_str.split(',')[0]
    
    # Try pandas parser with dayfirst
    try:
        return pd.to_datetime(date_str, errors='coerce', dayfirst=True)
    except:
        return pd.NaT

df['Date_parsed'] = df['Date'].apply(parse_date)

# Filter for 2020 onwards
df_2020 = df[df['Date_parsed'] >= '2020-01-01'].copy()

# Identify Asia indices based on the index symbols we found
asia_indices = ['N225', 'HSI', 'NSEI', '000001.SS', 'TWII', '399001.SZ']

# Filter for Asia indices
df_asia = df_2020[df_2020['Index'].isin(asia_indices)].copy()

# Calculate intraday volatility
df_asia['Intraday_Volatility'] = (df_asia['High'] - df_asia['Low']) / df_asia['Open']

# Remove invalid values
df_asia = df_asia[df_asia['Intraday_Volatility'].notna() & np.isfinite(df_asia['Intraday_Volatility'])]

# Calculate average volatility per index
volatility_stats = df_asia.groupby('Index')['Intraday_Volatility'].agg(['mean', 'count']).round(6)
volatility_stats = volatility_stats.sort_values('mean', ascending=False)

print("Average intraday volatility (2020+) by Asia index:")
print(volatility_stats)

result = {
    'rankings': volatility_stats.to_dict('index'),
    'top_index': volatility_stats.index[0],
    'top_volatility': float(volatility_stats.iloc[0]['mean']),
    'total_asia_records': len(df_asia)
}

print("__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': 'Loaded 48151 records', 'var_functions.execute_python:16': {'records': 100, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'indices': ['HSI']}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:22': {'total_records': 0, 'unique_indices': 0, 'asia_indices_count': 0, 'indices_sample': [], 'asia_indices': []}, 'var_functions.execute_python:26': {'records': 100, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'index_sample': ['HSI'], 'date_sample': ['31 Dec 1986, 00:00', 'January 02, 1987 at 12:00 AM', 'January 15, 1987 at 12:00 AM', 'January 16, 1987 at 12:00 AM', 'January 19, 1987 at 12:00 AM'], 'date_sample_end': ['October 19, 1987 at 12:00 AM', '26 Oct 1987, 00:00', 'October 27, 1987 at 12:00 AM', '28 Oct 1987, 00:00', '29 Oct 1987, 00:00']}, 'var_functions.execute_python:30': {'error': 'Could not load variables'}, 'var_functions.query_db:32': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:38': [{'Index': 'N225', 'count': '13874'}, {'Index': 'GSPTSE', 'count': '10526'}, {'Index': 'NSEI', 'count': '3346'}, {'Index': 'GDAXI', 'count': '8438'}, {'Index': 'J203.JO', 'count': '2346'}, {'Index': 'IXIC', 'count': '12690'}, {'Index': 'HSI', 'count': '8492'}, {'Index': '000001.SS', 'count': '5791'}, {'Index': 'SSMI', 'count': '7671'}, {'Index': 'TWII', 'count': '5869'}, {'Index': 'NYA', 'count': '13947'}, {'Index': 'N100', 'count': '5474'}, {'Index': '399001.SZ', 'count': '5760'}]}

exec(code, env_args)
