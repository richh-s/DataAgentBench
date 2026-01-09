code = """import json, pandas as pd

df = pd.DataFrame(var_call_0RMzr5bxmXJ3ARG8XvQvd67q)
# convert to numeric
for c in ['up_days','down_days']:
    df[c] = pd.to_numeric(df[c])
res = df[df['up_days']>df['down_days']].sort_values('Index')
answer = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_6jXalyZzHpPKJg6Jxetmpx6A': ['index_info'], 'var_call_v7qybHUqk1uJDGhf65C8XK9Z': ['index_trade'], 'var_call_aOoKcGRFdl1HzwNTSU0Q2xHz': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_jXt1rOehdVINn0H4tWISaqHz': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_0RMzr5bxmXJ3ARG8XvQvd67q': [{'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NYA', 'up_days': '37.0', 'down_days': '42.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}]}

exec(code, env_args)
