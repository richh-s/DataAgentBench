code = """import json

funding_result = locals()['var_functions.query_db:32']
civic_result = locals()['var_functions.query_db:6']

print('Total funding records:', len(funding_result))
print('Total civic documents:', len(civic_result))
print('First civic doc keys:', list(civic_result[0].keys()))
print('Sample civic doc text (first 1000 chars):')
print(civic_result[0]['text'][:1000])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
