code = """import json, pandas as pd

# Load NYSE non-ETF symbols
symbols_path = var_call_3MxZqE8D8mCsY0STYp4ujphc
with open(symbols_path, 'r') as f:
    nyse = json.load(f)
nyse_df = pd.DataFrame(nyse)
nyse_symbols = set(nyse_df['Symbol'].tolist())

# Load available trade tables
tables_path = var_call_uMrsBwkUnotoXp99tcZtbiOO
with open(tables_path, 'r') as f:
    tables = json.load(f)
avail = set(tables)

symbols = sorted(nyse_symbols & avail)

# Rank by number of up days in 2017 (with condition up_days > down_days)
# Use DuckDB: union all per-table aggregates using read from each table directly.
# Chunk to avoid huge query strings.
chunks = [symbols[i:i+200] for i in range(0, len(symbols), 200)]

queries = []
for ch in chunks:
    parts = []
    for sym in ch:
        # table names may need quoting if special chars; assume standard uppercase letters
        parts.append(
            f"SELECT '{sym}' AS Symbol, "
            f"SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
            f"SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
            f"FROM {sym} WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
        )
    queries.append(" UNION ALL ".join(parts))

# Print queries for subsequent execution via query_db in python result
print('__RESULT__:')
print(json.dumps(queries))"""

env_args = {'var_call_3MxZqE8D8mCsY0STYp4ujphc': 'file_storage/call_3MxZqE8D8mCsY0STYp4ujphc.json', 'var_call_uMrsBwkUnotoXp99tcZtbiOO': 'file_storage/call_uMrsBwkUnotoXp99tcZtbiOO.json'}

exec(code, env_args)
