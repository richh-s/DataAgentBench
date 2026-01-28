code = """import json

def load_json_maybe_path(obj):
    if isinstance(obj, str):
        with open(obj, 'r') as f:
            return json.load(f)
    return obj

etf_recs = load_json_maybe_path(var_call_RiPZWWF1mTryWxhHo7gaq8ws)
etf_symbols = sorted({r.get('symbol') for r in etf_recs if r.get('symbol')})

tbl_recs = load_json_maybe_path(var_call_cw0Mxn4Y8hxFrStH0Eb8j1ha)
tables = [r['table_name'] for r in tbl_recs if r.get('table_name')]
tables_set = set(tables)

symbols = [s for s in etf_symbols if s in tables_set]

# select likely high-price ETFs to reduce query size
likely = [s for s in symbols if s in ['GOOG','AMZN']]

print('__RESULT__:')
print(json.dumps({'n_candidates': len(symbols), 'sample_symbols': symbols[:20]}))"""

env_args = {'var_call_RiPZWWF1mTryWxhHo7gaq8ws': 'file_storage/call_RiPZWWF1mTryWxhHo7gaq8ws.json', 'var_call_4WNlDK7WYm54JxmY57bjQxWF': 'file_storage/call_4WNlDK7WYm54JxmY57bjQxWF.json', 'var_call_cw0Mxn4Y8hxFrStH0Eb8j1ha': 'file_storage/call_cw0Mxn4Y8hxFrStH0Eb8j1ha.json', 'var_call_2oXONNb2ezm4aYKJgPYWyzxh': [{'Date': '1993-01-29', 'Open': '43.96875', 'High': '43.96875', 'Low': '43.75', 'Close': '43.9375', 'Adj Close': '26.299287796020508', 'Volume': '1003200'}], 'var_call_rhE6aBgEuCOmI7T1olT3mC7b': [{'symbol': 'SPY'}], 'var_call_soOWbhmClZ092XG6UJLR4pDk': {'ok': True}, 'var_call_SSfhZFNqg7kZbIVI6roo9no1': {'s': "SELECT 'A' AS symbol"}, 'var_call_yx7MXgh0SGCEllav0uMVdNMQ': [], 'var_call_2TgS9tjXuKrFriTStoISzzG4': [], 'var_call_ZYqeBMdDPUhphBCtT8mII3W6': [], 'var_call_8utG35WGdjIAqTVtOTYvqo6g': [], 'var_call_5DXxB8rU1NnUM0RoZOQ8bytM': [{'symbol': 'SPY', 'max_adj_close': '193.3121490478516'}]}

exec(code, env_args)
