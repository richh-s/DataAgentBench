code = """import pandas as pd
import json

file_path = locals()['var_function-call-921167764703847430']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

df_2018 = df[df['Date'].dt.year == 2018]

stats = {}
for index_name, group in df_2018.groupby('Index'):
    up_days = group[group['Close'] > group['Open']].shape[0]
    down_days = group[group['Close'] < group['Open']].shape[0]
    stats[index_name] = {'up': up_days, 'down': down_days}

print("__RESULT__:")
print(json.dumps(stats))"""

env_args = {'var_function-call-16127450285086483910': ['index_info'], 'var_function-call-2384260976866712086': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}], 'var_function-call-7906930925696955887': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-4358639227729216070': [{'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}], 'var_function-call-12350373791488134860': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}], 'var_function-call-921167764703847430': 'file_storage/function-call-921167764703847430.json', 'var_function-call-659942337817825181': ['IXIC']}

exec(code, env_args)
