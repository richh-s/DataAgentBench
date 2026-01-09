code = """import json, pandas as pd

# Load NYSE non-ETF symbols and names
nyse = var_call_OnB6fCK9Z9sc0oRJT1v3w7fS
if isinstance(nyse, str):
    with open(nyse, 'r') as f:
        nyse = json.load(f)
nyse_df = pd.DataFrame(nyse)
nyse_symbols = set(nyse_df['Symbol'].astype(str))

# Load available trade tables
tables = var_call_MW2L0mKITaFAwthgkJuiG1GZ
if isinstance(tables, str):
    with open(tables, 'r') as f:
        tables = json.load(f)

db_tables = set(tables)
use_symbols = sorted(nyse_symbols.intersection(db_tables))

# Chunk symbols for SQL UNION ALL queries
chunks = [use_symbols[i:i+80] for i in range(0, len(use_symbols), 80)]

queries = []
for ch in chunks:
    parts = []
    for sym in ch:
        # Quote table name for DuckDB
        parts.append(f"SELECT '{sym}' AS Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days FROM \"{sym}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'")
    q = " UNION ALL ".join(parts)
    queries.append(q)

# Output the list of chunk queries for subsequent query_db calls
out = json.dumps({"n_symbols": len(use_symbols), "n_chunks": len(queries), "queries": queries[:10], "all_queries_path_needed": len(queries) > 10})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_KX5UnkAb3MmDwt33HLN1ZTMv': ['stockinfo'], 'var_call_OnB6fCK9Z9sc0oRJT1v3w7fS': 'file_storage/call_OnB6fCK9Z9sc0oRJT1v3w7fS.json', 'var_call_MW2L0mKITaFAwthgkJuiG1GZ': 'file_storage/call_MW2L0mKITaFAwthgkJuiG1GZ.json'}

exec(code, env_args)
