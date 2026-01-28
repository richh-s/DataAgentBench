code = """import json, re

civic_docs = json.load(open('tmptjtu3_1d.json', 'r'))
funding = json.load(open('tmpw8a01a0z.json', 'r'))

print('Loaded data files')
print('Civic docs:', len(civic_docs))
print('Funding records:', len(funding))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['civic_docs'], 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
