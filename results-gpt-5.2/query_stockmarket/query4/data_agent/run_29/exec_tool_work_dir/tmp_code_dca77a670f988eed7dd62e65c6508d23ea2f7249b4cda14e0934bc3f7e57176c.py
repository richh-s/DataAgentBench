code = """import json, pandas as pd

# load nyse symbols and trade tables
with open(var_call_FkIcp45dYkD0AfIXWtu9qwon,'r') as f:
    df_syms=pd.DataFrame(json.load(f))
with open(var_call_095dKGkyaTg3X8vySvAxz7Nb,'r') as f:
    df_tabs=pd.DataFrame(json.load(f))

nyse=set(df_syms['Symbol'].astype(str))
tables=set(df_tabs['table_name'].astype(str))

# DuckDB has tables with special chars (#, etc). We will restrict to exact intersection and also
# exclude known mismatches where stockinfo symbol doesn't exist as table due to e.g. suffix differences.
# But since we used intersection, mismatch like DCI shouldn't happen; implies DCI is in nyse but not in tables.
# So remove symbols not in tables (recompute carefully)
syms=sorted([s for s in nyse if s in tables])

# sanity check for DCI
has_dci = 'DCI' in syms

# build chunked queries
parts=[]
for s in syms:
    tbl='"'+s.replace('"','""')+'"'
    parts.append(f"SELECT '{s}' AS Symbol, SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close<Open THEN 1 ELSE 0 END) AS down_days FROM {tbl} WHERE Date>='2017-01-01' AND Date<='2017-12-31'")

chunk_size=150
queries=[]
for i in range(0,len(parts),chunk_size):
    queries.append('SELECT * FROM ('+' UNION ALL '.join(parts[i:i+chunk_size])+')')

print('__RESULT__:')
print(json.dumps({'n_symbols': len(syms), 'has_dci': has_dci, 'n_queries': len(queries), 'queries': queries[:3]}))"""

env_args = {'var_call_FkIcp45dYkD0AfIXWtu9qwon': 'file_storage/call_FkIcp45dYkD0AfIXWtu9qwon.json', 'var_call_095dKGkyaTg3X8vySvAxz7Nb': 'file_storage/call_095dKGkyaTg3X8vySvAxz7Nb.json', 'var_call_BEq2wofHUpx6ZZbJafCsuNRH': 'file_storage/call_BEq2wofHUpx6ZZbJafCsuNRH.json', 'var_call_vUX3Kfpl0jiRLjS0qwWhXx5G': {'n_queries': 2}, 'var_call_1USJEtgC4VH3JVFMTcUY2WTc': 'file_storage/call_1USJEtgC4VH3JVFMTcUY2WTc.json'}

exec(code, env_args)
