code = """import json
import os

# Find the latest MongoDB result file
import glob
mongo_files = glob.glob('/tmp/results/*mongodb*civic_docs*.json')
print('Mongo files found:', mongo_files)

if mongo_files:
    latest_mongo = sorted(mongo_files)[-1]
    print('Using file:', latest_mongo)
    with open(latest_mongo, 'r') as f:
        civic_docs = json.load(f)
    print('Civic documents loaded:', len(civic_docs))
else:
    print('No mongo files found')

# Find the SQLite funding file
funding_files = glob.glob('/tmp/results/*sqlite*funding*.json')
if funding_files:
    latest_funding = sorted(funding_files)[-1]
    print('Using funding file:', latest_funding)
    with open(latest_funding, 'r') as f:
        funding_data = json.load(f)
    print('Funding records loaded:', len(funding_data))
else:
    print('No funding files found')

result = {'status': 'files_loaded'}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.list_db:30': ['civic_docs'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:52': 'file_storage/functions.query_db:52.json'}

exec(code, env_args)
