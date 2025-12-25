code = """import pandas as pd
import json

# Get the file path
file_path = locals()['var_function-call-6781599062925132606']

# Load data
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert columns to numeric
cols_to_convert = ['Open', 'High', 'Low']
for col in cols_to_convert:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Convert Date
df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')

# Filter >= 2020-01-01
df_recent = df[df['Date'] >= '2020-01-01'].copy()

# Filter valid Open > 0
df_recent = df_recent[df_recent['Open'] > 0]

# Calculate Volatility
df_recent['Volatility'] = (df_recent['High'] - df_recent['Low']) / df_recent['Open']

# Average Volatility
avg_volatility = df_recent.groupby('Index')['Volatility'].mean().reset_index()

# Sort
avg_volatility = avg_volatility.sort_values(by='Volatility', ascending=False)

print("__RESULT__:")
print(avg_volatility.to_json(orient='records'))"""

env_args = {'var_function-call-16091777784778834749': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-13639472935304336970': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}], 'var_function-call-14617715165106035019': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_function-call-6781599062925132606': 'file_storage/function-call-6781599062925132606.json'}

exec(code, env_args)
