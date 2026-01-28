code = """import json
import re
# var_call_8FYthHJvjhDSYs9BfJ0YBmBx is the storage key containing the JSON file path
path = var_call_8FYthHJvjhDSYs9BfJ0YBmBx
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

titles = []
for rec in records:
    filename = rec.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    text = rec.get('text', '')
    # Determine if publication year 2016 appears in the document (simple heuristic)
    if re.search(r'\b2016\b', text):
        titles.append(title)

# Deduplicate
titles = sorted(list(dict.fromkeys(titles)))

import json
print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_call_8FYthHJvjhDSYs9BfJ0YBmBx': 'file_storage/call_8FYthHJvjhDSYs9BfJ0YBmBx.json'}

exec(code, env_args)
