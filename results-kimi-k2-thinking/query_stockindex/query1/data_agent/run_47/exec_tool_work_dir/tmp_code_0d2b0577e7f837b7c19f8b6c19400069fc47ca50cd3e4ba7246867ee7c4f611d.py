code = """import json
import pandas as pd
import datetime

# Load the trade data from the file
trade_data_file = locals()['var_functions.query_db:12']
with open(trade_data_file, 'r') as f:
    trade_data = json.load(f)

# Convert to DataFrame
df_trade = pd.DataFrame(trade_data)

# Let's try to parse various date formats
def parse_date(date_str):
    formats = [
        '%Y-%m-%d',
        '%B %d, %Y at %I:%M %p',    # January 02, 1987 at 12:00 AM
        '%d %b %Y, %H:%M',          # 31 Dec 1986, 00:00
        '%b %d, %Y at %I:%M %p',    # July 01, 1987 at 12:00 AM
        '%d %b %Y, %M:%S',          # Custom format
        '%B %d, %Y at %M:%S'        # Custom format
    ]
    
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_str, fmt)
        except:
            continue
    return None

# Parse dates and filter for 2020 onwards
df_trade['Parsed_Date'] = df_trade['Date'].apply(parse_date)

# Filter for records where date is not None (successfully parsed) and is >= 2020-01-01
df_2020 = df_trade[
    (df_trade['Parsed_Date'].notna()) & 
    (df_trade['Parsed_Date'] >= datetime.datetime(2020, 1, 1))
].copy()

print('__RESULT__:')
print(json.dumps({
    'total_records': len(df_trade),
    'records_2020_onwards': len(df_2020),
    'date_range': f"{df_2020['Parsed_Date'].min()} to {df_2020['Parsed_Date'].max()}" if len(df_2020) > 0 else 'No data',
    'indices_in_data': df_2020['Index'].unique().tolist()
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.list_db:2': ['index_trade'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.execute_python:10': {'N225': 6349, 'NYA': 6265, 'IXIC': 5624, 'GSPTSE': 4830, 'HSI': 4006, 'GDAXI': 3881, 'SSMI': 3559, '000001.SS': 2752, 'TWII': 2751, '399001.SZ': 2719, 'N100': 2595, 'NSEI': 1610, 'J203.JO': 1210}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
