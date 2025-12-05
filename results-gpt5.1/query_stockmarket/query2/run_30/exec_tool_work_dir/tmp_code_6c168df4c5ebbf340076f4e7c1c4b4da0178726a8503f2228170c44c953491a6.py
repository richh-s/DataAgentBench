code = """import json, pandas as pd
from pathlib import Path

# Load full ETF symbol list for NYSE Arca
file_path = Path(var_call_0UK33FRa0fPb3IpEfMa4jNje)
with open(file_path, 'r') as f:
    etf_records = json.load(f)

symbols = [r['Symbol'] for r in etf_records]

# Build DuckDB SQL to scan each symbol table for 2015 adj close > 200
# We must only include symbols that exist as tables in stocktrade_database
trade_tables = set(var_call_lnSPpiwugTgF9JgEDk8W8VUl)

valid_symbols = [s for s in symbols if s in trade_tables]

# Construct UNION ALL query
union_queries = []
for s in valid_symbols:
    q = f"SELECT '{s}' AS Symbol FROM '{s}' WHERE strftime('%Y', Date) = '2015' AND ""Adj Close"" > 200 GROUP BY Symbol"
    union_queries.append(q)

if union_queries:
    final_query = " UNION ALL ".join(union_queries)
else:
    final_query = "SELECT '' AS Symbol WHERE 0"  # empty result safeguard

result = {
    'query': final_query,
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_0UK33FRa0fPb3IpEfMa4jNje': 'file_storage/call_0UK33FRa0fPb3IpEfMa4jNje.json', 'var_call_lnSPpiwugTgF9JgEDk8W8VUl': 'file_storage/call_lnSPpiwugTgF9JgEDk8W8VUl.json'}

exec(code, env_args)
