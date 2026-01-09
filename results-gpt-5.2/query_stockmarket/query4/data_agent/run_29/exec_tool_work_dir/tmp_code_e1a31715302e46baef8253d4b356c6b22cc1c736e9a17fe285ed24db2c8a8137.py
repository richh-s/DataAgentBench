code = """import json, pandas as pd

# load nyse symbols from file
with open(var_call_FkIcp45dYkD0AfIXWtu9qwon,'r') as f:
    syms = json.load(f)
df_syms = pd.DataFrame(syms)
nyse_symbols = set(df_syms['Symbol'].astype(str))

# load trade tables
with open(var_call_095dKGkyaTg3X8vySvAxz7Nb,'r') as f:
    tabs = json.load(f)
df_tabs = pd.DataFrame(tabs)
trade_tables = set(df_tabs['table_name'].astype(str))

symbols = sorted(nyse_symbols & trade_tables)

# build one safe query for all symbols present in trade_tables
parts=[]
for s in symbols:
    tbl='"'+s.replace('"','""')+'"'
    parts.append(f"SELECT '{s}' AS Symbol, SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close<Open THEN 1 ELSE 0 END) AS down_days FROM {tbl} WHERE Date>='2017-01-01' AND Date<='2017-12-31'")
union_all=" UNION ALL ".join(parts)
q="SELECT * FROM ("+union_all+")"
print('__RESULT__:')
print(json.dumps({'query': q, 'n_symbols': len(symbols)}))"""

env_args = {'var_call_FkIcp45dYkD0AfIXWtu9qwon': 'file_storage/call_FkIcp45dYkD0AfIXWtu9qwon.json', 'var_call_095dKGkyaTg3X8vySvAxz7Nb': 'file_storage/call_095dKGkyaTg3X8vySvAxz7Nb.json', 'var_call_BEq2wofHUpx6ZZbJafCsuNRH': 'file_storage/call_BEq2wofHUpx6ZZbJafCsuNRH.json', 'var_call_vUX3Kfpl0jiRLjS0qwWhXx5G': {'n_queries': 2}}

exec(code, env_args)
