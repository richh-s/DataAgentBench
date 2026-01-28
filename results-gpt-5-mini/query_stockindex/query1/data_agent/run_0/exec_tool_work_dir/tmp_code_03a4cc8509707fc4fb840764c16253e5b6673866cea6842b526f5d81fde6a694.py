code = """import json
# var_call_KirHGrA02eU1UMmdqQVlOzmS is available from previous query
data = var_call_KirHGrA02eU1UMmdqQVlOzmS
# Convert and find max
for d in data:
    d['avg_intraday_vol'] = float(d['avg_intraday_vol'])
max_rec = max(data, key=lambda x: x['avg_intraday_vol'])
symbol = max_rec['Index']
avg_vol = max_rec['avg_intraday_vol']
# Map symbols to exchange/names
mapping = {
    '399001.SZ': {'name': 'Shenzhen Component Index', 'exchange': 'Shenzhen Stock Exchange'},
    '000001.SS': {'name': 'SSE Composite Index', 'exchange': 'Shanghai Stock Exchange'},
    'NSEI': {'name': 'Nifty 50', 'exchange': 'National Stock Exchange of India'},
    'HSI': {'name': 'Hang Seng Index', 'exchange': 'Hong Kong Stock Exchange'},
    'TWII': {'name': 'Taiwan Weighted Index', 'exchange': 'Taiwan Stock Exchange'},
    'N225': {'name': 'Nikkei 225', 'exchange': 'Tokyo Stock Exchange'}
}
info = mapping.get(symbol, {'name': None, 'exchange': None})
result = {
    'index_symbol': symbol,
    'index_name': info['name'],
    'exchange': info['exchange'],
    'region': 'Asia',
    'avg_intraday_vol': avg_vol,
    'avg_intraday_vol_pct': f"{avg_vol*100:.2f}%",
    'period': 'since 2020-01-01'
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rk2dM0rhBS1M1SLyDOKHmzE7': ['index_trade'], 'var_call_fBPwk3Yq0fUdP9sIvqelYQdk': ['index_info'], 'var_call_g48NPQ4u3B2dygOa1j0LS7hH': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_KirHGrA02eU1UMmdqQVlOzmS': [{'Index': '399001.SZ', 'avg_intraday_vol': '0.020202435308195866'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.01731142407102674'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.01585173971531033'}, {'Index': 'HSI', 'avg_intraday_vol': '0.01382304680245353'}, {'Index': 'TWII', 'avg_intraday_vol': '0.01348835226084207'}, {'Index': 'N225', 'avg_intraday_vol': '0.008720764073041308'}]}

exec(code, env_args)
