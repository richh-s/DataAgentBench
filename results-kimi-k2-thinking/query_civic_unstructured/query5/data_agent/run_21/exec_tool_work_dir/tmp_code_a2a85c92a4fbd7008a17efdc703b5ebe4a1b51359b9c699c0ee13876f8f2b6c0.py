code = """import json

# Read the full result from the file
file_path = var_functions.query_db:0
with open(file_path, 'r') as f:
    documents = json.load(f)

print(f"Number of documents: {len(documents)}")
print("First document preview:")
print(json.dumps(documents[0], indent=2)[:2000])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
