code = """import json

# Read the civic documents data
civic_docs_path = locals()['var_functions.query_db:0']
with open(civic_docs_path, 'r') as f:
    civic_docs_data = json.load(f)

# Read the funding data
funding_path = locals()['var_functions.query_db:2']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'civic_docs_count': len(civic_docs_data),
    'funding_records_count': len(funding_data),
    'sample_civic_doc': civic_docs_data[0] if civic_docs_data else None,
    'sample_funding': funding_data[0] if funding_data else None
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
