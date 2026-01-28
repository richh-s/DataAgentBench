code = """import json
import re

docs_path = var_call_T7sf1DXAkweBowsJnBnlIKEa
funding_path = var_call_sk4Py445O2dS9gieZNkgmkxu

with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

season_keywords = ['spring']
month_keywords = ['march','april','may']

candidates = []
for doc in docs:
    lines = doc.get('text','').splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        if '2022' in low and (any(k in low for k in season_keywords) or any(m in low for m in month_keywords) or '2022-spring' in low or 'spring 2022' in low):
            # search backwards for a title-like line
            title = None
            for j in range(i-1, max(-1, i-13), -1):
                if j < 0:
                    break
                cand = lines[j].strip()
                if not cand:
                    continue
                clow = cand.lower()
                # skip administrative lines
                if any(clow.startswith(p) for p in ['page', 'agenda', 'item', 'to:', 'subject', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'recommend', 'discussion', 'updates']):
                    continue
                # prefer lines containing project-like words
                if ('project' in clow) or any(w in clow for w in ['repair','repairs','improvements','park','study','facility','walkway','resurfacing','drain','retaining','playground','skate','treatment','road','signal','median','culvert','bridge','traffic','slope','shade','construction']):
                    title = cand
                    break
            if title:
                candidates.append(title)

# deduplicate preserving order
seen = set()
projects = []
for p in candidates:
    np = p.strip()
    if np and np not in seen:
        seen.add(np)
        projects.append(np)

# load funding
amount_by_name = {}
for r in funding:
    name = r.get('Project_Name','')
    try:
        amt = int(r.get('Amount') or 0)
    except:
        try:
            amt = int(float(r.get('Amount')))
        except:
            amt = 0
    amount_by_name.setdefault(name, 0)
    amount_by_name[name] += amt

# match projects to funding
results = []
total_funding = 0
for proj in projects:
    matched = []
    proj_low = proj.lower()
    # exact matches
    for name, amt in amount_by_name.items():
        if name.lower() == proj_low:
            matched.append((name, amt))
    if not matched:
        for name, amt in amount_by_name.items():
            if proj_low in name.lower() or name.lower() in proj_low:
                matched.append((name, amt))
    sum_amt = sum(a for _,a in matched)
    total_funding += sum_amt
    results.append({'project': proj, 'matched_amount': sum_amt, 'matched_records': [n for n,_ in matched]})

output = {'count_projects': len(projects), 'total_funding': total_funding, 'projects': results}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_HW9ZkBmGMYzpwgAdnQj3jbbt': ['civic_docs'], 'var_call_tAowD8W9bhtcSi6T7DehBuLG': ['Funding'], 'var_call_T7sf1DXAkweBowsJnBnlIKEa': 'file_storage/call_T7sf1DXAkweBowsJnBnlIKEa.json', 'var_call_sk4Py445O2dS9gieZNkgmkxu': 'file_storage/call_sk4Py445O2dS9gieZNkgmkxu.json', 'var_call_Nb7i27L6OQRid4duyT4fxfav': {'count_projects': 0, 'total_funding': 0, 'projects': []}}

exec(code, env_args)
