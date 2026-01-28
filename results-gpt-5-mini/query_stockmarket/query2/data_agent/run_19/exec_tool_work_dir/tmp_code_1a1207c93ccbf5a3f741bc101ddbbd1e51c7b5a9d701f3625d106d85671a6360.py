code = """import json
# load storage files
p1 = var_call_NIDNMEeHl81D5HYgLuX7GEFj
p2 = var_call_8cVsmLvz8FcPWR1jERTMyhAK
with open(p1, 'r') as f:
    stockinfo = json.load(f)
with open(p2, 'r') as f:
    tables = json.load(f)
symbols = [r['Symbol'] for r in stockinfo]
# intersect with available tables
tables_set = set(tables)
candidates = [s for s in symbols if s in tables_set]
# build union query
parts = []
for s in candidates:
    part = f"SELECT '{s}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{s}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
    parts.append(part)
if not parts:
    query = ''
else:
    query = ' UNION ALL '.join(parts) + ';'
print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_call_NIDNMEeHl81D5HYgLuX7GEFj': 'file_storage/call_NIDNMEeHl81D5HYgLuX7GEFj.json', 'var_call_8cVsmLvz8FcPWR1jERTMyhAK': 'file_storage/call_8cVsmLvz8FcPWR1jERTMyhAK.json', 'var_call_NEqKAPASIrmuOXlZt1W1DLeW': []}

exec(code, env_args)
