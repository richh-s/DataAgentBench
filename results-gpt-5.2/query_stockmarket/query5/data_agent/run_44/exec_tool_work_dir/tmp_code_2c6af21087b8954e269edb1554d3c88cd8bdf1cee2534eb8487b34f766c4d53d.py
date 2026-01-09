code = """import json, pandas as pd

p = var_call_4aGwTzh70bt8xarEObPHR1xp
with open(p, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

p2 = var_call_ptTAFVhG5hNvbNHxEpsBJBbz
with open(p2, 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

symbols = [s for s in info_df['Symbol'].tolist() if s in tables_set]

parts = []
for sym in symbols:
    parts.append(f"SELECT '{sym}' AS Symbol, COUNT(*) AS days FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND High > 1.2*Low")

union_query = "\nUNION ALL\n".join(parts)
final_query = f"SELECT Symbol, days FROM ({union_query}) t ORDER BY days DESC, Symbol ASC LIMIT 5"

print('__RESULT__:')
print(json.dumps({'n_symbols': len(symbols), 'query_len': len(final_query), 'query': final_query[:1000]}))"""

env_args = {'var_call_4aGwTzh70bt8xarEObPHR1xp': 'file_storage/call_4aGwTzh70bt8xarEObPHR1xp.json', 'var_call_ptTAFVhG5hNvbNHxEpsBJBbz': 'file_storage/call_ptTAFVhG5hNvbNHxEpsBJBbz.json'}

exec(code, env_args)
