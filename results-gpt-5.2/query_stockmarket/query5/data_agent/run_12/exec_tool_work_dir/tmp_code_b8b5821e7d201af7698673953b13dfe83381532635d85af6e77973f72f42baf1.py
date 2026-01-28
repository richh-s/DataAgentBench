code = """import json, pandas as pd

# load capital market symbols
cap_path = var_call_0cRCwuXzy0ygPKXxZNGk722D
with open(cap_path, 'r') as f:
    cap = json.load(f)
df_cap = pd.DataFrame(cap)
cap_syms = set(df_cap['Symbol'].astype(str))

# load available trade tables
tbl_path = var_call_QmgXm74iO39N022IImWIvqGm
with open(tbl_path, 'r') as f:
    tables = json.load(f)
avail = set(tables)

syms = sorted(cap_syms & avail)

# build a UNION ALL query across all relevant ticker tables restricted to 2019
parts = []
for s in syms:
    # duckdb table names may need quoting if special chars; use double quotes universally
    parts.append(
        f"SELECT '{s}' AS Symbol, COUNT(*) AS days FROM \"{s}\" "
        "WHERE Date >= '2019-01-01' AND Date < '2020-01-01' "
        "AND Low IS NOT NULL AND High IS NOT NULL AND Low > 0 "
        "AND (High - Low) / Low > 0.2"
    )

query = "SELECT Symbol, days FROM (\n" + "\nUNION ALL\n".join(parts) + "\n) ORDER BY days DESC, Symbol ASC LIMIT 5;"

print('__RESULT__:')
print(json.dumps({'query': query, 'n_syms': len(syms)}))"""

env_args = {'var_call_0cRCwuXzy0ygPKXxZNGk722D': 'file_storage/call_0cRCwuXzy0ygPKXxZNGk722D.json', 'var_call_QmgXm74iO39N022IImWIvqGm': 'file_storage/call_QmgXm74iO39N022IImWIvqGm.json'}

exec(code, env_args)
