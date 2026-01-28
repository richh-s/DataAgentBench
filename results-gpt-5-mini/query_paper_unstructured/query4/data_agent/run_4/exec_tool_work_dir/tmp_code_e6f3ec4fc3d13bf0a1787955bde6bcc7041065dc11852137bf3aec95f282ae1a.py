code = """import json, re
p = var_call_40G8suqyORvGvH2VqbbBEhkO
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)

results = []

for rec in data:
    filename = rec.get('filename','')
    text = rec.get('text','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    # find year in first 1000 chars
    m = re.search(r"\b(19[9][0-9]|20(0[0-9]|1[0-9]|2[0-5]))\b", text[:1000])
    year = None
    if m:
        year = int(m.group(0))
    else:
        yrs = [(m.start(), int(m.group(0))) for m in re.finditer(r"\b(19[9][0-9]|20[0-2][0-9])\b", text)]
        if yrs:
            yrs.sort()
            year = yrs[0][1]
    domain_match = 'physical activity' in text.lower()
    if domain_match:
        results.append({'title': title, 'year': year})

# filter for year==2016
res2016 = [r['title'] for r in results if r['year']==2016]
res2016 = sorted(list(dict.fromkeys(res2016)))
print('__RESULT__:')
print(json.dumps(res2016))"""

env_args = {'var_call_UeAwGvyL4BRgCq5TsBDxPehn': 'file_storage/call_UeAwGvyL4BRgCq5TsBDxPehn.json', 'var_call_dtnwJdFJIovt8fdBMoCOC9Z5': [], 'var_call_40G8suqyORvGvH2VqbbBEhkO': 'file_storage/call_40G8suqyORvGvH2VqbbBEhkO.json'}

exec(code, env_args)
