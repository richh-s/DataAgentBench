code = """import pandas as pd
import json

file_path = locals()['var_function-call-14049573361377234326']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure numeric columns are floats
cols = ['Open', 'Close']
for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Group by Index and count up/down days
results = []
for index_name, group in df.groupby('Index'):
    up_days = group[group['Close'] > group['Open']].shape[0]
    down_days = group[group['Close'] < group['Open']].shape[0]
    
    # print(f"Index: {index_name}, Up: {up_days}, Down: {down_days}")
    if up_days > down_days:
        results.append(index_name)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5191062286505320799': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_function-call-5191062286505322968': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'NYA'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-14049573361377234326': 'file_storage/function-call-14049573361377234326.json'}

exec(code, env_args)
