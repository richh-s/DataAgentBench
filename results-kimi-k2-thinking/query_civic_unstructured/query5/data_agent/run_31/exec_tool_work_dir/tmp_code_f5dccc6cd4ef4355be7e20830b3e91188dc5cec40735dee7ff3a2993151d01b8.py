code = """import json
import re

# Access the stored result properly
result_key = 'var_functions.query_db:0'
result = locals().get(result_key)

if result:
    print(f"Result type: {type(result)}")
    print(f"Result preview: {str(result)[:200]}...")
else:
    print("Result not found in locals")

# Try to read as file path if it's a string
if isinstance(result, str):
    try:
        with open(result, 'r') as f:
            documents = json.load(f)
        print(f"Loaded {len(documents)} documents")
        
        # Let's explore the first document
        if documents:
            first_doc = documents[0]
            print(f"\nFirst document keys: {first_doc.keys()}")
            print(f"Filename: {first_doc.get('filename', 'N/A')}")
            print(f"\nText preview (first 300 chars):")
            print(first_doc.get('text', '')[:300])
            
    except Exception as e:
        print(f"Error reading file: {e}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
