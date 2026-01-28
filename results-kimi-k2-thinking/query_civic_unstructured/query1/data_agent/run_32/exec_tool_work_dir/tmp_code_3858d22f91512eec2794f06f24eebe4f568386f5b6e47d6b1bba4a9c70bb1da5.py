code = """import json

# Load the data directly from storage (not from files)
civic_docs = locals()['var_functions.query_db:5']
funding_data = locals()['var_functions.query_db:30']

# Ensure they're in the right format
if isinstance(civic_docs, str):
    civic_docs = eval(civic_docs)
if isinstance(funding_data, str):
    funding_data = eval(funding_data)

# Count projects
result = 0
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        result += 1

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
