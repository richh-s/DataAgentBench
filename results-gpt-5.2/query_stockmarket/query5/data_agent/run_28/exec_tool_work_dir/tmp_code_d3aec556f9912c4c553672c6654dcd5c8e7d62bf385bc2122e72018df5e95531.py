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
    sym_sql = s.replace("\"", "\"\"")
    sym_lit = s.replace("'", "''")
    q = "SELECT '{lit}' AS Symbol, COUNT(*) AS cnt FROM \"{tbl}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low > 0 AND (High - Low) / Low > 0.2".format(lit=sym_lit, tbl=sym_sql)
    parts.append(q)

if not parts:
    payload = {'final_query': None, 'symbols_count': 0}
else:
    union_query = " UNION ALL ".join(parts)
    final_query = "SELECT Symbol, cnt FROM (" + union_query + ") t GROUP BY Symbol, cnt ORDER BY cnt DESC, Symbol ASC LIMIT 5"
    payload = {'final_query': final_query, 'symbols_count': len(syms)}

print('__RESULT__:')
print(json.dumps(payload))"""

env_args = {'var_call_vtBADGPBhuCPaqDbRa2Ulwlx': 'file_storage/call_vtBADGPBhuCPaqDbRa2Ulwlx.json', 'var_call_YlueU3v832DyoXFN3JazX9wk': 'file_storage/call_YlueU3v832DyoXFN3JazX9wk.json'}

exec(code, env_args)
