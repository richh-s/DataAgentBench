code = """import json
import re

# Load the civic documents
civic_docs_path = var_functions.query_db:0
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Number of documents: {len(civic_docs)}")
print("\nFirst document preview:")
print(json.dumps(civic_docs[0], indent=2)[:2000] + "...")

# Let's see what filenames we have to understand the date ranges
filenames = [doc['filename'] for doc in civic_docs]
print(f"\nFilenames (first 10): {filenames[:10]}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
