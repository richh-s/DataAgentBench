code = """import json

civic_docs = locals().get('var_functions.query_db:28', [])

if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

print(f'Found {len(civic_docs)} documents with Spring 2022 patterns')

# Show first document structure
if civic_docs:
    print('\nFirst document structure:')
    doc = civic_docs[0]
    print(f"Keys: {list(doc.keys())}")
    print(f"Filename: {doc.get('filename')}")
    print(f"Text preview: {doc.get('text')[:200]}")

print('__RESULT__:')
print(json.dumps({'doc_count': len(civic_docs), 'sample_keys': list(civic_docs[0].keys()) if civic_docs else []}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Funding'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'total_civic_docs': 5, 'total_funding_records': 500}, 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
