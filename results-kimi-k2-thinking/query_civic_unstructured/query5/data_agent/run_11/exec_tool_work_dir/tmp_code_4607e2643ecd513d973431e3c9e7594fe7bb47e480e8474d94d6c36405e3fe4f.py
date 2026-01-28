code = """import json
import re

# Read the full result from the file
file_path = 'var_functions.query_db:2'
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'num_docs': len(civic_docs),
    'first_doc_keys': list(civic_docs[0].keys()) if civic_docs else [],
    'sample_filename': civic_docs[0]['filename'] if civic_docs else '',
    'sample_text_preview': civic_docs[0]['text'][:500] if civic_docs else ''
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
