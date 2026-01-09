code = """import json

path_info = var_call_gKoK14VmHOpdSnLGsEJyjiQI
with open(path_info, 'r') as f:
    info = json.load(f)

path_tbls = var_call_bzHgWJ1f135Ch9vkcGJQ06eI
with open(path_tbls, 'r') as f:
    tbls = set(json.load(f))

candidates = [r for r in info if r['symbol'] in tbls]
syms = [r['symbol'] for r in candidates]

parts = []
for s in syms:
    parts.append("SELECT '{}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(s, s))
union = " UNION ALL ".join(parts)
query = "SELECT symbol, max_adj_close_2015 FROM ({}) t WHERE max_adj_close_2015 > 200 ORDER BY symbol".format(union)

print('__RESULT__:')
print(json.dumps({'query': query, 'candidate_count': len(syms)}))"""

env_args = {'var_call_gKoK14VmHOpdSnLGsEJyjiQI': 'file_storage/call_gKoK14VmHOpdSnLGsEJyjiQI.json', 'var_call_bzHgWJ1f135Ch9vkcGJQ06eI': 'file_storage/call_bzHgWJ1f135Ch9vkcGJQ06eI.json'}

exec(code, env_args)
