code = """import json

# Access the stored file path
civic_docs_path = 'var_functions.query_db:2'

# Read the file
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'num_docs': len(civic_docs),
    'first_doc': {
        'filename': civic_docs[0]['filename'],
        'text_preview': civic_docs[0]['text'][:200]
    }
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
