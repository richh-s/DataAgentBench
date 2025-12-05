code = """import json, os

# load Arca ETF symbols
path = var_call_zEgXiLp0cida1f7Sn6muzwtw
with open(path, 'r') as f:
    etfs = json.load(f)
syms = [r['Symbol'] for r in etfs]

# build DuckDB SQL: some tables may not exist; but list_db showed stocktrade_database has many of them.
# We'll generate a UNION ALL of EXISTS-filtered selects using DuckDB's information_schema.tables

selects = []
for s in syms:
    # each subquery checks if table exists before querying using EXECUTE IMMEDIATE pattern is not available; instead we'll rely on the fact that
    # the provided stocktrade_database should have tables only for tickers present; from list_db preview many ARCA ETFs appear.
    selects.append(f"SELECT '{s}' AS Symbol FROM '{s}' WHERE strftime('%Y', Date) = '2015' AND \"Adj Close\" > 200")

if selects:
    union_query = " UNION ALL ".join(selects)
else:
    union_query = "SELECT NULL AS Symbol WHERE 0"  # empty

out = json.dumps({'duckdb_query': f"SELECT DISTINCT Symbol FROM ({union_query});"})
print("__RESULT__:")
print(out)"""

env_args = {'var_call_zEgXiLp0cida1f7Sn6muzwtw': 'file_storage/call_zEgXiLp0cida1f7Sn6muzwtw.json', 'var_call_2HaBLtJ0cx1yqeUOibjKUzka': 'file_storage/call_2HaBLtJ0cx1yqeUOibjKUzka.json', 'var_call_wZB844YkYNjs4Y4kqWO7UCyh': {'symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'n_etfs_arca': 1435, 'note': 'Next step: query DuckDB with UNION over these tables.'}}

exec(code, env_args)
