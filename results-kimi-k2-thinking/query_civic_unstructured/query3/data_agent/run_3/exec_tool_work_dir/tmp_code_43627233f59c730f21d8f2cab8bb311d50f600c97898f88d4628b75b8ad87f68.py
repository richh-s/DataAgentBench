code = """import json

# First, let's see what we have in storage
print("Available storage keys:")
for key in dir():
    if key.startswith('var_'):
        print(f"  {key}")

# Try to access the query_db result
storage_key = 'var_functions.query_db:2'
if storage_key in globals():
    file_path = str(globals()[storage_key])
    print(f"\nFile path found: {file_path}")
    
    # Try to load the data
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        print(f"Successfully loaded {len(data)} documents")
        
        # Show first document structure
        if data:
            doc = data[0]
            print(f"First doc keys: {list(doc.keys())}")
            if 'text' in doc:
                preview = doc['text'][:200]
                print(f"Text preview: {preview}...")
                
    except Exception as e:
        print(f"Error loading file: {e}")
else:
    print(f"Storage key {storage_key} not found in globals")

print('__RESULT__:')
print(json.dumps({"status": "loaded"}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding']}

exec(code, env_args)
