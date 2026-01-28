code = """import json

rows = var_call_sM0d3CfqNWCJapPcbwYsDshb
# Infer North America: US (IXIC, NYA) and Canada (GSPTSE)
na = {'IXIC','NYA','GSPTSE'}
res = []
for r in rows:
    idx = r['idx']
    if idx in na:
        up = float(r['up_days'])
        down = float(r['down_days'])
        if up > down:
            res.append({'Index': idx, 'UpDays': int(up), 'DownDays': int(down)})
res = sorted(res, key=lambda x: x['Index'])
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_MguXL3XS35IDBiLJYOHnABHv': ['index_info'], 'var_call_3SBmDjTgtaB68YTyRy9Miel0': ['index_trade'], 'var_call_sM0d3CfqNWCJapPcbwYsDshb': [{'idx': 'J203.JO', 'up_days': '37.0', 'down_days': '44.0'}, {'idx': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'idx': 'N225', 'up_days': '32.0', 'down_days': '42.0'}, {'idx': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'idx': 'NSEI', 'up_days': '40.0', 'down_days': '39.0'}, {'idx': 'GDAXI', 'up_days': '50.0', 'down_days': '48.0'}, {'idx': 'NYA', 'up_days': '37.0', 'down_days': '42.0'}, {'idx': '000001.SS', 'up_days': '47.0', 'down_days': '37.0'}, {'idx': 'SSMI', 'up_days': '54.0', 'down_days': '39.0'}, {'idx': 'TWII', 'up_days': '39.0', 'down_days': '39.0'}, {'idx': 'N100', 'up_days': '32.0', 'down_days': '36.0'}, {'idx': '399001.SZ', 'up_days': '33.0', 'down_days': '43.0'}, {'idx': 'HSI', 'up_days': '44.0', 'down_days': '42.0'}]}

exec(code, env_args)
