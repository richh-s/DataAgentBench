code = """import json, re

# Load the large Mongo query result from the provided storage file path
with open(var_call_MofUK2m03WbBxbNaWInNuQUc, 'r', encoding='utf-8') as f:
    docs = json.load(f)

results = []
for d in docs:
    filename = d.get('filename', '')
    text = d.get('text', '') or ''
    title = filename.rsplit('.txt', 1)[0]
    # Try to find year in the first 400 chars, fallback to whole text
    head = text[:400]
    m = re.search(r"\b(19|20)\d{2}\b", head)
    if not m:
        m = re.search(r"\b(19|20)\d{2}\b", text)
    year = int(m.group(0)) if m else None
    lower = text.lower()
    domain_flag = False
    # check for 'physical activity' phrase or variations
    if 'physical activity' in lower or 'physical-activity' in lower or 'physicalactivities' in lower:
        domain_flag = True
    # Also check keywords or author keywords lines
    if not domain_flag:
        if 'keywords' in lower and 'physical' in lower and 'activity' in lower:
            domain_flag = True
    if year == 2016 and domain_flag:
        results.append({'title': title, 'year': year})

# Prepare JSON-serializable output: list of titles
titles = [r['title'] for r in results]

import json
print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_call_MofUK2m03WbBxbNaWInNuQUc': 'file_storage/call_MofUK2m03WbBxbNaWInNuQUc.json'}

exec(code, env_args)
