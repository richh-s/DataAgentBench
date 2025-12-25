code = """import pandas as pd
import json

# Load data
file_path = locals()['var_function-call-12558309893784223529']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert columns to numeric, coercing errors
cols = ['Open', 'High', 'Low']
for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop rows with NaN in price columns or Open=0
df = df.dropna(subset=cols)
df = df[df['Open'] > 0]

# Parse dates
# We can try to standardize by removing time parts which seem inconsistent
# The formats are quite varied. Let's use pd.to_datetime with 'mixed' if available, or just let it infer.
try:
    df['Date'] = pd.to_datetime(df['Date'], format='mixed')
except:
    # Fallback if 'mixed' not supported in older pandas
    df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format=True)

# Filter for date >= 2020-01-01
df_recent = df[df['Date'] >= '2020-01-01'].copy()

# Calculate Intraday Volatility
# Volatility = (High - Low) / Open
df_recent['Volatility'] = (df_recent['High'] - df_recent['Low']) / df_recent['Open']

# Group by Index and calculate mean
result = df_recent.groupby('Index')['Volatility'].mean().reset_index()
result = result.sort_values(by='Volatility', ascending=False)

print("__RESULT__:")
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-946398065074369481': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-946398065074369724': ['index_trade'], 'var_function-call-18001589981688159033': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-220456462175644306': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}], 'var_function-call-12558309893784223529': 'file_storage/function-call-12558309893784223529.json'}

exec(code, env_args)
