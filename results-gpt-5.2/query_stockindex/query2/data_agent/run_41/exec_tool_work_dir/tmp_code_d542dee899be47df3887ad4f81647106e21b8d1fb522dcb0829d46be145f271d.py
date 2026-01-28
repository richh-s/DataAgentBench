code = """import json, pandas as pd

df = pd.DataFrame(var_call_xNHmj5wi4PEw4GBnEYUj1Gsy)
for c in ['total_days','up_days','down_days']:
    df[c] = pd.to_numeric(df[c])

# Infer North America indices present in dataset
north_america = {'IXIC': 'NASDAQ Composite (US)', 'NYA': 'NYSE Composite (US)', 'GSPTSE': 'S&P/TSX Composite (Canada)'}

df_na = df[df['Index'].isin(north_america.keys())].copy()
df_na['name'] = df_na['Index'].map(north_america)

df_more_up = df_na[df_na['up_days'] > df_na['down_days']].copy()
df_more_up = df_more_up.sort_values(['up_days','down_days'], ascending=[False, True])

out = df_more_up[['Index','name','up_days','down_days','total_days']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_O70xPt8abQXAGrxqBRzfPesF': ['index_info'], 'var_call_nPI00kuZ60dmyO6rB3OCxrnj': ['index_trade'], 'var_call_xNHmj5wi4PEw4GBnEYUj1Gsy': [{'Index': 'J203.JO', 'total_days': '81', 'up_days': '37.0', 'down_days': '44.0'}, {'Index': 'N225', 'total_days': '74', 'up_days': '32.0', 'down_days': '42.0'}, {'Index': 'GSPTSE', 'total_days': '86', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NSEI', 'total_days': '79', 'up_days': '40.0', 'down_days': '39.0'}, {'Index': 'GDAXI', 'total_days': '98', 'up_days': '50.0', 'down_days': '48.0'}, {'Index': 'IXIC', 'total_days': '75', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'HSI', 'total_days': '86', 'up_days': '44.0', 'down_days': '42.0'}, {'Index': 'NYA', 'total_days': '79', 'up_days': '37.0', 'down_days': '42.0'}, {'Index': '000001.SS', 'total_days': '84', 'up_days': '47.0', 'down_days': '37.0'}, {'Index': 'SSMI', 'total_days': '93', 'up_days': '54.0', 'down_days': '39.0'}, {'Index': 'TWII', 'total_days': '78', 'up_days': '39.0', 'down_days': '39.0'}, {'Index': 'N100', 'total_days': '68', 'up_days': '32.0', 'down_days': '36.0'}, {'Index': '399001.SZ', 'total_days': '76', 'up_days': '33.0', 'down_days': '43.0'}]}

exec(code, env_args)
