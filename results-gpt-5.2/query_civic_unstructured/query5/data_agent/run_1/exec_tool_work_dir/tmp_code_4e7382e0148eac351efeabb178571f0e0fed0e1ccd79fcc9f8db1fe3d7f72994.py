code = """import json, re, pandas as pd

# load funding
funding_src = var_call_DxZXrgir7bSPofq0krrauG1m
if isinstance(funding_src, str) and funding_src.endswith('.json'):
    with open(funding_src,'r',encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = funding_src

docs_src = var_call_JfAXMaifEjUuzNF65e2KwdVd
if isinstance(docs_src, str) and docs_src.endswith('.json'):
    with open(docs_src,'r',encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce').fillna(0).astype(int)

project_names = set(fund_df['Project_Name'].dropna().astype(str))

# heuristic: disaster-related if project name contains FEMA/CalOES/CalJPIA/disaster/woolsey/fire/emergency
pat_disaster_name = re.compile(r"\b(FEMA|CalOES|CalJPIA|disaster|Woolsey|fire|emergency)\b", re.IGNORECASE)

# determine which of these disaster-related projects started in 2022 based on civic docs text vicinity
start_2022 = set()

# precompile patterns to detect schedule/start lines
# We'll search for each project name occurrence and look ahead a window for start indicators containing 2022
start_indicators = [
    re.compile(r"\bStart\b[^\n]{0,80}2022", re.IGNORECASE),
    re.compile(r"\bBegin\s+Construction\b[^\n]{0,80}2022", re.IGNORECASE),
    re.compile(r"\bBegin\b[^\n]{0,80}2022", re.IGNORECASE),
    re.compile(r"\bConstruction\s+Start\b[^\n]{0,80}2022", re.IGNORECASE),
    re.compile(r"\bst\b\s*[:\-]?\s*2022", re.IGNORECASE),
]

# Some docs list: 'Project Schedule:' then bullet 'Begin Construction: Fall 2023'
# We'll also accept if line contains 'Begin' and '2022' within same line.

for d in docs:
    text = d.get('text','') or ''
    if '2022' not in text:
        continue
    # Speed: check only if any disaster keyword in doc
    if not pat_disaster_name.search(text) and 'Disaster Recovery Projects' not in text:
        # still could contain (FEMA Project) in project names list; pat_disaster_name covers FEMA
        pass
    lower_text = text.lower()
    for pn in project_names:
        if pn in ('Discussion','Recommended Action'):
            continue
        if not pat_disaster_name.search(pn):
            continue
        # find occurrences quickly via substring; case-sensitive, also try case-insensitive by lower
        idx = lower_text.find(pn.lower())
        if idx == -1:
            continue
        # iterate all occurrences
        start = 0
        while True:
            idx = lower_text.find(pn.lower(), start)
            if idx == -1:
                break
            window = text[idx: idx+1500]  # look ahead
            # split into lines and examine nearby lines for 2022 and start indicators
            # check indicator regexes
            if any(p.search(window) for p in start_indicators):
                start_2022.add(pn)
                break
            # fallback: if within window there's a line containing 2022 and the words 'begin' or 'start'
            for line in window.splitlines()[:40]:
                if '2022' in line and re.search(r"\b(begin|start)\b", line, re.IGNORECASE):
                    start_2022.add(pn)
                    break
            if pn in start_2022:
                break
            start = idx + len(pn)

# If none found (extraction too strict), fallback to treating 'started in 2022' as project name contains 2022 and disaster-related
if len(start_2022)==0:
    start_2022 = set([pn for pn in project_names if pat_disaster_name.search(pn) and '2022' in pn])

subset = fund_df[fund_df['Project_Name'].isin(start_2022)]

total = int(subset['Amount'].sum())

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'n_projects': int(subset['Project_Name'].nunique())}))"""

env_args = {'var_call_DxZXrgir7bSPofq0krrauG1m': 'file_storage/call_DxZXrgir7bSPofq0krrauG1m.json', 'var_call_JfAXMaifEjUuzNF65e2KwdVd': 'file_storage/call_JfAXMaifEjUuzNF65e2KwdVd.json', 'var_call_TCTs3cGEi5kICAZ0yDI5sy91': ['civic_docs'], 'var_call_umEJ4GpybYpolnXPUAjvCwXZ': ['Funding']}

exec(code, env_args)
