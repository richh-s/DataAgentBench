code = """import json, pandas as pd

# load symbols from file
path_symbols = var_call_q7oLujAQPcdluZq4wIf6UcE4
with open(path_symbols, 'r') as f:
    symbols = [r['symbol'] for r in json.load(f)]

# load available tables list
path_tables = var_call_xKK2gQkeQKeKmrdma80MfrG0
with open(path_tables, 'r') as f:
    tables = set(json.load(f))

# intersect
symbols = [s for s in symbols if s in tables]

# build union query to find max Adj Close in 2015 for each symbol
parts = []
for s in symbols:
    # quote table name for duckdb
    t = '"' + s.replace('"','""') + '"'
    parts.append(f"SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM {t} WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'")

# DuckDB can handle large UNION ALL; chunk if extremely large
chunk_size = 400
results = []
for i in range(0, len(parts), chunk_size):
    q = " UNION ALL ".join(parts[i:i+chunk_size])
    res = functions.query_db({'db_name':'stocktrade_database','query': q})
    if isinstance(res, str):
        raise RuntimeError(res)
    results.extend(res)

df = pd.DataFrame(results)
df['max_adj_close_2015'] = pd.to_numeric(df['max_adj_close_2015'], errors='coerce')
filtered = df[df['max_adj_close_2015'] > 200].copy()
filtered = filtered.sort_values(['symbol']).reset_index(drop=True)
answer_obj = {
    'total_etfs': int(filtered.shape[0]),
    'etfs': filtered.to_dict(orient='records')
}
print('__RESULT__:')
print(json.dumps(answer_obj))"""

env_args = {'var_call_q7oLujAQPcdluZq4wIf6UcE4': 'file_storage/call_q7oLujAQPcdluZq4wIf6UcE4.json', 'var_call_xKK2gQkeQKeKmrdma80MfrG0': 'file_storage/call_xKK2gQkeQKeKmrdma80MfrG0.json'}

exec(code, env_args)
