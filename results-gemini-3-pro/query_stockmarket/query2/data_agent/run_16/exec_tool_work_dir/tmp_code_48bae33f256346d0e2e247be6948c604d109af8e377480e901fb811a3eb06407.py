code = """import json

# Get filenames
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

# Batch 1: 0 to 150
batch = valid_etfs[0:150]
parts = []
for sym in batch:
    # Minimal query: SELECT 'SYM',MAX("Adj Close")m FROM "SYM" WHERE Date GLOB '2015*' HAVING m>200
    # Note: DuckDB allows HAVING without GROUP BY if aggregating everything
    # But for UNION, columns must match.
    # SELECT 'SYM', MAX("Adj Close") FROM ...
    p = "SELECT '" + sym + "' s,MAX(\"Adj Close\") m FROM \"" + sym + "\" WHERE Date GLOB '2015*'"
    parts.append(p)

full_query = "SELECT s FROM (" + " UNION ALL ".join(parts) + ") WHERE m > 200"

print("__RESULT__:")
print(json.dumps(full_query))"""

env_args = {'var_function-call-17042838615002828598': 'file_storage/function-call-17042838615002828598.json', 'var_function-call-1654927262755686554': 'file_storage/function-call-1654927262755686554.json', 'var_function-call-8866745000760518391': 'file_storage/function-call-8866745000760518391.json', 'var_function-call-802954950120546445': 1435, 'var_function-call-13265981638886937521': 'OK'}

exec(code, env_args)
