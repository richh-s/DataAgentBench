code = """import json, pandas as pd

# Load full ETF symbol list from file
path = var_call_x8XqfuEaEJmdvwgwcztUv5Ci
with open(path, 'r') as f:
    etf_records = json.load(f)

etf_symbols = [r['Symbol'] for r in etf_records]

# Build DuckDB SQL to union all relevant tables and filter by 2015 and Adj Close > 200
# Use DuckDB's read_parquet-like syntax is not needed; tables are already there. We'll generate a UNION ALL query.

conditions = []
for sym in etf_symbols:
    # table names in DuckDB appear exactly as tickers
    conditions.append(f"SELECT '{sym}' AS Symbol, Date, ""Adj Close"" FROM \"{sym}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31' AND ""Adj Close"" > 200")

union_sql = " UNION ALL ".join(conditions)

# Wrap as outer query to get distinct symbols
final_sql = f"SELECT DISTINCT Symbol FROM ({union_sql});"

result = {
    'sql': final_sql[:10000],
    'symbols_sample': etf_symbols[:10],
    'count_etfs_arca': len(etf_symbols)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_x8XqfuEaEJmdvwgwcztUv5Ci': 'file_storage/call_x8XqfuEaEJmdvwgwcztUv5Ci.json', 'var_call_zVJj06zwVA1qHoJ9cWWadphu': 'file_storage/call_zVJj06zwVA1qHoJ9cWWadphu.json'}

exec(code, env_args)
