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

# chunk symbols to keep query size manageable
chunks = []
chunk = []
max_chunk = 120
for s in symbols:
    chunk.append(s)
    if len(chunk) >= max_chunk:
        chunks.append(chunk)
        chunk = []
if chunk:
    chunks.append(chunk)

union_queries = []
for ch in chunks:
    subqs = []
    for s in ch:
        subqs.append("SELECT '{sym}' AS symbol, MAX(\"Adj Close\")::DOUBLE AS max_adj_close FROM \"{sym}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(sym=s))
    union_queries.append("SELECT symbol FROM ({u}) t WHERE max_adj_close > 200".format(u=" UNION ALL ".join(subqs)))

final_query = "SELECT DISTINCT symbol FROM (" + " UNION ALL ".join(union_queries) + ") x ORDER BY symbol;"

print('__RESULT__:')
print(json.dumps({'final_query': final_query, 'n_candidates': len(symbols), 'n_chunks': len(chunks)}))"""

env_args = {'var_call_RiPZWWF1mTryWxhHo7gaq8ws': 'file_storage/call_RiPZWWF1mTryWxhHo7gaq8ws.json', 'var_call_4WNlDK7WYm54JxmY57bjQxWF': 'file_storage/call_4WNlDK7WYm54JxmY57bjQxWF.json', 'var_call_cw0Mxn4Y8hxFrStH0Eb8j1ha': 'file_storage/call_cw0Mxn4Y8hxFrStH0Eb8j1ha.json', 'var_call_2oXONNb2ezm4aYKJgPYWyzxh': [{'Date': '1993-01-29', 'Open': '43.96875', 'High': '43.96875', 'Low': '43.75', 'Close': '43.9375', 'Adj Close': '26.299287796020508', 'Volume': '1003200'}]}

exec(code, env_args)
