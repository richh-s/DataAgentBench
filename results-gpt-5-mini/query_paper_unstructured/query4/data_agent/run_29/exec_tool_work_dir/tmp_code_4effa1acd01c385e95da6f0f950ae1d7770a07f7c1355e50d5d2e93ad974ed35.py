code = """import json
path = var_call_MMyKqAbaWyK4YDL1TloCDU5l
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

titles = []
for d in docs:
    fn = d.get('filename', '')
    if fn.endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    # Check if '2016' appears in text (anywhere)
    text = d.get('text', '')
    if '2016' in text:
        titles.append(title)

# dedupe and sort
titles = sorted(list(dict.fromkeys(titles)))

import json
print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_call_MMyKqAbaWyK4YDL1TloCDU5l': 'file_storage/call_MMyKqAbaWyK4YDL1TloCDU5l.json'}

exec(code, env_args)
