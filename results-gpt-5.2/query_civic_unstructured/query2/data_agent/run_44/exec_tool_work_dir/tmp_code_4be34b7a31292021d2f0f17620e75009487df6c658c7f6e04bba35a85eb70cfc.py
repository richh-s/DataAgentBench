code = """import json, re, pandas as pd

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

# extract park-related completed-in-2022 projects from civic texts
park_completed_2022 = set()

# regex helpers
re_completed_line = re.compile(r'^(?P<name>.+?)\s*$\n\s*\(?(?:cid:[^\n]*\n)*\s*\(?\s*cid:[^\n]*\n)?', re.M)

def add_if(name):
    name = re.sub(r'\s+', ' ', name).strip(' \t\r\n:-')
    if not name:
        return
    # park-related by name keywords
    if re.search(r'\bpark\b|\bplayground\b|\bbluffs\b|\blegacy park\b|\bskate\b', name, re.I):
        park_completed_2022.add(name)

for doc in civic_docs:
    text = doc.get('text','') or ''
    # look for bullets where updates mention completed and a 2022 month
    # capture preceding project header by scanning for patterns: header line followed by "Updates:" section
    lines = text.splitlines()
    current_project = None
    for ln in lines:
        lns = ln.strip()
        # project headers often non-empty and not starting with bullet markers and not containing ':'
        if lns and not lns.lower().startswith(('updates', 'project schedule', 'estimated schedule', 'project description', 'recommended action', 'discussion')) and ':' not in lns and len(lns) < 120:
            # heuristic: title case or contains key terms
            if re.search(r'Project|Park|Playground|Bluffs|Skate|Walkway|Shade Structure', lns, re.I):
                current_project = lns
        if 'completed' in lns.lower() and '2022' in lns:
            if current_project:
                add_if(current_project)
        # also some lines like "Construction was completed November 2022."
        if re.search(r'completed\s+(?:in\s+)?(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+2022', lns, re.I):
            if current_project:
                add_if(current_project)

# map extracted names to funding names: use exact match first; else try closest by case-insensitive exact
fund_keys_lower = {k.lower(): k for k in fund_map.keys()}
matched = []
missing = []
for name in sorted(park_completed_2022):
    if name in fund_map:
        matched.append((name, name, fund_map[name]))
    elif name.lower() in fund_keys_lower:
        k = fund_keys_lower[name.lower()]
        matched.append((name, k, fund_map[k]))
    else:
        # try small normalization (remove trailing 'Project')
        n2 = re.sub(r'\s+Project\s*$', '', name, flags=re.I).strip()
        if n2 in fund_map:
            matched.append((name, n2, fund_map[n2]))
        elif n2.lower() in fund_keys_lower:
            k = fund_keys_lower[n2.lower()]
            matched.append((name, k, fund_map[k]))
        else:
            missing.append(name)

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
