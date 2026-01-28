code = """import json

# Load data from files
with open('file_storage/functions.query_db:5.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:6.json', 'r') as f:
    civic_docs = json.load(f)

funding_count = len(funding_data)
civic_count = len(civic_docs)

# Build a dictionary mapping project names to amounts
funding_by_project = {}
for record in funding_data:
    funding_by_project[record['Project_Name']] = int(record['Amount'])

print('Funding records:', funding_count)
print('Civic documents:', civic_count)
print('Sample funding project:', list(funding_by_project.items())[0])

result = {'funding_count': funding_count, 'civic_count': civic_count, 'sample': list(funding_by_project.items())[0]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:18': {'funding_file': 'file_storage/functions.query_db:5.json', 'civic_file': 'file_storage/functions.query_db:6.json'}, 'var_functions.execute_python:22': {'funding_count': 500, 'civic_count': 19}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
