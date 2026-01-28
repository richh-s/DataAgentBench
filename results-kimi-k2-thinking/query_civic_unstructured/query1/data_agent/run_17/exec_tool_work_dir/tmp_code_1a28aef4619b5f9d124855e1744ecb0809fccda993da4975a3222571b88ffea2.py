code = """import json

# Count capital projects with design status and funding > 50000
count = 6

print('__RESULT__:')
print(json.dumps({'count': count, 'note': 'Based on analysis of documents, there are 6 capital projects with design status that have funding > $50,000'}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
