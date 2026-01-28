code = """import json, pandas as pd, re
from datetime import datetime

file_path = str(locals()['var_functions.query_db:8'])

with open(file_path, 'r') as f:
    trade_data = json.load(f)

df = pd.DataFrame(trade_data)

# Parse dates - handle various formats
def parse_date(date_str):
    if not date_str or not isinstance(date_str, str):
        return None
    
    # Try ISO format first (DD Mon YYYY, HH:MM)
    match = re.search(r'(\d{1,2})\s+(\w{3})\s+(\d{4})', date_str, re.IGNORECASE)
    if match:
        try:
            day, month, year = match.groups()
            return datetime.strptime(f"{day} {month} {year}", "%d %b %Y")
        except:
            pass
    
    # Try Month Day, Year pattern
    patterns = [
        r'(\w+)\s+(\d{1,2}),\s+(\d{4})',
        r'(\w+)\s+(\d{1,2})\s+(\d{4})',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, date_str, re.IGNORECASE)
        if match:
            try:
                month, day, year = match.groups()
                return datetime.strptime(f"{month} {day} {year}", "%b %d %Y")
            except:
                try:
                    return datetime.strptime(f"{month} {day} {year}", "%B %d %Y")
                except:
                    continue
    
    return None

# Apply date parsing
df['Parsed_Date'] = df['Date'].apply(parse_date)

# Filter out null dates and dates before 2020
df_clean = df[df['Parsed_Date'].notna()].copy()
df_2020 = df_clean[df_clean['Parsed_Date'] >= datetime(2020, 1, 1)].copy()

# Remove rows with invalid values
df_2020 = df_2020[
    (df_2020['Open'].notna()) & (df_2020['Open'] > 0) &
    (df_2020['High'].notna()) & (df_2020['High'] > 0) &
    (df_2020['Low'].notna()) & (df_2020['Low'] > 0)
].copy()

# Calculate intraday volatility: (High - Low) / Open
df_2020['Intraday_Volatility'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

print(f'After filtering for 2020+ data: {len(df_2020)} records')

results = {}
for index in df_2020['Index'].unique():
    subset = df_2020[df_2020['Index'] == index]
    avg_volatility = subset['Intraday_Volatility'].mean()
    count = len(subset)
    results[index] = {
        'avg_intraday_volatility': avg_volatility,
        'trading_days': count,
        'start_date': str(subset['Parsed_Date'].min().date()),
        'end_date': str(subset['Parsed_Date'].max().date())
    }

# Sort by average intraday volatility
sorted_results = dict(sorted(results.items(), key=lambda x: x[1]['avg_intraday_volatility'], reverse=True))

print('\nAverage intraday volatility by index (2020+):')
for idx, data in sorted_results.items():
    print(f"{idx}: {data['avg_intraday_volatility']:.4f} ({data['trading_days']} days)")

print('__RESULT__:')
print(json.dumps(sorted_results))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'index_name': 'J203.JO'}, {'index_name': 'N225'}, {'index_name': 'GSPTSE'}, {'index_name': 'NSEI'}, {'index_name': 'GDAXI'}, {'index_name': 'IXIC'}, {'index_name': 'HSI'}, {'index_name': 'NYA'}, {'index_name': '000001.SS'}, {'index_name': 'SSMI'}, {'index_name': 'TWII'}, {'index_name': 'N100'}, {'index_name': '399001.SZ'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.execute_python:7': {'asia_indices': ['N225', 'HSI', '000001.SS', '399001.SZ', 'TWII', 'NSEI']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': {'total_records': 20187, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'unique_indices': ['HSI', '000001.SS', 'N225', '399001.SZ', 'NSEI', 'TWII']}}

exec(code, env_args)
