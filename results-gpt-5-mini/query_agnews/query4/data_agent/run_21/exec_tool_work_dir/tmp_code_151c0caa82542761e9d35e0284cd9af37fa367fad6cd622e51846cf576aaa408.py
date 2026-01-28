code = """import json
# read the stored JSON file from previous query
path = var_call_mdnPRBN1N7wUInnWRo8kyd6d
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
# extract article_ids as integers
ids = [int(r['article_id']) for r in records]
# produce JSON string
out = json.dumps(ids)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_mdnPRBN1N7wUInnWRo8kyd6d': 'file_storage/call_mdnPRBN1N7wUInnWRo8kyd6d.json'}

exec(code, env_args)
