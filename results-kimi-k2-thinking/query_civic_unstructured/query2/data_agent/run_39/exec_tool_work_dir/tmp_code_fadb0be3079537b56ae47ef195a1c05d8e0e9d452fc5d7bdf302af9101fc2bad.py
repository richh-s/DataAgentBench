code = """import json

mongo_path = locals()['var_functions.query_db:2']
funding_path = locals()['var_functions.query_db:5']

with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding_recs = json.load(f)

# Count documents
result = {
    'mongo_docs': len(mongo_docs),
    'funding_records': len(funding_recs)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB', 'var_functions.execute_python:18': {'funding_records': 500, 'mongo_documents': 19}}

exec(code, env_args)
