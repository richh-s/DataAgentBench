code = """import json, pandas as pd

with open(var_call_vtBADGPBhuCPaqDbRa2Ulwlx,'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)
with open(var_call_W26OTZUyMvjJFX3mWC7QSjG3,'r') as f:
    tbls = json.load(f)
tbls_set = set([r['table_name'] for r in tbls])

syms = info_df[info_df['Symbol'].isin(tbls_set)]['Symbol'].tolist()

# chunk symbols into groups of 20
chunks = [syms[i:i+20] for i in range(0, len(syms), 20)]
queries = []
for ch in chunks:
    parts=[]
    for s in ch:
        tbl = s.replace('"','""')
        parts.append("SELECT '{s}' AS Symbol, COUNT(*) AS days FROM \"{tbl}\" WHERE Date >= '2019-01-01' AND Date < '2020-01-01' AND Low > 0 AND (High - Low)/Low > 0.2".format(s=s.replace("'","''"), tbl=tbl))
    q = "SELECT Symbol, days FROM (" + " UNION ALL ".join(parts) + ") x"
    queries.append(q)

print('__RESULT__:')
print(json.dumps({'n_symbols': len(syms), 'n_chunks': len(chunks), 'queries': queries}))"""

env_args = {'var_call_vtBADGPBhuCPaqDbRa2Ulwlx': 'file_storage/call_vtBADGPBhuCPaqDbRa2Ulwlx.json', 'var_call_YlueU3v832DyoXFN3JazX9wk': 'file_storage/call_YlueU3v832DyoXFN3JazX9wk.json', 'var_call_sUkwfNUSJ8It516qnAZdJJdV': [{'table_name': 'AAAU'}], 'var_call_W26OTZUyMvjJFX3mWC7QSjG3': 'file_storage/call_W26OTZUyMvjJFX3mWC7QSjG3.json', 'var_call_iBId8oF3sytNiRbSpexg7vWA': {'symbols_count': 86}, 'var_call_TdpT5fq3kN6ptmIVGmXhLZ6x': {'ok': True}, 'var_call_SWQ0mIWir1nFvOw7BVlCK75a': [{'Symbol': 'APEX', 'days': '15'}, {'Symbol': 'AGMH', 'days': '13'}]}

exec(code, env_args)
