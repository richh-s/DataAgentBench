code = """import json
import re

# Load the documents from the previous query
documents_path = locals()['var_functions.query_db:0']
with open(documents_path, 'r') as f:
    documents = json.load(f)

print(f"Found {len(documents)} documents")

# Let's examine the first document structure
if documents:
    print(f"First document keys: {list(documents[0].keys())}")
    # Print a snippet of the text
    text_sample = documents[0]['text'][:1000]
    print(f"Text sample (first 1000 chars):\n{text_sample}")
    
    # Count occurrences of emergency/FEMA in the documents
    emergency_count = sum(1 for doc in documents if 'emergency' in doc['text'].lower())
    fema_count = sum(1 for doc in documents if 'fema' in doc['text'].lower())
    print(f"Documents with 'emergency': {emergency_count}")
    print(f"Documents with 'FEMA': {fema_count}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
