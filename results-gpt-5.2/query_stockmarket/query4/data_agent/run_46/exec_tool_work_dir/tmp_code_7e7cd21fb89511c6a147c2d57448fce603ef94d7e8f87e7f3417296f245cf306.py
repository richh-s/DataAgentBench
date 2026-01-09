code = """import json, pandas as pd

# Load NYSE non-ETF symbols from SQLite result (may be file path)
raw = var_call_nRg4zi2zm0tDJpk3JAndwSRL
if isinstance(raw, str):
    with open(raw, 'r') as f:
        nyse_recs = json.load(f)
else:
    nyse_recs = raw
nyse_df = pd.DataFrame(nyse_recs)
nyse_syms = set(nyse_df['Symbol'].astype(str))

# Load available trade tables
raw2 = var_call_2eLtZz9Xkk8ZzWBJcJg9PuVs
if isinstance(raw2, str):
    with open(raw2, 'r') as f:
        trade_tables = json.load(f)
else:
    trade_tables = raw2
trade_set = set(trade_tables)

candidates = sorted(nyse_syms.intersection(trade_set))

# Prepare list of unions in chunks to avoid huge SQL
chunks = [candidates[i:i+200] for i in range(0, len(candidates), 200)]
queries = []
for ch in chunks:
    parts = []
    for sym in ch:
        # quote table name for DuckDB, and compute up/down in 2017
        parts.append(
            f"SELECT '{sym}' AS Symbol, "
            f"SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
            f"SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
            f"FROM \"{sym}\" WHERE Date >= '2017-01-01' AND Date < '2018-01-01'"
        )
    queries.append(" UNION ALL ".join(parts))

# Store queries for next step
out = {"candidate_count": len(candidates), "query_chunks": queries}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_nRg4zi2zm0tDJpk3JAndwSRL': 'file_storage/call_nRg4zi2zm0tDJpk3JAndwSRL.json', 'var_call_2eLtZz9Xkk8ZzWBJcJg9PuVs': 'file_storage/call_2eLtZz9Xkk8ZzWBJcJg9PuVs.json'}

exec(code, env_args)
