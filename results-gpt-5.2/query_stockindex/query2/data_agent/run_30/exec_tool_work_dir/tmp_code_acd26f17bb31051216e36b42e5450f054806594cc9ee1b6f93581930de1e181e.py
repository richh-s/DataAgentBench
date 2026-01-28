code = """import json, pandas as pd

df = pd.DataFrame(var_call_hztArY5JEpGLPMGfLoHUs4MQ)
# coerce numeric
for c in ['up_days','down_days','flat_days','total_days']:
    df[c] = pd.to_numeric(df[c])

# infer North America indices present in dataset
north_america = {
    'IXIC': 'NASDAQ Composite (US)',
    'NYA': 'NYSE Composite (US)',
    'GSPTSE': 'S&P/TSX Composite (Canada)'
}

df_na = df[df['idx'].isin(north_america.keys())].copy()
df_na['name'] = df_na['idx'].map(north_america)
df_na['more_up_than_down'] = df_na['up_days'] > df_na['down_days']

winners = df_na[df_na['more_up_than_down']].sort_values('idx')
answer = [{'Index': r.idx, 'Name': r.name, 'UpDays': int(r.up_days), 'DownDays': int(r.down_days)} for r in winners.itertuples(index=False)]

print('__RESULT__:')
print(json.dumps({'winners': answer}))"""

env_args = {'var_call_hztArY5JEpGLPMGfLoHUs4MQ': [{'idx': 'J203.JO', 'up_days': '37.0', 'down_days': '44.0', 'flat_days': '0.0', 'total_days': '81'}, {'idx': 'IXIC', 'up_days': '44.0', 'down_days': '31.0', 'flat_days': '0.0', 'total_days': '75'}, {'idx': 'HSI', 'up_days': '44.0', 'down_days': '42.0', 'flat_days': '0.0', 'total_days': '86'}, {'idx': 'N225', 'up_days': '32.0', 'down_days': '42.0', 'flat_days': '0.0', 'total_days': '74'}, {'idx': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0', 'flat_days': '1.0', 'total_days': '86'}, {'idx': 'NSEI', 'up_days': '40.0', 'down_days': '39.0', 'flat_days': '0.0', 'total_days': '79'}, {'idx': 'GDAXI', 'up_days': '50.0', 'down_days': '48.0', 'flat_days': '0.0', 'total_days': '98'}, {'idx': 'NYA', 'up_days': '37.0', 'down_days': '42.0', 'flat_days': '0.0', 'total_days': '79'}, {'idx': '000001.SS', 'up_days': '47.0', 'down_days': '37.0', 'flat_days': '0.0', 'total_days': '84'}, {'idx': 'SSMI', 'up_days': '54.0', 'down_days': '39.0', 'flat_days': '0.0', 'total_days': '93'}, {'idx': 'TWII', 'up_days': '39.0', 'down_days': '39.0', 'flat_days': '0.0', 'total_days': '78'}, {'idx': 'N100', 'up_days': '32.0', 'down_days': '36.0', 'flat_days': '0.0', 'total_days': '68'}, {'idx': '399001.SZ', 'up_days': '33.0', 'down_days': '43.0', 'flat_days': '0.0', 'total_days': '76'}], 'var_call_IRIFUDWxLs02JaWDHNO6jKvZ': ['index_info']}

exec(code, env_args)
