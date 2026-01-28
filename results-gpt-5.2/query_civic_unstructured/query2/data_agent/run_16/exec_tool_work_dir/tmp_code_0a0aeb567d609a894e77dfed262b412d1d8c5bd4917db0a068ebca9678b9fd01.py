code = """import json, re, pandas as pd

civic_src = var_call_N2B5sN7opgvi4CCMp14UolUN
if isinstance(civic_src, str) and civic_src.endswith('.json'):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

fund_src = var_call_ZDwhamrPlRpdZCy8VVOCjSiZ
if isinstance(fund_src, str) and fund_src.endswith('.json'):
    with open(fund_src, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = fund_src

fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df.get('total_amount'), errors='coerce').fillna(0).astype(int)

park_kw = re.compile(r'\bpark\b|\bplayground\b|\bbluffs\b|\bskate\b', re.IGNORECASE)
completed_2022_kw = re.compile(r'completed[^\n\.]{0,200}2022|2022[^\n\.]{0,200}completed|completed\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+2022', re.IGNORECASE)

project_names = fund_df['Project_Name'].dropna().astype(str).unique().tolist()
project_names_sorted = sorted(project_names, key=len, reverse=True)

completed_2022_park_projects = set()

for doc in civic_docs:
    text = doc.get('text', '') or ''
    if not text:
        continue
    low = text.lower()
    if 'completed' not in low or '2022' not in text:
        continue
    for pn in project_names_sorted:
        if len(pn) < 6:
            continue
        idx = low.find(pn.lower())
        if idx == -1:
            continue
        window = text[max(0, idx-120):min(len(text), idx+400)]
        if not park_kw.search(window):
            continue
        if completed_2022_kw.search(window):
            completed_2022_park_projects.add(pn)

park_name_kw = re.compile(r'Park|Playground|Skate', re.IGNORECASE)
for doc in civic_docs:
    text = doc.get('text', '') or ''
    if not text:
        continue
    low = text.lower()
    if 'completed' not in low or '2022' not in text:
        continue
    for pn in project_names_sorted:
        if pn in completed_2022_park_projects:
            continue
        if not park_name_kw.search(pn):
            continue
        idx = low.find(pn.lower())
        if idx == -1:
            continue
        window = text[max(0, idx-80):min(len(text), idx+450)]
        if completed_2022_kw.search(window):
            completed_2022_park_projects.add(pn)

sel_df = fund_df[fund_df['Project_Name'].isin(sorted(completed_2022_park_projects))].copy()

out = {
    'total_funding_completed_2022_parks': int(sel_df['total_amount'].sum()),
    'projects': sel_df.sort_values('total_amount', ascending=False)[['Project_Name','total_amount']].to_dict('records')
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_N2B5sN7opgvi4CCMp14UolUN': 'file_storage/call_N2B5sN7opgvi4CCMp14UolUN.json', 'var_call_ZDwhamrPlRpdZCy8VVOCjSiZ': 'file_storage/call_ZDwhamrPlRpdZCy8VVOCjSiZ.json'}

exec(code, env_args)
