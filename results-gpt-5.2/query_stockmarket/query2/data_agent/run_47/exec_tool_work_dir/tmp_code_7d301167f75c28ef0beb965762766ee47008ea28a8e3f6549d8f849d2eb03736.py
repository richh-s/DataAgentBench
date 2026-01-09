code = """import json
with open(var_call_gKoK14VmHOpdSnLGsEJyjiQI,'r') as f:
    info=json.load(f)
with open(var_call_bzHgWJ1f135Ch9vkcGJQ06eI,'r') as f:
    tbls=set(json.load(f))
syms=[r['symbol'] for r in info if r['symbol'] in tbls]
parts=[]
for s in syms[:5]:
    parts.append("SELECT '{}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(s,s))
union=' UNION ALL '.join(parts)
query="SELECT symbol, max_adj_close_2015 FROM ({}) t WHERE max_adj_close_2015 > 200 ORDER BY symbol".format(union)
print('__RESULT__:')
print(json.dumps({'query':query}))"""

env_args = {'var_call_gKoK14VmHOpdSnLGsEJyjiQI': 'file_storage/call_gKoK14VmHOpdSnLGsEJyjiQI.json', 'var_call_bzHgWJ1f135Ch9vkcGJQ06eI': 'file_storage/call_bzHgWJ1f135Ch9vkcGJQ06eI.json', 'var_call_C6acdiGqab5ugUH68pm0zEs7': {'n': 1435, 'first10': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}}

exec(code, env_args)
