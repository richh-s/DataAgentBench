code = """import json
path = var_call_zEgXiLp0cida1f7Sn6muzwtw
with open(path, 'r') as f:
    etfs = json.load(f)
syms = [r['Symbol'] for r in etfs]
selects = []
for s in syms:
    selects.append("SELECT '" + s + "' AS Symbol FROM '" + s + "' WHERE strftime('%Y', Date) = '2015' AND \"Adj Close\" > 200")
union_query = " UNION ALL ".join(selects) if selects else "SELECT NULL AS Symbol WHERE 0"
query = "SELECT DISTINCT Symbol FROM (" + union_query + ");"
out = json.dumps({'duckdb_query': query})
print("__RESULT__:")
print(out)"""

env_args = {'var_call_zEgXiLp0cida1f7Sn6muzwtw': 'file_storage/call_zEgXiLp0cida1f7Sn6muzwtw.json', 'var_call_2HaBLtJ0cx1yqeUOibjKUzka': 'file_storage/call_2HaBLtJ0cx1yqeUOibjKUzka.json', 'var_call_wZB844YkYNjs4Y4kqWO7UCyh': {'symbols': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA'], 'n_etfs_arca': 1435, 'note': 'Next step: query DuckDB with UNION over these tables.'}}

exec(code, env_args)
