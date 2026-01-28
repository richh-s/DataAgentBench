code = """import json
import re

# Read the civic_docs result from the file path stored in the variable
civic_docs_path = var_functions.query_db:2
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Number of documents: {len(civic_docs)}")
print("\nFirst document keys:")
first_doc = civic_docs[0]
print(list(first_doc.keys()))

# Show a preview of the text
print("\nText preview:")
print(first_doc.get('text', '')[:500])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
