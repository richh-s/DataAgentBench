code = """import json, pandas as pd

# Load NYSE Arca ETFs list
p = var_call_v8UAmsuj3jIxT9Csk8ySlzip
with open(p, 'r') as f:
    etfs = json.load(f)

symbols = sorted({r['Symbol'] for r in etfs if r.get('Symbol')})

# Load available price tables
p2 = var_call_7cQ5gSCfYebF9BuEJ5E83c8m
with open(p2, 'r') as f:
    tables = set(json.load(f))

symbols_in_db = [s for s in symbols if s in tables]

# chunk symbols to keep query length reasonable
chunks = [symbols_in_db[i:i+200] for i in range(0, len(symbols_in_db), 200)]

queries = []
for chunk in chunks:
    union_parts = []
    for sym in chunk:
        # quote column names with spaces
        union_parts.append(
            f"SELECT '{sym}' AS symbol, MAX(\"Adj Close\") AS max_adj_close FROM \"{sym}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
        )
    queries.append(" UNION ALL ".join(union_parts))

final_rows = []
for q in queries:
    # wrap with outer select for safety
    sql = f"SELECT symbol, max_adj_close FROM ({q}) t"
    # execute via query_db
    from pathlib import Path
    # Can't call tools from python; instead emit SQL strings as result for next step
    final_rows.append(sql)

print('__RESULT__:')
print(json.dumps({'symbols_total': len(symbols), 'symbols_in_price_db': len(symbols_in_db), 'sql_chunks': final_rows}))"""

env_args = {'var_call_v8UAmsuj3jIxT9Csk8ySlzip': 'file_storage/call_v8UAmsuj3jIxT9Csk8ySlzip.json', 'var_call_7cQ5gSCfYebF9BuEJ5E83c8m': 'file_storage/call_7cQ5gSCfYebF9BuEJ5E83c8m.json'}

exec(code, env_args)
