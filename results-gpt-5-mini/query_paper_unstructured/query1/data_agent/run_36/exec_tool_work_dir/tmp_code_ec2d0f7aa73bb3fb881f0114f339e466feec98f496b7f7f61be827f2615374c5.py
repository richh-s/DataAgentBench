code = """import json
p = var_call_MDtlVjLS0yg0lo56pfyzoxg8
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)
# extract titles from filenames, remove .txt
titles = []
for d in data:
    fn = d.get('filename','')
    if fn.lower().endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    titles.append(title)
# deduplicate while preserving order
seen = set()
unique_titles = []
for t in titles:
    if t not in seen:
        seen.add(t)
        unique_titles.append(t)

import json
print("__RESULT__:")
print(json.dumps(unique_titles))"""

env_args = {'var_call_MDtlVjLS0yg0lo56pfyzoxg8': 'file_storage/call_MDtlVjLS0yg0lo56pfyzoxg8.json'}

exec(code, env_args)
