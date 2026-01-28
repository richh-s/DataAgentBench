code = """import json
import pandas as pd
import datetime

# Load the trade data from the file
trade_data_file = locals()['var_functions.query_db:12']
with open(trade_data_file, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df_trade = pd.DataFrame(trade_data)

# Define date parsing function for multiple formats
def parse_date(date_str):
    formats = [
        '%Y-%m-%d',
        '%B %d, %Y at %I:%M %p',    # January 02, 1987 at 12:00 AM
        '%d %b %Y, %H:%M',          # 31 Dec 1986, 00:00
        '%b %d, %Y at %I:%M %p',    # July 01, 1987 at 12:00 AM
    ]
    
    for fmt in formats:
        try:
            return pd.to_datetime(date_str, format=fmt)
        except:
            continue
    
    # Fallback to pandas general parser
    try:
        return pd.to_datetime(date_str, errors='coerce')
    except:
        return None

# Parse dates and convert data types
df_trade['Parsed_Date'] = df_trade['Date'].apply(parse_date)
df_trade['Open'] = pd.to_numeric(df_trade['Open'], errors='coerce')
df_trade['High'] = pd.to_numeric(df_trade['High'], errors='coerce')
df_trade['Low'] = pd.to_numeric(df_trade['Low'], errors='coerce')
df_trade['Close'] = pd.to_numeric(df_trade['Close'], errors='coerce')

# Filter for dates >= 2020-01-01
df_2020 = df_trade[
    (df_trade['Parsed_Date'].notna()) & 
    (df_trade['Parsed_Date'] >= pd.Timestamp('2020-01-01')) &
    (df_trade['Open'] > 0) &  # Ensure valid prices
    (df_trade['High'] > 0) &
    (df_trade['Low'] > 0)
].copy()

# Calculate intraday volatility: (High - Low) / Open
df_2020['Intraday_Volatility'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

# Calculate average intraday volatility per index
avg_volatility = df_2020.groupby('Index')['Intraday_Volatility'].agg(['mean', 'count']).reset_index()

# Map indices to their exchanges and regions
index_to_exchange = {
    'N225': 'Tokyo Stock Exchange',
    'HSI': 'Hong Kong Stock Exchange',
    '000001.SS': 'Shanghai Stock Exchange',
    '399001.SZ': 'Shenzhen Stock Exchange',
    'TWII': 'Taiwan Stock Exchange',
    'NSEI': 'National Stock Exchange of India'
}

# Add exchange info
avg_volatility['Exchange'] = avg_volatility['Index'].map(index_to_exchange)

# Focus on Asian markets (we already filtered for Asian indices)
avg_volatility = avg_volatility.sort_values('mean', ascending=False)

# Get the top index
if len(avg_volatility) > 0:
    top_index = avg_volatility.iloc[0]
    result = {
        'index': top_index['Index'],
        'exchange': top_index['Exchange'],
        'avg_intraday_volatility': float(top_index['mean']),
        'trading_days_analyzed': int(top_index['count'])
    }
else:
    result = {'error': 'No data found'}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.execute_python:10': {'N225': 6349, 'NYA': 6265, 'IXIC': 5624, 'GSPTSE': 4830, 'HSI': 4006, 'GDAXI': 3881, 'SSMI': 3559, '000001.SS': 2752, 'TWII': 2751, '399001.SZ': 2719, 'N100': 2595, 'NSEI': 1610, 'J203.JO': 1210}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'total_records': 20187, 'records_2020_onwards': 973, 'date_range': '2020-01-02 00:00:00 to 2021-06-03 00:00:00', 'indices_in_data': ['HSI', '000001.SS', 'N225', '399001.SZ', 'NSEI', 'TWII']}}

exec(code, env_args)
