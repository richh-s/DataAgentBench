code = """import json, re

# Load civic docs
src = var_call_eCYT6mwb8a9Kpa5X4KBBvjMo
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = src

# Load funding totals per project
fsrc = var_call_wUAIQWHnhpnImBn34Zbk6oW2
if isinstance(fsrc, str):
    with open(fsrc, 'r', encoding='utf-8') as f:
        funds = json.load(f)
else:
    funds = fsrc
fund_map = {r['Project_Name']: int(r['total_amount']) for r in funds}

completed_2022_projects = set()
complete_pat = re.compile(r'(?:construction\s+was\s+completed|complete\s+construction|completed)\b[^\n\r]{0,80}2022', re.IGNORECASE)

for d in docs:
    text = d.get('text','') or ''
    if re.search(r'\bpark\b', text, re.IGNORECASE) is None:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        if re.search(r'\bpark\b', ln, re.IGNORECASE) and not re.search(r'^(updates|project schedule|estimated schedule|project description)\b', ln, re.IGNORECASE):
            window = "\n".join(lines[i:i+9])
            if complete_pat.search(window):
                proj = re.sub(r'\s+', ' ', ln).strip(' -\t')
                completed_2022_projects.add(proj)

# Backtrack method
for d in docs:
    text = d.get('text','') or ''
    lines = [ln.strip() for ln in text.splitlines()]
    prev = None
    for ln in lines:
        if not ln:
            continue
        if complete_pat.search(ln):
            if prev and re.search(r'\bpark\b', prev, re.IGNORECASE):
                proj = re.sub(r'\s+', ' ', prev).strip(' -\t')
                completed_2022_projects.add(proj)
        prev = ln

matched = []
unmatched = []
total = 0
for proj in sorted(completed_2022_projects):
    amt = fund_map.get(proj)
    if amt is None:
        unmatched.append(proj)
    else:
        matched.append({'Project_Name': proj, 'total_amount': amt})
        total += amt

out = {'total_funding_completed_2022_park_projects': total,
       'matched_projects': matched,
       'unmatched_projects': unmatched}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_eCYT6mwb8a9Kpa5X4KBBvjMo': 'file_storage/call_eCYT6mwb8a9Kpa5X4KBBvjMo.json', 'var_call_wUAIQWHnhpnImBn34Zbk6oW2': 'file_storage/call_wUAIQWHnhpnImBn34Zbk6oW2.json'}

exec(code, env_args)
