code = """import json, re
# Load the queried MongoDB results from storage file
with open(var_call_z44fGCrcdv8xi0cJHcIwkqeH, 'r', encoding='utf-8') as f:
    records = json.load(f)

titles = []
filtered = []
for r in records:
    filename = r.get('filename','')
    text = r.get('text','') or ''
    if filename.lower().endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    # confirm 2016 presence
    has2016 = bool(re.search(r'\b2016\b', text))
    # confirm physical activity mention
    has_pa = bool(re.search(r'physical activity', text, flags=re.I))
    if has2016 and has_pa:
        filtered.append({'title': title})
        titles.append(title)

# deduplicate while preserving order
seen = set()
unique_titles = []
for t in titles:
    if t not in seen:
        seen.add(t)
        unique_titles.append(t)

result = unique_titles
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_z44fGCrcdv8xi0cJHcIwkqeH': 'file_storage/call_z44fGCrcdv8xi0cJHcIwkqeH.json'}

exec(code, env_args)
