code = """import json

k1 = 'var_function-call-17042838615002828598'
k2 = 'var_function-call-1654927262755686554'
f1 = locals()[k1]
f2 = locals()[k2]

with open(f1, 'r') as f:
    d1 = json.load(f)
etf_symbols = set([item['Symbol'] for item in d1])

with open(f2, 'r') as f:
    d2 = json.load(f)
table_set = set(d2)

valid_etfs = sorted(list(etf_symbols.intersection(table_set)))

batch = valid_etfs[0:150]
parts = []
# Use format to avoid escaping issues
tmpl = "SELECT '{}' s,MAX(\"Adj Close\") m FROM \"{}\" WHERE Date GLOB '2015*'"

for sym in batch:
    parts.append(tmpl.format(sym, sym))

full_query = "SELECT s FROM (" + " UNION ALL ".join(parts) + ") WHERE m > 200"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-17042838615002828598': 'file_storage/function-call-17042838615002828598.json', 'var_function-call-1654927262755686554': 'file_storage/function-call-1654927262755686554.json', 'var_function-call-8866745000760518391': 'file_storage/function-call-8866745000760518391.json', 'var_function-call-802954950120546445': 1435, 'var_function-call-13265981638886937521': 'OK'}

exec(code, env_args)
