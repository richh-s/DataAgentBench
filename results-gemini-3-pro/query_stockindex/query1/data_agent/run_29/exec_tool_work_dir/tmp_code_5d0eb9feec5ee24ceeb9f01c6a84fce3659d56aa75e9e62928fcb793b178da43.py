code = """import pandas as pd
import json

# Load the data from the previous query result
file_path = locals()['var_function-call-859223431930931286']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse Date
# The formats are mixed. Let's try to utilize pd.to_datetime with some cleanup
# Clean " at 12:00 AM" which seems common
df['Date_Clean'] = df['Date'].astype(str).str.replace(' at 12:00 AM', '', regex=False).str.replace(', 00:00', '', regex=False)

# Now let's try to convert. formats like "January 02, 1987" or "31 Dec 1986" should be parsable.
df['dt'] = pd.to_datetime(df['Date_Clean'], errors='coerce')

# Filter for >= 2020-01-01
df_2020 = df[df['dt'] >= '2020-01-01'].copy()

# Calculate Intraday Volatility: (High - Low) / Open
# Ensure numeric
cols = ['Open', 'High', 'Low']
for c in cols:
    df_2020[c] = pd.to_numeric(df_2020[c], errors='coerce')

# Drop invalid rows
df_2020 = df_2020.dropna(subset=cols)
df_2020 = df_2020[df_2020['Open'] > 0]

df_2020['Volatility'] = (df_2020['High'] - df_2020['Low']) / df_2020['Open']

# Calculate average volatility per index
avg_vol = df_2020.groupby('Index')['Volatility'].mean().reset_index()
avg_vol = avg_vol.sort_values(by='Volatility', ascending=False)

print("__RESULT__:")
print(avg_vol.to_json(orient='records'))"""

env_args = {'var_function-call-9316001085281555861': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'IXIC'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-9316001085281554504': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-859223431930931286': 'file_storage/function-call-859223431930931286.json'}

exec(code, env_args)
