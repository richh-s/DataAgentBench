code = """import json, re, pandas as pd

# load funding per project
path_f = var_call_zUvUXYQoyPETIUUBoSSsfNcu
with open(path_f,'r') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

# load civic docs
path_d = var_call_g2qskuSxRxcFvL6Yz5EArSjM
with open(path_d,'r') as f:
    docs = json.load(f)

project_starts_2022 = set()

def extract_projects_started_2022(text):
    # Find lines that look like project names, followed by a schedule line containing 'Begin' and '2022'
    # We'll scan in windows: when we see a non-empty line without ':' and not bullets, treat as possible project name.
    lines = [ln.strip() for ln in text.splitlines()]
    # normalize weird chars
    lines = [re.sub(r'\s+', ' ', ln).strip() for ln in lines]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        # candidate project name: starts with letter/number, not too long, and not generic headings
        if any(ln.lower().startswith(h) for h in [
            'public works', 'agenda', 'item', 'to', 'prepared', 'approved', 'date', 'meeting',
            'subject', 'recommended action', 'discussion', 'capital improvement projects',
            'disaster recovery projects', 'page', 'updates', 'project schedule', 'estimated schedule',
            'project description', 'project updates', 'capital improvement projects (', 'disaster recovery projects (']):
            continue
        if ':' in ln:
            continue
        if len(ln) > 120:
            continue
        # look ahead next 20 lines for Begin Construction / Begin ... in 2022
        window = ' '.join(lines[i+1:i+25]).lower()
        if ('begin construction' in window or re.search(r'\bbegin\b', window)) and '2022' in window:
            # ensure begin date corresponds to 2022
            # capture phrases like 'Begin Construction: Fall 2022' or 'Begin: 2022-02'
            if re.search(r'begin[^\n]{0,50}2022', window):
                project_starts_2022.add(ln)

# Extract from docs, only disaster sections
for d in docs:
    txt = d.get('text','')
    # focus on Disaster Recovery Projects section if exists
    low = txt.lower()
    if 'disaster recovery projects' in low:
        # take substring from that header to end
        idx = low.find('disaster recovery projects')
        sub = txt[idx:]
        extract_projects_started_2022(sub)

# Filter to disaster-like names if any slipped
# Heuristic: disaster projects often include FEMA/CalOES/CalJPIA or are in disaster section already.
projects = sorted(project_starts_2022)

# Join with funding by exact Project_Name match
fund_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount']))
matched = {p: fund_map.get(p) for p in projects if p in fund_map}

total = int(sum(matched.values())) if matched else 0

out = {
    'total_funding': total,
    'matched_projects': matched,
    'unmatched_projects': [p for p in projects if p not in fund_map]
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_mH4Vxmvq3ReMcbXlZLykb20w': ['Funding'], 'var_call_gbjPHSa1Y6wa84bGMdSamFGX': ['civic_docs'], 'var_call_zUvUXYQoyPETIUUBoSSsfNcu': 'file_storage/call_zUvUXYQoyPETIUUBoSSsfNcu.json', 'var_call_g2qskuSxRxcFvL6Yz5EArSjM': 'file_storage/call_g2qskuSxRxcFvL6Yz5EArSjM.json'}

exec(code, env_args)
