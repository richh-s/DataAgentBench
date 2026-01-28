code = """import json, os, re, sys

files = os.listdir('.')
print('Files found:', files)

# Look for query result files
funding_files = [f for f in files if 'query' in f and 'db' in f and ('14' in f or '28' in f)]
civic_files = [f for f in files if 'query' in f and 'db' in f and ('15' in f or '24' in f)]

print('Funding files:', funding_files)
print('Civic files:', civic_files)

if funding_files:
    with open(funding_files[0], 'r') as f:
        funding_sample = json.load(f)[:5]
    print('Sample funding data:', funding_sample)

if civic_files:
    with open(civic_files[0], 'r') as f:
        civic_sample = json.load(f)[:2]
    print('Sample civic data keys:', [list(doc.keys()) for doc in civic_sample])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:18': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
