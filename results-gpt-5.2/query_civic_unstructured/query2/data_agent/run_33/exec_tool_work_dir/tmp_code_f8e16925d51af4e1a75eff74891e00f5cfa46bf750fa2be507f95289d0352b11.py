code = """import json, re, pandas as pd

cd = var_call_mKx22czaa3jAzofSuck53jro
if isinstance(cd, str):
    with open(cd, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = cd

fd = var_call_VwxSmDfdfUtOLBviyvTA7n5n
if isinstance(fd, str):
    with open(fd, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = fd

fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'], errors='coerce').fillna(0).astype(int)

projects = set()
park_keywords = re.compile(r"\bpark\b|playground|skate\s*park|bluffs\s*park|legacy\s*park|trancas\s+canyon\s+park", re.IGNORECASE)
completed_re = re.compile(r"\bcompleted\b", re.IGNORECASE)

for doc in civic_docs:
    text = doc.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not ln or len(ln) < 4:
            continue
        low = ln.lower().strip()
        if low in {'updates:', 'project schedule:', 'project description:', 'discussion:', 'recommended action'}:
            continue
        if not park_keywords.search(ln):
            continue
        window = "\n".join(lines[i:i+25])
        if completed_re.search(window) and ('2022' in window):
            name = re.sub(r"\s+", " ", ln).strip(' :-\t')
            projects.add(name)

completed_2022_texts = [d.get('text','') for d in civic_docs if '2022' in d.get('text','') and completed_re.search(d.get('text',''))]

if len(projects) == 0 and not fund_df.empty:
    cand = fund_df[fund_df['Project_Name'].str.contains(r"Park|Playground|Skate", case=False, na=False)]['Project_Name'].tolist()
    for pn in cand:
        pat = re.compile(re.escape(pn))
        for tx in completed_2022_texts:
            if pat.search(tx) and park_keywords.search(pn):
                projects.add(pn)
                break

proj_list = sorted(projects)

if not fund_df.empty and proj_list:
    sel = fund_df[fund_df['Project_Name'].isin(proj_list)].copy()
    total = int(sel['Total_Amount'].sum())
else:
    sel = pd.DataFrame(columns=['Project_Name','Total_Amount'])
    total = 0

out = {'total_funding': total, 'projects': sel.sort_values('Project_Name').to_dict(orient='records')}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_RHGWjSkOVeS4UMb8GtTjU0oX': ['Funding'], 'var_call_mKx22czaa3jAzofSuck53jro': 'file_storage/call_mKx22czaa3jAzofSuck53jro.json', 'var_call_VwxSmDfdfUtOLBviyvTA7n5n': 'file_storage/call_VwxSmDfdfUtOLBviyvTA7n5n.json'}

exec(code, env_args)
