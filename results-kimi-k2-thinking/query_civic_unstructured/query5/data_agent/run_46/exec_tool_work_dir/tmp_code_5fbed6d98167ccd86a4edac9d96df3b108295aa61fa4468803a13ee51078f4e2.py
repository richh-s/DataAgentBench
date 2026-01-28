code = """import json

# Load the data from the JSON files
civic_docs_file = 'var_functions.query_db:5.json'
funding_file = 'var_functions.query_db:2.json'

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

print('__RESULT__:')
print(json.dumps({
    "civic_docs_count": len(civic_docs),
    "funding_count": len(funding_data),
    "sample_doc_keys": list(civic_docs[0].keys()) if civic_docs else [],
    "sample_funding_keys": list(funding_data[0].keys()) if funding_data else []
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
