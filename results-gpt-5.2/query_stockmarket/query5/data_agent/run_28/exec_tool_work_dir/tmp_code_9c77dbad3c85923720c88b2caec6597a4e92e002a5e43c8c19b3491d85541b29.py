code = """import json, pandas as pd

with open(var_call_vtBADGPBhuCPaqDbRa2Ulwlx,'r') as f:
    info = json.load(f)
info_df = pd.DataFrame(info)

with open(var_call_W26OTZUyMvjJFX3mWC7QSjG3,'r') as f:
    tbls = json.load(f)
tbls_set = set([r['table_name'] for r in tbls])

target = info_df[info_df['Symbol'].isin(tbls_set)][['Symbol','company_name']].copy()

print('__RESULT__:')
print(json.dumps({'symbols_count': int(len(target))}))"""

env_args = {'var_call_vtBADGPBhuCPaqDbRa2Ulwlx': 'file_storage/call_vtBADGPBhuCPaqDbRa2Ulwlx.json', 'var_call_YlueU3v832DyoXFN3JazX9wk': 'file_storage/call_YlueU3v832DyoXFN3JazX9wk.json', 'var_call_sUkwfNUSJ8It516qnAZdJJdV': [{'table_name': 'AAAU'}], 'var_call_W26OTZUyMvjJFX3mWC7QSjG3': 'file_storage/call_W26OTZUyMvjJFX3mWC7QSjG3.json'}

exec(code, env_args)
