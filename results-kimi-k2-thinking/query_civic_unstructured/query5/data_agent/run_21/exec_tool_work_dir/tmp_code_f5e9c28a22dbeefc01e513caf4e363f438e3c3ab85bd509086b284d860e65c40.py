code = """import json

# Read the full result from the file stored in var_functions.query_db:0
file_path = "var_functions.query_db:0"
with open(file_path, 'r') as f:
    documents = json.load(f)

print(f"Number of documents: {len(documents)}")
# Show a few document previews
for i, doc in enumerate(documents[:3]):
    print(f"\nDocument {i+1}:")
    print(f"  filename: {doc['filename']}")
    print(f"  text preview: {doc['text'][:200]}...")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
