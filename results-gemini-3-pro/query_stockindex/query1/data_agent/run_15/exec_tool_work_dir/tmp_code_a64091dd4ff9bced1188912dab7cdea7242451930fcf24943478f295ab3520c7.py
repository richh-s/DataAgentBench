code = """import pandas as pd
import json

# Load data
file_path = locals()['var_function-call-8407735086257018162']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert columns to numeric
cols = ['Open', 'High', 'Low']
for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Parse Date
# The formats are mixed. pd.to_datetime usually handles this but can be slow.
# Given the smallish size (subset of 100k rows), it should be fine.
# We'll use errors='coerce' to handle unparseable dates.
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter for date >= 2020-01-01
df_filtered = df[df['Date'] >= '2020-01-01'].copy()

# Remove rows where Open is 0 or NaN to avoid division by zero
df_filtered = df_filtered[df_filtered['Open'] > 0]

# Calculate Intraday Volatility
df_filtered['Volatility'] = (df_filtered['High'] - df_filtered['Low']) / df_filtered['Open']

# Group by Index and calculate average volatility
result_df = df_filtered.groupby('Index')['Volatility'].mean().reset_index()
result_df = result_df.sort_values(by='Volatility', ascending=False)

print("__RESULT__:")
print(result_df.to_json(orient='records'))"""

env_args = {'var_function-call-17122105110820272393': ['index_info'], 'var_function-call-17122105110820274016': ['index_trade'], 'var_function-call-12028607703810222879': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-8723578037757185447': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_function-call-14766927872622268700': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_function-call-8854890833415893293': [{'count_star()': '104224'}], 'var_function-call-8407735086257018162': 'file_storage/function-call-8407735086257018162.json'}

exec(code, env_args)
