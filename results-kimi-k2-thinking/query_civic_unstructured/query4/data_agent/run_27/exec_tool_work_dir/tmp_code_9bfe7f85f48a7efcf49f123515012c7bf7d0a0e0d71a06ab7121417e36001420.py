code = """import json
import re

# Get the file paths from storage
mongo_file = str(globals()['var_functions.query_db:5'])
funding_file = str(globals()['var_functions.query_db:20'])

print('Mongo file:', mongo_file[:100])
print('Funding file:', funding_file[:100])

# Load data
with open(mongo_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_records = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'status': 'loaded',
    'civic_docs': len(civic_docs),
    'funding_records': len(funding_records)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:14': ['Funding'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
