code = """import json, re
# var_call_R6gwTreaDcfvqovoD3OXntlB is available in storage as a path to the JSON file
path = var_call_R6gwTreaDcfvqovoD3OXntlB
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

results = []
for rec in records:
    filename = rec.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = rec.get('text','')
    # search for year in first 500 chars
    head = text[:800]
    years = re.findall(r'\b(20\d{2})\b', head)
    pub_year = None
    if years:
        # pick first year between 2000 and 2026
        for y in years:
            if 2000 <= int(y) <= 2026:
                pub_year = int(y)
                break
    if pub_year is None:
        # search entire text
        years = re.findall(r'\b(20\d{2})\b', text)
        for y in years:
            if 2000 <= int(y) <= 2026:
                pub_year = int(y)
                break
    # If we still don't have pub_year, skip
    if pub_year is None:
        continue
    # domain check: we queried for "physical activity", but ensure it appears
    domain_present = bool(re.search(r'physical activity', text, flags=re.I))
    if domain_present and pub_year == 2016:
        results.append(title)

# dedupe
results = sorted(list(dict.fromkeys(results)))
output = json.dumps(results)
print('__RESULT__:')
print(output)"""

env_args = {'var_call_R6gwTreaDcfvqovoD3OXntlB': 'file_storage/call_R6gwTreaDcfvqovoD3OXntlB.json'}

exec(code, env_args)
