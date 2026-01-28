code = """import json
# Read the Mongo query result file path from storage variable
path = var_call_9WoMyZXHel3IZtSfmfVKeOEL
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

titles = []
for r in records:
    fn = r.get('filename', '')
    if fn.endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    titles.append(title)

# deduplicate and sort
titles = sorted(list(dict.fromkeys(titles)))

import json
print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_call_XvIdCElT5ohEvKleaoRLZRkz': ['paper_docs'], 'var_call_baL61nsUAI6gDYOO9hjpbPwa': ['Citations', 'sqlite_sequence'], 'var_call_X5TWoFeQoQbCKUA4aHf3zi8D': 'file_storage/call_X5TWoFeQoQbCKUA4aHf3zi8D.json', 'var_call_9WoMyZXHel3IZtSfmfVKeOEL': 'file_storage/call_9WoMyZXHel3IZtSfmfVKeOEL.json'}

exec(code, env_args)
