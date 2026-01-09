code = """import json, pandas as pd

# Load NYSE non-ETF symbols with company names
path_info = var_call_xuUBpv3sy51zl3phgaF7zb0y
with open(path_info, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

# Load available trade tables (symbols)
path_tables = var_call_XVn8eaOQR3oF28TjAK0kSeBn
with open(path_tables, 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

# Intersect to those we can query
candidates = info_df[info_df['symbol'].isin(tables_set)].copy()

# Escape table names for DuckDB (double quotes); also filter out symbols with illegal chars just in case
# We'll keep those that are alnum or contain '.' or '-' maybe; but duckdb quoted identifiers can handle many.
# We'll just quote and double any embedded quotes.

def dq_ident(s: str) -> str:
    return '"' + s.replace('"','""') + '"'

# Build a UNION ALL query in chunks to count up/down days in 2017 for each symbol
symbols = candidates['symbol'].tolist()

chunks = []
chunk_size = 120  # keep query size manageable
for i in range(0, len(symbols), chunk_size):
    sym_chunk = symbols[i:i+chunk_size]
    selects = []
    for sym in sym_chunk:
        t = dq_ident(sym)
        selects.append(
            f"SELECT '{sym}' AS symbol, "
            f"SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) AS up_days, "
            f"SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) AS down_days "
            f"FROM {t} WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
        )
    chunks.append(' UNION ALL '.join(selects))

result_frames = []
# Execute each chunk via query_db
from datetime import datetime

# We'll print instructions for tool usage by returning list of queries to run
queries = chunks

print('__RESULT__:')
print(json.dumps({'num_candidates': len(symbols), 'num_chunks': len(queries), 'queries': queries[:5], 'remaining_queries': len(queries)-5}))"""

env_args = {'var_call_xuUBpv3sy51zl3phgaF7zb0y': 'file_storage/call_xuUBpv3sy51zl3phgaF7zb0y.json', 'var_call_XVn8eaOQR3oF28TjAK0kSeBn': 'file_storage/call_XVn8eaOQR3oF28TjAK0kSeBn.json'}

exec(code, env_args)
