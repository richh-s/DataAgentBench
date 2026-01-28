code = """import json
rows = var_call_0sDk9KLpcU8AV9vYioTu0SI4
# convert avg_intraday_vol to float and find max
for r in rows:
    r['avg_intraday_vol'] = float(r['avg_intraday_vol'])
best = max(rows, key=lambda r: r['avg_intraday_vol'])
result = {
    'index': best['Index'],
    'avg_intraday_vol': best['avg_intraday_vol'],
    'avg_intraday_vol_pct': best['avg_intraday_vol'] * 100
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cfOkhexXadGwRjhkzseeWroB': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_0sDk9KLpcU8AV9vYioTu0SI4': [{'Index': '399001.SZ', 'avg_intraday_vol': '0.020202435308195866'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.01731142407102674'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.01585173971531033'}, {'Index': 'HSI', 'avg_intraday_vol': '0.01382304680245353'}, {'Index': 'TWII', 'avg_intraday_vol': '0.01348835226084207'}, {'Index': 'N225', 'avg_intraday_vol': '0.008720764073041308'}]}

exec(code, env_args)
