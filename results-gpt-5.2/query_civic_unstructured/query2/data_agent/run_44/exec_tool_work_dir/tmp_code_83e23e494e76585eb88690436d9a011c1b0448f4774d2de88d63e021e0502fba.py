code = """import json, re

# load civic docs
civic_src = var_call_9vrprRc0iVCVVR5cceIUDiOM
if isinstance(civic_src, str) and civic_src.endswith('.json'):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

# load funding sums
fund_src = var_call_PronSciMyK2VlIx0HZyL35ZJ
if isinstance(fund_src, str) and fund_src.endswith('.json'):
    with open(fund_src, 'r', encoding='utf-8') as f:
        fund_rows = json.load(f)
else:
    fund_rows = fund_src

fund_map = {r['Project_Name']: float(r['TotalAmount']) for r in fund_rows}
fund_keys_lower = {k.lower(): k for k in fund_map.keys()}

park_completed_2022 = set()

month_pat = r'(January|February|March|April|May|June|July|August|September|October|November|December)'

for doc in civic_docs:
    text = doc.get('text','') or ''
    lines = text.splitlines()
    current_project = None
    for ln in lines:
        lns = ln.strip()
        if lns and ':' not in lns and len(lns) < 120:
            if re.search(r'Project|Park|Playground|Bluffs|Skate|Walkway|Shade Structure', lns, re.I):
                # avoid generic section headers
                if not re.match(r'^(Capital Improvement Projects|Disaster Recovery Projects|Agenda|Page|Item)\b', lns, re.I):
                    current_project = lns
        if current_project:
            if re.search(r'completed', lns, re.I) and re.search(r'\b2022\b', lns):
                if re.search(r'\bpark\b|\bplayground\b|\bbluffs\b|\blegacy park\b|\bskate\b', current_project, re.I):
                    park_completed_2022.add(current_project)
            if re.search(r'completed\s+(?:in\s+)?'+month_pat+r'\s+2022', lns, re.I):
                if re.search(r'\bpark\b|\bplayground\b|\bbluffs\b|\blegacy park\b|\bskate\b', current_project, re.I):
                    park_completed_2022.add(current_project)

matched = []
missing = []
for name in sorted(park_completed_2022):
    k = None
    if name in fund_map:
        k = name
    elif name.lower() in fund_keys_lower:
        k = fund_keys_lower[name.lower()]
    else:
        n2 = re.sub(r'\s+Project\s*$', '', name, flags=re.I).strip()
        if n2 in fund_map:
            k = n2
        elif n2.lower() in fund_keys_lower:
            k = fund_keys_lower[n2.lower()]
    if k is None:
        missing.append(name)
    else:
        matched.append((name, k, fund_map[k]))

total = sum(v for _,_,v in matched)

out = {
    'total_funding_park_projects_completed_2022': total,
    'matched_projects': [{'extracted_name': a, 'funding_project_name': b, 'total_amount': c} for a,b,c in matched],
    'unmatched_extracted_projects': missing
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_LKdiUOl4oslW9mQPRhHh1Wu0': ['Funding'], 'var_call_CrFjBOg6i9J70g3GuDcKlMMG': ['civic_docs'], 'var_call_9vrprRc0iVCVVR5cceIUDiOM': 'file_storage/call_9vrprRc0iVCVVR5cceIUDiOM.json', 'var_call_PronSciMyK2VlIx0HZyL35ZJ': 'file_storage/call_PronSciMyK2VlIx0HZyL35ZJ.json'}

exec(code, env_args)
