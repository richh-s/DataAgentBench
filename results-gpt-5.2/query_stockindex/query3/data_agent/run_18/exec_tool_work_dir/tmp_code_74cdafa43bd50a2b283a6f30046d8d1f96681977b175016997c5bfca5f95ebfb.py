code = """import json
from math import isfinite

rows = var_call_0ShFufcmeXfqCStBpO90JHXe
# Map index symbol to country (geographic knowledge)
country_map = {
  '399001.SZ': 'China',   # Shenzhen Component
  '000001.SS': 'China',   # Shanghai Composite
  'IXIC': 'United States', # Nasdaq Composite
  'NYA': 'United States',  # NYSE Composite
  'NSEI': 'India'          # NIFTY 50
}

out = []
for r in rows:
    idx = r['Index']
    tr = float(r['total_return'])
    out.append({
        'Index': idx,
        'Country': country_map.get(idx, None),
        'Overall_return_multiple_since_2000': tr
    })

result = json.dumps(out)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_sBd1NCszUbbcnbLEU2pFLmQS': ['index_info'], 'var_call_MGAnbgpOxiEGdo6M4LF6aXrI': ['index_trade'], 'var_call_0ShFufcmeXfqCStBpO90JHXe': [{'Index': '399001.SZ', 'total_return': '4.299262814004764'}, {'Index': 'IXIC', 'total_return': '3.5613081331723295'}, {'Index': 'NSEI', 'total_return': '3.2559043994701793'}, {'Index': 'NYA', 'total_return': '2.4807329257936566'}, {'Index': '000001.SS', 'total_return': '2.3416159589604826'}]}

exec(code, env_args)
