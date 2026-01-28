code = """import json
import re
# var_call_R3Jsc9jJ2f081nEgJYmXt0we is the storage key for the Mongo query result file path
path = var_call_R3Jsc9jJ2f081nEgJYmXt0we
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

papers = []
for d in docs:
    fn = d.get('filename','')
    if fn.lower().endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    text = d.get('text','')
    years = re.findall(r"\b(19|20)\d{2}\b", text)
    # The regex returned only the century part because of a group; fix to find full years
    years_full = re.findall(r"\b(?:19|20)\d{2}\b", text)
    year = None
    if years_full:
        # choose the earliest occurrence
        year = int(years_full[0])
    # include only those with year 2016
    if year == 2016:
        papers.append({"title": title, "year": year})

# Remove duplicates by title
unique = {p['title']: p for p in papers}
result = list(unique.values())

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_R3Jsc9jJ2f081nEgJYmXt0we': 'file_storage/call_R3Jsc9jJ2f081nEgJYmXt0we.json'}

exec(code, env_args)
