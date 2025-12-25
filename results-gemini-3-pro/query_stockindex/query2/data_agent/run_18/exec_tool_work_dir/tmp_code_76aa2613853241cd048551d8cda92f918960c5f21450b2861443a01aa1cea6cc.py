code = """import json
import pandas as pd

# Load the data
file_path = locals()['var_function-call-18242543158828746431']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure numeric columns are floats
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# Calculate up/down
df['Up'] = df['Close'] > df['Open']
df['Down'] = df['Close'] < df['Open']

# Group by Index
results = []
grouped = df.groupby('Index')
for name, group in grouped:
    up_count = group['Up'].sum()
    down_count = group['Down'].sum()
    
    if up_count > down_count:
        results.append(name)

# Print result
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5278399001406015755': ['index_info'], 'var_function-call-5278399001406016056': ['index_trade'], 'var_function-call-13170391964150397913': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-13170391964150396936': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-18242543158828746431': 'file_storage/function-call-18242543158828746431.json'}

exec(code, env_args)
