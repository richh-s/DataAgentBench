code = """import json
import pandas as pd
from datetime import datetime

# Read the full query result using locals()
storage_key = 'var_functions.query_db:8'
file_path = locals()[storage_key]

print(f"Reading from file: {file_path}")

with open(file_path, 'r') as f:
    trade_data = json.load(f)

print(f"Loaded {len(trade_data)} records")
print(f"Sample records: {trade_data[:3]}")

# Convert to DataFrame
df = pd.DataFrame(trade_data)

# Convert Date to datetime and CloseUSD to float
df['Date'] = pd.to_datetime(df['Date'])
df['CloseUSD'] = df['CloseUSD'].astype(float)

print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
print(f"Indices: {sorted(df['Index'].unique())}")
print(f"Number of indices: {len(df['Index'].unique())}")

# Check data availability per index
index_stats = df.groupby('Index').agg({
    'Date': ['min', 'max', 'count']
}).round(2)

index_stats.columns = ['First_Date', 'Last_Date', 'Days_Count']
index_stats = index_stats.reset_index()

print("Index statistics:")
for _, row in index_stats.iterrows():
    print(f"{row['Index']}: {row['First_Date'][:10]} to {row['Last_Date'][:10]}, {row['Days_Count']} days")

# Calculate the number of years of data for each index
current_date = datetime.now()
index_stats['Years_of_Data'] = index_stats['Last_Date'].apply(
    lambda x: (pd.to_datetime(x) - pd.to_datetime('2000-01-01')).days / 365.25
)

print("\nYears of data since 2000:")
for _, row in index_stats.iterrows():
    print(f"{row['Index']}: {row['Years_of_Data']:.2f} years")"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
