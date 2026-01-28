code = """import json
# var_call_jQ5dhQ0C3EMQSuPbocUQbQ1H is a file path to the JSON result from the previous query_db call
path = var_call_jQ5dhQ0C3EMQSuPbocUQbQ1H
with open(path, 'r') as f:
    records = json.load(f)
# Extract article_ids, convert to int
ids = sorted({int(r['article_id']) for r in records})
# Output as JSON string
out = json.dumps(ids)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_jQ5dhQ0C3EMQSuPbocUQbQ1H': 'file_storage/call_jQ5dhQ0C3EMQSuPbocUQbQ1H.json'}

exec(code, env_args)
