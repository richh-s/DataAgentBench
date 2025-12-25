code = """import pandas as pd
import json

# Load data from the file provided in previous step
# The key is var_function-call-17482105252661011086
# But I must use the filename string stored in that variable.
file_path = locals()['var_function-call-17482105252661011086']

with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert columns to numeric, just in case
cols = ['Open', 'High', 'Low']
for c in cols:
    df[c] = pd.to_numeric(df[c], errors='coerce')

# Convert Date
# Since formats are mixed, let pandas handle it.
# Note: In older pandas, infer_datetime_format=True might be needed or it tries to guess.
# In newer pandas, it's deprecated but still works or is default.
# Given the formats seen: "31 Dec 1986, 00:00", "January 02, 1987 at 12:00 AM", "1987-01-05 00:00:00"
# pd.to_datetime usually handles these well.
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter for Date >= 2020-01-01
df_filtered = df[df['Date'] >= '2020-01-01'].copy()

# Calculate Intraday Volatility: (High - Low) / Open
# Handle division by zero if Open is 0 (unlikely for indices but good to be safe)
df_filtered = df_filtered[df_filtered['Open'] > 0]
df_filtered['Volatility'] = (df_filtered['High'] - df_filtered['Low']) / df_filtered['Open']

# Group by Index and calculate mean
result = df_filtered.groupby('Index')['Volatility'].mean().sort_values(ascending=False)

# Prepare result for printing
output = result.to_dict()
# Also find the max index name
max_index = result.idxmax()
max_vol = result.max()

final_res = {
    "volatilities": output,
    "max_index": max_index,
    "max_volatility": max_vol
}

print("__RESULT__:")
print(json.dumps(final_res))"""

env_args = {'var_function-call-9633858484781229483': ['index_info'], 'var_function-call-6367313426728071531': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-8440068130572010515': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-16980424118990784536': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-3019672056435273857': [{'Date': '31 Dec 1986, 00:00'}], 'var_function-call-3959441879379135394': [{'cnt': '43132'}], 'var_function-call-17482105252661011086': 'file_storage/function-call-17482105252661011086.json'}

exec(code, env_args)
