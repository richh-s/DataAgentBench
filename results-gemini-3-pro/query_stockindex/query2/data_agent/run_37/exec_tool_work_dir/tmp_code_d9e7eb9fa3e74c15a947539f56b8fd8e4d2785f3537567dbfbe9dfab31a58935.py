code = """import pandas as pd
import json

# Get file path from storage
file_path = locals()['var_function-call-1773212316373150054']

with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse dates
# We use coerce to handle mixed formats. Pandas usually handles "Month DD, YYYY" and ISO well.
df['dt'] = pd.to_datetime(df['Date'], errors='coerce')

# Filter for 2018
df_2018 = df[df['dt'].dt.year == 2018].copy()

# Convert numeric
for col in ['Open', 'Close']:
    df_2018[col] = pd.to_numeric(df_2018[col], errors='coerce')

results = {}
for idx in df_2018['Index'].unique():
    sub = df_2018[df_2018['Index'] == idx]
    up = (sub['Close'] > sub['Open']).sum()
    down = (sub['Close'] < sub['Open']).sum()
    results[idx] = {'up': int(up), 'down': int(down)}

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-16831980965409320818': ['index_info'], 'var_function-call-16831980965409317307': ['index_trade'], 'var_function-call-4220619263127830695': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_function-call-15424594137061085806': [{'Index': 'J203.JO'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'IXIC'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-4766578470714734566': [{'Date': '31 Dec 1986, 00:00'}], 'var_function-call-1773212316373150054': 'file_storage/function-call-1773212316373150054.json'}

exec(code, env_args)
