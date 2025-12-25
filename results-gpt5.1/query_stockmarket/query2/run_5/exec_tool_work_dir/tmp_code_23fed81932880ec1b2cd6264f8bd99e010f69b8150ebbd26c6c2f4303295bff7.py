code = """import json, pandas as pd
from datetime import datetime

# load NYSE Arca ETF symbols
path = var_call_zEgXiLp0cida1f7Sn6muzwtw
with open(path, 'r') as f:
    etfs = json.load(f)
syms = [r['Symbol'] for r in etfs]

# we will build a SQL query that unions over all relevant symbol tables
# condition: any day in 2015 with Adj Close > 200
clauses = []
for s in syms:
    # table might not exist in stocktrade_database, will handle later
    clauses.append(f"SELECT '{s}' AS Symbol FROM '{s}' WHERE strftime('%Y', Date) = '2015' AND ""Adj Close"" > 200")

union_sql = " UNION SELECT DISTINCT Symbol FROM ("  # placeholder, we'll actually build full SQL in next step

result = {
  'symbols': syms[:20],
  'n_etfs_arca': len(syms),
  'note': 'Next step: query DuckDB with UNION over these tables.'
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_zEgXiLp0cida1f7Sn6muzwtw': 'file_storage/call_zEgXiLp0cida1f7Sn6muzwtw.json', 'var_call_2HaBLtJ0cx1yqeUOibjKUzka': 'file_storage/call_2HaBLtJ0cx1yqeUOibjKUzka.json'}

exec(code, env_args)
