code = """import pandas as pd
import json

# Load data
file_path = locals()['var_function-call-6917384859691824811']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Ensure numeric columns
df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

# List of North American indices
na_indices = ['NYA', 'IXIC', 'GSPTSE']

results = {}

for index in na_indices:
    subset = df[df['Index'] == index]
    up_days = subset[subset['Close'] > subset['Open']].shape[0]
    down_days = subset[subset['Close'] < subset['Open']].shape[0]
    results[index] = {'up': up_days, 'down': down_days}

# Filter indices with more up days than down days
final_indices = [idx for idx, counts in results.items() if counts['up'] > counts['down']]

print("__RESULT__:")
print(json.dumps(final_indices))"""

env_args = {'var_function-call-9837769711092617111': ['index_info'], 'var_function-call-7331310365832072191': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_function-call-17596839332593974068': ['index_trade'], 'var_function-call-1475115454811633272': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-6917384859691824811': 'file_storage/function-call-6917384859691824811.json'}

exec(code, env_args)
