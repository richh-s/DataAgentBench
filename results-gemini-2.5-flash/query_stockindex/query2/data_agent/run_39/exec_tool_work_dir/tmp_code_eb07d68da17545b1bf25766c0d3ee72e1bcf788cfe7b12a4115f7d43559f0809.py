code = """import pandas as pd
import json

df = pd.read_json(locals()['var_function-call-9899946586646133994'])

df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

df['Day_Result'] = df.apply(lambda row: 'up' if row['Close'] > row['Open'] else ('down' if row['Close'] < row['Open'] else 'flat'), axis=1)

up_down_counts = df.groupby('Index')['Day_Result'].value_counts().unstack(fill_value=0)

result_indices = up_down_counts[up_down_counts['up'] > up_down_counts['down']].index.tolist()

print('__RESULT__:')
print(json.dumps(result_indices))"""

env_args = {'var_function-call-2450864045472609314': ['index_info'], 'var_function-call-11062554896720696856': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_function-call-14820687679620224816': ['index_trade'], 'var_function-call-11359775600772677658': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_function-call-9899946586646133994': 'file_storage/function-call-9899946586646133994.json'}

exec(code, env_args)
