code = """import json, os, re, sys

# Read the full result from the file path stored in the variable
file_path = '/tmp/tmpub7z9f6a.json'

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        civic_docs = json.load(file)
    print('Successfully loaded ' + str(len(civic_docs)) + ' documents from MongoDB')
    
    # Show first document structure
    first_doc = civic_docs[0]
    print('\nFirst document keys: ' + str(list(first_doc.keys())))
    print('Filename: ' + str(first_doc.get('filename')))
    print('Text preview (first 500 chars):\n' + str(first_doc.get('text', ''))[:500])
else:
    print('File not found: ' + file_path)

print('__RESULT__:')
print(json.dumps({'status': 'loaded'}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
