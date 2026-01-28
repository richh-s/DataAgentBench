code = """import json

# Access the variable containing the file path
result_key = 'var_functions.query_db:0'
file_path = locals()[result_key]

# Read the full result from the file
with open(file_path, 'r') as f:
    documents = json.load(f)

print(f"Number of documents: {len(documents)}")
print("First document preview:")
print(json.dumps(documents[0], indent=2)[:2000])"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
