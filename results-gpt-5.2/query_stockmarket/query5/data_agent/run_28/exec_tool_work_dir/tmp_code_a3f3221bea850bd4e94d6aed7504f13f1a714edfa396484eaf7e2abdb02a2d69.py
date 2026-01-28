code = """import json, pandas as pd

p_info = var_call_vtBADGPBhuCPaqDbRa2Ulwlx
with open(p_info, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

p_tbls = var_call_YlueU3v832DyoXFN3JazX9wk
with open(p_tbls, 'r') as f:
    tbls = json.load(f)
tbls_set = set(tbls)

info_df = info_df[info_df['Symbol'].isin(tbls_set)].copy()
syms = info_df['Symbol'].tolist()

parts = []
for s in syms:
    parts.append("SELECT '{sym}' AS Symbol, COUNT(*) AS cnt FROM \"{sym}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low > 0 AND (High - Low) / Low > 0.2".format(sym=s.replace("'","''")))

if not parts:
    print('__RESULT__:')
    print(json.dumps({'final_query': None, 'symbols_count': 0}))
else:
    union_query = "\nUNION ALL\n".join(parts)
    final_query = "SELECT Symbol, cnt FROM (\n{u}\n) t ORDER BY cnt DESC, Symbol ASC LIMIT 5".format(u=union_query)
    print('__RESULT__:')
    print(json.dumps({'final_query': final_query, 'symbols_count': len(syms)}))"""

env_args = {'var_call_vtBADGPBhuCPaqDbRa2Ulwlx': 'file_storage/call_vtBADGPBhuCPaqDbRa2Ulwlx.json', 'var_call_YlueU3v832DyoXFN3JazX9wk': 'file_storage/call_YlueU3v832DyoXFN3JazX9wk.json'}

exec(code, env_args)
