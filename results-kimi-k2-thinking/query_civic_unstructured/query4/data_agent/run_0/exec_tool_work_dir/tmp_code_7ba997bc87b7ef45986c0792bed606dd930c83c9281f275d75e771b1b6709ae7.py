code = """import json
import os
import re

# Read the full result from the file
file_path = var_functions.query_db:5
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Number of documents: {len(civic_docs)}")
print(f"First document keys: {list(civic_docs[0].keys()) if civic_docs else 'No documents'}")

# Show sample documents
for i, doc in enumerate(civic_docs[:3]):
    print(f"\n--- Document {i+1} ---")
    print(f"Filename: {doc.get('filename', 'N/A')}")
    print(f"Text preview (first 500 chars): {doc.get('text', '')[:500]}...")

# Check if there are multiple documents
print(f"\nFilenames:")
for doc in civic_docs:
    print(f"- {doc.get('filename', 'N/A')}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
