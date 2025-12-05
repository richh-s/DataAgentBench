code = """import json, pandas as pd

# Load ETF symbols from file
with open(var_call_YVeiesweakL4gLNDAkh36spj, 'r') as f:
    etf_records = json.load(f)

etf_symbols = [r['Symbol'] for r in etf_records]

# We'll build a DuckDB SQL query that unions over all relevant symbol tables
# for 2015 where Adj Close > 200, but only for tables that actually exist.
with open(var_call_nYzeZrOYXfV9jxKrzR6AGoga, 'r') as f:
    all_trade_tables = json.load(f)

existing = sorted(set(etf_symbols).intersection(all_trade_tables))

# Construct a SQL that unions max Adj Close per symbol over 2015
union_parts = []
for sym in existing:
    # DuckDB identifier quoting with double quotes
    part = f"SELECT '{sym}' AS Symbol, MAX(""Adj Close"") AS max_adj_close FROM \"{sym}\" WHERE Date >= '2015-01-01' AND Date <= '2015-12-31'"
    union_parts.append(part)

if union_parts:
    full_sql = " UNION ALL ".join(union_parts)
else:
    full_sql = "SELECT NULL AS Symbol, NULL AS max_adj_close WHERE 1=0"

result = {'sql': full_sql, 'symbols_considered': len(existing)}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YVeiesweakL4gLNDAkh36spj': 'file_storage/call_YVeiesweakL4gLNDAkh36spj.json', 'var_call_nYzeZrOYXfV9jxKrzR6AGoga': 'file_storage/call_nYzeZrOYXfV9jxKrzR6AGoga.json'}

exec(code, env_args)
