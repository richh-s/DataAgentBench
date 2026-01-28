code = """import json, re, unicodedata

with open(var_call_1M7sMqR2IpdPIJ3evyKp9uWW, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_Itip1R3wzAsvEId1gYMLkyOS, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

# Extract design projects
design_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    start = text.find('Capital Improvement Projects (Design)')
    if start == -1:
        continue
    end_candidates = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']
    end = len(text)
    for cand in end_candidates:
        i = text.find(cand, start+1)
        if i != -1:
            end = min(end, i)
    section = text[start:end]
    pattern = re.compile(r'([^\n]+?)\n\s*\n\s*\(cid:')
    for m in pattern.findall(section):
        name = m.strip()
        if len(name) < 4:
            continue
        low = name.lower()
        if any(x in low for x in ['agenda', 'item', 'page', 'updates', 'project schedule', 'recommended action', 'discussion', 'meeting date']):
            continue
        design_projects.add(name)

# normalize
def normalize(s):
    s = s or ''
    s = s.lower()
    s = unicodedata.normalize('NFKD', s)
    s = re.sub(r'[^a-z0-9]+', ' ', s)
    return s.strip()

# funded names > 50000
funded = []
for r in funding_records:
    amt = 0
    try:
        amt = int(r.get('Amount', 0))
    except:
        try:
            amt = int(str(r.get('Amount','0')).replace(',', ''))
        except:
            amt = 0
    if amt > 50000:
        funded.append(r.get('Project_Name','').strip())

funded_norm = {fn: normalize(fn) for fn in funded}

# match
matched = []
for dp in sorted(design_projects):
    dpn = normalize(dp)
    for fn, fnn in funded_norm.items():
        if dpn == fnn or dpn in fnn or fnn in dpn:
            matched.append(dp)
            break

result = {'count': len(matched), 'matched_projects': matched}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_FnYNtZP9uJz9tYMvaWsgr5mp': ['civic_docs'], 'var_call_zcwXW7ppv08WDgDZpxMecKLl': ['Funding'], 'var_call_1M7sMqR2IpdPIJ3evyKp9uWW': 'file_storage/call_1M7sMqR2IpdPIJ3evyKp9uWW.json', 'var_call_Itip1R3wzAsvEId1gYMLkyOS': 'file_storage/call_Itip1R3wzAsvEId1gYMLkyOS.json'}

exec(code, env_args)
