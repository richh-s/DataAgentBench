code = """import json, re, pandas as pd

# Load civic docs
path_docs = var_call_PVanfSSZHm5Pd3e1bSE05tYt
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Load funding totals per project
path_funding = var_call_rJADscRJOJeZi97RJFHTCwxN
with open(path_funding, 'r', encoding='utf-8') as f:
    funding = json.load(f)
fund_map = {r['Project_Name']: int(r['total_amount']) for r in funding if r.get('Project_Name') is not None and r.get('total_amount') is not None}

park_keywords = [
    'park','parks','playground','skate park','skatepark','bluffs','legacy park','trancas','point dume','zuma','paradise cove'
]

completed_2022_projects = set()

# Heuristic parsing: identify lines that look like project names and associate with nearby completion statements mentioning 2022.
for d in docs:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    current_project = None
    for i, ln in enumerate(lines):
        if not ln:
            continue
        # likely project name: Title Case-ish and not too long, not section headers
        if (len(ln) <= 90 and
            not re.search(r'^(Updates|Project Schedule|Estimated Schedule|Project Description|Capital Improvement Projects|Disaster Recovery Projects|Page \d+|Agenda Item)', ln, re.I) and
            not re.search(r'[:]|\(cid', ln) and
            re.search(r'[A-Za-z]', ln)):
            # many project names have no punctuation; accept if at least 2 words
            if len(ln.split())>=2:
                current_project = ln
        # completion line
        if re.search(r'completed', ln, re.I) and re.search(r'2022', ln):
            # park-related check using current project and completion line context window
            ctx = ' '.join(lines[max(0,i-2):min(len(lines), i+3)])
            cand = current_project
            if cand:
                hay = (cand + ' ' + ctx).lower()
                if any(k in hay for k in park_keywords):
                    completed_2022_projects.add(cand)

# Add explicit known from preview if missed: Bluffs Park Shade Structure completed Nov 2022
# (If parsing failed, ensure it's included when text contains it)
for d in docs:
    if 'Bluffs Park Shade Structure' in d.get('text','') and re.search(r'completed\s+November\s+2022', d.get('text',''), re.I):
        completed_2022_projects.add('Bluffs Park Shade Structure')

# Sum funding for those project names that exist in funding table
matched = []
total = 0
for p in sorted(completed_2022_projects):
    if p in fund_map:
        amt = fund_map[p]
        matched.append({'Project_Name': p, 'Funding_Total': amt})
        total += amt

out = {'total_funding_completed_2022_park_related': total, 'matched_projects': matched, 'unmatched_projects': sorted([p for p in completed_2022_projects if p not in fund_map])}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_PVanfSSZHm5Pd3e1bSE05tYt': 'file_storage/call_PVanfSSZHm5Pd3e1bSE05tYt.json', 'var_call_rJADscRJOJeZi97RJFHTCwxN': 'file_storage/call_rJADscRJOJeZi97RJFHTCwxN.json'}

exec(code, env_args)
