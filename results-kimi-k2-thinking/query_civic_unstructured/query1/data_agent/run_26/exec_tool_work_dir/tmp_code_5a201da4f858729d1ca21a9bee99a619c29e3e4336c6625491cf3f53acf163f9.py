code = """import json

# Access the stored results using locals()
funding_result = locals()['var_functions.query_db:0']
civic_docs_result = locals()['var_functions.query_db:2']

# Load the JSON data
with open(funding_result, 'r') as f:
    funding_data = json.load(f)

with open(civic_docs_result, 'r') as f:
    civic_docs = json.load(f)

print('__RESULT__:')
print(json.dumps({
    "funding_records": len(funding_data),
    "civic_docs": len(civic_docs)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
