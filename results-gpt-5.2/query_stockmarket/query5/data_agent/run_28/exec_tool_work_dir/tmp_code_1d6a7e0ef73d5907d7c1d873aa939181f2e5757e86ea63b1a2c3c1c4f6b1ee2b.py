code = """import json, pandas as pd

with open(var_call_vtBADGPBhuCPaqDbRa2Ulwlx,'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)
with open(var_call_W26OTZUyMvjJFX3mWC7QSjG3,'r') as f:
    tbls = json.load(f)
tbls_set = set([r['table_name'] for r in tbls])
syms = info_df[info_df['Symbol'].isin(tbls_set)]['Symbol'].tolist()

parts=[]
for s in syms:
    tbl = s.replace('"','""')
    lit = s.replace("'","''")
    q = "SELECT '{lit}' AS Symbol, COUNT(*) AS days FROM \"{tbl}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low > 0 AND (High - Low)/Low > 0.2".format(lit=lit, tbl=tbl)
    parts.append(q)

union_query = " UNION ALL ".join(parts)
final_query = "SELECT Symbol, days FROM (" + union_query + ") x ORDER BY days DESC, Symbol ASC LIMIT 5"

print('__RESULT__:')
print(json.dumps({'query_preview': final_query[:500], 'len': len(final_query)}))"""

env_args = {'var_call_vtBADGPBhuCPaqDbRa2Ulwlx': 'file_storage/call_vtBADGPBhuCPaqDbRa2Ulwlx.json', 'var_call_YlueU3v832DyoXFN3JazX9wk': 'file_storage/call_YlueU3v832DyoXFN3JazX9wk.json', 'var_call_sUkwfNUSJ8It516qnAZdJJdV': [{'table_name': 'AAAU'}], 'var_call_W26OTZUyMvjJFX3mWC7QSjG3': 'file_storage/call_W26OTZUyMvjJFX3mWC7QSjG3.json', 'var_call_iBId8oF3sytNiRbSpexg7vWA': {'symbols_count': 86}, 'var_call_TdpT5fq3kN6ptmIVGmXhLZ6x': {'ok': True}}

exec(code, env_args)
