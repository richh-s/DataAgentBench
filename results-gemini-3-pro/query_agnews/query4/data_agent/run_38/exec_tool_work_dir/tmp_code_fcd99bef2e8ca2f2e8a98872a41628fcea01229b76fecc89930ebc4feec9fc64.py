code = """import json

# The file path is in the variable 'var_function-call-5438198083873646081'
file_path = locals()['var_function-call-5438198083873646081']

with open(file_path, 'r') as f:
    metadata_list = json.load(f)

article_ids = [int(item['article_id']) for item in metadata_list]
print(f"Total articles in 2015: {len(article_ids)}")

print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_function-call-5438198083873646081': 'file_storage/function-call-5438198083873646081.json'}

exec(code, env_args)
