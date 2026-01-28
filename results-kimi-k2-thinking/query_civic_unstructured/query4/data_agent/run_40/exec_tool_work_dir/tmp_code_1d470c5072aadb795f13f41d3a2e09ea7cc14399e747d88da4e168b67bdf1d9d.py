code = """import json
import re

# Access the data from variables
funding_data = locals().get('var_functions.query_db:5')
civic_docs = locals().get('var_functions.query_db:2')

# If they're file paths, load them
if isinstance(funding_data, str) and '.json' in str(funding_data):
    print("Loading funding data from file...")
    import os
    # Try to find the file
    possible_paths = [funding_data, '/root/shared_data/' + funding_data, '/tmp/' + funding_data]
    for path in possible_paths:
        if os.path.exists(path):
            with open(path, 'r') as f:
                funding_data = json.load(f)
            break
    
if isinstance(civic_docs, str) and '.json' in str(civic_docs):
    print("Loading civic docs from file...")
    import os
    possible_paths = [civic_docs, '/root/shared_data/' + civic_docs, '/tmp/' + civic_docs]
    for path in possible_paths:
        if os.path.exists(path):
            with open(path, 'r') as f:
                civic_docs = json.load(f)
            break

# Debug information
print("Type of funding_data:", type(funding_data))
print("Type of civic_docs:", type(civic_docs))

if isinstance(funding_data, list):
    print("Funding records:", len(funding_data))
    if funding_data:
        print("Sample funding record:", funding_data[0])
        
if isinstance(civic_docs, list):
    print("Civic documents:", len(civic_docs))
    if civic_docs:
        print("Sample civic doc keys:", list(civic_docs[0].keys()))
        print("Sample civic doc text (first 500 chars):", civic_docs[0]['text'][:500])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
