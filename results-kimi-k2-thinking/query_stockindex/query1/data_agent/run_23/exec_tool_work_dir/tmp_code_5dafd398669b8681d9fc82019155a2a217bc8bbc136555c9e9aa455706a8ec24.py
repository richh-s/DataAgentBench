code = """import json
import pandas as pd
from datetime import datetime

# Load data from the file
with open('file_storage/functions.query_db:28.json', 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Parse dates
def parse_date(date_str):
    try:
        if 'at' in str(date_str):
            # Handle format like "January 01, 2020 at 12:00 AM"
            return pd.to_datetime(date_str, format='%B %d, %Y at %I:%M %p', errors='coerce')
        elif '-' in str(date_str):
            # Handle format like "2020-01-01 00:00:00" or similar
            return pd.to_datetime(date_str, errors='coerce')
        elif ',' in str(date_str) and ':' in str(date_str):
            # Handle format like "01 Jan 2020, 00:00"
            return pd.to_datetime(date_str, format='%d %b %Y, %H:%M', errors='coerce')
        else:
            return pd.to_datetime(date_str, errors='coerce')
    except:
        return pd.to_datetime(date_str, errors='coerce')

# Apply date parsing
df['Date_parsed'] = df['Date'].apply(parse_date)

# Filter for dates from 2020-01-01 onwards
df_filtered = df[df['Date_parsed'] >= '2020-01-01'].copy()

# Convert numeric columns
df_filtered['Open'] = pd.to_numeric(df_filtered['Open'])
df_filtered['High'] = pd.to_numeric(df_filtered['High'])
df_filtered['Low'] = pd.to_numeric(df_filtered['Low'])

# Calculate intraday volatility: (High - Low) / Open
df_filtered['intraday_volatility'] = (df_filtered['High'] - df_filtered['Low']) / df_filtered['Open']

# Group by index and calculate average
def get_exchange_name(index_symbol):
    mapping = {
        'N225': 'Tokyo Stock Exchange',
        'HSI': 'Hong Kong Stock Exchange',
        '000001.SS': 'Shanghai Stock Exchange',
        '399001.SZ': 'Shenzhen Stock Exchange',
        'TWII': 'Taiwan Stock Exchange',
        'NSEI': 'National Stock Exchange of India'
    }
    return mapping.get(index_symbol, 'Unknown')

results = df_filtered.groupby('Index').agg({
    'intraday_volatility': ['mean', 'count'],
    'Date_parsed': ['min', 'max']
}).round(6)

results.columns = ['avg_volatility', 'count', 'start_date', 'end_date']
results = results.reset_index()
results['exchange'] = results['Index'].apply(get_exchange_name)
results = results.sort_values('avg_volatility', ascending=False)

print('__RESULT__:')
print(results.to_json(orient='records', date_format='iso'))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': [{'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'record_count': '5791'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'record_count': '5760'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'record_count': '8438'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'record_count': '10526'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'record_count': '8492'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'record_count': '12690'}, {'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'record_count': '2346'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'record_count': '5474'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'record_count': '13874'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00', 'last_date': 'September 30, 2014 at 12:00 AM', 'record_count': '3346'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'record_count': '13947'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'record_count': '7671'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'record_count': '5869'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': [{'Index': 'N225', 'mean': 0.0135564246, 'count': 279}, {'Index': 'TWII', 'mean': 0.0134712558, 'count': 285}], 'var_functions.query_db:24': [{'Index': 'N225', 'count_2020': '242'}, {'Index': 'NSEI', 'count_2020': '250'}, {'Index': 'HSI', 'count_2020': '248'}, {'Index': '000001.SS', 'count_2020': '243'}, {'Index': 'TWII', 'count_2020': '245'}, {'Index': '399001.SZ', 'count_2020': '243'}], 'var_functions.query_db:26': [{'Index': 'NSEI', 'Date': '01 Jan 2020, 00:00', 'Open': '12202.15039', 'High': '12222.2002', 'Low': '12165.29981'}, {'Index': 'NSEI', 'Date': '2020-01-02 00:00:00', 'Open': '12198.54981', 'High': '12289.90039', 'Low': '12195.25'}, {'Index': 'NSEI', 'Date': 'January 03, 2020 at 12:00 AM', 'Open': '12261.09961', 'High': '12265.59961', 'Low': '12191.34961'}, {'Index': 'NSEI', 'Date': '2020-01-06 00:00:00', 'Open': '12170.59961', 'High': '12179.09961', 'Low': '11974.2002'}, {'Index': 'NSEI', 'Date': 'January 07, 2020 at 12:00 AM', 'Open': '12079.09961', 'High': '12152.15039', 'Low': '12005.34961'}, {'Index': 'NSEI', 'Date': 'January 08, 2020 at 12:00 AM', 'Open': '11939.09961', 'High': '12044.9502', 'Low': '11929.59961'}, {'Index': 'NSEI', 'Date': '09 Jan 2020, 00:00', 'Open': '12153.15039', 'High': '12224.04981', 'Low': '12132.54981'}, {'Index': 'NSEI', 'Date': '2020-01-10 00:00:00', 'Open': '12271.0', 'High': '12311.2002', 'Low': '12213.2002'}, {'Index': 'NSEI', 'Date': '13 Jan 2020, 00:00', 'Open': '12296.7002', 'High': '12337.75', 'Low': '12285.79981'}, {'Index': 'NSEI', 'Date': '14 Jan 2020, 00:00', 'Open': '12333.09961', 'High': '12374.25', 'Low': '12308.7002'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
