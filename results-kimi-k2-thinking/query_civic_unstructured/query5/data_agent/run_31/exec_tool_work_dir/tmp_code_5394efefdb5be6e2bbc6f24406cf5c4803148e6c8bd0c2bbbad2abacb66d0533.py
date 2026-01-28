code = """import json

# Get the result
result = locals()['var_functions.query_db:0']

# Initialize an empty list for documents
documents = []

# Try to read as file path if it's a string
if isinstance(result, str):
    try:
        with open(result, 'r') as f:
            documents = json.load(f)
    except:
        pass
else:
    documents = result

# Create a simple report
report = {
    'doc_count': len(documents),
    'first_doc_keys': list(documents[0].keys()) if documents else [],
    'filename': documents[0].get('filename', 'N/A') if documents else 'N/A'
}

# Print in required format
print('__RESULT__:')
print(json.dumps(report))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
