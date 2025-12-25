code = """import pandas as pd
import json

file_path = locals()['var_function-call-18323960598310562074']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df['Open'] = pd.to_numeric(df['Open'])
df['Close'] = pd.to_numeric(df['Close'])

df['up_day'] = df['Close'] > df['Open']
df['down_day'] = df['Close'] < df['Open']

up_down_counts = df.groupby('Index').agg(up_days=('up_day', 'sum'), down_days=('down_day', 'sum')).reset_index()

result = up_down_counts[up_down_counts['up_days'] > up_down_counts['down_days']]

print('__RESULT__:')
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-1813515839735428447': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_function-call-18323960598310562074': 'file_storage/function-call-18323960598310562074.json'}

exec(code, env_args)
