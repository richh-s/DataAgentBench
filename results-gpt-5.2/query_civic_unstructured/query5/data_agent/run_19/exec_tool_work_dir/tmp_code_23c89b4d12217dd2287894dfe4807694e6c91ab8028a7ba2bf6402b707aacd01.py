code = """import json, re, pandas as pd

# Load funding per project
fund_path = var_call_WHrlzje0QOdM5LXX1osbzV3A
with open(fund_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

# Load docs
docs_path = var_call_0CnqxWQsjqy2gwyNYQFjegOX
with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Parse disaster projects and their begin/start timing.
# Strategy: In each document, find the 'Disaster Recovery Projects' section, then for each project name, look ahead for 'Begin Construction:' line.

disaster_projects_2022 = set()

proj_name_line = re.compile(r'^(?!Page\b)([A-Za-z0-9].{3,120}?)\s*$')
begin_line = re.compile(r'Begin\s+Construction\s*:\s*([A-Za-z0-9\- ,/]+)', re.IGNORECASE)
section_start = re.compile(r'Disaster\s+Recovery\s+Projects', re.IGNORECASE)
section_end = re.compile(r'Capital\s+Improvement\s+Projects', re.IGNORECASE)

for d in docs:
    text = d.get('text','') or ''
    lines = [ln.strip() for ln in text.splitlines()]
    # find disaster sections (could be multiple). Use indices where line matches start.
    starts = [i for i,ln in enumerate(lines) if section_start.search(ln)]
    for si in starts:
        # take slice until next 'Capital Improvement Projects' after start or end of doc
        ei = None
        for j in range(si+1, len(lines)):
            if section_end.search(lines[j]):
                ei = j
                break
        sub = lines[si:ei] if ei else lines[si:]
        # iterate, detect project name, then within next 25 lines search begin construction
        for idx, ln in enumerate(sub):
            if not ln or ':' in ln:  # skip label lines
                continue
            if ln.lower() in {'updates','project schedule','estimated schedule','project description','project updates','discussion','recommended action'}:
                continue
            # project name likely standalone line, not bullet
            if ln.startswith(('•','-','cid:')):
                continue
            if len(ln) > 120:
                continue
            # Candidate project name if it appears in funding list
            if ln in set(fund_df['Project_Name']):
                window = sub[idx: idx+30]
                begin = None
                for w in window:
                    m = begin_line.search(w)
                    if m:
                        begin = m.group(1).strip()
                        break
                if begin and '2022' in begin:
                    disaster_projects_2022.add(ln)

# Sum funding for those projects
sel = fund_df[fund_df['Project_Name'].isin(disaster_projects_2022)]
ans = int(sel['total_amount'].sum())

print('__RESULT__:')
print(json.dumps({'total_funding': ans, 'num_projects': int(sel.shape[0]), 'projects': sorted(disaster_projects_2022)}))"""

env_args = {'var_call_WHrlzje0QOdM5LXX1osbzV3A': 'file_storage/call_WHrlzje0QOdM5LXX1osbzV3A.json', 'var_call_0CnqxWQsjqy2gwyNYQFjegOX': 'file_storage/call_0CnqxWQsjqy2gwyNYQFjegOX.json'}

exec(code, env_args)
