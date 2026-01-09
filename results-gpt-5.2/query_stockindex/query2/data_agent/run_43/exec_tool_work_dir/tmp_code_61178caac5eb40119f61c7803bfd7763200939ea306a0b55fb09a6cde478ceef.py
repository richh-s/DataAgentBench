code = """import json, pandas as pd

data = var_call_q84r6FSaBF9qjjrJ1hksEmx5
# Coerce numeric fields
for r in data:
    for k in ['total_days','up_days','down_days']:
        r[k] = float(r[k])

df = pd.DataFrame(data)

# North American indices in dataset: IXIC (Nasdaq Composite, US), NYA (NYSE Composite, US), GSPTSE (S&P/TSX Composite, Canada)
na = {'IXIC','NYA','GSPTSE'}
res = df[df['Index'].isin(na)].copy()
res['more_up_than_down'] = res['up_days'] > res['down_days']
ans = res[res['more_up_than_down']][['Index','up_days','down_days']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_tHJ4flwImBYdfG8VMaXVhpfX': ['index_info'], 'var_call_sH15oXvd5rU0Ur7J5z4bIeFl': ['index_trade'], 'var_call_q84r6FSaBF9qjjrJ1hksEmx5': [{'Index': 'J203.JO', 'total_days': '81', 'up_days': '37.0', 'down_days': '44.0'}, {'Index': 'N225', 'total_days': '74', 'up_days': '32.0', 'down_days': '42.0'}, {'Index': 'GSPTSE', 'total_days': '86', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NSEI', 'total_days': '79', 'up_days': '40.0', 'down_days': '39.0'}, {'Index': 'GDAXI', 'total_days': '98', 'up_days': '50.0', 'down_days': '48.0'}, {'Index': 'IXIC', 'total_days': '75', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'HSI', 'total_days': '86', 'up_days': '44.0', 'down_days': '42.0'}, {'Index': '000001.SS', 'total_days': '84', 'up_days': '47.0', 'down_days': '37.0'}, {'Index': 'SSMI', 'total_days': '93', 'up_days': '54.0', 'down_days': '39.0'}, {'Index': 'TWII', 'total_days': '78', 'up_days': '39.0', 'down_days': '39.0'}, {'Index': 'N100', 'total_days': '68', 'up_days': '32.0', 'down_days': '36.0'}, {'Index': '399001.SZ', 'total_days': '76', 'up_days': '33.0', 'down_days': '43.0'}, {'Index': 'NYA', 'total_days': '79', 'up_days': '37.0', 'down_days': '42.0'}]}

exec(code, env_args)
