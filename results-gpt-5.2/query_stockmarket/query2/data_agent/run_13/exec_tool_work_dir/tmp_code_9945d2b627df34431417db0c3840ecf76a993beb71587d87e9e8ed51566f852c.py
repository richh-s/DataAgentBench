code = """import json, pandas as pd

path_symbols = var_call_q7oLujAQPcdluZq4wIf6UcE4
with open(path_symbols, 'r') as f:
    symbols = [r['symbol'] for r in json.load(f)]

path_tables = var_call_xKK2gQkeQKeKmrdma80MfrG0
with open(path_tables, 'r') as f:
    tables = set(json.load(f))

symbols = [s for s in symbols if s in tables]

parts = []
for s in symbols:
    t = '"' + s.replace('"','""') + '"'
    parts.append(
        "SELECT '{sym}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM {tbl} "
        "WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(sym=s, tbl=t)
    )

chunk_size = 400
results = []
for i in range(0, len(parts), chunk_size):
    q = " UNION ALL ".join(parts[i:i+chunk_size])
    res = functions.query_db({'db_name':'stocktrade_database','query': q})
    if isinstance(res, str):
        raise RuntimeError(res)
    results.extend(res)

df = pd.DataFrame(results)
if not df.empty:
    df['max_adj_close_2015'] = pd.to_numeric(df['max_adj_close_2015'], errors='coerce')
filtered = df[df['max_adj_close_2015'] > 200].copy() if not df.empty else df
filtered = filtered.sort_values(['symbol']).reset_index(drop=True) if not filtered.empty else filtered

answer_obj = {
    'total_etfs': int(filtered.shape[0]) if hasattr(filtered, 'shape') else 0,
    'etfs': filtered.to_dict(orient='records') if not filtered.empty else []
}

print('__RESULT__:')
print(json.dumps(answer_obj))"""

env_args = {'var_call_q7oLujAQPcdluZq4wIf6UcE4': 'file_storage/call_q7oLujAQPcdluZq4wIf6UcE4.json', 'var_call_xKK2gQkeQKeKmrdma80MfrG0': 'file_storage/call_xKK2gQkeQKeKmrdma80MfrG0.json'}

exec(code, env_args)
