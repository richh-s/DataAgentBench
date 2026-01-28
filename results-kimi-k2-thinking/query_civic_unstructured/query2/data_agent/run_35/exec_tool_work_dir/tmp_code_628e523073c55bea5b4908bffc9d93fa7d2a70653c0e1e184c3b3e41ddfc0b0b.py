code = """import json

# Load the civic documents data
civic_docs_path = var_functions.query_db:2
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Number of civic documents: {len(civic_docs)}")
print("\nFirst document preview:")
print(f"Filename: {civic_docs[0]['filename']}")
print(f"Text preview (first 500 chars): {civic_docs[0]['text'][:500]}...")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
