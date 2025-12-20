code = """import json

# Get the file path from the stored variable
file_path = locals()['var_function-call-2680107260476408076']

# Load the result
with open(file_path, 'r') as f:
    metadata_records = json.load(f)

# Extract article_ids and convert to int
ids = [int(record['article_id']) for record in metadata_records]

print("__RESULT__:")
print(json.dumps(ids))"""

env_args = {'var_function-call-2680107260476408076': 'file_storage/function-call-2680107260476408076.json'}

exec(code, env_args)
