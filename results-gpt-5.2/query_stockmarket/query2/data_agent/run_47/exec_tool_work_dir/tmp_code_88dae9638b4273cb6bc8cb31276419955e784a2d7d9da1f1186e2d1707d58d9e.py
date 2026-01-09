code = """import json, pandas as pd

# load results
path_info = var_call_gKoK14VmHOpdSnLGsEJyjiQI
with open(path_info, 'r') as f:
    info = json.load(f)

path_tbls = var_call_bzHgWJ1f135Ch9vkcGJQ06eI
with open(path_tbls, 'r') as f:
    tbls = set(json.load(f))

# candidate NYSE Arca ETFs that have trade tables
candidates = [r for r in info if r['symbol'] in tbls]
syms = [r['symbol'] for r in candidates]

# build UNION ALL query to find those with max adj close in 2015 > 200
parts = []
for s in syms:
    parts.append(f"SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{s}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")
union = " UNION ALL ".join(parts)
query = f"SELECT symbol, max_adj_close_2015 FROM ({union}) t WHERE max_adj_close_2015 > 200 ORDER BY symbol;"

print('__RESULT__:')
print(json.dumps({'query': query, 'candidate_count': len(syms)}))"""

env_args = {'var_call_gKoK14VmHOpdSnLGsEJyjiQI': 'file_storage/call_gKoK14VmHOpdSnLGsEJyjiQI.json', 'var_call_bzHgWJ1f135Ch9vkcGJQ06eI': 'file_storage/call_bzHgWJ1f135Ch9vkcGJQ06eI.json'}

exec(code, env_args)
