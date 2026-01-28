code = """import json

# Load the data
civic_docs_key = 'var_functions.query_db:5'
funding_key = 'var_functions.query_db:8'

civic_docs_str = locals().get(civic_docs_key)
funding_str = locals().get(funding_key)

# Load from file if needed
civic_docs = json.loads(open(civic_docs_str).read()) if isinstance(civic_docs_str, str) and civic_docs_str.endswith('.json') else civic_docs_str
funding_data = json.loads(open(funding_str).read()) if isinstance(funding_str, str) and funding_str.endswith('.json') else funding_str

# Count records
result = {
    'civic_docs_count': len(civic_docs),
    'funding_records_count': len(funding_data)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'total_civic_docs': 5, 'total_funding_records': 500}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
