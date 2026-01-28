code = """import json

with open('file_storage/functions.query_db:2.json', 'r') as f:
    funding_data = json.load(f)

with open('file_storage/functions.query_db:3.json', 'r') as f:
    civic_docs_data = json.load(f)

funding_count = len(funding_data)
civic_count = len(civic_docs_data)

print('__RESULT__:')
print(json.dumps({
    'funding_count': funding_count,
    'civic_count': civic_count,
    'sample_funding': funding_data[0] if funding_count > 0 else None,
    'sample_civic': civic_docs_data[0]['text'][:100] if civic_count > 0 else None
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'funding_type': "<class 'str'>", 'funding_preview': 'file_path', 'civic_type': "<class 'str'>", 'civic_preview': 'file_storage/functions.query_db:3.json'}}

exec(code, env_args)
