code = """import json
import os

# Read the full result from the file
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

# Let's explore the structure of the documents
print('__RESULT__:')
print(json.dumps({
    'total_docs': len(civic_docs),
    'sample_doc_preview': civic_docs[0]['text'][:1000] if civic_docs else 'No docs found'
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
