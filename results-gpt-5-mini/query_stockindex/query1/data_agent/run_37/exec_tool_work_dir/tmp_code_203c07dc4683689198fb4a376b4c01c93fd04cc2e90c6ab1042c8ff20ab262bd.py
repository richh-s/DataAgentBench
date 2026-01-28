code = """import json
records = var_call_I8znI6ugRsnDn05GTte28SqX
# Convert avg_intraday_vol to float
for r in records:
    r['avg_intraday_vol'] = float(r['avg_intraday_vol'])
# Find max
max_r = max(records, key=lambda x: x['avg_intraday_vol'])
# Map index to exchange/full name (inferred)
mapping = {
    '399001.SZ': 'Shenzhen Stock Exchange (SZSE) - SZSE Component (399001.SZ)',
    '000001.SS': 'Shanghai Stock Exchange (SSE) - Shanghai Composite (000001.SS)',
    'NSEI': 'National Stock Exchange of India - NIFTY 50 (NSEI)',
    'HSI': 'Hong Kong Stock Exchange - Hang Seng Index (HSI)',
    'TWII': 'Taiwan Stock Exchange - Taiwan Weighted (TWII)',
    'N225': 'Tokyo Stock Exchange - Nikkei 225 (N225)'
}
exchange = mapping.get(max_r['Index'], '')
result = {
    'index': max_r['Index'],
    'avg_intraday_vol': max_r['avg_intraday_vol'],
    'exchange': exchange,
    'region': 'Asia',
    'period': 'since 2020-01-01'
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WSWS1To2yKd6A74WqJjQnEzj': [{'Index': 'J203.JO'}, {'Index': 'HSI'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'NYA'}, {'Index': 'IXIC'}], 'var_call_I8znI6ugRsnDn05GTte28SqX': [{'Index': '399001.SZ', 'avg_intraday_vol': '0.020202435308195866'}, {'Index': '000001.SS', 'avg_intraday_vol': '0.01731142407102674'}, {'Index': 'NSEI', 'avg_intraday_vol': '0.01585173971531033'}, {'Index': 'HSI', 'avg_intraday_vol': '0.01382304680245353'}, {'Index': 'TWII', 'avg_intraday_vol': '0.01348835226084207'}, {'Index': 'N225', 'avg_intraday_vol': '0.008720764073041308'}]}

exec(code, env_args)
