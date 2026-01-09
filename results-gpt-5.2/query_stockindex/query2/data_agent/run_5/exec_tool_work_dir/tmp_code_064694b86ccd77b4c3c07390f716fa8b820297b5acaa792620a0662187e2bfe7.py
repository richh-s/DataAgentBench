code = """import json
import pandas as pd

df = pd.DataFrame(var_call_z0WHvBR2ifYV2QJSjYjMMlHf)
# coerce numeric
for c in ['up_days','down_days']:
    df[c] = pd.to_numeric(df[c])

# North America indices: NYA (NYSE Composite), IXIC (NASDAQ Composite), GSPTSE (S&P/TSX Composite)
na = df[df['idx'].isin(['NYA','IXIC','GSPTSE'])].copy()
na['more_up_than_down'] = na['up_days'] > na['down_days']
res = na[na['more_up_than_down']].sort_values('idx')[['idx','up_days','down_days']]
answer = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_z0WHvBR2ifYV2QJSjYjMMlHf': [{'idx': 'J203.JO', 'up_days': '37.0', 'down_days': '44.0'}, {'idx': 'N225', 'up_days': '32.0', 'down_days': '42.0'}, {'idx': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'idx': 'NSEI', 'up_days': '40.0', 'down_days': '39.0'}, {'idx': 'GDAXI', 'up_days': '50.0', 'down_days': '48.0'}, {'idx': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'idx': 'HSI', 'up_days': '44.0', 'down_days': '42.0'}, {'idx': '000001.SS', 'up_days': '47.0', 'down_days': '37.0'}, {'idx': 'SSMI', 'up_days': '54.0', 'down_days': '39.0'}, {'idx': 'TWII', 'up_days': '39.0', 'down_days': '39.0'}, {'idx': 'NYA', 'up_days': '37.0', 'down_days': '42.0'}, {'idx': 'N100', 'up_days': '32.0', 'down_days': '36.0'}, {'idx': '399001.SZ', 'up_days': '33.0', 'down_days': '43.0'}], 'var_call_nLd1g0VcpzQ6FT30UPG2l5rT': ['index_info'], 'var_call_r0uWw50FBPzSDWImKp61c588': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
