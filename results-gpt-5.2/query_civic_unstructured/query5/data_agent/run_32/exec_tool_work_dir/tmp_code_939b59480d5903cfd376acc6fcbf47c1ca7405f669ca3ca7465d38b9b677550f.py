code = """import json, re, pandas as pd

path_f = var_call_zUvUXYQoyPETIUUBoSSsfNcu
with open(path_f,'r') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])
fund_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount']))

path_d = var_call_g2qskuSxRxcFvL6Yz5EArSjM
with open(path_d,'r') as f:
    docs = json.load(f)

project_starts_2022 = set()

skip_prefixes = [
    'public works','agenda','item','to','prepared','approved','date','meeting',
    'subject','recommended action','discussion','capital improvement projects',
    'disaster recovery projects','page','updates','project schedule','estimated schedule',
    'project description','project updates'
]

def extract_projects_started_2022(text):
    lines = [re.sub(r'\s+',' ', ln.strip()) for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        ll = ln.lower()
        if any(ll.startswith(h) for h in skip_prefixes):
            continue
        if ll.startswith('capital improvement projects (') or ll.startswith('disaster recovery projects ('):
            continue
        if ':' in ln:
            continue
        if len(ln) > 120:
            continue
        window = ' '.join(lines[i+1:i+25]).lower()
        if ('begin construction' in window or re.search(r'\bbegin\b', window)) and '2022' in window:
            if re.search(r'begin[^\n]{0,80}2022', window):
                project_starts_2022.add(ln)

for d in docs:
    txt = d.get('text','')
    low = txt.lower()
    if 'disaster recovery projects' in low:
        idx = low.find('disaster recovery projects')
        sub = txt[idx:]
        extract_projects_started_2022(sub)

projects = sorted(project_starts_2022)
matched = {p: int(fund_map[p]) for p in projects if p in fund_map}

total = int(sum(matched.values())) if matched else 0
out = {'total_funding': total, 'matched_projects': matched, 'unmatched_projects': [p for p in projects if p not in fund_map]}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_mH4Vxmvq3ReMcbXlZLykb20w': ['Funding'], 'var_call_gbjPHSa1Y6wa84bGMdSamFGX': ['civic_docs'], 'var_call_zUvUXYQoyPETIUUBoSSsfNcu': 'file_storage/call_zUvUXYQoyPETIUUBoSSsfNcu.json', 'var_call_g2qskuSxRxcFvL6Yz5EArSjM': 'file_storage/call_g2qskuSxRxcFvL6Yz5EArSjM.json'}

exec(code, env_args)
