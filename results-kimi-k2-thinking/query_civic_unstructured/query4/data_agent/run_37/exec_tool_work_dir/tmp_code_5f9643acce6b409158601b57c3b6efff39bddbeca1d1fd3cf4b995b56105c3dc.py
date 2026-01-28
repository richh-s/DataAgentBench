code = """import json, os

file_path = '/tmp/tmpub7z9f6a.json'

try:
    with open(file_path, 'r') as file:
        civic_docs = json.load(file)
    
    count = len(civic_docs)
    print('Loaded count:', str(count))
    
    if count > 0:
        first_doc = civic_docs[0]
        print('Keys:', list(first_doc.keys()))
        print('Filename:', str(first_doc.get('filename')))
    
    result = {'status': 'success', 'count': count}
except Exception as e:
    print('Error:', str(e))
    result = {'status': 'error', 'message': str(e)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
