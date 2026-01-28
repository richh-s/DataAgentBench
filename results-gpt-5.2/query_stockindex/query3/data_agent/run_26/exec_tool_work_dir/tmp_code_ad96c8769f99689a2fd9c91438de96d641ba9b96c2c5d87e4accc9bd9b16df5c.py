code = """import json
indices = [r['Index'] for r in var_call_58CJsaM3XS7iGgDMos6u73SY]
# Map known index symbols to countries (geographic knowledge)
country_map = {
  '399001.SZ': 'China',  # Shenzhen Component
  '000001.SS': 'China',  # SSE Composite (Shanghai)
  'IXIC': 'United States',  # NASDAQ Composite
  'NYA': 'United States',  # NYSE Composite
  'NSEI': 'India',  # NIFTY 50
}
out = []
for r in var_call_58CJsaM3XS7iGgDMos6u73SY:
    idx = r['Index']
    out.append({
        'Index': idx,
        'total_return_since_2000': float(r['total_return']),
        'country': country_map.get(idx, None)
    })
result = json.dumps(out)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_WwiCezo2mdcHP1Am4qEepuEj': ['index_info'], 'var_call_qF3X0lsotjONowqnxyCb173L': ['index_trade'], 'var_call_58CJsaM3XS7iGgDMos6u73SY': [{'Index': '399001.SZ', 'n_months': '257', 'total_return': '3.0221563755444905'}, {'Index': 'IXIC', 'n_months': '256', 'total_return': '2.375268668829846'}, {'Index': 'NSEI', 'n_months': '164', 'total_return': '2.1295668828787284'}, {'Index': 'NYA', 'n_months': '256', 'total_return': '1.4280838592365757'}, {'Index': '000001.SS', 'n_months': '256', 'total_return': '1.3686189382256182'}]}

exec(code, env_args)
