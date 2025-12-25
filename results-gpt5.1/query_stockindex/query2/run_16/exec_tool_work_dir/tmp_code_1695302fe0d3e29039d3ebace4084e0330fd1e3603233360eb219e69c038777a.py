code = """import json

# Map indices to regions based on geographic knowledge
region_map = {
    'NYA': 'North America',      # New York Stock Exchange Composite
    'IXIC': 'North America',     # NASDAQ Composite
    'GSPTSE': 'North America',   # S&P/TSX Composite (Toronto)
    'N225': 'Asia',
    'HSI': 'Asia',
    '000001.SS': 'Asia',
    '399001.SZ': 'Asia',
    'NSEI': 'Asia',
    'GDAXI': 'Europe',
    'N100': 'Europe',
    'SSMI': 'Europe',
    'TWII': 'Asia',
    'J203.JO': 'Africa',
}

records = var_call_tNDSfTEgaBXzCo5mx3z2Qy5U

north_american = []
for r in records:
    idx = r['Index']
    if region_map.get(idx) == 'North America':
        up = float(r['up_days'])
        down = float(r['down_days'])
        if up > down:
            north_american.append({'Index': idx, 'up_days': up, 'down_days': down})

result = json.dumps(north_american)

print('__RESULT__:')
print(result)"""

env_args = {'var_call_t59YbKvCPonoSvxXznogsFah': ['index_info'], 'var_call_i8wNyZHc2GHzcPodvbtbdhNe': ['index_trade'], 'var_call_u9P9lnQtMrr5Y1aNauborsTv': [{'Exchange': 'New York Stock Exchange'}, {'Exchange': 'NASDAQ'}, {'Exchange': 'Hong Kong Stock Exchange'}, {'Exchange': 'Shanghai Stock Exchange'}, {'Exchange': 'Tokyo Stock Exchange'}, {'Exchange': 'Euronext'}, {'Exchange': 'Shenzhen Stock Exchange'}, {'Exchange': 'Toronto Stock Exchange'}, {'Exchange': 'National Stock Exchange of India'}, {'Exchange': 'Frankfurt Stock Exchange'}, {'Exchange': 'Korea Exchange'}, {'Exchange': 'SIX Swiss Exchange'}, {'Exchange': 'Taiwan Stock Exchange'}, {'Exchange': 'Johannesburg Stock Exchange'}], 'var_call_452ryx2fNC1ctWBjyh7nWMWi': [{'Index': 'J203.JO'}, {'Index': 'IXIC'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'NYA'}, {'Index': 'N100'}, {'Index': '399001.SZ'}, {'Index': 'HSI'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_call_tNDSfTEgaBXzCo5mx3z2Qy5U': [{'Index': 'N225', 'up_days': '32.0', 'down_days': '42.0'}, {'Index': 'GSPTSE', 'up_days': '44.0', 'down_days': '41.0'}, {'Index': 'NSEI', 'up_days': '40.0', 'down_days': '38.0'}, {'Index': 'GDAXI', 'up_days': '50.0', 'down_days': '48.0'}, {'Index': 'HSI', 'up_days': '43.0', 'down_days': '42.0'}, {'Index': '000001.SS', 'up_days': '47.0', 'down_days': '37.0'}, {'Index': 'SSMI', 'up_days': '54.0', 'down_days': '39.0'}, {'Index': 'TWII', 'up_days': '39.0', 'down_days': '39.0'}, {'Index': 'N100', 'up_days': '31.0', 'down_days': '36.0'}, {'Index': '399001.SZ', 'up_days': '33.0', 'down_days': '43.0'}, {'Index': 'NYA', 'up_days': '36.0', 'down_days': '42.0'}, {'Index': 'IXIC', 'up_days': '44.0', 'down_days': '31.0'}, {'Index': 'J203.JO', 'up_days': '37.0', 'down_days': '44.0'}]}

exec(code, env_args)
