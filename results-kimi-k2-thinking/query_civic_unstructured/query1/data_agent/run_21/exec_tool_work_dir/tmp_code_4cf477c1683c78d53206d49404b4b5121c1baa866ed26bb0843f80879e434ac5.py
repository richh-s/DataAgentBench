code = """import json

# Access civic_docs result
# This returns a file path, need to read the file
civic_doc_path = locals().get('var_functions.query_db:10', '')

if isinstance(civic_doc_path, str) and civic_doc_path:
    with open(civic_doc_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = locals().get('var_functions.query_db:10', [])

# Check the first document as a sample
sample_doc = civic_docs[0] if civic_docs else {}
print('__RESULT__:')
print(json.dumps({
    'total_documents': len(civic_docs),
    'sample_doc_keys': list(sample_doc.keys()) if sample_doc else [],
    'sample_text_preview': sample_doc.get('text', '')[:500] if sample_doc else ''
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': {'funding_records_over_50000': 276}, 'var_functions.list_db:6': ['civic_docs'], 'var_functions.list_db:8': ['civic_docs'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
