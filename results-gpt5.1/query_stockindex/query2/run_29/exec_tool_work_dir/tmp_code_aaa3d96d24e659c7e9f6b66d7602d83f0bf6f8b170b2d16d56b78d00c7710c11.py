code = """import json, pandas as pd

path = var_call_0UQcdhP0HGG7QhoFrJyQvoI6
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

for col in ['Open', 'Close']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# classify up/down days
up_down = df.groupby('Index').apply(lambda g: pd.Series({
    'up_days': int((g['Close'] > g['Open']).sum()),
    'down_days': int((g['Close'] < g['Open']).sum())
})).reset_index()

# identify North American indices manually
north_american = {
    'NYA': 'New York Stock Exchange (USA)',
    'IXIC': 'NASDAQ Composite (USA)',
    'GSPTSE': 'S&P/TSX Composite (Canada)'
}

na_results = up_down[up_down['Index'].isin(north_american.keys())].copy()
na_results['more_up_than_down'] = na_results['up_days'] > na_results['down_days']

answer_indices = na_results[na_results['more_up_than_down']]['Index'].tolist()

result = {
    'north_american_indices_with_more_up_than_down_2018': answer_indices,
    'details': na_results.to_dict(orient='records')
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_umKhKQmtVl142z6OXWKkXHCj': ['index_info'], 'var_call_NRYRrNbm9xggQwXQFJxlfXz3': ['index_trade'], 'var_call_uCXu8aqUMMgeS016K4Ws1ibf': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_7wIyyAxvM99B8HwhvvuVgFQI': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_0UQcdhP0HGG7QhoFrJyQvoI6': 'file_storage/call_0UQcdhP0HGG7QhoFrJyQvoI6.json'}

exec(code, env_args)
