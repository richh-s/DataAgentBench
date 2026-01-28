code = """import json

result_path = locals()['var_functions.query_db:2']

with open(result_path, 'r') as f:
    civic_docs = json.load(f)

result_str = json.dumps({
    'count': len(civic_docs),
    'first_doc_keys': list(civic_docs[0].keys()) if civic_docs else [],
    'sample_text': civic_docs[0]['text'][:200] if civic_docs else ''
})

print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
