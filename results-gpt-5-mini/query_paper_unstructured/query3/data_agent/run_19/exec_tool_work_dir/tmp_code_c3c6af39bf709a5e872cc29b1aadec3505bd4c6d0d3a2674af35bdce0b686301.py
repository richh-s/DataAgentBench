code = """import json, re
# Load the Mongo query result stored in var_call_x25nJEfcG3wmoSMaJyeMAZKX (path to json)
path = var_call_x25nJEfcG3wmoSMaJyeMAZKX
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

results = []
for r in records:
    filename = r.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = r.get('text', '')
    # find first 4-digit year 2000-2026
    years = re.findall(r"\b(20\d{2})\b", text)
    year = int(years[0]) if years else None
    has_empirical = bool(re.search(r"\bempirical\b", text, re.I))
    if year and year > 2016 and has_empirical:
        results.append({'title': title, 'year': year})

# deduplicate by title, keep earliest year (though year should be same)
by_title = {}
for item in results:
    t = item['title']
    y = item['year']
    if t not in by_title or y < by_title[t]:
        by_title[t] = y

titles = sorted(by_title.keys())

import json
print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_call_x25nJEfcG3wmoSMaJyeMAZKX': 'file_storage/call_x25nJEfcG3wmoSMaJyeMAZKX.json'}

exec(code, env_args)
