code = """import json
# load the metadata query result from storage
path = var_call_lHMvQvEmX9h6BOCb6lygiCdV
with open(path, 'r') as f:
    data = json.load(f)
# extract unique article_ids as integers
ids = sorted({int(item['article_id']) for item in data})
import json
print("__RESULT__:")
print(json.dumps(ids))"""

env_args = {'var_call_lHMvQvEmX9h6BOCb6lygiCdV': 'file_storage/call_lHMvQvEmX9h6BOCb6lygiCdV.json'}

exec(code, env_args)
