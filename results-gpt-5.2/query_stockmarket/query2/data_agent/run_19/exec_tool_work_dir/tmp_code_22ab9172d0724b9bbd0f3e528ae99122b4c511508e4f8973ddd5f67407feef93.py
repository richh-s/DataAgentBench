code = """import json
syms = ['SPY']
results=[]
for s in syms:
    q = 'SELECT MAX("Adj Close") AS max_adj_close FROM "{}" WHERE "Date">=\'2015-01-01\' AND "Date"<=\'2015-12-31\';'.format(s)
    recs = query_db(db_name='stocktrade_database', query=q)
    results.append(recs)
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_9gr3C52aJISXb1HRdB6mzE3y': 'file_storage/call_9gr3C52aJISXb1HRdB6mzE3y.json', 'var_call_BQsEwl6Xrktdi72zmjmmTlES': 'file_storage/call_BQsEwl6Xrktdi72zmjmmTlES.json', 'var_call_Ev5x5EekyLRagCfvanEzWZEQ': [{'ok': '1'}], 'var_call_qSp1hGtsjy4lpooQ5cSwghQE': {'ok': True}, 'var_call_Iw3CpdACyRK2w0yJZGadaOWf': {'n': 1435, 'first': [{'symbol': 'AAAU'}, {'symbol': 'AADR'}, {'symbol': 'ABEQ'}]}, 'var_call_vC6ACx0MkOFtUMwrTO9aWBr1': {'n_syms': 1435, 'n_trade_tables': 2753, 'n_intersection': 1435, 'sample': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY']}, 'var_call_gRucDhPY8luoUjitxtKlPmUt': [{'max_adj_close': '193.3121490478516'}], 'var_call_C4ftzuf9OkSmHtf409na6diM': {'a': 'x"y'}}

exec(code, env_args)
