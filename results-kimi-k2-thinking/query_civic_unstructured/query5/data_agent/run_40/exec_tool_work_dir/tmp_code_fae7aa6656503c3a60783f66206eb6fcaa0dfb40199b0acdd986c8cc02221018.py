code = """import json

# Load civic documents
civic_docs_path = locals()['var_functions.query_db:2']
print(f"Civic docs path: {civic_docs_path}")

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Number of civic documents: {len(civic_docs)}")

# Let's examine the structure of the first document
if civic_docs:
    first_doc = civic_docs[0]
    print(f"\nFirst document keys: {list(first_doc.keys())}")
    print(f"Filename: {first_doc.get('filename')}")
    print(f"Text length: {len(first_doc.get('text', ''))}")
    print(f"\nFirst 1000 chars of text:\n{first_doc.get('text', '')[:1000]}")"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
