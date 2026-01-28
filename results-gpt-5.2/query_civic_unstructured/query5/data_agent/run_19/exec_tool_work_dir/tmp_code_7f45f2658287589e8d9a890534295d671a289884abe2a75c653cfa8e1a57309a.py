code = """import json, re, pandas as pd

fund_path = var_call_WHrlzje0QOdM5LXX1osbzV3A
with open(fund_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)
fund_names = set(fund_df['Project_Name'].tolist())

# docs
path = var_call_0CnqxWQsjqy2gwyNYQFjegOX
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Candidate approach: disaster-related if project name contains FEMA/CalOES/CalJPIA/Fire/Woolsey or appears in a Disaster section.
# Started in 2022: look for start/begin markers containing 2022 near the project name.

start_markers = [
    re.compile(r'\bStart(?:ed)?\b\s*:?\s*([A-Za-z0-9\- ,/]+)', re.IGNORECASE),
    re.compile(r'\bBegin\s+Construction\b\s*:?\s*([A-Za-z0-9\- ,/]+)', re.IGNORECASE),
    re.compile(r'\bBegin\b\s*:?\s*(\d{4}[A-Za-z0-9\- ,/]*)', re.IGNORECASE),
]

# Build regex for funding project names to search quickly: use escaping and word-boundary-ish
# Too many names; instead, for each doc, scan for lines that exactly equal a funding project name OR contain one.

related_kw = re.compile(r'FEMA|CalOES|CalJPIA|Woolsey|Fire|Disaster', re.IGNORECASE)

def find_started_2022_for_project(text, pname):
    # look at vicinity around first occurrence
    idx = text.find(pname)
    if idx == -1:
        return False
    snippet = text[max(0, idx-400): idx+800]
    if not related_kw.search(snippet) and not related_kw.search(pname):
        return False
    for pat in start_markers:
        m = pat.search(snippet)
        if m and '2022' in m.group(1):
            return True
    # also accept plain '2022' near 'Project Schedule' with 'Begin Construction' line in next lines
    if '2022' in snippet and re.search(r'Begin\s+Construction', snippet, re.IGNORECASE):
        # if any year 2022 occurs within 120 chars of Begin Construction
        for m in re.finditer(r'Begin\s+Construction[^\n]{0,80}', snippet, flags=re.IGNORECASE):
            if '2022' in m.group(0):
                return True
    return False

started_2022_projects = set()

for d in docs:
    text = d.get('text','') or ''
    # quick filter: if no 2022 then skip
    if '2022' not in text:
        continue
    # check only funding names that appear in text (simple contains)
    for pname in fund_names:
        if pname in text:
            if find_started_2022_for_project(text, pname):
                started_2022_projects.add(pname)

sel = fund_df[fund_df['Project_Name'].isin(started_2022_projects)]
ans = int(sel['total_amount'].sum())

print('__RESULT__:')
print(json.dumps({'total_funding': ans, 'num_projects': int(sel.shape[0]), 'num_unique_projects': len(started_2022_projects), 'projects': sorted(started_2022_projects)[:50]}))"""

env_args = {'var_call_WHrlzje0QOdM5LXX1osbzV3A': 'file_storage/call_WHrlzje0QOdM5LXX1osbzV3A.json', 'var_call_0CnqxWQsjqy2gwyNYQFjegOX': 'file_storage/call_0CnqxWQsjqy2gwyNYQFjegOX.json', 'var_call_NeiwFZNACJVkcMK3PXRvWo6A': {'total_funding': 0, 'num_projects': 0, 'projects': []}}

exec(code, env_args)
