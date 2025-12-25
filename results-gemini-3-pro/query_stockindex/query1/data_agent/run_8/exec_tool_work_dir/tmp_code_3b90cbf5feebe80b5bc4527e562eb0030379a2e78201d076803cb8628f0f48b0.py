code = """import pandas as pd
import json

file_path = locals()['var_function-call-504483122947925747']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates. We have mixed formats.
# Let's try to coerce errors and handle them if needed, but pd.to_datetime usually works well.
# Given the formats, dateutil parser (used by pandas) should handle them.
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter for date >= 2020-01-01
df_filtered = df[df['Date'] >= '2020-01-01'].copy()

# Calculate Intraday Volatility: (High - Low) / Open
# Ensure numeric types
cols = ['High', 'Low', 'Open']
for c in cols:
    df_filtered[c] = pd.to_numeric(df_filtered[c], errors='coerce')

# Drop rows with NaN in these columns or Open=0
df_filtered = df_filtered.dropna(subset=cols)
df_filtered = df_filtered[df_filtered['Open'] > 0]

df_filtered['volatility'] = (df_filtered['High'] - df_filtered['Low']) / df_filtered['Open']

# Average by Index
avg_volatility = df_filtered.groupby('Index')['volatility'].mean().reset_index()
avg_volatility = avg_volatility.sort_values(by='volatility', ascending=False)

print("__RESULT__:")
print(avg_volatility.to_json(orient='records'))"""

env_args = {'var_function-call-1761236436845143949': ['index_info'], 'var_function-call-1761236436845142708': ['index_trade'], 'var_function-call-8216857866269149980': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-8216857866269147669': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}], 'var_function-call-1583759612255736453': 'file_storage/function-call-1583759612255736453.json', 'var_function-call-3116664523764468445': [{'count_star()': '43132'}], 'var_function-call-17468176566199285037': [{'Date': 'September 30, 2020 at 12:00 AM'}, {'Date': 'September 30, 2011 at 12:00 AM'}, {'Date': 'September 30, 2010 at 12:00 AM'}, {'Date': 'September 30, 2009 at 12:00 AM'}, {'Date': 'September 30, 1993 at 12:00 AM'}], 'var_function-call-504483122947925747': 'file_storage/function-call-504483122947925747.json'}

exec(code, env_args)
