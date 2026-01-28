code = """import json, re
# var_call_h8CIT19siyAbgT4EYFNOWynA is the storage key containing the file path to the Mongo query result
path = var_call_h8CIT19siyAbgT4EYFNOWynA
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

results = []
for d in docs:
    filename = d.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text', '') or ''
    # find first 4-digit year between 1900 and 2030
    years = re.findall(r"\b(19|20)\d{2}\b", text)
    # The above finds only the prefix; instead find full matches
    years_full = re.findall(r"\b(19|20)\d{2}\b", text)
    # Actually need full matched strings; do another findall
    years_full = re.findall(r"\b(?:19|20)\d{2}\b", text)
    year = None
    if years_full:
        try:
            year = int(years_full[0])
        except:
            year = None
    # ensure 'empirical' present
    if year and year > 2016 and re.search(r"empirical", text, re.I):
        results.append({"title": title, "year": year})

# deduplicate by title
seen = set()
unique_results = []
for r in results:
    if r['title'] not in seen:
        seen.add(r['title'])
        unique_results.append(r)

import json
print("__RESULT__:")
print(json.dumps(unique_results))"""

env_args = {'var_call_h8CIT19siyAbgT4EYFNOWynA': 'file_storage/call_h8CIT19siyAbgT4EYFNOWynA.json'}

exec(code, env_args)
