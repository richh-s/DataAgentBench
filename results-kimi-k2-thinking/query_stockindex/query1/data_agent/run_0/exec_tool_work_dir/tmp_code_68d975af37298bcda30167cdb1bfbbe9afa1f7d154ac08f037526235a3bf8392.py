code = """import json
import pandas as pd
from datetime import datetime

# Read the data from the file
file_path = var_functions.query_db:8
with open(file_path, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Display basic info about the data
print(f"Total records: {len(df)}")
print(f"Indices: {df['Index'].unique()}")
print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
print(f"First few records:")
print(df.head())

# Clean and parse dates
def parse_date(date_str):
    try:
        # Try different date formats
        formats = [
            '%Y-%m-%d',
            '%d %b %Y, %H:%M',
            '%B %d, %Y at %I:%M %p',
            '%b %d, %Y at %I:%M %p'
        ]
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except:
                continue
        return None
    except:
        return None

df['ParsedDate'] = df['Date'].apply(parse_date)
df = df.dropna(subset=['ParsedDate'])

# Filter for 2020 and later
df_2020 = df[df['ParsedDate'] >= datetime(2020, 1, 1)].copy()

print(f"\nRecords from 2020 onwards: {len(df_2020)}")

# Convert price columns to float
df_2020['Open'] = pd.to_numeric(df_2020['Open'], errors='coerce')
df_2020['High'] = pd.to_numeric(df_2020['High'], errors='coerce')
df_2020['Low'] = pd.to_numeric(df_2020['Low'], errors='coerce')

# Remove rows with missing or zero Open prices
df_2020 = df_2020.dropna(subset=['Open', 'High', 'Low'])
df_2020 = df_2020[df_2020['Open'] > 0]

# Calculate intraday volatility
 df_2020['IntradayVolatility'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

# Group by index and calculate average volatility
volatility_by_index = df_2020.groupby('Index')['IntradayVolatility'].agg(['mean', 'count']).reset_index()
volatility_by_index = volatility_by_index.sort_values('mean', ascending=False)

print("\nAverage intraday volatility by index (2020+):")
print(volatility_by_index)

# Get the index with highest volatility
top_index = volatility_by_index.iloc[0]

print(f"\n\n=== RESULT ===")
print(f"Index: {top_index['Index']}")
print(f"Average Intraday Volatility: {top_index['mean']:.4f}")
print(f"Trading Days: {top_index['count']}")"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
