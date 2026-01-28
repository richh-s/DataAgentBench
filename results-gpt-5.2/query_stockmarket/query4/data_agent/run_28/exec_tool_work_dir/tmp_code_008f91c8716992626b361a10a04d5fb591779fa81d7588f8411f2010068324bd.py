code = """import json
v2=var_call_53fSB6wCGArWqzaRLsIKLcr4
if isinstance(v2,str):
    tables=json.load(open(v2))
else:
    tables=v2
trade_set=set(tables)
for s in ['DHI','GES','DB','KSU']:
    print('__RESULT__:')
    import json as _json
    print(_json.dumps({s: s in trade_set, 'sample_similar':[t for t in tables if t.startswith(s[:2])][:10]}))
    break"""

env_args = {'var_call_8Rmh6nq21wxXn4UkriQTxNnE': 'file_storage/call_8Rmh6nq21wxXn4UkriQTxNnE.json', 'var_call_53fSB6wCGArWqzaRLsIKLcr4': 'file_storage/call_53fSB6wCGArWqzaRLsIKLcr4.json', 'var_call_fgUZlAnSreN5Yh3kqwKzCzRT': 'file_storage/call_fgUZlAnSreN5Yh3kqwKzCzRT.json', 'var_call_7UpfW7yFAS8XXLPO6POIvZU0': {'n_sqls': 2, 'n_symbols': 234}, 'var_call_x9AcRZPOnYc0zbV9uGogn3CO': 'file_storage/call_x9AcRZPOnYc0zbV9uGogn3CO.json'}

exec(code, env_args)
