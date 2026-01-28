code = """import json
# var_call_kth3DK7yurdyKturPn9BhPUF is available from previous query
data = var_call_kth3DK7yurdyKturPn9BhPUF
# Ensure numeric conversion
for d in data:
    d['avg_intraday_vol'] = float(d['avg_intraday_vol'])
# Find top
top = max(data, key=lambda x: x['avg_intraday_vol'])
# Infer region mapping for known Asian indices
region_map = {
    'N225': 'Asia (Japan)',
    'HSI': 'Asia (Hong Kong)',
    '000001.SS': 'Asia (China - Shanghai)',
    '399001.SZ': 'Asia (China - Shenzhen)',
    'TWII': 'Asia (Taiwan)',
    'NSEI': 'Asia (India)'
}
region = region_map.get(top['Index'], 'Asia')
result = {
    'top_index': top['Index'],
    'region': region,
    'avg_intraday_vol': top['avg_intraday_vol'],
    'avg_intraday_vol_pct': top['avg_intraday_vol'] * 100
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GCLNsGWWBgoSYtXQ78bHz7g0': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'IXIC'}], 'var_call_kth3DK7yurdyKturPn9BhPUF': [{'Index': '399001.SZ', 'avg_intraday_vol': '0.020202435308195866'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.01731142407102674'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.01585173971531033'}, {'Index': 'HSI', 'avg_intraday_vol': '0.01382304680245353'}, {'Index': 'TWII', 'avg_intraday_vol': '0.01348835226084207'}, {'Index': 'N225', 'avg_intraday_vol': '0.008720764073041308'}]}

exec(code, env_args)
