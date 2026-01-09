code = """import json

path_syms = var_call_9gr3C52aJISXb1HRdB6mzE3y
with open(path_syms, 'r') as f:
    syms = [r['symbol'] for r in json.load(f)]

path_tbl = var_call_BQsEwl6Xrktdi72zmjmmTlES
with open(path_tbl, 'r') as f:
    tbls = set(json.load(f))

syms = [s for s in syms if s in tbls]

results = []
for s in syms:
    q = "SELECT MAX(\"Adj Close\") AS max_adj_close FROM \"{}\" WHERE \"Date\">='2015-01-01' AND \"Date\"<='2015-12-31';".format(s)
    recs = query_db(db_name='stocktrade_database', query=q)
    if isinstance(recs, str):
        continue
    mx = recs[0].get('max_adj_close') if recs else None
    if mx is not None and float(mx) > 200:
        results.append({'symbol': s, 'max_adj_close_2015': float(mx)})

results = sorted(results, key=lambda x: x['symbol'])
out = {'etfs': results, 'total': len(results)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_9gr3C52aJISXb1HRdB6mzE3y': 'file_storage/call_9gr3C52aJISXb1HRdB6mzE3y.json', 'var_call_BQsEwl6Xrktdi72zmjmmTlES': 'file_storage/call_BQsEwl6Xrktdi72zmjmmTlES.json'}

exec(code, env_args)
