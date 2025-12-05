code = """import json, pandas as pd
from pathlib import Path

# Load full ETF symbol list from file
with open(var_call_YXTpAScbwNX1UU9QYEi2dZPW, 'r') as f:
    etf_records = json.load(f)

etf_symbols = sorted({r['Symbol'] for r in etf_records})

# Filter to symbols that exist as tables in stocktrade_database
with open(var_call_qShfDQVYTAaQBPYx8iDZijPA, 'r') as f:
    all_tables = set(json.load(f))

symbols = sorted(list(set(etf_symbols) & all_tables))

# Build query to check Adj Close > 200 in 2015 for these symbols
# We'll generate a DuckDB query that UNION ALLs per-symbol selects with a symbol column

selects = []
for sym in symbols:
    s_escaped = sym.replace('"', '""')
    selects.append(f"SELECT '{s_escaped}' AS Symbol FROM '{s_escaped}' WHERE strftime('%Y', Date) = '2015' AND ""Adj Close"" > 200")

if selects:
    union_query = " UNION ALL ".join(selects)
else:
    union_query = "SELECT '' as Symbol WHERE 0"  # no symbols fallback

result = {
  'query': union_query,
  'count_symbols': len(symbols)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_YXTpAScbwNX1UU9QYEi2dZPW': 'file_storage/call_YXTpAScbwNX1UU9QYEi2dZPW.json', 'var_call_qShfDQVYTAaQBPYx8iDZijPA': 'file_storage/call_qShfDQVYTAaQBPYx8iDZijPA.json'}

exec(code, env_args)
