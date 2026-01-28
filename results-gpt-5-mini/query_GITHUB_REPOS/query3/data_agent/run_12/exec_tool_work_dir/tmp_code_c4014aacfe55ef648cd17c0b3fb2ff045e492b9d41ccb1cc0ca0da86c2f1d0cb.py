code = """import json

# var_call_6M31FDKP9tgPv9rO4QH7QbV3 is provided by previous query_db call and contains the path to the full JSON result
path = var_call_6M31FDKP9tgPv9rO4QH7QbV3
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Extract unique repo_name values
repo_names = sorted({r['repo_name'] for r in records if 'repo_name' in r and r['repo_name']})

import json as _json
print("__RESULT__:")
print(_json.dumps(repo_names))"""

env_args = {'var_call_6M31FDKP9tgPv9rO4QH7QbV3': 'file_storage/call_6M31FDKP9tgPv9rO4QH7QbV3.json'}

exec(code, env_args)
