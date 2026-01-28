code = """import json, pandas as pd, re
from datetime import datetime

file_path = str(locals()['var_functions.query_db:8'])

with open(file_path, 'r') as f:
    trade_data = json.load(f)

df = pd.DataFrame(trade_data)

numeric_cols = ['Open', 'High', 'Low', 'Close']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse dates
def parse_date_flexible(date_str):
    if not date_str or not isinstance(date_str, str):
        return None
    year_match = re.search(r'(\d{4})', date_str)
    if not year_match:
        return None
    year = int(year_match.group(1))
    month_names = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    month_num = None
    for i, month_name in enumerate(month_names, 1):
        if month_name in date_str.lower():
            month_num = i
            break
    if not month_num:
        return None
    day_match = re.search(r'\b(\d{1,2})\b', date_str)
    if not day_match:
        return None
    day = int(day_match.group(1))
    try:
        return datetime(year, month_num, day)
    except:
        return None

df['Parsed_Date'] = df['Date'].apply(parse_date_flexible)
df_clean = df.dropna(subset=['Parsed_Date'])
df_2020 = df_clean[df_clean['Parsed_Date'] >= datetime(2020, 1, 1)].copy()

# Calculate intraday volatility
df_2020 = df_2020[(df_2020['Open'] > 0) & (df_2020['High'] > 0) & (df_2020['Low'] > 0)].copy()
df_2020['Intraday_Volatility'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

results = []
for index in sorted(df_2020['Index'].unique()):
    subset = df_2020[df_2020['Index'] == index]
    avg_vol = subset['Intraday_Volatility'].mean()
    results.append({
        'index': index,
        'avg_volatility': float(avg_vol),
        'trading_days': len(subset)
    })

def get_key(x):
    return x['avg_volatility']

results_sorted = sorted(results, key=get_key, reverse=True)

print('__RESULT__:')
print(json.dumps(results_sorted))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'index_name': 'J203.JO'}, {'index_name': 'N225'}, {'index_name': 'GSPTSE'}, {'index_name': 'NSEI'}, {'index_name': 'GDAXI'}, {'index_name': 'IXIC'}, {'index_name': 'HSI'}, {'index_name': 'NYA'}, {'index_name': '000001.SS'}, {'index_name': 'SSMI'}, {'index_name': 'TWII'}, {'index_name': 'N100'}, {'index_name': '399001.SZ'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.execute_python:7': {'asia_indices': ['N225', 'HSI', '000001.SS', '399001.SZ', 'TWII', 'NSEI']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': {'total_records': 20187, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'unique_indices': ['HSI', '000001.SS', 'N225', '399001.SZ', 'NSEI', 'TWII']}, 'var_functions.execute_python:24': [{'index': '399001.SZ', 'avg_volatility': 0.019375, 'trading_days': 39}, {'index': 'NSEI', 'avg_volatility': 0.017565, 'trading_days': 34}, {'index': 'HSI', 'avg_volatility': 0.014769, 'trading_days': 40}, {'index': 'N225', 'avg_volatility': 0.014314, 'trading_days': 40}, {'index': '000001.SS', 'avg_volatility': 0.01418, 'trading_days': 29}, {'index': 'TWII', 'avg_volatility': 0.013563, 'trading_days': 45}]}

exec(code, env_args)
