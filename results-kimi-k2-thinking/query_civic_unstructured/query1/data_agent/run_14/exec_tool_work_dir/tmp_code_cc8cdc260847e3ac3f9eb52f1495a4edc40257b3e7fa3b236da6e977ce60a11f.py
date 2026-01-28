code = """import json

# Access variables properly
funding_file = globals()['var_functions.query_db:4']
civic_file = globals()['var_functions.query_db:5']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

print("__RESULT__:")
print(json.dumps({
    "funding_count": len(funding_data),
    "civic_docs_count": len(civic_docs),
    "sample_funding_name": funding_data[0]['Project_Name'] if funding_data else None
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:14': ['var_functions.list_db:0', 'var_functions.list_db:1', 'var_functions.query_db:4', 'var_functions.query_db:5']}

exec(code, env_args)
