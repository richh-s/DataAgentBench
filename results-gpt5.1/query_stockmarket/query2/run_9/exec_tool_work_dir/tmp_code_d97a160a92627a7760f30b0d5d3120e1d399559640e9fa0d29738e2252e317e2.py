code = """import json, pandas as pd
from pathlib import Path

# Load ETF symbols listed on NYSE Arca
file_path = Path(var_call_Plp7MpcdgcGsnYwJNvvVxhVz)
with open(file_path, 'r') as f:
    etf_records = json.load(f)

etf_symbols = [r['Symbol'] for r in etf_records]

# Build DuckDB SQL to union over all relevant symbol tables and filter 2015 & Adj Close > 200
# Need to ensure symbols exist as tables in stocktrade_database; use provided table list
trade_tables_path = Path(var_call_0THu8ncTdHTfqwy12BviJ5Iq)
with open(trade_tables_path, 'r') as f:
    trade_tables = json.load(f)

trade_set = set(trade_tables)

symbols = [s for s in etf_symbols if s in trade_set]

# Construct a UNION ALL query over all matching symbol tables
parts = []
for s in symbols:
    parts.append(f"SELECT '{s}' AS Symbol, Date, ""Adj Close"" FROM '{s}' WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND ""Adj Close"" > 200")

if parts:
    union_query = " UNION ALL ".join(parts)
else:
    union_query = None

result = {
    'symbols': symbols,
    'union_query': union_query[:10000] if union_query else None
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Plp7MpcdgcGsnYwJNvvVxhVz': 'file_storage/call_Plp7MpcdgcGsnYwJNvvVxhVz.json', 'var_call_0THu8ncTdHTfqwy12BviJ5Iq': 'file_storage/call_0THu8ncTdHTfqwy12BviJ5Iq.json'}

exec(code, env_args)
