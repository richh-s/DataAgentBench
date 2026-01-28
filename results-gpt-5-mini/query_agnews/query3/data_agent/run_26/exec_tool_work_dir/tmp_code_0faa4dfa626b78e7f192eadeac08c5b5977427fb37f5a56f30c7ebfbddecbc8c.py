code = """import json
# Read the metadata query result file path from storage variable
path = var_call_N8MNBxN3AzUMtJlQbB4fIAXW
with open(path, 'r') as f:
    records = json.load(f)
# Extract article_ids as ints and deduplicate
ids = sorted({int(r['article_id']) for r in records})
import json
print("__RESULT__:")
print(json.dumps(ids))"""

env_args = {'var_call_N8MNBxN3AzUMtJlQbB4fIAXW': 'file_storage/call_N8MNBxN3AzUMtJlQbB4fIAXW.json'}

exec(code, env_args)
