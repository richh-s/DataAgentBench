code = """import json
import pandas as pd
import numpy as np
from datetime import datetime
import re

# Read the data from the file
price_data_file = var_functions.query_db:10
with open(price_data_file, 'r') as f:
    price_data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(price_data)

# Parse dates - the Date column has various formats
# We'll try to parse using pandas with errors='coerce' and then handle missing values
def parse_date(date_str):
    if pd.isna(date_str):
        return None
    
    # Try different common formats
    formats = [
        '%Y-%m-%d %H:%M:%S',  # 2000-01-04 00:00:00
        '%Y-%m-%d',           # 2000-01-04
        '%d %b %Y, %H:%M',    # 31 Dec 1986, 00:00
        '%B %d, %Y at %I:%M %p',  # January 02, 1987 at 12:00 AM
        '%d %b %Y, %H:%M:%S', # 06 Jan 1987, 00:00
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(str(date_str), fmt)
        except ValueError:
            continue
    
    # If all formats fail, try pandas parser
    try:
        return pd.to_datetime(date_str, errors='raise')
    except:
        return None

# Apply date parsing
df['Date_parsed'] = df['Date'].apply(parse_date)

# Filter out rows where date parsing failed
df_clean = df.dropna(subset=['Date_parsed']).copy()

# Convert CloseUSD to float (it might be string)
df_clean['CloseUSD'] = pd.to_numeric(df_clean['CloseUSD'], errors='coerce')

# Filter for dates from 2000-01-01 onwards
df_clean['Date_parsed'] = pd.to_datetime(df_clean['Date_parsed'])
df_clean = df_clean[df_clean['Date_parsed'] >= '2000-01-01']

# Add year-month column for grouping
df_clean['YearMonth'] = df_clean['Date_parsed'].dt.to_period('M')

# Group by index and year-month to get end-of-month prices (or closest to month end)
monthly_data = []
for idx, group in df_clean.groupby(['Index', 'YearMonth']):
    index_symbol, ym = idx
    # Get the last trading day of the month
    last_day = group.loc[group['Date_parsed'].idxmax()]
    monthly_data.append({
        'Index': index_symbol,
        'YearMonth': str(ym),
        'Date': last_day['Date_parsed'],
        'CloseUSD': last_day['CloseUSD']
    })

df_monthly = pd.DataFrame(monthly_data)

# Sort by Index and Date
df_monthly = df_monthly.sort_values(['Index', 'Date'])

# Show what we have
print('__RESULT__:')
print(json.dumps({
    'num_indices': df_monthly['Index'].nunique(),
    'total_months': len(df_monthly),
    'date_range': f"{df_monthly['Date'].min()} to {df_monthly['Date'].max()}",
    'indices': sorted(df_monthly['Index'].unique().tolist())
}))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'HSI', 'Date': '31 Dec 1986, 00:00', 'Open': '2568.300049', 'High': '2568.300049', 'Low': '2568.300049', 'Close': '2568.300049', 'Adj Close': '2568.300049', 'CloseUSD': '333.87900637'}, {'Index': 'HSI', 'Date': 'January 02, 1987 at 12:00 AM', 'Open': '2540.100098', 'High': '2540.100098', 'Low': '2540.100098', 'Close': '2540.100098', 'Adj Close': '2540.100098', 'CloseUSD': '330.21301274'}, {'Index': 'HSI', 'Date': '1987-01-05 00:00:00', 'Open': '2552.399902', 'High': '2552.399902', 'Low': '2552.399902', 'Close': '2552.399902', 'Adj Close': '2552.399902', 'CloseUSD': '331.81198726'}, {'Index': 'HSI', 'Date': '06 Jan 1987, 00:00', 'Open': '2583.899902', 'High': '2583.899902', 'Low': '2583.899902', 'Close': '2583.899902', 'Adj Close': '2583.899902', 'CloseUSD': '335.90698726000005'}, {'Index': 'HSI', 'Date': '07 Jan 1987, 00:00', 'Open': '2607.100098', 'High': '2607.100098', 'Low': '2607.100098', 'Close': '2607.100098', 'Adj Close': '2607.100098', 'CloseUSD': '338.92301274'}, {'Index': 'HSI', 'Date': '1987-01-08 00:00:00', 'Open': '2603.300049', 'High': '2603.300049', 'Low': '2603.300049', 'Close': '2603.300049', 'Adj Close': '2603.300049', 'CloseUSD': '338.42900637'}, {'Index': 'HSI', 'Date': '1987-01-09 00:00:00', 'Open': '2561.699951', 'High': '2561.699951', 'Low': '2561.699951', 'Close': '2561.699951', 'Adj Close': '2561.699951', 'CloseUSD': '333.02099363'}, {'Index': 'HSI', 'Date': '1987-01-12 00:00:00', 'Open': '2614.899902', 'High': '2614.899902', 'Low': '2614.899902', 'Close': '2614.899902', 'Adj Close': '2614.899902', 'CloseUSD': '339.93698726'}, {'Index': 'HSI', 'Date': '1987-01-13 00:00:00', 'Open': '2590.800049', 'High': '2590.800049', 'Low': '2590.800049', 'Close': '2590.800049', 'Adj Close': '2590.800049', 'CloseUSD': '336.80400637'}, {'Index': 'HSI', 'Date': '1987-01-14 00:00:00', 'Open': '2578.199951', 'High': '2578.199951', 'Low': '2578.199951', 'Close': '2578.199951', 'Adj Close': '2578.199951', 'CloseUSD': '335.16599363'}], 'var_functions.query_db:8': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
