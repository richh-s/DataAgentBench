code = """import json

# Load civic documents
civic_docs_path = var_functions.query_db:2
if isinstance(civic_docs_path, str) and civic_docs_path.endswith('.json'):
    with open(civic_docs_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_functions.query_db:2

print(f"Number of documents: {len(civic_docs)}")
print(f"First document keys: {list(civic_docs[0].keys())}")

# Show first part of first document's text
text = civic_docs[0].get('text', '')
print("First 500 chars of text:\n")
print(text[:500])
print("\n===\n")

# Look for park-related projects completed in 2022
lines = text.split('\n')
for i, line in enumerate(lines[:30]):
    print(f"{i}: {line[:80]}")

result = json.dumps({"status": "data_loaded"})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
