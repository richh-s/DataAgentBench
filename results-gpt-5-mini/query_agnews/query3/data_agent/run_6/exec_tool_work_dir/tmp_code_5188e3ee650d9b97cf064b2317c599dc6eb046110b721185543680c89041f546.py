code = """import json
# var_call_nB1p5TIHl9VbLipRXchbATYi is the file path to the large JSON result
path = var_call_nB1p5TIHl9VbLipRXchbATYi
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)
# extract article_ids as ints
ids = [int(r['article_id']) for r in records]
# print result as JSON
print("__RESULT__:")
print(json.dumps(ids))"""

env_args = {'var_call_nB1p5TIHl9VbLipRXchbATYi': 'file_storage/call_nB1p5TIHl9VbLipRXchbATYi.json'}

exec(code, env_args)
