code = """import json, pandas as pd, re
from datetime import datetime

file_path = str(locals()['var_functions.query_db:8'])

with open(file_path, 'r') as f:
    trade_data = json.load(f)

df = pd.DataFrame(trade_data)

# Convert numeric columns to float for proper calculations
numeric_cols = ['Open', 'High', 'Low', 'Close']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse dates
def parse_date(date_str):
    if not date_str or not isinstance(date_str, str):
        return None
    
    date_str_clean = re.sub(r',?\s+\d{1,2}:\d{2}.*$', '', date_str)
    date_str_clean = re.sub(r'\s+at\s+\d{1,2}:\d{2}.*$', '', date_str_clean, flags=re.IGNORECASE)
    
    formats = [
        '%d %b %Y',
        '%b %d, %Y',
        '%B %d, %Y',
        '%b %d %Y',
        '%B %d %Y'
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str_clean, fmt)
        except:
            continue
    
    return None

df['Parsed_Date'] = df['Date'].apply(parse_date)
df_clean = df.dropna(subset=['Parsed_Date'])
df_2020 = df_clean[df_clean['Parsed_Date'] >= datetime(2020, 1, 1)].copy()

# Remove rows with invalid/negative values
df_2020 = df_2020[
    (df_2020['Open'] > 0) & 
    (df_2020['High'] > 0) & 
    (df_2020['Low'] > 0)
].copy()

# Calculate intraday volatility: (High - Low) / Open
df_2020['Intraday_Volatility'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

results = []
for index in sorted(df_2020['Index'].unique()):
    subset = df_2020[df_2020['Index'] == index]
    avg_vol = subset['Intraday_Volatility'].mean()
    results.append({
        'index': index,
        'avg_volatility': round(avg_vol, 6),
        'trading_days': len(subset)
    })

results_sorted = sorted(results, key=lambda x: x['avg_volatility'], reverse=True)

print('__RESULT__:')
print(json.dumps(results_sorted, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'index_name': 'J203.JO'}, {'index_name': 'N225'}, {'index_name': 'GSPTSE'}, {'index_name': 'NSEI'}, {'index_name': 'GDAXI'}, {'index_name': 'IXIC'}, {'index_name': 'HSI'}, {'index_name': 'NYA'}, {'index_name': '000001.SS'}, {'index_name': 'SSMI'}, {'index_name': 'TWII'}, {'index_name': 'N100'}, {'index_name': '399001.SZ'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.execute_python:7': {'asia_indices': ['N225', 'HSI', '000001.SS', '399001.SZ', 'TWII', 'NSEI']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': {'total_records': 20187, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'unique_indices': ['HSI', '000001.SS', 'N225', '399001.SZ', 'NSEI', 'TWII']}}

exec(code, env_args)
