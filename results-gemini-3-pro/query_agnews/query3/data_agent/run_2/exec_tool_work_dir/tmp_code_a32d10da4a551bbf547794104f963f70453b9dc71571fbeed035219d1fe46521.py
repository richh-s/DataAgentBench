code = """import json

with open('var_function-call-18399428532014092056', 'r') as f:
    metadata_records = json.load(f)

count = len(metadata_records)
print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_function-call-12102129638019306028': ['authors', 'article_metadata'], 'var_function-call-12102129638019306837': ['articles'], 'var_function-call-18399428532014092056': 'file_storage/function-call-18399428532014092056.json'}

exec(code, env_args)
