code = """import json, pandas as pd

# load tickers list from file if needed
src = var_call_5NexJwt9r8tmm7M3boorcoK4
if isinstance(src, str):
    with open(src, 'r') as f:
        recs = json.load(f)
else:
    recs = src

symbols = sorted({r['Symbol'] for r in recs if r.get('Symbol')})
company = {r['Symbol']: r.get('company_name') for r in recs}

# Build a UNION ALL query across all ticker tables that exist in stocktrade_database.
# We don't know which tables exist; ask duckdb catalog via information_schema.

# We'll emit result with symbols+company as JSON so next step can query existing tables and compute.
out = json.dumps({'symbols': symbols, 'company': company})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_5NexJwt9r8tmm7M3boorcoK4': 'file_storage/call_5NexJwt9r8tmm7M3boorcoK4.json'}

exec(code, env_args)
