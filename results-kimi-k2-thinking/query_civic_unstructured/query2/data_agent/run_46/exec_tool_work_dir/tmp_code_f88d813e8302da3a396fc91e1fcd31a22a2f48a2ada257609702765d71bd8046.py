code = """import json
import re

# Debug: print types and sample data
print('DEBUG: Type of civic_docs:', type(locals()['var_functions.query_db:8']))
print('DEBUG: Length:', len(locals()['var_functions.query_db:8']))
print('DEBUG: First item type:', type(locals()['var_functions.query_db:8'][0]))

print('DEBUG: Type of funding:', type(locals()['var_functions.query_db:10']))
print('DEBUG: Length:', len(locals()['var_functions.query_db:10']))
print('DEBUG: First item:', locals()['var_functions.query_db:10'][0])

print('__RESULT__:', json.dumps({'debug': 'done'}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.list_db:42': ['civic_docs']}

exec(code, env_args)
