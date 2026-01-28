code = """import json
p1 = var_call_NIDNMEeHl81D5HYgLuX7GEFj
p2 = var_call_8cVsmLvz8FcPWR1jERTMyhAK
with open(p1, 'r') as f:
    stockinfo = json.load(f)
with open(p2, 'r') as f:
    tables = json.load(f)
symbols = [r['Symbol'] for r in stockinfo]
tables_set = set(tables)
candidates = [s for s in symbols if s in tables_set]
parts = []
for s in candidates:
    parts.append("SELECT '{}' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"{}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(s, s))
query = ' UNION ALL '.join(parts) + ';' if parts else ''
# limit size of query if too big? we'll output full
print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_call_NIDNMEeHl81D5HYgLuX7GEFj': 'file_storage/call_NIDNMEeHl81D5HYgLuX7GEFj.json', 'var_call_8cVsmLvz8FcPWR1jERTMyhAK': 'file_storage/call_8cVsmLvz8FcPWR1jERTMyhAK.json', 'var_call_NEqKAPASIrmuOXlZt1W1DLeW': [], 'var_call_Hi2GhiDvgtaJo4RqeOOZjApS': {'num_stockinfo_symbols': 1435, 'num_tables': 2753, 'first_5_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'first_5_tables': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ']}}

exec(code, env_args)
