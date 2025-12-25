code = """import json

# Get the file path from the variable
file_path = locals()['var_function-call-12987280970809318212']

# Load the result
with open(file_path, 'r') as f:
    metadata_list = json.load(f)

# Extract article_ids as integers
article_ids = [int(item['article_id']) for item in metadata_list]

print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_function-call-12987280970809318212': 'file_storage/function-call-12987280970809318212.json'}

exec(code, env_args)
