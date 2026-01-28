code = """import json

# Get the result from the stored variable
result = locals()['var_functions.query_db:0']

# Try to read as file path if it's a string
if isinstance(result, str):
    try:
        with open(result, 'r') as f:
            documents = json.load(f)
        print('Loaded documents from file')
        print('Number of documents:', len(documents))
        
        if documents:
            first_doc = documents[0]
            print('First doc keys:', list(first_doc.keys()))
            print('Filename:', first_doc.get('filename', 'N/A'))
            print('Text preview (first 200 chars):')
            print(first_doc.get('text', '')[:200])
            
    except Exception as e:
        print('Error:', str(e))
else:
    print('Result is not a file path string')
    print('Type:', type(result))

print('Done')"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
