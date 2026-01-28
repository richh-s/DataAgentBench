code = """import json, re
# Load the JSON result stored in var_call_ljFqEPHt3JaolG63Bbs4op2U
path = var_call_ljFqEPHt3JaolG63Bbs4op2U
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

results = []
for d in docs:
    filename = d.get('filename')
    title = filename[:-4] if filename and filename.lower().endswith('.txt') else filename
    text = d.get('text','')
    # Check domain mention
    if not re.search(r'physical\s*activity', text, re.I):
        continue
    # Find first year between 2000 and 2022 in the first 1000 chars
    header = text[:1000]
    years = re.findall(r'20\d{2}|19\d{2}', header)
    pub_year = None
    for y in years:
        yi = int(y)
        if 2000 <= yi <= 2022:
            pub_year = yi
            break
    if pub_year == 2016:
        results.append({'title': title, 'filename': filename})

# If none found, we will also try scanning whole text for a clear publication year line like '2016' after venue mention
if not results:
    for d in docs:
        filename = d.get('filename')
        title = filename[:-4] if filename and filename.lower().endswith('.txt') else filename
        text = d.get('text','')
        if not re.search(r'physical\s*activity', text, re.I):
            continue
        # search for standalone 2016 occurrences
        if re.search(r'\b2016\b', text):
            results.append({'title': title, 'filename': filename})

# Deduplicate
seen = set()
uniq = []
for r in results:
    if r['title'] not in seen:
        seen.add(r['title'])
        uniq.append(r)

print("__RESULT__:")
print(json.dumps(uniq))"""

env_args = {'var_call_ljFqEPHt3JaolG63Bbs4op2U': 'file_storage/call_ljFqEPHt3JaolG63Bbs4op2U.json'}

exec(code, env_args)
