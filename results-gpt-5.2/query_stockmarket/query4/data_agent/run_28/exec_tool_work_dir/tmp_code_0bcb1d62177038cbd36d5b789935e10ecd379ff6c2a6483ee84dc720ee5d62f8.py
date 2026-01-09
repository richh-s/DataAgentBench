code = """import json, pandas as pd

# load info
v = var_call_8Rmh6nq21wxXn4UkriQTxNnE
if isinstance(v,str):
    info=json.load(open(v))
else:
    info=v
info_df=pd.DataFrame(info)

# load trade tables
v2=var_call_53fSB6wCGArWqzaRLsIKLcr4
if isinstance(v2,str):
    tables=json.load(open(v2))
else:
    tables=v2
trade_set=set(tables)

# intersect and ensure exact existence
symbols=sorted(set(info_df.Symbol).intersection(trade_set))

# regenerate SQLs with these symbols
parts=[]
for sym in symbols:
    tbl='"'+sym.replace('"','""')+'"'
    parts.append(f"SELECT '{sym}' AS Symbol, SUM(CASE WHEN Close>Open THEN 1 ELSE 0 END) AS up_days, SUM(CASE WHEN Close<Open THEN 1 ELSE 0 END) AS down_days FROM {tbl} WHERE Date >= '2017-01-01' AND Date < '2018-01-01'")
max_parts=100
sqls=[]
for i in range(0,len(parts),max_parts):
    sqls.append("SELECT * FROM ("+" UNION ALL ".join(parts[i:i+max_parts])+")")

print('__RESULT__:')
print(json.dumps({'sqls': sqls, 'n_sqls': len(sqls), 'n_symbols': len(symbols), 'head_syms': symbols[:20], 'tail_syms': symbols[-20:]}))"""

env_args = {'var_call_8Rmh6nq21wxXn4UkriQTxNnE': 'file_storage/call_8Rmh6nq21wxXn4UkriQTxNnE.json', 'var_call_53fSB6wCGArWqzaRLsIKLcr4': 'file_storage/call_53fSB6wCGArWqzaRLsIKLcr4.json', 'var_call_fgUZlAnSreN5Yh3kqwKzCzRT': 'file_storage/call_fgUZlAnSreN5Yh3kqwKzCzRT.json', 'var_call_7UpfW7yFAS8XXLPO6POIvZU0': {'n_sqls': 2, 'n_symbols': 234}}

exec(code, env_args)
