code = """import json
import re

# Read the full civic documents result
with open('/tmp/tmp8r9gntdv.json', 'r') as f:
    civic_docs = json.load(f)

print('__RESULT__:')
print(json.dumps({
    "num_documents": len(civic_docs),
    "first_doc_keys": list(civic_docs[0].keys()) if civic_docs else [],
    "first_doc_filename": civic_docs[0].get("filename") if civic_docs else None,
    "text_preview": civic_docs[0].get('text', '')[:500] if civic_docs else None
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
