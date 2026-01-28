code = """import json
# load storage variables
p1 = var_call_NOrOeolxry3KNh5kwmiCZwYH
p2 = var_call_mt89zRyxGP2HAtEkz4Dmna3z

with open(p1, 'r') as f:
    data1 = json.load(f)
with open(p2, 'r') as f:
    data2 = json.load(f)

symbols_info = {rec['Symbol']: rec.get('Company Description','') for rec in data1}
trade_symbols = set(data2)

candidates = []
for s, desc in symbols_info.items():
    if s in trade_symbols:
        candidates.append({'Symbol': s, 'Company Description': desc})

# sort candidates by symbol for consistency
candidates = sorted(candidates, key=lambda x: x['Symbol'])

result = json.dumps(candidates)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_NOrOeolxry3KNh5kwmiCZwYH': 'file_storage/call_NOrOeolxry3KNh5kwmiCZwYH.json', 'var_call_mt89zRyxGP2HAtEkz4Dmna3z': 'file_storage/call_mt89zRyxGP2HAtEkz4Dmna3z.json'}

exec(code, env_args)
