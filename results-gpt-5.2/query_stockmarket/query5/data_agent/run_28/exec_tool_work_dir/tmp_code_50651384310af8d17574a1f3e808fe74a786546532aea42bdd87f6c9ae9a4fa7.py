code = """import json, pandas as pd

with open(var_call_vtBADGPBhuCPaqDbRa2Ulwlx, 'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

with open(var_call_YlueU3v832DyoXFN3JazX9wk, 'r') as f:
    tbls = json.load(f)
tbls_set = set(tbls)

syms = info_df[info_df['Symbol'].isin(tbls_set)]['Symbol'].tolist()

parts = []
for s in syms:
    tbl = s.replace('"','""')
    lit = s.replace("'","''")
    q = "SELECT '{lit}' AS Symbol, COUNT(*) AS cnt FROM \"{tbl}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low > 0 AND (High - Low) / Low > 0.2".format(lit=lit, tbl=tbl)
    parts.append(q)

final_query = None
if parts:
    union_query = " UNION ALL ".join(parts)
    final_query = "SELECT Symbol, cnt FROM (" + union_query + ") t ORDER BY cnt DESC, Symbol ASC LIMIT 5"

print('__RESULT__:')
print(json.dumps({'final_query': final_query, 'symbols_count': len(syms)}))"""

env_args = {'var_call_vtBADGPBhuCPaqDbRa2Ulwlx': 'file_storage/call_vtBADGPBhuCPaqDbRa2Ulwlx.json', 'var_call_YlueU3v832DyoXFN3JazX9wk': 'file_storage/call_YlueU3v832DyoXFN3JazX9wk.json'}

exec(code, env_args)
