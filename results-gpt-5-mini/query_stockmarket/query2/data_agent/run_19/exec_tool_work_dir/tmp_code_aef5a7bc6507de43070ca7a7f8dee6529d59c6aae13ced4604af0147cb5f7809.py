code = """import json
p1 = var_call_NIDNMEeHl81D5HYgLuX7GEFj
p2 = var_call_8cVsmLvz8FcPWR1jERTMyhAK
with open(p1,'r') as f:
    stockinfo = json.load(f)
with open(p2,'r') as f:
    tables = json.load(f)
symbols = [r['Symbol'] for r in stockinfo]
tables_set = set(tables)
candidates = [s for s in symbols if s in tables_set]
# chunk candidates into groups of 100
chunks = [candidates[i:i+100] for i in range(0, len(candidates), 100)]
queries = []
for chunk in chunks:
    parts = []
    for s in chunk:
        parts.append("SELECT '" + s + "' AS Symbol, MAX(\"Adj Close\") AS max_adj FROM \"" + s + "\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")
    q = ' UNION ALL '.join(parts) + ';'
    queries.append(q)
out = {'num_candidates': len(candidates), 'num_chunks': len(chunks), 'queries': queries}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_NIDNMEeHl81D5HYgLuX7GEFj': 'file_storage/call_NIDNMEeHl81D5HYgLuX7GEFj.json', 'var_call_8cVsmLvz8FcPWR1jERTMyhAK': 'file_storage/call_8cVsmLvz8FcPWR1jERTMyhAK.json', 'var_call_NEqKAPASIrmuOXlZt1W1DLeW': [], 'var_call_Hi2GhiDvgtaJo4RqeOOZjApS': {'num_stockinfo_symbols': 1435, 'num_tables': 2753, 'first_5_symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF'], 'first_5_tables': ['AAAU', 'AADR', 'AAME', 'AAWW', 'AAXJ']}, 'var_call_hHtRIbEuHf1WJU8z4mWFTV78': [{'Symbol': 'SPY'}], 'var_call_tB0XwtvjumK5JsSPctqVXthP': [{'max_adj': '193.3121490478516'}]}

exec(code, env_args)
