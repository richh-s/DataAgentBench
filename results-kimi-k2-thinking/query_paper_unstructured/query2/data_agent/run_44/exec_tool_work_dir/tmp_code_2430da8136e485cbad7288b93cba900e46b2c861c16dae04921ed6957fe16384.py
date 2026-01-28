code = """import json

# Get citation data
citation_file = locals()['var_functions.query_db:0']
print('Citation file path:', citation_file)

# Load first few lines to debug
with open(citation_file, 'r') as f:
    lines = f.readlines()[:5]
    print('First 5 lines:')
    for i, line in enumerate(lines):
        print(f'{i}: {repr(line[:50])}')

# Get ACM papers
acm_file = locals()['var_functions.query_db:26']
print('ACM file path:', acm_file)

# Load first few lines
with open(acm_file, 'r') as f:
    lines = f.readlines()[:5]
    print('First 5 lines of ACM file:')
    for i, line in enumerate(lines):
        print(f'{i}: {repr(line[:50])}')

print('__RESULT__')
print(json.dumps({'status': 'debug complete'}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'status': 'files_checked'}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
