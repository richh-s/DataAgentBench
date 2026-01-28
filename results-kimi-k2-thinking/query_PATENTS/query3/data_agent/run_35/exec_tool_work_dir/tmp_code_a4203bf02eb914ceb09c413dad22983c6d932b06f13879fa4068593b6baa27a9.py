code = """import json

data = var_functions.query_db:2

print('Records:', len(data))

# First record info
if data:
    rec = data[0]
    print('\nKeys:', list(rec.keys()))
    print('\nPatents_info:', rec['Patents_info'])
    print('\nFirst 100 chars of citation:', rec['citation'][:100] if rec['citation'] else 'None')
    print('\nFirst 100 chars of cpc:', rec['cpc'][:100] if rec['cpc'] else 'None')
    
print('\n__RESULT__:')
print('len=%d' % len(data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
