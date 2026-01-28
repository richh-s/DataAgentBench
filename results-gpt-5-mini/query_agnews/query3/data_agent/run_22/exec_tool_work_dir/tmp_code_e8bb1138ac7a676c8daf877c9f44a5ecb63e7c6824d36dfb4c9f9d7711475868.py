code = """import json
# var_call_qIvueCq5gTNkJLTTzXw17dGe is available in the environment as path to the JSON result
path = var_call_qIvueCq5gTNkJLTTzXw17dGe
with open(path, 'r') as f:
    records = json.load(f)
ids = [int(r['article_id']) for r in records]
# remove duplicates and sort
ids = sorted(list(set(ids)))
import json
print("__RESULT__:")
print(json.dumps(ids))"""

env_args = {'var_call_qIvueCq5gTNkJLTTzXw17dGe': 'file_storage/call_qIvueCq5gTNkJLTTzXw17dGe.json'}

exec(code, env_args)
