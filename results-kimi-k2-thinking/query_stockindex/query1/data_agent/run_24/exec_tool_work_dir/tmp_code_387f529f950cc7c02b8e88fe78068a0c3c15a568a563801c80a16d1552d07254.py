code = """import json
import pandas as pd
import numpy as np
from datetime import datetime
import re

# Load trade data from file
trade_data_file = 'file_storage/functions.query_db:6.json'
with open(trade_data_file, 'r') as f:
    trade_data = json.load(f)

# Create DataFrame
df_trade = pd.DataFrame(trade_data)

# Parse dates - handle multiple formats
def parse_date(date_str):
    try:
        # Try format like: "31 Dec 1986, 00:00"
        return pd.to_datetime(date_str, format='%d %b %Y, %H:%M')
    except:
        try:
            # Try format like: "January 02, 1987 at 12:00 AM"
            return pd.to_datetime(date_str, format='%B %d, %Y at %I:%M %p')
        except:
            try:
                # Try format like: "22 Jan 1987, 00:00"
                return pd.to_datetime(date_str, format='%d %b %Y, %H:%M')
            except:
                try:
                    # Try format like: "January 15, 1987 at 12:00 AM"
                    return pd.to_datetime(date_str, format='%B %d, %Y at %I:%M %p')
                except:
                    # Last resort - let pandas infer
                    return pd.to_datetime(date_str, errors='coerce')

# Apply date parsing
df_trade['Date_parsed'] = df_trade['Date'].apply(parse_date)

# Filter for 2020 onwards
df_2020 = df_trade[df_trade['Date_parsed'] >= '2020-01-01'].copy()

# Convert price columns to float
df_2020['Open'] = pd.to_numeric(df_2020['Open'], errors='coerce')
df_2020['High'] = pd.to_numeric(df_2020['High'], errors='coerce')
df_2020['Low'] = pd.to_numeric(df_2020['Low'], errors='coerce')

# Check data
print(f'Rows since 2020: {len(df_2020)}')
print(f'Indices: {sorted(df_2020["Index"].unique())}')

print('__RESULT__:')
print(json.dumps({
    'rows_2020': len(df_2020),
    'indices_in_2020': sorted(df_2020['Index'].unique().tolist()),
    'date_range': {
        'min': str(df_2020['Date_parsed'].min()),
        'max': str(df_2020['Date_parsed'].max())
    }
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'info_var': "<class 'list'>", 'trade_indices_var': "<class 'list'>", 'result': "<class 'str'>"}, 'var_functions.execute_python:12': {'file_path_type': "<class 'str'>", 'file_path_value': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:14': {'trade_rows': 48151, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'CloseUSD'], 'sample_dates': ['31 Dec 1986, 00:00', 'January 02, 1987 at 12:00 AM', 'January 15, 1987 at 12:00 AM', 'January 16, 1987 at 12:00 AM', 'January 19, 1987 at 12:00 AM']}}

exec(code, env_args)
