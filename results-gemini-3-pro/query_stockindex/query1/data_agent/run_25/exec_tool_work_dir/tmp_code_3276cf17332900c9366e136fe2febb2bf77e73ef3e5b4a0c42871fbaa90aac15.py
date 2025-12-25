code = """import pandas as pd
import json
import os
from dateutil.parser import parse

# Load the data
file_path = locals()['var_function-call-17778337764171878471']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Function to parse dates robustly
def parse_date_custom(date_str):
    try:
        return pd.to_datetime(date_str)
    except:
        try:
            return parse(date_str)
        except:
            return pd.NaT

# Apply date parsing
# Using pd.to_datetime directly usually works for these common formats
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Check if we have many NaT
if df['Date'].isnull().sum() > len(df) * 0.5:
    # If standard parsing failed for many, try more expensive dateutil or custom format
    # But usually pd.to_datetime handles "31 Dec 1986" and "January 02, 1987" fine.
    pass

# Filter for >= 2020-01-01
df_2020 = df[df['Date'] >= '2020-01-01'].copy()

# Calculate Intraday Volatility: (High - Low) / Open
# Ensure numeric columns
cols = ['Open', 'High', 'Low']
for col in cols:
    df_2020[col] = pd.to_numeric(df_2020[col], errors='coerce')

df_2020 = df_2020.dropna(subset=cols)
# Avoid division by zero
df_2020 = df_2020[df_2020['Open'] > 0]

df_2020['Volatility'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

# Group by Index and calculate mean
avg_volatility = df_2020.groupby('Index')['Volatility'].mean()

# Find the highest
if not avg_volatility.empty:
    max_vol_index = avg_volatility.idxmax()
    max_vol_value = avg_volatility.max()
    
    result = {
        "index_volatilities": avg_volatility.to_dict(),
        "highest_volatility_index": max_vol_index,
        "highest_volatility_value": max_vol_value
    }
else:
    result = {"error": "No data found after 2020"}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-3140219745462827775': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_function-call-3140219745462826938': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-17778337764171878471': 'file_storage/function-call-17778337764171878471.json'}

exec(code, env_args)
