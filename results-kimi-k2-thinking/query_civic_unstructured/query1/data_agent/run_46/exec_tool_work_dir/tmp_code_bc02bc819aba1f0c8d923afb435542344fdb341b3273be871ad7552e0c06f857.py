code = """import json
import re

# Read funding file
funding_data = []
with open(var_functions.query_db:6, 'r') as f:
    for line in f:
        if line.strip():
            funding_data.extend(json.loads(line))

# Read civic documents
civic_docs = []
with open(var_functions.query_db:8, 'r') as f:
    for line in f:
        if line.strip():
            civic_docs.extend(json.loads(line))

print('__RESULT__:')
print(json.dumps({'funding_records': len(funding_data), 'civic_docs': len(civic_docs)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
