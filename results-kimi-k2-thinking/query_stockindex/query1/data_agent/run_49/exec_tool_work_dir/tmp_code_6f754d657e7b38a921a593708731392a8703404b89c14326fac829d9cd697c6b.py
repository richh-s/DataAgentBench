code = """import json
import pandas as pd
from datetime import datetime
import re

# Read the full data
file_path = locals()['var_functions.query_db:26']
with open(file_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Try to parse dates with multiple patterns
def parse_date(date_str):
    date_str = str(date_str)
    patterns = [
        (r'(\d{4})-(\d{2})-(\d{2}).*', '%Y-%m-%d'),  # 2020-03-13 00:00:00
        (r'(\d{2}) (\w{3}) (\d{4}),.*', '%d %b %Y'),  # 31 Dec 1986, 00:00
        (r'(\w+) (\d{1,2}), (\d{4}) at.*', '%B %d, %Y'),  # January 02, 1987 at 12:00 AM
    ]
    
    for pattern, fmt in patterns:
        if re.match(pattern, date_str):
            try:
                # Extract just the date part
                if fmt == '%Y-%m-%d':
                    match = re.match(r'(\d{4}-\d{2}-\d{2})', date_str)
                    if match:
                        return datetime.strptime(match.group(1), fmt)
                elif fmt == '%d %b %Y':
                    match = re.match(r'(\d{1,2} \w{3} \d{4})', date_str)
                    if match:
                        return datetime.strptime(match.group(1), fmt)
                elif fmt == '%B %d, %Y':
                    match = re.match(r'(\w+ \d{1,2}, \d{4})', date_str)
                    if match:
                        return datetime.strptime(match.group(1), fmt)
            except:
                continue
    return None

# Parse dates
df['parsed_date'] = df['Date'].apply(parse_date)

# Convert numeric columns
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['High'] = pd.to_numeric(df['High'], errors='coerce')
df['Low'] = pd.to_numeric(df['Low'], errors='coerce')

# Filter for 2020 and later
df_2020 = df[df['parsed_date'] >= datetime(2020, 1, 1)].copy()

# Remove rows with missing values
df_2020 = df_2020.dropna(subset=['Open', 'High', 'Low', 'parsed_date'])

# Calculate intraday volatility
df_2020['intraday_volatility'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

# Group by index and calculate average volatility
result = df_2020.groupby('Index')['intraday_volatility'].agg(['mean', 'count']).reset_index()
result = result.sort_values('mean', ascending=False)

print('__RESULT__:')
print(result.to_json(orient='records'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}], 'var_functions.query_db:8': [{'Index': 'HSI', 'count': '8492'}, {'Index': '000001.SS', 'count': '5791'}, {'Index': 'TWII', 'count': '5869'}, {'Index': '399001.SZ', 'count': '5760'}, {'Index': 'N225', 'count': '13874'}, {'Index': 'NSEI', 'count': '3346'}], 'var_functions.query_db:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': [], 'var_functions.query_db:16': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.execute_python:21': {'total_records': 20187, 'sample': [{'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Index': 'HSI'}, {'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Index': 'HSI'}, {'Date': 'January 15, 1987 at 12:00 AM', 'Open': '2559.100098', 'High': '2559.100098', 'Low': '2559.100098', 'Index': 'HSI'}]}, 'var_functions.query_db:24': [{'Date': '2020-03-13 00:00:00', 'Index': 'HSI'}, {'Date': '2020-03-20 00:00:00', 'Index': 'HSI'}, {'Date': '2020-03-23 00:00:00', 'Index': 'HSI'}, {'Date': '2020-03-25 00:00:00', 'Index': 'HSI'}, {'Date': '2020-03-27 00:00:00', 'Index': 'HSI'}, {'Date': '2020-03-30 00:00:00', 'Index': 'HSI'}, {'Date': '2020-04-01 00:00:00', 'Index': 'HSI'}, {'Date': '2020-04-03 00:00:00', 'Index': 'HSI'}, {'Date': '2020-04-06 00:00:00', 'Index': 'HSI'}, {'Date': '2020-04-07 00:00:00', 'Index': 'HSI'}, {'Date': '2020-04-09 00:00:00', 'Index': 'HSI'}, {'Date': '2020-04-21 00:00:00', 'Index': 'HSI'}, {'Date': '2020-04-22 00:00:00', 'Index': 'HSI'}, {'Date': '2020-04-23 00:00:00', 'Index': 'HSI'}, {'Date': '2020-05-04 00:00:00', 'Index': 'HSI'}, {'Date': '2020-05-11 00:00:00', 'Index': 'HSI'}, {'Date': '2020-05-15 00:00:00', 'Index': 'HSI'}, {'Date': '2020-05-18 00:00:00', 'Index': 'HSI'}, {'Date': '2020-05-19 00:00:00', 'Index': 'HSI'}, {'Date': '2020-05-29 00:00:00', 'Index': 'HSI'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'total_rows': 43132, 'columns': ['Index', 'Date', 'Open', 'High', 'Low'], 'sample': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902'}]}, 'var_functions.execute_python:30': {'pattern_counts': {'other': 330, 'dd_mm_yyyy': 327, 'iso_format': 343}, 'sample_dates': ['31 Dec 1986, 00:00', 'January 02, 1987 at 12:00 AM', '1987-01-05 00:00:00', '06 Jan 1987, 00:00', '07 Jan 1987, 00:00', '1987-01-08 00:00:00', '1987-01-09 00:00:00', '1987-01-12 00:00:00', '1987-01-13 00:00:00', '1987-01-14 00:00:00']}}

exec(code, env_args)
