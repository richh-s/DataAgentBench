code = """import json
import pandas as pd

rows = var_call_0GNvly6BvSOctbcfLiplZACw

df = pd.DataFrame(rows)
for c in ['total_days','up_days','down_days']:
    df[c] = pd.to_numeric(df[c])

# North American indices in this dataset (by common symbol knowledge):
na = {'IXIC': 'NASDAQ Composite (US)', 'NYA': 'NYSE Composite (US)', 'GSPTSE': 'S&P/TSX Composite (Canada)'}
df_na = df[df['Index'].isin(na.keys())].copy()
df_na['name'] = df_na['Index'].map(na)
df_na['more_up_than_down'] = df_na['up_days'] > df_na['down_days']
ans = df_na[df_na['more_up_than_down']].sort_values('Index')[['Index','name','up_days','down_days']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_OXtRGCKc4zFGjvgJSLqWAKD6': ['index_info'], 'var_call_h6zIXPNUh6UGhcrXgACchaKp': ['index_trade'], 'var_call_0GNvly6BvSOctbcfLiplZACw': [{'Index': 'J203.JO', 'total_days': '81', 'up_days': '37.0', 'down_days': '44.0'}, {'Index': 'N225', 'total_days': '74', 'up_days': '32.0', 'down_days': '42.0'}, {'Index': 'GSPTSE', 'total_days': '86', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NSEI', 'total_days': '79', 'up_days': '40.0', 'down_days': '39.0'}, {'Index': 'GDAXI', 'total_days': '98', 'up_days': '50.0', 'down_days': '48.0'}, {'Index': 'IXIC', 'total_days': '75', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'HSI', 'total_days': '86', 'up_days': '44.0', 'down_days': '42.0'}, {'Index': 'NYA', 'total_days': '79', 'up_days': '37.0', 'down_days': '42.0'}, {'Index': '000001.SS', 'total_days': '84', 'up_days': '47.0', 'down_days': '37.0'}, {'Index': 'SSMI', 'total_days': '93', 'up_days': '54.0', 'down_days': '39.0'}, {'Index': 'TWII', 'total_days': '78', 'up_days': '39.0', 'down_days': '39.0'}, {'Index': 'N100', 'total_days': '68', 'up_days': '32.0', 'down_days': '36.0'}, {'Index': '399001.SZ', 'total_days': '76', 'up_days': '33.0', 'down_days': '43.0'}]}

exec(code, env_args)
