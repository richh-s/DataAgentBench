code = """import json, pandas as pd, re
from datetime import datetime

file_path = str(locals()['var_functions.query_db:8'])

with open(file_path, 'r') as f:
    trade_data = json.load(f)

df = pd.DataFrame(trade_data)

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
df_valid = df.dropna(subset=['Parsed_Date']).copy()
df_valid['Year'] = df_valid['Parsed_Date'].dt.year

# Show year distribution
year_dist = df_valid['Year'].value_counts().sort_index()
print('Year distribution in data:')
print(year_dist)

# Show date range for each index
indices = sorted(df_valid['Index'].unique())
index_ranges = {}
for idx in indices:
    subset = df_valid[df_valid['Index'] == idx]
    index_ranges[idx] = {
        'min_year': int(subset['Year'].min()),
        'max_year': int(subset['Year'].max()),
        'records': len(subset)
    }

print('\nIndex date ranges:')
for idx, info in index_ranges.items():
    print(f"{idx}: {info['min_year']}-{info['max_year']} ({info['records']} records)")

result = {
    'year_distribution': dict(year_dist),
    'index_ranges': index_ranges
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'index_name': 'J203.JO'}, {'index_name': 'N225'}, {'index_name': 'GSPTSE'}, {'index_name': 'NSEI'}, {'index_name': 'GDAXI'}, {'index_name': 'IXIC'}, {'index_name': 'HSI'}, {'index_name': 'NYA'}, {'index_name': '000001.SS'}, {'index_name': 'SSMI'}, {'index_name': 'TWII'}, {'index_name': 'N100'}, {'index_name': '399001.SZ'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.execute_python:7': {'asia_indices': ['N225', 'HSI', '000001.SS', '399001.SZ', 'TWII', 'NSEI']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': {'total_records': 20187, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'unique_indices': ['HSI', '000001.SS', 'N225', '399001.SZ', 'NSEI', 'TWII']}, 'var_functions.execute_python:24': [{'index': '399001.SZ', 'avg_volatility': 0.019375, 'trading_days': 39}, {'index': 'NSEI', 'avg_volatility': 0.017565, 'trading_days': 34}, {'index': 'HSI', 'avg_volatility': 0.014769, 'trading_days': 40}, {'index': 'N225', 'avg_volatility': 0.014314, 'trading_days': 40}, {'index': '000001.SS', 'avg_volatility': 0.01418, 'trading_days': 29}, {'index': 'TWII', 'avg_volatility': 0.013563, 'trading_days': 45}], 'var_functions.execute_python:28': []}

exec(code, env_args)
