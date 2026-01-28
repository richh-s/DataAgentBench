code = """import json
# read the stored results
with open('file_storage/call_p3wehT7WbD92Ab0NJaPpAfGD.json','r') as f:
    stockinfo = json.load(f)
with open('file_storage/call_Brv828NQIaemUxAB6OfCNpOc.json','r') as f:
    trade_tables = json.load(f)
mapping = {item['Symbol']: item.get('Company Description','') for item in stockinfo}
# filter out ETFs explicitly marked 'Y'
mapping = {k:v for k,v in mapping.items()}
symbols = [s for s in mapping.keys() if s in trade_tables]
# limit to first 500 symbols to avoid too large UNION ALL
symbols = sorted(symbols)
print_count = min(5, len(symbols))
sample = symbols[:print_count]
output = {'symbols_sample': sample, 'symbols_count': len(symbols)}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_p3wehT7WbD92Ab0NJaPpAfGD': 'file_storage/call_p3wehT7WbD92Ab0NJaPpAfGD.json', 'var_call_Brv828NQIaemUxAB6OfCNpOc': 'file_storage/call_Brv828NQIaemUxAB6OfCNpOc.json', 'var_call_vXJROydgUZN5l3qOIPDotLEG': ['file_storage/call_p3wehT7WbD92Ab0NJaPpAfGD.json', 'file_storage/call_Brv828NQIaemUxAB6OfCNpOc.json']}

exec(code, env_args)
