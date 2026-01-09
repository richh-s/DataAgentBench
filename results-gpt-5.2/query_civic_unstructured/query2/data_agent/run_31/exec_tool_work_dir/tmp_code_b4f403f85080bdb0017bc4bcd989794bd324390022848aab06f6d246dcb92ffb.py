code = """import json, re
import pandas as pd

# Load civic docs result (may be file path)
docs_src = var_call_eCYT6mwb8a9Kpa5X4KBBvjMo
if isinstance(docs_src, str):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

fund_src = var_call_wUAIQWHnhpnImBn34Zbk6oW2
if isinstance(fund_src, str):
    with open(fund_src, 'r', encoding='utf-8') as f:
        funds = json.load(f)
else:
    funds = fund_src

fund_map = {r['Project_Name']: int(r['total_amount']) for r in funds}

# Find completed-in-2022 park-related projects from docs
completed_2022_projects = set()

# Heuristic: detect completion lines like "Construction was completed ... 2022" or "Complete Construction: ... 2022" etc.
complete_pat = re.compile(r'(?:construction\s+was\s+completed|complete\s+construction|completed)\b[^\n\r]{0,80}2022', re.IGNORECASE)

for d in docs:
    text = d.get('text','')
    if not text:
        continue
    # Only consider docs that mention park keywords somewhere
    if re.search(r'\bpark\b', text, re.IGNORECASE) is None:
        continue

    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        # candidate project name line if it contains Park and is not updates/schedule header
        if re.search(r'\bpark\b', ln, re.IGNORECASE) and not re.search(r'^(updates|project schedule|estimated schedule|project description)\b', ln, re.IGNORECASE):
            # look ahead for completion mention within next 8 lines
            window = "\n".join(lines[i:i+9])
            if complete_pat.search(window):
                # Normalize spacing
                proj = re.sub(r'\s+', ' ', ln).strip(' -\t')
                completed_2022_projects.add(proj)

# Also catch cases where completion line may appear on same line without the word park in project line, but project is park-related:
# For all lines, if completion in 2022 and previous non-empty line contains park and looks like project name.
for d in docs:
    text = d.get('text','')
    if not text:
        continue
    lines = [ln.strip() for ln in text.splitlines()]
    prev = None
    for ln in lines:
        if not ln:
            continue
        if complete_pat.search(ln):
            # backtrack to find preceding line that includes park
            if prev and re.search(r'\bpark\b', prev, re.IGNORECASE):
                proj = re.sub(r'\s+', ' ', prev).strip(' -\t')
                completed_2022_projects.add(proj)
        prev = ln

# Join to funding: exact match on Project_Name
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

out = {
    'total_funding_completed_2022_park_projects': total,
    'matched_projects': matched,
    'unmatched_projects': unmatched
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_eCYT6mwb8a9Kpa5X4KBBvjMo': 'file_storage/call_eCYT6mwb8a9Kpa5X4KBBvjMo.json', 'var_call_wUAIQWHnhpnImBn34Zbk6oW2': 'file_storage/call_wUAIQWHnhpnImBn34Zbk6oW2.json'}

exec(code, env_args)
