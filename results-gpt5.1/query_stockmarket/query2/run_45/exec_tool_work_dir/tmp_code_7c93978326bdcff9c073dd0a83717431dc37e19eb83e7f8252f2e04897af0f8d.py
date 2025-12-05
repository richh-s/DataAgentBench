code = """import json, pandas as pd
from pathlib import Path

# Load full ETF symbol list from file
file_path = var_call_Q7oxVNcem3P3gl49PplPDVLm
etf_symbols = pd.read_json(file_path)

tickers = etf_symbols['Symbol'].tolist()

# Build DuckDB SQL to scan all relevant symbol tables and find those exceeding $200 in 2015
# We will construct a UNION ALL of per-table queries, then select distinct symbol names

parts = []
for sym in tickers:
    # DuckDB identifiers: wrap in double quotes; escape existing quotes if any
    ident = '"' + sym.replace('"', '""') + '"'
    part = f"SELECT '{sym}' AS Symbol FROM {ident} WHERE strptime(Date, '%Y-%m-%d') BETWEEN DATE '2015-01-01' AND DATE '2015-12-31' AND \"Adj Close\" > 200"
    parts.append(part)

if parts:
    union_sql = " UNION ALL ".join(parts)
else:
    union_sql = "SELECT '' AS Symbol WHERE 1=0"

result = {'sql': union_sql[:65000]}  # ensure not oversized

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Q7oxVNcem3P3gl49PplPDVLm': 'file_storage/call_Q7oxVNcem3P3gl49PplPDVLm.json', 'var_call_OueCLQnQmAlTVjfjIkoDVw68': 'file_storage/call_OueCLQnQmAlTVjfjIkoDVw68.json'}

exec(code, env_args)
