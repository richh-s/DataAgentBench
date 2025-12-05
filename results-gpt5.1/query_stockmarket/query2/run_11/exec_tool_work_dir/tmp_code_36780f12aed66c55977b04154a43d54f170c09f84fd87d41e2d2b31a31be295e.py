code = """import json, pandas as pd
from pathlib import Path

# Load full ETF symbol list from file
file_path = Path(var_call_MVlDabnT6QfaIeGaWhpi3AKg)
rows = json.loads(file_path.read_text())

df = pd.DataFrame(rows)
tickers = df['Symbol'].tolist()

# Build SQL to check each ticker table for 2015 adj close > 200
conditions = []
for t in tickers:
    # DuckDB requires quoting identifiers that are not simple; assume ticker names as given
    conditions.append(f"(SELECT DISTINCT '{t}' AS Symbol FROM '{t}' WHERE strftime('%Y', Date) = '2015' AND \"Adj Close\" > 200)")

union_sql = " UNION ALL ".join(conditions)

result_sql = f"WITH hits AS ({union_sql}) SELECT DISTINCT Symbol FROM hits ORDER BY Symbol;"

print('__RESULT__:')
print(json.dumps(result_sql))"""

env_args = {'var_call_MVlDabnT6QfaIeGaWhpi3AKg': 'file_storage/call_MVlDabnT6QfaIeGaWhpi3AKg.json', 'var_call_P9vUvAqe8ClxpYIkJzs0Kjiw': 'file_storage/call_P9vUvAqe8ClxpYIkJzs0Kjiw.json'}

exec(code, env_args)
