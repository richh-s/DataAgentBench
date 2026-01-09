code = """import json

def load_maybe_path(v):
    if isinstance(v, str):
        with open(v, 'r') as f:
            return json.load(f)
    return v

d = load_maybe_path(var_call_NFw8A9LxqHusRAUtJGqoeSLr)
# limit tickers to those likely above 200 to reduce queries: keep those containing 'SPX' etc? can't. We'll just take all and query with SQL per ticker in DuckDB may be heavy; instead build a UNION ALL query for subset? still large.
# We'll do incremental batched UNION queries with python building and later merging results.

tickers = d['tickers']
print('__RESULT__:')
print(json.dumps({'n_tickers': len(tickers)}))"""

env_args = {'var_call_jMt97FSyhoanOw2XfsV5xNc8': 'file_storage/call_jMt97FSyhoanOw2XfsV5xNc8.json', 'var_call_nXA3YSD1lrPQqkZBI4V8Tkvb': 'file_storage/call_nXA3YSD1lrPQqkZBI4V8Tkvb.json', 'var_call_NFw8A9LxqHusRAUtJGqoeSLr': 'file_storage/call_NFw8A9LxqHusRAUtJGqoeSLr.json'}

exec(code, env_args)
