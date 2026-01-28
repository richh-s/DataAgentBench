code = """import json
import pandas as pd
from datetime import datetime

# Load the full dataset file path from query result
data_file = str(locals()['var_functions.query_db:8'])

# Read the JSON file
with open(data_file, 'r') as f:
    trade_data = json.load(f)

# Create DataFrame
df = pd.DataFrame(trade_data)

# Convert numeric columns
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['High'] = pd.to_numeric(df['High'], errors='coerce')
df['Low'] = pd.to_numeric(df['Low'], errors='coerce')

# Parse the date format "DD Mon YYYY, HH:MM"
# Example: "01 Apr 2003, 00:00"
def parse_date(date_str):
    try:
        # Extract first part before comma
        date_part = date_str.split(',')[0]
        return datetime.strptime(date_part.strip(), '%d %b %Y')
    except:
        return None

df['Parsed_Date'] = df['Date'].apply(parse_date)

# Filter for 2020 and later
df_2020 = df[df['Parsed_Date'] >= datetime(2020, 1, 1)].copy()

# Remove invalid data
df_2020 = df_2020[
    (df_2020['Open'] > 0) & 
    (df_2020['High'] > 0) & 
    (df_2020['Low'] > 0)
].copy()

# Calculate intraday volatility: (High - Low) / Open
df_2020['Intraday_Volatility'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

# Calculate average volatility for each index
results = {}
for idx in df_2020['Index'].unique():
    subset = df_2020[df_2020['Index'] == idx]
    if len(subset) > 0:
        avg_vol = subset['Intraday_Volatility'].mean()
        results[idx] = {
            'avg_volatility': round(avg_vol, 6),
            'trading_days': len(subset)
        }

# Sort by volatility descending
sorted_results = sorted(results.items(), key=lambda x: x[1]['avg_volatility'], reverse=True)

print("Average Intraday Volatility by Asian Index (2020+):")
for idx, data in sorted_results:
    print(f"{idx}: {data['avg_volatility']:.6f} (over {data['trading_days']} trading days)")

print("__RESULT__:")
print(json.dumps(sorted_results))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'index_name': 'J203.JO'}, {'index_name': 'N225'}, {'index_name': 'GSPTSE'}, {'index_name': 'NSEI'}, {'index_name': 'GDAXI'}, {'index_name': 'IXIC'}, {'index_name': 'HSI'}, {'index_name': 'NYA'}, {'index_name': '000001.SS'}, {'index_name': 'SSMI'}, {'index_name': 'TWII'}, {'index_name': 'N100'}, {'index_name': '399001.SZ'}], 'var_functions.query_db:5': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.execute_python:7': {'asia_indices': ['N225', 'HSI', '000001.SS', '399001.SZ', 'TWII', 'NSEI']}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': {'total_records': 20187, 'columns': ['Index', 'Date', 'Open', 'High', 'Low', 'Close'], 'unique_indices': ['HSI', '000001.SS', 'N225', '399001.SZ', 'NSEI', 'TWII']}, 'var_functions.execute_python:24': [{'index': '399001.SZ', 'avg_volatility': 0.019375, 'trading_days': 39}, {'index': 'NSEI', 'avg_volatility': 0.017565, 'trading_days': 34}, {'index': 'HSI', 'avg_volatility': 0.014769, 'trading_days': 40}, {'index': 'N225', 'avg_volatility': 0.014314, 'trading_days': 40}, {'index': '000001.SS', 'avg_volatility': 0.01418, 'trading_days': 29}, {'index': 'TWII', 'avg_volatility': 0.013563, 'trading_days': 45}], 'var_functions.execute_python:28': [], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json'}

exec(code, env_args)
