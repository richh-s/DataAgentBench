code = """import json
import re

# Load data sources
fund_file = var_functions.query_db:5
with open(var_functions.query_db:5, 'r') as f:
    funding_data = json.load(f)

with open(var_functions.query_db:2, 'r') as f:
    mongo_data = json.load(f)

print('__RESULT__:')
print(json.dumps({
    "funding_records": len(funding_data),
    "mongo_documents": len(mongo_data)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': "Available variables: ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5']", 'var_functions.execute_python:12': 'Loaded 19 documents from MongoDB'}

exec(code, env_args)
