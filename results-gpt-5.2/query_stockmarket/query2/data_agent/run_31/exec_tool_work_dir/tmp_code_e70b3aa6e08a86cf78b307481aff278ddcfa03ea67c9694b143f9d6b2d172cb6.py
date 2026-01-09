code = """import json, pandas as pd

arca_path = var_call_SfzowiPGo9Cwx7lWlMWFey8F
with open(arca_path, 'r') as f:
    arca = json.load(f)
df_arca = pd.DataFrame(arca)

lst_path = var_call_Fr7BmlftWmKTW4WkvlHqFvSv
with open(lst_path, 'r') as f:
    tables = json.load(f)
set_tables = set(tables)

df_arca = df_arca[df_arca['symbol'].isin(set_tables)].copy()
syms = sorted(df_arca['symbol'].unique().tolist())

parts = []
for s in syms:
    q = "SELECT '{sym}' AS symbol, MAX(\"Adj Close\") AS max_adj_close_2015 FROM \"{sym}\" WHERE \"Date\" >= '2015-01-01' AND \"Date\" <= '2015-12-31'".format(sym=s)
    parts.append(q)

union_query = " UNION ALL ".join(parts)

out = json.dumps({'n_symbols_with_tables': int(len(syms)), 'union_query': union_query})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_SfzowiPGo9Cwx7lWlMWFey8F': 'file_storage/call_SfzowiPGo9Cwx7lWlMWFey8F.json', 'var_call_Fr7BmlftWmKTW4WkvlHqFvSv': 'file_storage/call_Fr7BmlftWmKTW4WkvlHqFvSv.json'}

exec(code, env_args)
