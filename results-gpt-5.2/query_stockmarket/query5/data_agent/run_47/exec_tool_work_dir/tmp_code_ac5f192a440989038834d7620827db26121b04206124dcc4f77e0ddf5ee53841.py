code = """import json, pandas as pd

# load symbols list
path = var_call_TQ2qbdhno8m08VxqXsNvkb8Z
with open(path, 'r') as f:
    recs = json.load(f)

symbols = [r['Symbol'] for r in recs]
companies = {r['Symbol']: r['company_name'] for r in recs}

# build a duckdb UNION ALL query over existing tables
# Use information_schema to keep only symbols with a corresponding table
import duckdb

con = duckdb.connect(database=':memory:')
# can't access external db here; just construct query text for query_db tool

# produce SQL to fetch existing tables from duckdb info_schema, then dynamically union
# We'll do this in two steps with query_db: (1) list tables; (2) compute counts in python with smaller per-table queries if needed.

out = json.dumps({'symbols': symbols, 'n_symbols': len(symbols), 'companies_sample': list(companies.items())[:3]})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_TQ2qbdhno8m08VxqXsNvkb8Z': 'file_storage/call_TQ2qbdhno8m08VxqXsNvkb8Z.json'}

exec(code, env_args)
