code = """import json
import pandas as pd
from datetime import datetime
import re

# Load the query result using locals() to access the variable with special characters
result_file = locals()['var_functions.query_db:8']

with open(result_file, 'r') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Parse dates - handle multiple formats
def parse_date(date_str):
    if not date_str:
        return None
    
    # Try multiple date formats
    formats = [
        '%Y-%m-%d',  # 2020-01-01
        '%d %b %Y, %H:%M',  # 31 Dec 1986, 00:00
        '%B %d, %Y at %I:%M %p',  # January 02, 1987 at 12:00 AM
        '%B %d, %Y',  # January 02, 1987
        '%Y-%m-%d %H:%M:%S',  # 2020-01-01 00:00:00
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except:
            continue
    
    # Try to extract year using regex
    year_match = re.search(r'(\d{4})', date_str)
    if year_match:
        year = int(year_match.group(1))
        if year >= 2020:
            return datetime(year, 1, 1)
    
    return None

# Apply date parsing
df['Date_parsed'] = df['Date'].apply(parse_date)

# Filter for dates since 2020
df_2020 = df[df['Date_parsed'] >= datetime(2020, 1, 1)].copy()

# Calculate intraday volatility: (High - Low) / Open
df_2020['Open'] = pd.to_numeric(df_2020['Open'], errors='coerce')
df_2020['High'] = pd.to_numeric(df_2020['High'], errors='coerce')
df_2020['Low'] = pd.to_numeric(df_2020['Low'], errors='coerce')

df_2020 = df_2020.dropna(subset=['Open', 'High', 'Low'])
df_2020 = df_2020[df_2020['Open'] > 0]  # Avoid division by zero

df_2020['Intraday_Volatility'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

# Calculate average intraday volatility by index
avg_volatility = df_2020.groupby('Index')['Intraday_Volatility'].mean().reset_index()
avg_volatility = avg_volatility.sort_values('Intraday_Volatility', ascending=False)

# Display results
result = avg_volatility.to_dict('records')

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
