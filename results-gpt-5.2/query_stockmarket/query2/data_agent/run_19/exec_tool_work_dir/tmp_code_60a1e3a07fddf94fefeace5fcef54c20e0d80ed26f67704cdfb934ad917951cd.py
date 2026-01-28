code = """import json
path_syms = var_call_9gr3C52aJISXb1HRdB6mzE3y
with open(path_syms,'r') as f:
    syms = [r['symbol'] for r in json.load(f)]
path_tbl = var_call_BQsEwl6Xrktdi72zmjmmTlES
with open(path_tbl,'r') as f:
    tbls = set(json.load(f))
syms2 = [s for s in syms if s in tbls]
print('__RESULT__:')
print(json.dumps({'n_syms': len(syms), 'n_trade_tables': len(tbls), 'n_intersection': len(syms2), 'sample': syms2[:10]}))"""

env_args = {'var_call_9gr3C52aJISXb1HRdB6mzE3y': 'file_storage/call_9gr3C52aJISXb1HRdB6mzE3y.json', 'var_call_BQsEwl6Xrktdi72zmjmmTlES': 'file_storage/call_BQsEwl6Xrktdi72zmjmmTlES.json', 'var_call_Ev5x5EekyLRagCfvanEzWZEQ': [{'ok': '1'}], 'var_call_qSp1hGtsjy4lpooQ5cSwghQE': {'ok': True}, 'var_call_Iw3CpdACyRK2w0yJZGadaOWf': {'n': 1435, 'first': [{'symbol': 'AAAU'}, {'symbol': 'AADR'}, {'symbol': 'ABEQ'}]}}

exec(code, env_args)
