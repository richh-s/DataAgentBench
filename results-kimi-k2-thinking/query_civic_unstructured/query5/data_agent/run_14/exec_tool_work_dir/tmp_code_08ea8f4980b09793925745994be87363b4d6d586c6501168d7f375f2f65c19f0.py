code = """import json

# Load funding records
funding_path = locals()['var_functions.query_db:10']
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Load civic documents  
docs_path = locals()['var_functions.query_db:2']
with open(docs_path, 'r') as f:
    civic_docs = json.load(f)

result_obj = {
    'funding_count': len(funding_records),
    'docs_count': len(civic_docs),
    'sample_funding': funding_records[:3] if funding_records else [],
    'sample_doc_keys': list(civic_docs[0].keys()) if civic_docs else [],
}

print('__RESULT__:')
print(json.dumps(result_obj))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'count': 5, 'first_doc_keys': ['_id', 'filename', 'text'], 'sample_text': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
