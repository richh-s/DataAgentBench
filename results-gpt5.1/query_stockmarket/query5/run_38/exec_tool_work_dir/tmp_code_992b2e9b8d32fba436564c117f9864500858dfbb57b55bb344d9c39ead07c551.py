code = """import json, pandas as pd
from datetime import datetime

# load stockinfo result
path = var_call_hiPTs3xYnOFJ9HbswramArc3
with open(path, 'r') as f:
    stockinfo = json.load(f)

symbols = [r['Symbol'] for r in stockinfo]

# We'll build DuckDB SQL to union all per-symbol counts for 2019
parts = []
for sym in symbols:
    parts.append(f"SELECT '{sym}' AS Symbol, SUM(CASE WHEN (CAST(strftime('%Y', Date) AS INT) = 2019 AND (High - Low) / NULLIF(Low,0) > 0.20) THEN 1 ELSE 0 END) AS volatile_days FROM '{sym}'")

union_sql = " UNION ALL ".join(parts)

result_sql = f"SELECT s.Symbol, si.CompanyDescription, s.volatile_days FROM ({union_sql}) s JOIN (SELECT Symbol, \"Company Description\" AS CompanyDescription FROM stockinfo) si ON s.Symbol = si.Symbol WHERE s.volatile_days > 0 ORDER BY s.volatile_days DESC, s.Symbol ASC LIMIT 5;"

print('__RESULT__:')
print(json.dumps(result_sql))"""

env_args = {'var_call_wR8Gn69vnqvkWdb8Z2MLxH3t': 'file_storage/call_wR8Gn69vnqvkWdb8Z2MLxH3t.json', 'var_call_hiPTs3xYnOFJ9HbswramArc3': 'file_storage/call_hiPTs3xYnOFJ9HbswramArc3.json'}

exec(code, env_args)
