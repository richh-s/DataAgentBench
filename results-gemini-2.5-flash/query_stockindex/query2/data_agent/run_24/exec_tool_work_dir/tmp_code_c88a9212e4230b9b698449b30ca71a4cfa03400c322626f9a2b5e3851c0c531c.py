code = """import pandas as pd

data = locals()['var_function-call-15357935559596183247']
df = pd.DataFrame(data)

# Convert 'up_days' and 'down_days' to numeric, as they are strings from the query result.
df['up_days'] = pd.to_numeric(df['up_days'])
df['down_days'] = pd.to_numeric(df['down_days'])

# Filter for indices with more up days than down days
result = df[df['up_days'] > df['down_days']]['Index'].tolist()

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-16766468493629174225': ['index_info'], 'var_function-call-16766468493629176992': ['index_trade'], 'var_function-call-11159718393329839045': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_function-call-7034103721722904857': [{'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'J203.JO'}], 'var_function-call-15357935559596183247': [{'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'NYA', 'up_days': '37.0', 'down_days': '42.0'}]}

exec(code, env_args)
