code = """import json
import pandas as pd
from datetime import datetime

# Read the data from the file
with open('var_functions.query_db:8', 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Clean and parse dates - handle various date formats
def parse_date(date_str):
    try:
        # Remove time portion if exists
        if 'at' in date_str:
            date_part = date_str.split(' at ')[0]
        elif ',' in date_str:
            date_part = date_str.split(',')[0]
        else:
            date_part = date_str
        
        # Try different date formats
        formats = [
            '%B %d, %Y',  # January 02, 2020
            '%d %b %Y',   # 02 Jan 2020
            '%Y-%m-%d',   # 2020-01-02
            '%b %d %Y',   # Jan 02 2020
            '%m/%d/%Y'    # 01/02/2020
        ]
        
        for fmt in formats:
            try:
                return datetime.strptime(date_part.strip(), fmt)
            except:
                continue
        
        # If all formats fail, return None
        return None
    except:
        return None

# Apply date parsing
df['Date_parsed'] = df['Date'].apply(parse_date)

# Filter for dates from 2020 onwards
df_2020 = df[df['Date_parsed'] >= datetime(2020, 1, 1)].copy()

# Convert price columns to numeric
df_2020['Open'] = pd.to_numeric(df_2020['Open'], errors='coerce')
df_2020['High'] = pd.to_numeric(df_2020['High'], errors='coerce')
df_2020['Low'] = pd.to_numeric(df_2020['Low'], errors='coerce')

# Calculate intraday volatility for each day: (High - Low) / Open
df_2020['Intraday_Volatility'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

# Group by index and calculate average intraday volatility
avg_volatility = df_2020.groupby('Index')['Intraday_Volatility'].agg(['mean', 'count']).round(6)
avg_volatility.columns = ['Avg_Intraday_Volatility', 'Days_Count']

# Sort by average volatility descending
avg_volatility_sorted = avg_volatility.sort_values('Avg_Intraday_Volatility', ascending=False)

print('__RESULT__:')
print(avg_volatility_sorted.to_json())"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
