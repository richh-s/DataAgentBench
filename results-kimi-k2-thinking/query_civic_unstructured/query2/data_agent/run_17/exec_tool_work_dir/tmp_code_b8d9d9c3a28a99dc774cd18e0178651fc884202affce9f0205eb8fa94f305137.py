code = """import json
import re

# Load civic documents data
civic_docs_file = var_functions.query_db_5
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

print('Total civic documents:', len(civic_docs))

# Let's look at one document to understand structure
sample_doc = civic_docs[0]
print('\nSample document keys:', list(sample_doc.keys()))
print('\nSample filename:', sample_doc.get('filename'))
print('\nSample text (first 1000 chars):')
print(sample_doc.get('text', '')[:1000])

print('__RESULT__:')
print(json.dumps({'doc_count': len(civic_docs)}))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
